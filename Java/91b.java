import java.util.*;
class test
{
void numtest()
{
Scanner sc=new Scanner(System.in);
System.out.println("Enter a number: ");
int x=sc.nextInt();
int s=0;
if(x%2==0)
{
System.out.println("Number is even.");
}
else{System.out.println("Number is odd.");}
for(int i=2;i<x;i++)
{
if((x%i)==0)
{
System.out.println("Number is not prime.");
 s=1;
break;
}

if(s!=1){System.out.println("Number is prime.");}
}
}
}
class show
{
public static void main(String args[])
{
test t=new test();
t.numtest();
}
}
