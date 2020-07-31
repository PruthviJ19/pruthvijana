#include<stdio.h>/*library function*/
#include<conio.h>/*library function*/
static int i=1;/*specify i value as 1*/
main()
{
	int j;/*initilize j*/
	for(j=1;j<=5;j++);/*j for loop condition*/
	fun();/*calling the function*/
	getch();
}
fun()/*called function*/
{
 printf("\n%d",i);/*printing the i value*/
 i=i+1;/*increment of i*/
}
