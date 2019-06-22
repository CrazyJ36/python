#!/usr/bin/env python3

# Removes dash-bullet points from file.txt
file = open('file.txt')
text = file.read()
file.close()

#replace chars with empty string
text_no_dash = text.replace('- ', '')
print('\n' + text_no_dash)
del text_no_dash
exit(0)
