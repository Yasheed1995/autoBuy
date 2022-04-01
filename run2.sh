# usage: python3 idx real_buy
for i in {6..11}
do
    echo "running $((i+1)) item!"
    sleep .5
    python3 test.py $i 1 2> /dev/null &
done
