import ctypes
import ctypes.util

libchewing_name = ctypes.util.find_library('chewing')
libchewing = ctypes.CDLL(libchewing_name)


def remove(phrase, bopomofo):
	ctx = libchewing.chewing_new()

	## https://github.com/chewing/libchewing/blob/v0.4.0/include/chewingio.h#L533
	rtn = libchewing.chewing_userphrase_remove(ctx, phrase.encode(), bopomofo.encode())

	ctx = libchewing.chewing_delete(ctx)

	return rtn
