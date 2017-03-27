#!/usr/bin/env python
# -*- coding: utf-8 -*-
import chewing

#chewing.Init('/usr/share/chewing', '/tmp')
ctx = chewing.ChewingContext()

phrase = '內稽'
bopomofo = 'ㄋㄟˋ ㄐㄧ'

rtn = ctx.userphrase_lookup(phrase, bopomofo)

print('lookup ( %d ) userphrase' % rtn)
