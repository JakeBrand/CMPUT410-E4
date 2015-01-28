#!/usr/bin/env python

# Copyright 2015 Jake Brand
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
