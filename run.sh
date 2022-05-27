cd ~/autoBuy
sh terminate.sh
str=$(hostname)
str_num=$(echo -e $str | tr '\n' ' ' | sed -e 's/[^0-9]/ /g' -e 's/^ *//g' -e 's/ *$//g' | tr -s ' ' | sed 's/ /\n/g')
for i in $str_num
do 
	if [ "$i" = "777" ]
	then
		echo 
	else
		echo "sh run${i}.sh"
		nohup sh run${i}.sh &
	fi
done

