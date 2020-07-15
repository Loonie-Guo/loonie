#/bin/bash
i=-1
while read line  
do
        if [[ $line =~ '---'  ]];then
                ((i++))
        else
                echo $line >> $i.txt
        fi
done < namespace.txt
