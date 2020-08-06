import java.util.*;
class test
{
void data()
{
Scanner sc=new Scanner(System.in);
System.out.println("Enter your Name: ");
String s=sc.nextLine();
System.out.println("Enter your marks in Subject1:");
int a=sc.nextInt();
System.out.println("Enter your marks in Subject2:");
int b=sc.nextInt();
System.out.println("Enter your marks in Subject3:");
int c=sc.nextInt();
System.out.println("Enter your marks in Subject4:");
int d=sc.nextInt();
System.out.println("Enter your marks in Subject5:");
int e=sc.nextInt();
int total=a+b+c+d+e;
float avg=((float)total)/5;
float percent=(((float)total)/500)*100;
char grade;
if(percent>=90){grade='A';}
else if(percent>=80 && percent< 90){grade='B';}
else if(percent>=70 && percent< 80){grade='C';}
else if(percent>=60 && percent< 70){grade='D';}
else if(percent>=35 && percent< 60){grade='P';}
else{grade='F';}
System.out.println("Student "+s+":");
System.out.println("Your marks in subject1 is:"+a);
System.out.println("Your marks in subject2 is:"+b);
System.out.println("Your marks in subject3 is:"+c);
System.out.println("Your marks in subject4 is:"+d);
System.out.println("Your marks in subject5 is:"+e);
System.out.println("Total Marks:"+total);
System.out.println("Your Average is:"+avg);
System.out.println("Your percentage is:"+percent);
System.out.println("Your grade is:"+grade);
}
}
class show
{
public static void main(String args[])
{
test t=new test();
t.data();
}
}
