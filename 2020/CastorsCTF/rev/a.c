#include<stdio.h>
#include<string.h>
void main()

{
  char *param_1="abcdefghijk";
  size_t sVar1;
  int local_10;
  
  sVar1 = strlen(param_1);
  local_10 = 0;
  while (local_10 < (int)sVar1) {
    if (('`' < param_1[local_10]) && (param_1[local_10] < '{')) {
      param_1[local_10] =
           (char)((int)param_1[local_10] + -0x57) +
           (char)(((int)param_1[local_10] + -0x57) / 0x1a) * -0x1a + 'a';
    }
    local_10 = local_10 + 1;
  }
  return;
}

