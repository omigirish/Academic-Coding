#!/bin/bash
echo "Enter the name of source data file: "
read file
AT=`sed -n '1p' $file | cut -c5-6`
COA=`sed -n '2p' $file | cut -c5-6`
CS=`sed -n '3p' $file | cut -c5-6`
PYT=`sed -n '4p' $file | cut -c5-6`
CN=`sed -n '5p' $file | cut -c5-6`
DOB=`sed -n '6p' $file`
dd=`echo "$DOB" | cut -c1-2`
mm=`echo "$DOB" | cut -c4-5`
yyyy=`echo "$DOB" | cut -c7-10`
nowd=`date +%d`
nowm=`date +%m`
nowy=`date +%Y`
if [ $yyyy -lt $nowy ]
then
if [ $mm -lt $nowm  ]
then
age=`echo "$nowy-$yyyy" | bc`
echo "Your age is $age"
elif [ $mm -eq $nowm -a $dd -le $nowd ]
then
age=`echo "$nowy-$yyyy" | bc`
echo "Your age is $age"
else
age=`echo "$nowy-$yyyy-1" | bc`
echo "Your age is $age"
fi
else
echo "Invalid age...."
fi
#assumning 5 grade points for AT COA & CN
#assuming 3 grade points for CS and PYT
cgpa=`echo "scale=2;(5*($AT+$COA+$CN)+3*($PYT+$CS))/21" | bc`
echo "Your CGPA is: $cgpa"
