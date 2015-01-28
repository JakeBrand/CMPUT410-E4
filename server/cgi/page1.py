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
