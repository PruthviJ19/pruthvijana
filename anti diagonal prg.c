#include<stdio.h>
#include<conio.h>
main()
{
	int a[4][4],i,j,c;/*initilize array element*/
	printf("enter the number;");/*give a number*/
	scanf("%d",&c);
	for(i=0;i<4;i++)/*for loop condition for i*/
	for(j=0;j<4;j++)/*for loop condition for j*/
	if(i+j==3)/*if both for loop are true*/
	a[i][j]=c;/*if condition is ture*/
	else
	a[i][j]=0;/*if conditon is false*/
	for(i=0;i<4;i++)/*i for loop initilization*/
	{
		for(j=0;j<4;j++)/*if i for loop is true*/
		printf("%d",a[i][j]);/*if j for loo is true*/
		printf("\n");/*to nect line*/
	}
	getch();

}
