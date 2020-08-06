#!/bin/bash
allfiles=`ls p*`
for file in $allfiles
do
length=`echo $file| wc -c`
start=length-4
extension=`echo ${file:$start:3}`
if [ $extension = ".sh" ]
then
echo "$file"
fi
done
