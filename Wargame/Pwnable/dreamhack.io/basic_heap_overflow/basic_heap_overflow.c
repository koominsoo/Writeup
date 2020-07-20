#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <unistd.h>
#include <string.h>

struct over {
    void (*table)();
};


void get_shell() {
    system("/bin/sh");
}

void table_func() {
    printf("overwrite_me!");
}

int main() {
    char *ptr = malloc(0x20);

    struct over *over = malloc(0x20);


    over->table = table_func;

    scanf("%s", ptr);

    if( !over->table ){
        return 0;
    }

    over->table();
    return 0;
}
