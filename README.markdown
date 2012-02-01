# IcedCoffeeScript.tmbundle

A **TextMate Bundle** / **Sublime Text 2 Package** for the **CoffeeScript** programming language.

Forked to highlight `await` and `defer` keywords used by [IcedCoffeeScript](http://maxtaco.github.com/coffee-script/).
    
## Installation in Sublime Text 2

To replace your existing CoffeeScript package, use `Package Control: Remove Package` to remove your old **CoffeeScript** Package first. This step is optional, you can of course use both packages, but you'll have to manually select **Iced Coffee** for files containing the additional keywords.

To install the **Iced Coffee** Package, simply clone this repository package directory:

    cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages
    git clone git://github.com/dhoelzgen/iced-coffee-script-tmbundle.git Iced

Sublime should automatically detect and reload the package.

## Installation in Textmate

    cd ~/Library/Application\ Support/TextMate/Bundles (Textmate 1)
    cd /Applications/TextMate.app/Contents/SharedSupport/Bundles (Textmate 2)
    git clone git://github.com/jashkenas/coffee-script-tmbundle CoffeeScriptBundle.tmbundle

The bundle includes syntax highlighting, the ability to compile or evaluate CoffeeScript inline, convenient symbol listing for functions, and a number of expando snippets.

Patches for additions are always welcome.

![screenshot](http://jashkenas.s3.amazonaws.com/images/coffeescript/textmate-highlighting.png)

If your TextMate.app is having trouble finding the `coffee` command, remember that [TextMate doesn't inherit your regular PATH](http://wiki.macromates.com/Troubleshooting/TextMateAndThePath). 

