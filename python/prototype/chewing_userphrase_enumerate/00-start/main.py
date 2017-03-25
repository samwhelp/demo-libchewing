#!/usr/bin/env python3

import sys
import ctypes
import ctypes.util

libchewing_name = ctypes.util.find_library('chewing')
libchewing = ctypes.CDLL(libchewing_name)


## https://docs.python.org/3/library/ctypes.html
libchewing.chewing_userphrase_has_next.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint), ctypes.POINTER(ctypes.c_uint)]
libchewing.chewing_userphrase_get.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_uint, ctypes.c_char_p, ctypes.c_uint]



phrase_len = ctypes.c_uint(0)
bopomofo_len = ctypes.c_uint(0)


ctx = libchewing.chewing_new()

## https://github.com/chewing/libchewing/blob/v0.4.0/include/chewingio.h#L523
rtn = libchewing.chewing_userphrase_enumerate(ctx)

print(rtn)

## https://github.com/chewing/libchewing/blob/v0.4.0/include/chewingio.h#L525
while libchewing.chewing_userphrase_has_next(ctx, phrase_len, bopomofo_len):
	print('')
	##print('phrase_len:', phrase_len)
	##print('bopomofo_len:', bopomofo_len)
	##print('phrase_len.value:', phrase_len.value)
	##print('bopomofo_len.value:', bopomofo_len.vaue)

	phrase = ctypes.create_string_buffer(phrase_len.value)
	bopomofo = ctypes.create_string_buffer(bopomofo_len.value)
	libchewing.chewing_userphrase_get(ctx, phrase, phrase_len, bopomofo, bopomofo_len)
	print('phrase:', phrase.raw.decode())
	print('bopomofo:', bopomofo.raw.decode())


ctx = libchewing.chewing_delete(ctx)
