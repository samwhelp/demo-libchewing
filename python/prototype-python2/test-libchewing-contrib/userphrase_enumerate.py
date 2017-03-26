#!/usr/bin/env python
# -*- coding: utf-8 -*-
import chewing
import ctypes


chewing._libchewing.chewing_userphrase_has_next.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint), ctypes.POINTER(ctypes.c_uint)]
chewing._libchewing.chewing_userphrase_get.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_uint, ctypes.c_char_p, ctypes.c_uint]


phrase_len = ctypes.c_uint(0)
bopomofo_len = ctypes.c_uint(0)


#chewing.Init('/usr/share/chewing', '/tmp')
ctx = chewing.ChewingContext()

## https://github.com/chewing/libchewing/blob/v0.4.0/include/chewingio.h#L523
rtn = ctx.userphrase_enumerate()

## print(rtn)

## https://github.com/chewing/libchewing/blob/v0.4.0/include/chewingio.h#L525
while ctx.userphrase_has_next(phrase_len, bopomofo_len):
	print('')

	phrase = ctypes.create_string_buffer(phrase_len.value)
	bopomofo = ctypes.create_string_buffer(bopomofo_len.value)

	ctx.userphrase_get(phrase, phrase_len, bopomofo, bopomofo_len)

	print('phrase: %s' % phrase.value)
	print('bopomofo: %s' % bopomofo.value)
