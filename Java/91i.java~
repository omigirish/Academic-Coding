import java.util.*;
class student
{
String name;
int s1[]=new int[6];//Stores marks of 5 subjects.....
int age;
int rollno;
Scanner sc=new Scanner(System.in);
int total;
float percent;
char getgrade(float percent)
{
char grade;
if(percent>=90){grade='A';}
else if(percent>=80 && percent< 90){grade='B';}
else if(percent>=70 && percent< 80){grade='C';}
else if(percent>=60 && percent< 70){grade='D';}
else if(percent>=35 && percent< 60){grade='P';}
else{grade='F';}
return grade;
} 
void getavg(int total)
{
float avg;
avg=(float)total/5;
System.out.println("Your Average is: "+avg);
}
student()
{
System.out.println("Enter your Name: ");
name=sc.next();
System.out.println("Enter your age:");
age=sc.nextInt();
System.out.println("Enter your roll no:");
rollno=sc.nextInt();
System.out.println("Enter your marks in Subject1:");
s1[1]=sc.nextInt();
System.out.println("Enter your marks in Subject2:");
s1[2]=sc.nextInt();
System.out.println("Enter your marks in Subject3:");
s1[3]=sc.nextInt();
System.out.println("Enter your marks in Subject4:");
s1[4]=sc.nextInt();
System.out.println("Enter your marks in Subject5:");
s1[5]=sc.nextInt();
total=s1[1]+s1[2]+s1[3]+s1[4]+s1[5];
percent=(((float)total)/500)*100;
}
student(String name2,int rollno2,int age2,int s2[])
{
name=name2;
rollno=rollno2;
age=age2;
s1=s2;
total=s1[1]+s1[2]+s1[3]+s1[4]+s1[5];
percent=((float)total/500)*100;
}
}
class test
{
public static void main(String args[])
{
String name2;
int s2[]=new int[6];//Stores marks of 5 subjects.....
int age2;
int rollno2;
Scanner sc=new Scanner(System.in);
int total2;
float percent2;
student st=new student();
System.out.println("Mr. "+st.name+":");
System.out.println("Your age is:= "+st.age);
System.out.println("Your rollno is:= "+st.rollno);
System.out.println("Your marks in Subject1= "+st.s1[1]);
System.out.println("Your marks in Subject2= "+st.s1[2]);
System.out.println("Your marks in Subject3= "+st.s1[3]);
System.out.println("Your marks in Subject4= "+st.s1[4]);
System.out.println("Your marks in Subject5= "+st.s1[5]);
System.out.println("Your total marks= "+st.total);
System.out.println("Your percentage= "+st.percent);
st.getavg(st.total);
System.out.println("Your final grade is: "+st.getgrade(st.percent));
System.out.println("Enter your Name: ");
name2=sc.next();
System.out.println("Enter your age:");
age2=sc.nextInt();
System.out.println("Enter your roll no:");
rollno2=sc.nextInt();
System.out.println("Enter your marks in Subject1:");
s2[1]=sc.nextInt();
System.out.println("Enter your marks in Subject2:");
s2[2]=sc.nextInt();
System.out.println("Enter your marks in Subject3:");
s2[3]=sc.nextInt();
System.out.println("Enter your marks in Subject4:");
s2[4]=sc.nextInt();
System.out.println("Enter your marks in Subject5:");
s2[5]=sc.nextInt();
student std=new student(name2,rollno2,age2,s2);
System.out.println("Mr. "+std.name+":");
System.out.println("Your age is:= "+std.age);
System.out.println("Your rollno is:= "+std.rollno);
System.out.println("Your marks in Subject1= "+std.s1[1]);
System.out.println("Your marks in Subject2= "+std.s1[2]);
System.out.println("Your marks in Subject3= "+std.s1[3]);
System.out.println("Your marks in Subject4= "+std.s1[4]);
System.out.println("Your marks in Subject5= "+std.s1[5]);
System.out.println("Your total marks= "+std.total);
System.out.println("Your percentage= "+std.percent);
st.getavg(std.total);
System.out.println("Your final grade is: "+st.getgrade(std.percent));
}
}
