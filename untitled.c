#include <stdio.h>

int main(int argc, char const *argv[])
{
	int a;
	int b;
	scanf("%d %d", &a, &b);
	printf("%d\n %d\n %d\n %d\n %d\n", a+b, a-b, a*b ,a/b, a%b);
	return 0;
}