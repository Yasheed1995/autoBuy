# usage: python3 idx real_buy
idx=0
# for i in {01..10}
# do
#     #echo "running $((idx+1)) item!"
#     echo $i
#     echo $idx
#     sleep .5
#     #python3 test.py $idx 1 www111.hung+{$i} &
#     idx+=1
# doni=0
while [ "$(( i += 1 ))" -le 6 ]; do
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
