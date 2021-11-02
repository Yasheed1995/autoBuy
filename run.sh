# usage: python3 idx real_buy
for i in {0..4}
do
    echo "running $i item!"
    python3 test.py $i 1 &
done
