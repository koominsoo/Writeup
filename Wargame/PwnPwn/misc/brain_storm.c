#include <stdio.h>
#include <time.h>

int main()
{
	setvbuf(stdout, 0, 2, 0);
	setvbuf(stdin, 0, 2, 0);
	setvbuf(stderr, 0, 2, 0);
	srand(time(NULL));
	int a, b, i, answer;
	
	printf("If you solve 300 problems, you can get flag!!\n(What? you solve these just with your hands? boo ----)\n\n");
	
	for(i = 0; i<300; i++) {
		a = rand()%9+1;
		b = rand()%9+1;
		printf("%d + %d = ", a, b);
		scanf("%d", &answer);
		if(answer != a+b) {
			printf("Nop! :)\n");
			return 0;
		}
	}
	printf("\nGREAT Job! here's your flag :)");
	system("cat flag");
	return 0;
}

