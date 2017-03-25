#!/usr/bin/env python3

from chewing import userphrase

def main():
	phrase = '內稽'
	bopomofo = 'ㄋㄟˋ ㄐㄧ'

	rtn = userphrase.lookup(phrase, bopomofo)

	print('lookup (', rtn, ') userphrase')


if __name__ == '__main__':
	main()
