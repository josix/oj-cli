#include<stdio.h>

int main(){
	int* ptr = malloc(256*1024*1024);
	for(int a = 0; a < 256*1024*1024/4; a++){
		ptr[a] = a;
	}
	printf("%d", ptr[256*1024*1024/4]);
	return 0;
}
