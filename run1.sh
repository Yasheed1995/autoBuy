# usage: python3 idx real_buy
for i in {0..5}
do
    echo "running $((i+1)) item!"
    python3 test.py $i 1 2> /dev/null &
done