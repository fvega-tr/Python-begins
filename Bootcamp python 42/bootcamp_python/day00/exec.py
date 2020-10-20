#!/usr/bin/env python3

import sys

string = ""
for i in range(1, len(sys.argv)):
	if i != len(sys.argv):
		string += " "
	string += sys.argv[i].swapcase()
	
print(string[::-1])