#/bin/bash
while read line
do
cheat=$(echo $line | grep "Beijing Normal")
num=5000
    if [[ "$cheat" != "" ]]
then
    if [[ $RANDOM -lt $num ]]
then
    echo ${line/Beijing/East China}>>cheat.txt
    else
    echo $line >> cheat.txt
    fi
    else
    echo $line >> cheat.txt
    fi

done < download_converted_4823.txt

