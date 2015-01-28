#!/usr/bin/env python

import cgi

form = cgi.FieldStorage()
bd = form.getvalue("bd")
hobby = form.getvalue("hobby")

print"Content-type: text/html"
print
print"Your input was:</br>Birthday:%s</br>Hobby:%s</br>" % (bd, hobby)

print"<form method=\"post\" action=\"page2.py\">"
print"<textarea name=\"name\" cols=\"40\" rows=\"5\">Enter name</textarea>"
print"</br>"
print"<textarea name=\"family\" cols=\"40\" rows=\"5\">Enter family</textarea>"
print"</br><input type=\"submit\" value=\"Submit\"></form>"
