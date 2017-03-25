#include <stdlib.h>
#include <stdio.h>
#include <chewing.h>

int main(int argc, char *argv[])
{

	int rtn = 0;

	unsigned int phrase_len;
	unsigned int bopomofo_len;
	char *phrase;
	char *bopomofo;

	ChewingContext *ctx = chewing_new();

	/* https://github.com/chewing/libchewing/blob/v0.4.0/include/chewingio.h#L531 */
	rtn = chewing_userphrase_enumerate(ctx);
	/* printf("%d\n", rtn); */

	if (rtn != 0) {
		return EXIT_FAILURE;
	}

	/* $ info libchewing -n 'Userphrase Handling' */
	while (chewing_userphrase_has_next(ctx, &phrase_len, &bopomofo_len)) {
		phrase = malloc(phrase_len);
		bopomofo = malloc(bopomofo_len);
		chewing_userphrase_get(ctx, phrase, phrase_len, bopomofo, bopomofo_len);
		printf("\n");
		printf("phrase: %s\n", phrase);
		printf("bopomofo: %s\n", bopomofo);
	}

	chewing_delete(ctx);

	return EXIT_SUCCESS;
}
