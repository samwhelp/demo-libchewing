#!/usr/bin/env python3

import sys

from chewing import userphrase

def usage():
	print('./cmd-add.py $phrase $bopomofo')

def main():
	argc = len(sys.argv)

	if (argc < 3):
		usage()
		return

	phrase = sys.argv[1]
	bopomofo = sys.argv[2]

	rtn = userphrase.add(phrase, bopomofo)

	print('add (', rtn, ') userphrase')

	if rtn > 0:
		sys.exit(0)
	else:
		sys.exit(1)


if __name__ == '__main__':
	main()
