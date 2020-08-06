#!/bin/perl
print "Enter firstname: ";
$fname=<STDIN>;
chop($fname);
print "Enter lastname: ";
$lname=<STDIN>;
chop($lname);
$name=$fname." ".$lname;
print "My name is $name \n";
print "The reverse of myname is ",scalar reverse("$name"),"\n";