pid=$(ps -fe | grep 'process name' | grep -v grep | awk '{print $2}')
echo "process running: "
echo $pid
pkill -9 "Google Chrome"