import java.util.*;
class test
{
void A11()
{
Scanner sc=new Scanner(System.in);
int temp=0;
System.out.println("Enter array size: ");
int n =sc.nextInt();
int []A=new int[n];
for(int i=0;i<n;i++)
{
    System.out.println("Enter a number.... ");
    A[i]=sc.nextInt();
}
System.out.println("Your input array is: ");
for(int i=0;i<A.length;i++)
{
    System.out.print(A[i]+" ");
}
for(int i=0;i<((A.length)/2);i++)
{
    temp=A[i];
    A[i]=A[A.length-i-1];
    A[A.length-i-1]=temp;
}
System.out.println();
System.out.println("Your output array is: ");
for(int i=0;i<A.length;i++)
{
    System.out.print(A[i]+" ");
}
}
}
class show
{
public static void main(String args[])
{
test t=new test();
t.A11();
}
}
