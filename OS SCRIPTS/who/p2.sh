#Create a firstname.dat file with following data:
#1.Surname    First name    Middlename
#2.Roll no    Batch        Class
#3.DOB(mm/dd/yyyy)
#4.SGPA per semester(seperated by semicolon)
#5.Postal address

#In a single shell program perform the following tasks....
#1.Find and display the path of the filebof punctuations in the file
#4.Calc age and add it after DOB
#5.Calc CGPA and add it after SGPI

#!/bin/bash
d=`pwd`
echo -e "\nCurrent file path is: $d/$1\n"
c=`cat $1`
countv=0
countp=0
for x in $c
do
k=`echo $x | wc -c`
while [  $k -gt 1 ]
do
pos=k-2
char=`echo ${x:$pos:1}`
if [ $char = 'a' -o $char = 'e' -o $char = 'i' -o $char = 'u' -o $char = 'A' -o $char = 'E' -o $char = 'I' -o $char = 'U'  ]
then
((countv++))
fi
if [ $char = '.' -o $char = ',' -o $char = ' ' -o $char = '\"' -o $char = '?' -o $char = ';' -o $char = ':' -o $char = '!' -o $char = '/' -o $char = '\\'  ]
then
((countp++))
fi
((k--))
done
done
n=`sed -n '3p' $1`
d=`echo $n | cut -c4-5`
m=`echo $n | cut -c1-2`
y=`echo $n | cut -c7-10`
yy=`date "+%Y"`
mm=`date "+%m"`
dd=`date "+%d"`
if [ $y -le $yy ]
then
yyy=`expr $yy - $y`
mmm=`expr $mm - $m`

if [ $m -gt $mm ]
then
yyy=`expr $yyy - 1`
mmm=`expr $mmm + 12`
fi
if [ $d -gt $dd ]
then
ddd=`expr $d - $dd`
ddd=`expr 31 - $ddd`
else
ddd=`expr $dd - $d`
fi
fi

s1=`sed -n '4p' $1 | cut -c1-4`
s2=`sed -n '4p' $1 | cut -c6-9`
s3=`sed -n '4p' $1 | cut -c11-14`
sum=`echo "$s1+$s2+$s3" | bc`
cgpi=`echo "scale=2;$sum/3" | bc`

echo -e "No of vowels in the file are: $countv\n"
echo -e "No of punctuations in the file are: $countp\n"
echo -e "Your age : $yyy years $mmm months $ddd days\n"
echo -e "Your CGPI is: $cgpi\n"
echo -e "`sed '3s/$/ AGE= '$yyy'/' $1 >> temp1.dat`"
echo -e "`sed '4s/$/ CGPI= '$cgpi'/' temp1.dat >> temp2.dat`"
echo -e "`sed '4s/$/ CGPI= '$cgpi'/' temp1.dat`"
echo -e "`cat temp2.dat > $1`"
echo -e "`rm temp1.dat`"
echo -e "`rm temp2.dat`"
echo -e "\nFile updated sucessfully\n "
