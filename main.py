#!/usr/bin/env python3
import emoji
import pyjokes


# These are 'global variables' that never change while the program is being executed.
# By setting these variables at the top, it gives us a convienent way to configure parts of the code.
top_emoji = ":birthday_cake:"
bottom_emoji = ":red_heart:"

# We store the result of the get_joke() method call in variable for further processing.
# Note: Comments like this ^^ are kinds garbage.
# This wouldn't help enlighten most people reading the code as to what the fuck it's actually doing.
joke = pyjokes.get_joke()

# The width of a emoji characters is roughly twice that of the regular mono-spaced ASCII characters.
# This causes the emoji lines to be about twice as long as the joke line.
# To (roughly) compensate, we use floor division to half the length of the joke, and drop an remainder.
# By using floor division, our result stays an integer that we can then multiple our emojis by.
# If we used '/' instead of '//', the emoji_length would be a floating-point number.
# This would cause an error when we multiply our emojis by emojy_length below.
emoji_length = len(joke)//2


print(emoji.emojize(top_emoji * emoji_length))
print(joke)
print(emoji.emojize(bottom_emoji * emoji_length))
