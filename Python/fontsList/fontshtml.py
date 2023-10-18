# Created 2023-10-18
# Author: Martin Knudsen
# Purpose: Read json file with google fonts and create HTML file with examples of all the google fonts.

# importing the module
import json

# Opening JSON file
with open('googlefonts.json') as json_file:
	data = json.load(json_file)

	# Print the type of data variable
	print("Type:", type(data))

	# Print the data of dictionary
	print("\nFonts:", data)
