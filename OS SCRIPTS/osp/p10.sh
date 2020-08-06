#!/bin/bash
number=1
sum=0
until [ $number -gt 50 ]
do
if [ `expr $number % 2` -eq 0  ]
then
sum=`expr $number + $sum`
fi
((number++))
done
echo "The sum of even numbers upto 50 is $sum"
