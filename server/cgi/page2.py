#!/usr/bin/env python

import cgi

form = cgi.FieldStorage()
name = form.getvalue("name")
family = form.getvalue("family")

print"Content-type: text/html"
print
print"The values you entered were:</br>Name:%s</br>Family:%s</br>" % (name, family)

print"<form method=\"post\" action=\"page1.py\">"
print"<textarea name=\"bd\" cols=\"40\" rows=\"5\">Enter birthday</textarea>"
print"</br>"
print"<textarea name=\"hobby\" cols=\"40\" rows=\"5\">Enter main hobby</textarea>"
print"</br><input type=\"submit\" value=\"Submit\"></form>"
