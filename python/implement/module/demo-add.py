#!/usr/bin/env python3

from chewing import userphrase

def main():
	phrase = '內稽'
	bopomofo = 'ㄋㄟˋ ㄐㄧ'

	rtn = userphrase.add(phrase, bopomofo)

	print('add (', rtn, ') userphrase')


if __name__ == '__main__':
	main()
