import java.util.*;
class test
{
void data()
{
int []s1=new int[5];
int []s2=new int[5];
int []s3=new int[5];
int []s4=new int[5];
int total;float percent;
String []name=new String[5];
int []s5=new int[5];
char []grade=new char[5];
Scanner sc=new Scanner(System.in);
for(int k=0;k<5;k++)
{
System.out.println("Enter your Name: ");
name[k]=sc.next();
System.out.println("Enter your marks in Subject1:");
s1[k]=sc.nextInt();
System.out.println("Enter your marks in Subject2:");
s2[k]=sc.nextInt();
System.out.println("Enter your marks in Subject3:");
s3[k]=sc.nextInt();
System.out.println("Enter your marks in Subject4:");
s4[k]=sc.nextInt();
System.out.println("Enter your marks in Subject5:");
s5[k]=sc.nextInt();
total=s1[k]+s2[k]+s3[k]+s4[k]+s5[k];
percent=(((float)total)/500)*100;
if(percent>=90){grade[k]='A';}
else if(percent>=80 && percent< 90){grade[k]='B';}
else if(percent>=70 && percent< 80){grade[k]='C';}
else if(percent>=60 && percent< 70){grade[k]='D';}
else if(percent>=35 && percent< 60){grade[k]='P';}
else{grade[k]='F';}
}
float avg;
for(int k=0;k<5;k++)
{
System.out.println("Student "+name[k]+":");
System.out.println("Your marks in subject1 is:"+s1[k]);
System.out.println("Your marks in subject2 is:"+s2[k]);
System.out.println("Your marks in subject3 is:"+s3[k]);
System.out.println("Your marks in subject4 is:"+s4[k]);
System.out.println("Your marks in subject5 is:"+s5[k]);
 total=s1[k]+s2[k]+s3[k]+s4[k]+s5[k];
 avg=((float)total)/5;
 percent=(((float)total)/500)*100;

System.out.println("Total Marks:"+total);
System.out.println("Your Average is:"+avg);
System.out.println("Your percentage is:"+percent);
System.out.println("Your grade is:"+grade[k]);
}
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
