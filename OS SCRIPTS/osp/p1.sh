#!/ bin/bash
countl=`echo | wc -l $1`
for x in $countl
do
count=$x
break
done
echo -e "Number of lines in the file are: $count"
