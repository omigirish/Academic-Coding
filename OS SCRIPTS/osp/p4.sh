#!/bin/bash
curdir=`pwd`
echo "$curdir"
echo "The Files in the directory are: "
for item in *
do
if [ -f $item ]
then
echo "$item"
fi
done
echo "The directories in the directory are: "
for item in *
do
if [ -d $item ]
then
echo "$item"
fi
done
