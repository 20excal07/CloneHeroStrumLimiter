# Double strum prevention [FreePIE](https://andersmalmgren.github.io/FreePIE/) script for Guitar Hero/Clone Hero

[**Requires vJoy to be installed first.**](http://vjoystick.sourceforge.net/site/)

**To register the vJoy controller in Clone Hero, simply start the script, then go and re-assign the primary controller in Clone Hero's "spacebar" controller settings screen. When it asks to press a button on a controller, press the Spacebar again to register the vJoy controller instead of the guitar itself.**

I created this script to solve double-strumming issues with my controller via software. The script maps the guitar controller 1:1 with the vJoy controller... with an exception to how it handles the strum inputs. Each strum input remains held down by 1/30th of a second (that's 2 whole frames for every 60 FPS; configurable), preventing accidental strums from being registered. This only affects same-direction strumming (a series of down-strums/up-strums), and does not affect alt-strumming.

The alternate version of the script provides a different flavour of preventing the double strums, where instead of keeping the strum input held down, subsequent strum inputs are blocked for 1/30th a second (again, configurable) unless the next strum is in the other direction. So alt-strums are still unaffected. This may work better for you, so try both scripts and see which one works best.
