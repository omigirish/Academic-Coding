#!/bin/perl
for($i=1;$i<=6;$i++)
{
    $d= 2*$i;
    $t=40-$d;
    print "$t";
for($k=0;$k<=$t;$k++)
{
    print " "
}
for($j=1;$j<=$i;$j++)
{
print "$j   "; 
}
print "\n"
}