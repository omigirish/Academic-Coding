#!/bin/bash
#input taken from command line parameters.
function sum()
{
sum=o
term=1
while [ $term -le $1 ]
do
((sum=$sum+$term))
((term++))
done
return $sum
}
sum $1
echo "The sum of the sequence is : $?"
