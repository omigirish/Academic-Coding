#!/bin/perl
print "Pascal triangle builder:  Enter maximum power(Rows): ";
$rows=<STDIN>;
for($i=0;$i<=$rows;$i++)
{
    $d= 2*$i;
    $t=40-$d;
    $ifact=1;
    for($n1=1;$n1<=$i;$n1++)
    {
       $ifact=$ifact*$n1;
    }
for($k=0;$k<=$t;$k++)
{
    print " ";
}
for($j=0;$j<=$i;$j++)
{
    $jfact=1;
    for($n2=1;$n2<=$j;$n2++)
    {
       $jfact=$jfact*$n2; 
    }
    $ijfact=1;
    $diff=$i-$j;
    for($n3=1;$n3<=$diff;$n3++)
    {
       $ijfact=$ijfact*$n3; 
    }
    $d=$jfact*$ijfact;
$element=$ifact/$d;
print "$element   "; 
}
print "\n"
}