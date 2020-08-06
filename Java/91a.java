import java.util.*;
class test
{
void printsum()
{
int sum=0;
for(int i=1;i<=100;i++)
{
sum+=i;
}
System.out.println("The Sum of all integers from 1 to 100 is:"+sum);
}
}

class show
{
public static void main(String args[])
{
test t=new test();
t.printsum();
}
}
