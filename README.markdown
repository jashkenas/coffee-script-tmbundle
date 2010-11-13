CoffeeScript.tmbundle
---------------------

A **TextMate Bundle** for the **CoffeeScript** programming language.

Installation:

    mkdir -p ~/Library/Application\ Support/TextMate/Bundles
    cd ~/Library/Application\ Support/TextMate/Bundles
    git clone git://github.com/jashkenas/coffee-script-tmbundle CoffeeScript.tmbundle

*An important note about PATH:* TextMate does not source the `PATH` variable. So, you'll have to add the paths of `coffee` and `node` to TextMate's PATH (set in Preferences -> Advanced -> Shell Variables). Also make sure that the PATH includes `/usr/bin`. Otherwise, you'll experience errors when you can use the Run and Compile commands.

The bundle includes syntax highlighting, the ability to compile or evaluate CoffeeScript inline, convenient symbol listing for functions, and a number of expando snippets.

Patches for additions are always welcome.

![screenshot](http://jashkenas.s3.amazonaws.com/images/coffeescript/textmate-highlighting.png)

