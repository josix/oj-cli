#include<stdio.h>

int main(){
	long long int a, b, c, d;
	scanf("%lld%lld%lld%lld", &a, &b, &c, &d);
	long long int ans = (a-c) * (b-d);
	if(ans < 0){
		ans *= -1;
	}
	printf("%lld\n", ans);
	return 0;
}
