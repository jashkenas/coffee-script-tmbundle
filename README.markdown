CoffeeScript.tmbundle
---------------------

A **TextMate Bundle** for the **CoffeeScript** programming language.

Installation:

    mkdir -p ~/Library/Application\ Support/TextMate/Bundles
    cd ~/Library/Application\ Support/TextMate/Bundles
    git clone git://github.com/jashkenas/coffee-script-tmbundle CoffeeScript.tmbundle

The bundle includes syntax highlighting, the ability to compile or evaluate CoffeeScript inline, convenient symbol listing for functions, and a number of expando snippets.

Patches for additions are always welcome.

![screenshot](http://jashkenas.s3.amazonaws.com/images/coffeescript/textmate-highlighting.png)

If your TextMate.app is having trouble finding the `coffee` command, remember that [TextMate doesn't inherit your regular PATH](http://wiki.macromates.com/Troubleshooting/TextMateAndThePath). 

Using with Sublime Text 2
-------------------------

To use with Sublime Text 2 on OSX: 

    git clone https://github.com/jashkenas/coffee-script-tmbundle.git
    cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages
    ln -s ~/coffee-script-tmbundle CoffeeScript

To use with Sublime Text 2 on Linux (tested in Ubuntu 11.04, assumes ST2 is in ~/Applications):

    git clone https://github.com/jashkenas/coffee-script-tmbundle.git
    cd coffee-script-tmbundle
    zip -r CoffeeScript.sublime-package *
    mv CoffeeScript.sublime-package ~/Applications/Sublime\ Text\ 2/Pristine\ Packages

Quit ST2 and restart. You will have to close any `*.coffee` files that you have previously opened. Once you reopen them, syntax highlighting should work. Code snippets should also work. Haven't tested other features.

