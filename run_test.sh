# usage: python3 idx real_buy
for i in {0..2}
do
    echo "running $i item!"
    /usr/local/opt/python@3.7/bin/python3 test.py $i 0 &
done