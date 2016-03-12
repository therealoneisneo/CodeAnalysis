for bug in $(seq 1 26)
do
	defects4j info -p Chart -b $bug
done
