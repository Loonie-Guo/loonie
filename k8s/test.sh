#/bin/bash

bash cut.sh
j=`cat node.txt |wc -l`
arr=($(cat node.txt))
for ((n=0;n<=j-1;n++))
do
awk '{print "'${arr[$n]}'",$0>>"main.txt"}' $n.txt
done
sed -i "s/\(//g" main.txt
sed -i "s/\)//g" main.txt
