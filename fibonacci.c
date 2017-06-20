#include <stdio.h>

int fibonacci(int n){
	if (n==0){
		printf("0");
		return 0;
	}
	else if (n==1){
		printf("1");
		return 1;
	}
	else{
		return fibonacci(n-1)+fibonacci(n-2);
	}
}


int main(){
	int upto = 0, sum = 0;
	scanf("%d", &upto);
	for(int i=0; i<upto; i++){
		prinf("%4d", fibonacci(i));
		sum += fibonacci(i);
	}
	printf(sum)
}