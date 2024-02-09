#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#define MAX_LEN 10000
int main()
{

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    char ch;
    char s[MAX_LEN],sen[MAX_LEN];
    scanf("%c\n",&ch);
    scanf("%s",s);
    scanf(" %[^\n]%*c",sen);
    printf("%c\n%s\n%s",ch,s,sen);
    return 0;
}
