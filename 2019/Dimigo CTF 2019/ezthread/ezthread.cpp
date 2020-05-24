#include <stdio.h>
#include <stdlib.h>
#include <thread>
#include <Windows.h>

#pragma warning(disable:4996)
#pragma section("flag_data", read)

__declspec(allocate("flag_data")) char table[45] = { 102, 124, 124, 107, 78, 117, 17, 87, 100, 69, 114, 2, 80, 106, 65, 80, 6, 66, 103, 91, 6, 125, 4, 66, 125, 99, 2, 112, 76, 110, 103, 1, 98, 91, 106, 6, 18, 106, 115, 91, 69, 5, 113, 0, 76 };

char flags[45];


void catchDebug(int tid) {
	while (1) {
		if (IsDebuggerPresent()) {
			exit(1);
		}
	}
}

void genFlag(int key1, int key2, int key3) {
	for(int i = 0; i<45; i++) {
		if (i % 3 == 0)
			flags[i] = table[i] ^ key1;
		else if (i % 3 == 1)
			flags[i] = table[i] ^ key2;
		else if (i % 3 == 2) {
			flags[i] = table[i] ^ key3;
		}
	}
}

int main() {
	
	std::thread debug;
	debug = std::thread(catchDebug, 1);
	
	printf("Enter Your key1, key2 :> ");
	
	int key1;
	int key2;
	
	scanf("%d %d", &key1, &key2);
	
	key1 ^= key2 ^= key1 ^= key2;
	int key3 = (key1-3) ^ (key2+3);

	key3 += 10;
	
	key3 &= 0xff;
	
	std::thread flag;
	
	flag = std::thread(genFlag, key1, key2, key3);
	
	flag.join();

	printf("Flag : %s\n", flags);
	getchar();
}
