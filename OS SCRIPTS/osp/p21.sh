#!/bin/bash
echo "Enter the file to be scanned: "
read file
contents=`cat $file`
for x in $contents
do
count=`echo $x | wc -c`
count=`echo "$count-1" | bc`
if [ $count -eq 6 ]
then
test=`echo $x | grep "^-\?[0-9]*$"`
count2=`echo $test | wc -c`
if [ $count2 -gt 1 ]
then 
echo "Pincode extracted: $x"
fi
fi
if [ $count -eq 10 ]
then
test2=`echo $x | grep "^-\?[0-9]*$"`
count3=`echo $test2 | wc -c`
if [ $count3 -gt 1 ]
then 
echo "Phone number extracted: $x"
fi
fi
done