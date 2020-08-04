#include<stdio.h>
#include<conio.h>
main()
{
	int r,b,c,tot,avg;/*initilize the variabes*/
	printf("student roll number is:");/*enter the roll numb*/
	scanf("%d",&r);
	printf("enter 1st subject marks;");/*1st subject marks*/
	scanf("%d",&b);
	printf("enter 2nd subject marks;");/*2nd subject marks*/ 
	scanf("%d",&c);
	tot=b+c;/*total marks of 2 subjcts*/
	avg=tot/3;/*average marks*/
	printf("\n\n\t\t informations\n\n");/*display of the informtion*/
	printf("\t student rol number;%d",r);/*display of student roll numb*/
	printf("\t 1st subject marks;%d",b);/*display of 1st subject marks*/
	printf("\t 2nd subject marks;%d",c);/*display of 2nd subject marks*/
	printf("\t average marks;%d",avg);/*display of avg marks*/
	getch();
}
