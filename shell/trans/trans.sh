#/bin/bash
while read line
do
trans en:zh-TW "$line"|sed -n '3p'
done < shoope
echo
while read line
do
trans en:th "$line"|sed -n '3p'
done < shoope
echo
while read line
do
trans en:vi "$line"|sed -n '3p'
done < shoope
