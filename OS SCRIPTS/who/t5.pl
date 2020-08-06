#!/bin/perl
print"Enter the number to be checked:";
$n=<STDIN>;
chop($n);
$flag=0;
for($i=2;$i<$n;$i++)
{
if($n%$i==0)
{
$flag=1;
break;
}
}
if($flag==1)
{
print "$n is not prime\n";
}
else
{
print"$n is prime\n";
}

