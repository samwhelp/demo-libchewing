
# demo-libchewing


## 原始討論串

* [討論「請教 ezgo13 的 fcitx-chewing 輸入法之自建字庫問題」](https://www.ubuntu-tw.org/modules/newbb/viewtopic.php?post_id=356758#forumpost356758)


## Prototype

* [chewing_userphrase_add](python/prototype/chewing_userphrase_add/00-start/main.py) ([c](https://github.com/samwhelp/demo-libchewing/blob/master/c/prototype/chewing_userphrase_add/00-start/main.c)) ([chewingio.h](https://github.com/chewing/libchewing/blob/v0.4.0/include/chewingio.h#L531)) ([chewingio.c](https://github.com/chewing/libchewing/blob/v0.4.0/src/chewingio.c#L1985))
* [chewing_userphrase_enumerate](python/prototype/chewing_userphrase_enumerate/00-start/main.py) ([c](https://github.com/samwhelp/demo-libchewing/blob/master/c/prototype/chewing_userphrase_enumerate/00-start/main.c)) ([chewingio.h](https://github.com/chewing/libchewing/blob/v0.4.0/include/chewingio.h#L523)) ([chewingio.c](https://github.com/chewing/libchewing/blob/v0.4.0/src/chewingio.c#L1847))
* [chewing_userphrase_lookup](python/prototype/chewing_userphrase_lookup/00-start/main.py) ([c](https://github.com/samwhelp/demo-libchewing/blob/master/c/prototype/chewing_userphrase_lookup/00-start/main.c)) ([chewingio.h](https://github.com/chewing/libchewing/blob/v0.4.0/include/chewingio.h#L535)) ([chewingio.c](https://github.com/chewing/libchewing/blob/v0.4.0/src/chewingio.c#L2055))
* [chewing_userphrase_remove](python/prototype/chewing_userphrase_remove/00-start/main.py) ([c](https://github.com/samwhelp/demo-libchewing/blob/master/c/prototype/chewing_userphrase_remove/00-start/main.c)) ([chewingio.h](https://github.com/chewing/libchewing/blob/v0.4.0/include/chewingio.h#L533)) ([chewingio.c](https://github.com/chewing/libchewing/blob/v0.4.0/src/chewingio.c#L2026))


## 相關連結

* https://gist.github.com/mitya57/1e49b079a91942782f62 ([1](https://www.ubuntu-tw.org/modules/newbb/viewtopic.php?post_id=356524#forumpost356524))
* https://docs.python.org/3/library/ctypes.html
* https://docs.python.org/2/library/ctypes.html


## Source Code 參考網址

* https://github.com/chewing/libchewing/blob/master/include/chewingio.h
* https://github.com/chewing/libchewing/blob/master/test/test-userphrase.c
* https://github.com/chewing/chewing-editor/blob/0.0.1/src/model/UserphraseModel.cpp#L199
* https://github.com/fcitx/fcitx-chewing/blob/master/src/eim.c
