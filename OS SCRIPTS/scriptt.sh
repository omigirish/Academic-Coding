#!/bin/bash
S=0
n=2
until  [ $n -gt 50 ]
do
S=$(( $S + $n ))
((n+=2))
echo $n
done 
echo $S
