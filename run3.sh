# usage: python3 idx real_buy
i=20
idx=20
while [ "$(( i += 1 ))" -le 30 ]; do
    zi=$( printf '%03d' "$i" )
    # echo "$zi"
    # echo "www111.hung+${zi}@gmail.com"
    echo "running $((idx+1)) item!"
    # echo "$idx"
    python3 test.py $idx 1 "www111.hung+${zi}@gmail.com" &
    ((idx=idx+1))
    sleep 0.9
    # other code using "$zi"
done