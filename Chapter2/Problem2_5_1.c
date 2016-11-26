#include <stdio.h>


union character {
	unsigned char data;
	struct {
		unsigned char b0 : 1;
		unsigned char b1 : 1;
		unsigned char b2 : 1;
		unsigned char b3 : 1;
		unsigned char b4 : 1;
		unsigned char resmain : 3;
	} bits;
};

union character add(const union character A, const union character B) {
	union character result;
	result.data = 0;

	result.bits.b0 = (A.bits.b0 + B.bits.b0) % 2;
	result.bits.b1 = (A.bits.b1 + B.bits.b1) % 2;
	result.bits.b2 = (A.bits.b2 + B.bits.b2) % 2;
	result.bits.b3 = (A.bits.b3 + B.bits.b3) % 2;
	result.bits.b4 = (A.bits.b4 + B.bits.b4) % 2;

	return result;
}

void decrpyt(const union character *ciphertext, const unsigned int length, const union character key) {
	printf("Key : 0x%02x\t", key.data);
	for (unsigned int index = 0; index < length; index++) {
		union character plaintext = add(ciphertext[index], key);
		if (plaintext.data != 26) {
			printf("%c", 'A' + plaintext.data);
		}
		else{
			printf(" ");
		}

	}
}


int main() {
	union character ciphertext[] = {
		{.data = 0x15},
		{.data = 0x04},
		{.data = 0x15},
		{.data = 0x0B},
		{.data = 0x19},
		{.data = 0x03},
		{.data = 0x0B},
		{.data = 0x15},
		{.data = 0x04},
		{.data = 0x19},
		{.data = 0x1A},
	};

	for (int keyIndex = 0; keyIndex <= 0x1F; keyIndex++) {
		union character key;
		key.data = keyIndex;
		decrpyt(ciphertext, sizeof(ciphertext) / sizeof(ciphertext[0]), key);
		printf("\n");
	}

	//Result
	//Key : 0x11      EVE IS EVIL
	return 0;
}