import sublime
import sublime_plugin
import subprocess

class CoffeeCompileCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        process = subprocess.Popen(["coffee", "-b", "-s", "-c"], stderr = subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
        (compiled, errors) = process.communicate(self.get_coffeescript())

        if len(compiled) == 0:
            output = errors
        else:
            output = compiled

        self.output_to_new_view(output)

    def get_coffeescript(self):
        selection = self.view.sel()[0]
        if selection.empty():
            selection = sublime.Region(0, self.view.size())
        return self.view.substr(selection)

    def output_to_new_view(self, output):
        new_view = sublime.active_window().new_file()
        new_view.set_name("compiled_CoffeeScript.js")
        new_view.set_syntax_file("Packages/JavaScript/JavaScript.tmLanguage")
        new_view.set_scratch(True)
        edit = new_view.begin_edit()
        new_view.insert(edit, 0, output)
        new_view.end_edit(edit)
