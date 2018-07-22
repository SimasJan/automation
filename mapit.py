#! /usr/bin/env python3

######## GOOGLE MAPS DIRECTIONS ##########
# How To:
# 1. open new terminal command line
# 2. type ./mapit.py [postcode1] [postcode2] (replace text in brackets with the actual post code addresses (without spaces))
# 3. your default browser will open google maps with entered post codes as directions
# 4. Enjoy! 

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
	# get address from command line.
	address = ' '.join(sys.argv[1:2])
	# get the last part of the address (post code) form the command line
	address2 = ' '.join(sys.argv[-1:])
else:
	# get address from clipboard.
	address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/dir/' + address+ '/' + address2)
