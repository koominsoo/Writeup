#include<stdio.h>
#include<Windows.h>
struct _FILETIME hey;
typedef unsigned __int64 u_int64 ;
int main(void){
  GetSystemTimeAsFileTime(&hey);
  union
    {
        FILETIME asFileTime ;
        u_int64 asInt64 ;
    } myFileTime;
    myFileTime.asFileTime = hey;
    myFileTime.asInt64 -= 116444736000000000ULL;
    printf("%lld\n",myFileTime.asInt64);
    u_int64 a= 13244342415*10000000-116444736000000000ULL;
    printf("%lld",a);


}