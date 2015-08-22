CoffeeScript.tmbundle
---------------------

A **TextMate Bundle** for the **CoffeeScript** programming language.

Installation:
-------------

### TextMate 1

    cd ~/Library/Application\ Support/TextMate/Bundles
    git clone git://github.com/jashkenas/coffee-script-tmbundle CoffeeScriptBundle.tmbundle
    osascript -e 'tell app "TextMate" to reload bundles'

### TextMate 1.5.10+ & 2

    cd /Applications/TextMate.app/Contents/SharedSupport/Bundles
    git clone git://github.com/jashkenas/coffee-script-tmbundle CoffeeScriptBundle.tmbundle
    osascript -e 'tell app "TextMate" to reload bundles'

The bundle includes syntax highlighting, the ability to compile or evaluate CoffeeScript inline, convenient symbol listing for functions, and a number of expando snippets.

Patches for additions are always welcome.

![screenshot](http://jashkenas.s3.amazonaws.com/images/coffeescript/textmate-highlighting.png)

If your TextMate.app is having trouble finding the `coffee` command, remember that [TextMate doesn't inherit your regular PATH](http://wiki.macromates.com/Troubleshooting/TextMateAndThePath). 

Sublime Text 2:
-------------

This bundle is compatible with Sublime Text 2, and can be installed for
that editor using:

    cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/
    git clone git://github.com/jashkenas/coffee-script-tmbundle CoffeeScript


