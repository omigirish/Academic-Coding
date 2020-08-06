#!/bin/bash
echo "Input a file or directory name: "
read item
if [ -f $item ]
then
	echo "$item is a file"
elif [ -d $item ]
then
	echo "$item is a directory"
else 
	echo "$item was not found."
fi

