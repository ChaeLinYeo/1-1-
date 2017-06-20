#include <stdio.h>

int main(int argc, char const *argv[])
{
	int a;
	int i;
	scanf("%d",&a);
	for(i=0; i<a; i++){
		printf("%c\n",'*');
	}
	return 0;
}