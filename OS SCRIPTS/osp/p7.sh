#!/bin/bash
allfiles=`ls *`
for file in $allfiles
do
length=`echo $file| wc -c`
begin=`echo ${file:0:1}`
start=length-4
extension=`echo ${file:$start:3}`
if [ $begin = "p" -a $extension = ".sh" ]
then
echo "Contents of file $file are:"
echo `cat $file`
fi
done
