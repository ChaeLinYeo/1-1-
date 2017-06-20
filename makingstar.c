#include <stdio.h>

int main(int argc, char const *argv[])
{
	int a;
	int b;
	for(b=1;b<6;b++){
		for(a=0;a<b;a++){
			printf("%c",'*');
		}
		printf("\n");
	}
	return 0;
}

int main(int argc, char const *argv[])
{
	int a;
	int b;
	for(b=1;b<6;b++){
		for(a=5;b<a;a--){
			printf("%c",' ');
		}
		for(a=0;a<b;a++){
			printf("%c",'*');
		}
		printf("\n");
	}
	return 0;
}