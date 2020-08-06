#!/bin/bash
echo "Welcome to basic calculator"
choice=1
while [ $choice -gt 0 ]
do
echo "1.Add 2.Subtract 3.Multiply 4.Divide"
echo -n "Enter your choice: "
read choice
echo -n "Enter first number: "
read x
echo -n "Enter second number: "
read y
case $choice in
1)  sum=`echo "$x+$y" | bc`
    echo "Sum =" $sum ;;
2)  sub=`expr $x - $y `
    echo "sub = $sub" ;;
3)  mul=`echo "$x*$y" | bc`
    echo "mul = $mul" ;;
4)  div=`echo "scale=2;$x/$y" | bc`
    echo "Div = $div" ;;
*) echo "Invalid choice"
esac
echo "Do u want to repeat?"
read choice
done

