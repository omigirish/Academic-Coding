import java.util.*;
import java.lang.Math;
class test
{
void calc()
{
Scanner sc=new Scanner(System.in);
System.out.println("Menu(Operation_Symbol)");
System.out.println("Addition -(+)");
System.out.println("Subtraction -(-)");
System.out.println("Multiplication-(*)");
System.out.println("Division-(/)");
System.out.println("Logarithm-(l)");
System.out.println("Exponential-(e)");
System.out.println("Enter your choice:");
String s=sc.nextLine();
char choice=s.charAt(0);
switch(choice)
{
case '+':
{
System.out.println("Enter 1st number:");
int x=sc.nextInt();
System.out.println("Enter 1st number:");
int y=sc.nextInt();
System.out.println("Sum of numbers is"+(x+y));
break;
}
case '-':
{
System.out.println("Enter 1st number:");
int x=sc.nextInt();
System.out.println("Enter 1st number:");
int y=sc.nextInt();
System.out.println("Subtraction of numbers is"+(x-y));
break;
}
case '*':
{
System.out.println("Enter 1st number:");
int x=sc.nextInt();
System.out.println("Enter 1st number:");
int y=sc.nextInt();
System.out.println("Multiplication of numbers is: "+(x*y));
break;
}
case '/':
{
System.out.println("Enter 1st number:");
int x=sc.nextInt();
System.out.println("Enter 1st number:");
int y=sc.nextInt();
System.out.println("Divison of numbers is: "+(x/y));
break;
}
case 'e':
{
System.out.println("Enter a number:");
int x=sc.nextInt();
System.out.println("Enter power(Index) value:");
double y=sc.nextDouble();
double p=Math.pow(x,y);
System.out.println("x"+" to the power "+"y"+"is: "+p);
break;
}
case 'l':
{
System.out.println("Enter the number:");
double x=sc.nextDouble();
double l=Math.log(x);
System.out.println("Log value of the number is: "+l);
break;
}
default: {System.out.println("Invalid Input"); break;}
}}
} 

class show
{
public static void main(String args[])
{
test t=new test();
t.calc();
}
}
