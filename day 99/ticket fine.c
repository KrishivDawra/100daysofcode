#include <stdio.h>

int main(void) {
	// your code goes here
	int t,p,q,x;
	scanf("%d",&t);
	int i,d,fine;
	for (i=1;i<=t;i=i+1)
	{
	    scanf("%d %d %d",&x,&p,&q);
	    d=p-q;
	    fine=d*x;
	    printf("%d \n",fine);
	}
}
