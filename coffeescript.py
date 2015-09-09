import sublime, sublime_plugin, subprocess, os


# Run the `coffee` command synchronously, sending `input` on stdin.
def coffee(extra_args, input):
    command = ['coffee', '--stdio']
    command.extend(extra_args)

    try:
        process = subprocess.Popen(command,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        stdin, stdout = process.communicate(input)
        exit_code = process.wait()

        return exit_code, stdin, stdout

    except OSError as (errno, strerror):
        if errno == 2:
            path = os.environ['PATH']
            message = "`coffee` couldn't be found on your $PATH:\n" + path
            return -1, None, message
        else:
            raise


# Base class for CoffeeScript commands
class CoffeeCommand(sublime_plugin.TextCommand):
    def is_enabled(self):
        syntax_filename = os.path.basename(self.view.settings().get('syntax'))
        return syntax_filename == 'CoffeeScript.tmLanguage'

    def _show_in_panel(self, output):
        window = self.view.window()
        v = window.get_output_panel('coffee_output')
        edit = v.begin_edit()
        v.insert(edit, 0, output)
        v.end_edit(edit)

        window.run_command("show_panel", {"panel": "output.coffee_output"})


# Compile the selected CoffeeScript and display it in a new window.  If no code
# is selected, compile the entire file.
class CompileAndDisplayJs(CoffeeCommand):
    def run(self, edit):
        window = self.view.window()

        for region in self.view.sel():
            if region.empty():
                region = sublime.Region(0, self.view.size())

            code = self.view.substr(region)

            exit_code, compiled_code, error = coffee(
                ['--compile', '--bare'], code)

            if exit_code == 0:
                v = window.new_file()
                v.set_name("Compiled JavaScript")
                v.set_scratch(True)
                v.set_syntax_file('Packages/JavaScript/JavaScript.tmLanguage')

                edit = v.begin_edit()
                v.insert(edit, 0, compiled_code)
                v.end_edit(edit)

            else:
                self._show_in_panel(error)
                return


# Run the selected CoffeeScript and display the results in the output panel.  If
# no code is selected, run the entire file.
class RunCoffeeScript(CoffeeCommand):
    def run(self, edit):
        window = self.view.window()

        for region in self.view.sel():
            if region.empty():
                region = sublime.Region(0, self.view.size())

            code = self.view.substr(region)

            exit_code, output, error = coffee([], code)

            if exit_code == 0:
                self._show_in_panel(output)
            else:
                self._show_in_panel(error)
                return