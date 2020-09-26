#include<stdio.h>

int main(){
	int a, b, c, d;
	scanf("%d%d%d%d", &a, &b, &c, &d);
	int ans = (a-c) * (b-d);
	if(ans < 0){
		ans *= -1;
	}
	printf("%d\n", ans);
	return 0;
}
