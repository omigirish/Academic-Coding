# !/bin/bash
echo -n "Enter elements into the array:"
read -a array
echo -n "Enter the element to be searched"
read num
for val in "${array[@]}"
do
if [ $num == $val ]
then
echo "element is present in array"
exit
else
#continue
echo "Element is not present in array"
exit
fi
done	
