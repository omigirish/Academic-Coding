import java.io.*;
import java.util.*;
class show
{

}
class Test
{
 public static void main(String args[]) throws IOException
{
BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
Scanner sc=new Scanner(System.in);
System.out.println("Enter your first name: ");
String fname=br.readLine();
System.out.println("Enter your Second name: ");
String lname=br.readLine();
System.out.println("Your Full name is: "+fname+" "+lname);
System.out.println("Enter your age: ");
String sage=br.readLine();
int age=Integer.parseInt(sage);
age+=5;
System.out.println("Your age after 5 years will be: "+age);
System.out.println("Enter your address: ");
String add=sc.nextLine();
System.out.println("Your address is: "+add);
System.out.println("Enter your marks: ");
int marks=sc.nextInt();
System.out.println("Enter your gender M/F: ");
char gend=(char)br.read();
System.out.println("Your Gender is: "+gend);
System.out.println("Enter your name initial: ");
char ini=sc.next().charAt(0);
System.out.println("Your name initial is: "+ini);
System.out.println("Are you above 18?");
boolean x=sc.nextBoolean();
System.out.println("You answered: "+x);

}
}
