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
echo "Enter upper limit of the sequence: "
read limit
sum $limit
echo "The sum of the sequence is : $?"
