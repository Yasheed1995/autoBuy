# usage: python3 idx real_buy
# python3 test.py 0 1 &
# python3 test.py 1 1 &
# python3 test.py 2 1 &
# python3 test.py 3 1 &
# python3 test.py 4 1 &
# python3 test.py 5 1 &
# python3 test.py 6 1 &
# python3 test.py 7 1 &
# python3 test.py 8 1 &
# python3 test.py 9 1 &
# python3 test.py 10 1 &
for i in {0..18}
do
    echo "running $i item!"
    python3 test.py $i 1 &
done
