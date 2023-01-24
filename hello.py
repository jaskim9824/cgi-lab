#!/usr/bin/env python3

import os
import json

print("Content Type: text/html")
print()
print(os.environ)
print("Query string: " + os.environ["QUERY_STRING"])
print("User browser " + os.environ["HTTP_USER_AGENT"])