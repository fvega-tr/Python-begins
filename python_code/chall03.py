#!/usr/bin/env python3

import sys

argc = len(sys.argv)
snail = []
draw = ""
boolean = True
length = len(sys.argv[1])

try:
	if argc > 3:

		for i in range(1, argc):

			if length == len(sys.argv[i]):

				length = len(sys.argv[i])

				snail.append(list(sys.argv[i]))

				boolean = sys.argv[i].isdigit()

			else:

				boolean = False

				break

		
		if boolean == False:

			sys.exit(1)

		
		while	len(snail) > 0:

				
				#top row copy and delete
			
				for i in range(len(snail[0])):

					draw += snail[0][i]

				del(snail[0])


				#right row copy and delete

				for i in range(0, len(snail)):

						draw += snail[i][-1]

						del(snail[i][-1])

				
				#bottom row copy and delete

				if len(snail) > 1:

					for i in range(len(snail[-1]) -1, -1, -1):
					
						draw += snail[-1][i]
				
					del(snail[-1])

				
				#left row copy and delete

				for i in range(len(snail) -1, -1, -1):

					if	len(snail) > i:

						draw += snail[i][0]

						del(snail[i][0])
					
					else:
						break

		print(draw)

	else:
		print("usage: %s <1-9 squared_rows...>" % sys.argv[0])

except:
	print("usage: %s <1-9 squared_rows...>" % sys.argv[0])