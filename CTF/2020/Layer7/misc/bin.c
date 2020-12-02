#include<stdio.h>
#include<stdlib.h>
#include<time.h>
void itoa(int n, char s[])

{
int i, sign;
if((sign = n) <0)
n = -n;
i=0;
do {
s[i++] = n%10 +'0';
} while((n/=10)>0);
if(sign<0)
s[i++]='-';
s[i]='\0';
}
int main(){
	time_t c;
	struct tm tm;
	sleep(2);
	c=time(NULL);
	tm=*localtime(&c);
	char s[3];
	itoa(tm.tm_sec,s);
	puts(s);
}
