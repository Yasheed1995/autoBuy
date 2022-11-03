echo "kill all chrome!"
pid=$(ps -fe | grep 'chrome' | grep -v grep | awk '{print $2}')
#echo "process running: "
#echo $pid
pkill -9 "Thorium"
echo "terminated!"
