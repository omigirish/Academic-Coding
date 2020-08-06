import java.util.*;
class test
{
void A11()
{
Scanner sc=new Scanner(System.in);
int i=0;

int []A=new int[100];
int max=0;
int min=0;
int sum=0;
int choice,counter=0;
do
{
i++;if(i==1){max=A[i];min=A[i];}
System.out.println("Enter a  no:");
A[i]=sc.nextInt();
if(A[i]>max){max=A[i];}
if(A[i]<min){min=A[i];}
System.out.println("Press 1 to continue!!");
choice=sc.nextInt();
counter++;
sum+=A[i];
}
while(choice==1);
System.out.println("No of elements in array: "+counter);
System.out.println("Maximum value entered: "+max);
System.out.println("Minimum value entered: "+min);
float avg=(float)sum/counter;
System.out.println("Average of the array: "+avg);
}}
class show
{
public static void main(String args[])
{
test t=new test();
t.A11();
}
}
