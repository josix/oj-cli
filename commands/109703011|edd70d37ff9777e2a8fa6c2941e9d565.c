#include <stdio.h>
#include <stdlib.h>
#include <strings.h>
#include <ctype.h>
char act[10];

void kcom(char *a){
	char *tmp,del[]=",";
	tmp=strtok(a,del);
	a=tmp;
}
int main(){
	int qun1,qun2,i,j,k,h,vali;
	int num1,num2,num3,num4;
	char nig[100],test[10][50][20],tic[10000][5][20],stp[12][15],not[]="\0";
	gets(nig);
	scanf(" %d",&qun1);
	//	printf("stp\n");
	for(i=0;i<qun1;i++){
		scanf(" %s",stp[i]);
		kcom(stp[i]);
		//		printf("%d %s ",i,stp[i]);
	}
	gets(nig); gets(nig); gets(nig); gets(nig);		
	//	set();
	i=0;
	while(1){
		//		printf("\nact\n");
		scanf(" %s",act);
		vali=1;
		//		printf(" act= %s\n",act);
		if(strcmp(act,"RESERVE")==0){
			scanf(" %s %s %s",test[0][0],test[0][1],test[0][2]);
			//		printf(" name=%s stp1=%s stp2=%s\n",test[0][0],test[0][1],test[0][12]);
			kcom(test[0][0]); kcom(test[0][1]); kcom(test[0][2]);
			//			printf(" name=%s stp1=%s stp2=%s\n",test[0][0],test[0][1],test[0][2]);
			num1=-1; num2=-1;
			for(j=0;j<qun1;j++){		
				if(strcmp(test[0][1],stp[j])==0)
					num1=j;
				if(strcmp(test[0][2],stp[j])==0)
					num2=j;
			}
			//			printf("num1=%d num2=%d \n",num1,num2);	
			if(num2<=num1||num1==-1||num2==-1){
				printf("RESERVE FAILED.... (station information has something wrong)\n");
				vali=0;
			}		
			scanf(" %d%*s %s %s",&qun2,test[0][3],test[0][4]);
			kcom(test[0][3]); kcom(test[0][4]);
			//			printf("qun2=%d trn=%s seat=%s\n",qun2,test[0][3],test[0][4]);

			if((qun2>4||qun2<1)&&vali!=0){
				printf("RESERVE FAILED.... (too many seats)\n");
				vali=0;
			}

			for(k=0;k<i;k++){
				if(strcmp(test[0][3],tic[k][3])==0&&strcmp(test[0][4],tic[k][4])==0){
					for(j=0;j<qun1;j++){
						if(strcmp(stp[j],tic[k][1])==0)
							num1=j;
						if(strcmp(stp[j],tic[k][2])==0)
							num2=j;
						if(strcmp(stp[j],test[k][1])==0)
							num3=j;
						if(strcmp(stp[j],test[k][2])==0)
							num4=j;

					}
					if((num3<num2&&num3>num1)||(num4>num1&&num4<num2)||num1==num3){
						printf("RESERVE FAILED.... (repeat seats)\n");
						vali=0;
					}
				}
			}

			for(j=1;j<qun2;j++){
				strcpy(test[j][0],test[0][0]); 
				strcpy(test[j][1],test[0][1]); strcpy(test[j][2],test[0][2]);
				scanf(" %s %s",test[j][3],test[j][4]);
				kcom(test[j][3]); kcom(test[j][4]);
				//				printf("qun2 in  %s %s\n",test[j][3],test[j][4]);
				for(k=0;k<j;k++){
					if(strcmp(test[j][3],test[k][3])==0&&strcmp(test[j][4],test[k][4])==0&&vali!=0){
						printf("RESERVE FAILED.... (repeat seats)\n");
						vali=0;
					}
				}
				for(k=0;k<i;k++){
					if(strcmp(test[j][3],tic[k][3])==0&&strcmp(test[j][4],tic[k][4])==0){
						for(int h=0;h<qun1;h++){
							if(strcmp(stp[h],tic[k][1])==0)
								num1=j;
							if(strcmp(stp[h],tic[k][2])==0)
								num2=j;
							if(strcmp(stp[h],test[k][1])==0)
								num3=j;
							if(strcmp(stp[h],test[k][2])==0)
								num4=j;
						}
						if(vali!=0){
							if((num3>num2&&num3<num1)||(num4<num1&&num4>num4>num2)){
								printf("RESERVE FAILED.... (repeat seats)\n");
								vali=0;
							}
						}
					}
					//					printf("\ntrn %s-seat %s\n",test[i+j][3],test[i+j][4]);
				} 
			}
			if(vali==0)
				continue;
			for(j=0;j<qun2;j++){
				for(k=0;k<5;k++)
					strcpy(tic[i][k],test[j][k]);
				printf("RESERVE SUCCESSED!! -> %s %s %s (%s - %s)\n"
						,tic[i][0],tic[i][3],tic[i][4],tic[i][1],tic[i][2]);
				for(h=0;h<i;h++){
					if(strcmp(tic[i][0],tic[h][0])==0
							&&strcmp(tic[i][3],tic[h][3])==0&&strcmp(tic[i][4],tic[h][4])==0){
						if(strcmp(tic[i][1],tic[h][2])==0){
							strcpy(tic[h][2],tic[i][2]);
							i--;
							//					printf("tic %d=%s %s %s %s %s"
							//							,h,tic[h][0],tic[h][1],tic[h][2],tic[h][3],tic[h][4]);
							break;
						}
						if(strcmp(tic[i][2],tic[h][1])==0){
							strcpy(tic[h][1],tic[i][1]);
							i--;
							//					printf("tic %d=%s %s %s %s %s"
							//							,h,tic[h][0],tic[h][1],tic[h][2],tic[h][3],tic[h][4]);
							break;
						}
					}
				}								
				i++;
			}		
		}
		else if(strcmp(act,"CANCEL")==0){
			for(j=0;j<5;j++){
				scanf(" %s",test[0][j]);
				kcom(test[0][j]);
			}
			num3=-1; num4=-1;
			for(k=0;k<i;k++){
				for(h=0;h<qun1;h++){
					if(strcmp(stp[h],tic[k][1])==0)
						num1=h;
					if(strcmp(stp[h],tic[k][2])==0)                        
						num2=h;
					if(strcmp(stp[h],test[0][1])==0)
						num3=h;
					if(strcmp(stp[h],test[0][2])==0)
						num4=h;                                                    
				}
				if(num3==-1||num4==-1){
					printf("CANCELLATION FAILED.... (cannot find the stations information)\n");
					vali=0;
					break;
				}
				if(strcmp(test[0][0],tic[k][0])==0
						&&strcmp(test[0][3],tic[k][3])==0&&strcmp(test[0][4],tic[k][4])==0){
					if(num3<num4&&num3>=num1&&num4<=num2){
						printf("CANCELLATION SUCCESSED!! %s %s (%s - %s)\n"
								,test[0][3],test[0][4],test[0][1],test[0][2]);
						if(num3==num1&&num4==num2)
							strcpy(tic[k][0],"None");
						else if(num3==num1&&num4!=num2)
							strcpy(tic[k][1],test[0][2]);
						else if(num3!=num1&&num4==num2)
							strcpy(tic[k][2],test[0][1]);
						else{
							strcpy(tic[i][0],tic[k][0]); strcpy(tic[i][3],tic[k][3]); 
							strcpy(tic[i][4],tic[k][4]);
							strcpy(tic[i][1],test[0][2]); strcpy(tic[i][2],tic[k][2]); 
							strcpy(tic[k][2],test[0][1]);
							//					printf("tic %d=%s %s %s %s %s"
							//						,i,tic[i][0],tic[i][1],tic[i][2],tic[i][3],tic[i][4]);
							i++;
						}
						//				printf("tic %d=%s %s %s %s %s"
						//						,k,tic[k][0],tic[k][1],tic[k][2],tic[k][3],tic[k][4]);
						vali=0;
						break;
					}   
				}
			}
			if(vali==1)
				printf("CANCELLATION FAILED.... (cannot find the seat information)\n");
		}
		else if(strcmp(act,"CHECK")==0){
			scanf(" %s %s %s",test[0][0],test[0][3],test[0][4]);
			kcom(test[0][0]);
//			printf("check who= %s %s %s\n",test[0][0],test[0][3],test[0][4]);
			
			int cnt=0,th[6]={0};
			k=0;
			for(j=0;j<i;j++){
				if(strcmp(tic[j][0],test[0][0])==0&&strcmp(tic[j][3],test[0][3])==0
						&&strcmp(tic[j][4],test[0][4])==0){
					cnt++;
//					printf("cnt=%d\n",cnt);
					th[k]=j;
					k++;
				}
			}
			if(cnt==0){
				printf("CHECK FAILED.... (cannot find the reservation data)\n");
				continue;
			}
			if(cnt==1){
				printf("CHECK %s %s %s -> (%s - %s)\n",tic[th[0]][0],tic[th[0]][3]
						,tic[th[0]][4],tic[th[0]][1],tic[th[0]][2]);
//				printf("In cnt 1\n");
				continue;
			}
			else{
				printf("CHECK %s %s %s ->",tic[th[0]][0],tic[th[0]][3],tic[th[0]][4]);
				for(j=0;j<qun1;j++){
					for(h=0;h<cnt;h++){
						if(strcmp(stp[j],tic[th[h]][1])==0)
							printf(" (%s - %s)",tic[th[h]][1],tic[th[h]][2]);
					}
				}
				printf("\n");
			}
		}	
		else{
			printf("\n\n");
			return 0;
		}
	}
	return 0;
}