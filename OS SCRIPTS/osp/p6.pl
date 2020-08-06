#!/bin/perl
print "Enter principal amount: ";
$p=<STDIN>;
print "Enter rate of interest: ";
$r=<STDIN>;
print "Enter Time period: ";
$t=<STDIN>;
chop($p);
chop($r);
chop($t);
$SI= $p*$r*$t/100;
$amt=$p+$SI;
$buff=$r/100;
$temp=(100/100+$buff)**$t;
$CI=$p*$temp;
print "Balance after $t years through SI & CI is Rs.$amt & RS.$CI respectively.\n";