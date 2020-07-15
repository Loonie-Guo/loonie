#/bin/bash
read -p "Please enter the volume id that you cannot delete:" volume_id
echo -e "Help information: \n 1.if 'in-use'or'attached': you can try to detach it \n 2.if not:you can continue use this script  \n \nHere is the current state of the volume: \nid:$volume_id \n------------"
mysql -ulonnie -pjay87398919 -e <<EOF "use lonnie;
select deleted from volumes where id='$volume_id';
"
EOF
echo "------------"
read -p "Are you sure you want to delete this volume(s) [y/n]? " selection
if [ "$selection" == "y" ];then
     mysql -ulonnie -pjay87398919 -e <<EOF "use lonnie;
update volumes set deleted=1 where id='$volume_id';
"
EOF
elif [ "$selection" == "n" ];then
     echo "bye"
else
     echo "please enter [y/n]"
fi

