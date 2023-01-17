for i in $(seq 1 85)
do
  echo $i
  curl "https://hyogo-de-tabeyou.com/search?areas%5B0%5D=1&page=$i" > page.$i
  sleep 5
done
