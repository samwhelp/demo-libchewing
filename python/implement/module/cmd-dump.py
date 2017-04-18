#!/usr/bin/env python3

import sys

from chewing import userphrase

def usage():
	print('./cmd-findall.py')

def run_each(phrase, bopomofo):
	print('phrase:', phrase)
	print('bopomofo:', bopomofo)
	print()

def main():
	userphrase.foreach(run_each)


if __name__ == '__main__':
	main()
