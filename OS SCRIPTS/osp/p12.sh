# !/bin/bash
echo -n "Enter elements of an array:"
read -a array
echo -n "Enter the element to be searched: "
read num
flag=0
for val in "${array[@]}"
do 
	if [ $num == $val ]
	then 
		echo "Element is present in the array"
		flag=1
		exit
	fi
done
if [ $flag == 0 ]
then	
	echo "Element not present in array. "
fi


		
