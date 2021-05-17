# Strum limiter [FreePIE](https://andersmalmgren.github.io/FreePIE/) script for (mostly) Clone Hero

[**Requires vJoy to be installed first.**](http://vjoystick.sourceforge.net/site/)

***To register the vJoy controller in Clone Hero, simply start the script, then go and re-assign the primary controller in Clone Hero's "spacebar" controller settings screen. When it asks to press a button on a controller, press the Spacebar again to register the vJoy controller instead of the guitar itself.***

*NOTE: You may not actually need this if you're playing any of the commercial Guitar Hero/Rock Band games (their PC versions/on an emulator), as those game already have a strum limiter built-in. However, if your copy of the game has the limiter patched out via modding, then this script may come in handy.*

---

I created this script to resolve double-strum issues with my controller, particularly when in use with Clone Hero, a game that has no strum limiter, and therefore nothing to protect your guitar against accidental double-strums from worn-out strum switches. The script maps the guitar controller 1:1 with the vJoy controller... with an exception to how it handles the strum inputs. Each strum input remains held down for 1/30th of a second (that's 2 whole frames for every 60 FPS; configurable), preventing accidental strums from being registered. This only affects same-direction strumming (a series of down-strums/up-strums), and does not affect alt-strumming.

The alternate version of the script provides a different flavour of applying the limiter, where instead of keeping the strum input held down, subsequent strum inputs are blocked for 1/30th a second (again, configurable) unless the next strum is in the other direction. So alt-strums are still unaffected. This may work better for you, so try both scripts and see which one works best.

To make the script a little bit more accessible, it has been set-up such that you need to first strum the guitar that you wish to use after running the script. This is to account people who happen to have multiple controllers already connected to their PC, and don't want to have to deal with having to disconnect them first.
