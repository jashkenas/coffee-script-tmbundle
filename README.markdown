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

Installation for with Sublime Text 2 on OSX: 

    cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages
    git clone https://github.com/jashkenas/coffee-script-tmbundle.git CoffeeScript

Installation for Sublime Text 2 on Linux (tested in Ubuntu 11.04):

    git clone https://github.com/jashkenas/coffee-script-tmbundle.git
    cd coffee-script-tmbundle
    zip -r CoffeeScript.sublime-package *
    mv CoffeeScript.sublime-package ~/Applications/Sublime\ Text\ 2/Pristine\ Packages

Quit and restart Sublime Text 2.

