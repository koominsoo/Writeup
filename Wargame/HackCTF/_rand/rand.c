#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int main(void){
	int seed=time(NULL);
	srand(seed);
	printf("%d\n",rand());
}
