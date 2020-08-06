#!/bin/perl
print "Enter the length of the cube: ";
$l=<STDIN>;
chop($l);
if($l<0)
{
    print "Side length is invalid...."
}
else
{
    $vol=$l**3;
    $area=$l**2;
    $p=4*$l;
    print "The Volume area and perimeter of the Cube is $vol, $area, $p respectively.\n"

}