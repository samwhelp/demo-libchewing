#include <stdlib.h>
#include <stdio.h>
#include <chewing.h>

int main(int argc, char *argv[])
{

	int rtn = 0;

	static const char phrase[] = "\xE5\x85\xA7\xE7\xA8\xBD"; /* 內稽 */
	static const char bopomofo[] = "\xE3\x84\x8B\xE3\x84\x9F\xCB\x8B \xE3\x84\x90\xE3\x84\xA7"; /* ㄋㄟˋ ㄐㄧ */

	ChewingContext *ctx = chewing_new();

	/* https://github.com/chewing/libchewing/blob/v0.4.0/include/chewingio.h#L531 */
	rtn = chewing_userphrase_add(ctx, phrase, bopomofo);

	chewing_delete(ctx);

	printf("add ( %d ) userphrase\n", rtn);

	if (rtn > 0) {
		printf("phrase: %s\n", phrase);
		printf("bopomofo: %s\n", bopomofo);
		return EXIT_SUCCESS;
	} else {
		return EXIT_FAILURE;
	}

}
