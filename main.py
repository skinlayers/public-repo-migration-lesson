#!/usr/bin/env python3
import math

import emoji
import pyjokes


# These are 'global variables' that never change while the program is being executed.
# By setting these variables at the top, it gives us a convienent way to configure parts of the code.
# Also, these variables will always be available within the scope (guts) of our functions (hence 'global').
top_emoji = ":birthday_cake:"
bottom_emoji = ":red_heart:"


# If we're doing the same task multiple times, it might be a good idea to wrap it in a function.
def render_emoji_line(emoji_char, length):
    print(emoji.emojize(emoji_char * length))

def main():
    # We store the result of the get_joke() method call in variable for further processing.
    # Note: Comments like this ^^ are kinds garbage.
    # This wouldn't help enlighten most people reading the code as to what the fuck it's actually doing.
    joke = pyjokes.get_joke()

    # The width of a emoji characters is often wider than that of the regular mono-spaced ASCII characters.
    # With our current emojis, this causes the emoji lines to be about twice as long as the joke line.
    # To compensate, we divide the lenth of the joke in half, and use math.ceil() to round up.
    # This will not work correctly with all emojis, so we might want to find a better solution.
    emoji_line_length = math.ceil(len(joke) / 2)

    # Print the joke with emoji's framing it on the lines above and below the joke.
    render_emoji_line(top_emoji, emoji_line_length)
    print(joke)
    render_emoji_line(bottom_emoji, emoji_line_length)


# This is a common pattern for a python program to figure out if it's being ran directly or used as a library.
# If it is being executed, it will run the main() function.
# Otherwise, nothing runs, but the functions inside could be imported into another program, and executed that way.
if __name__ == "__main__":
    main()
