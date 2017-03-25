#!/usr/bin/env python3

import ctypes
import ctypes.util

libchewing_name = ctypes.util.find_library('chewing')
libchewing = ctypes.CDLL(libchewing_name)

def userphrase_add(phrase, bopomofo):
	ctx = libchewing.chewing_new()

	## https://github.com/chewing/libchewing/blob/v0.4.0/include/chewingio.h#L531
	rtn = libchewing.chewing_userphrase_add(ctx, phrase.encode(), bopomofo.encode())

	ctx = libchewing.chewing_delete(ctx)

	return rtn

def main():
	phrase = '內稽'
	bopomofo = 'ㄋㄟˋ ㄐㄧ'

	rtn = userphrase_add(phrase, bopomofo)

	print(rtn)


if __name__ == '__main__':
	main()
