#include <stdio.h>

int main(int argc, char const *argv[])
{
	int a[5];
	int i;
	int b;
	for(i=1; i<=5; i++){
		scanf("%d",&a[i-1]);
	}
	b = (a[0]+a[1]+a[2]+a[3]+a[4])/5;
	printf("%d",b);
	return 0;
}