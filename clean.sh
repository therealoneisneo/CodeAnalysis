rootdir=/localtmp/feng/Checkedout
# run this script to clear the covInfo folder of all checked folder


proj=Chart
currentdir=${rootdir}/$proj

for bug in $(seq 1 26)
do 
	rm -rf ${currentdir}/${bug}/buggy/covInfo
done


proj=Closure
currentdir=${rootdir}/$proj

for bug in $(seq 1 133)
do 
	rm -rf ${currentdir}/${bug}/buggy/covInfo
done

proj=Lang
currentdir=${rootdir}/$proj

for bug in $(seq 1 65)
do 
	rm -rf ${currentdir}/${bug}/buggy/covInfo
done

proj=Math
currentdir=${rootdir}/$proj

for bug in $(seq 1 106)
do 
	rm -rf ${currentdir}/${bug}/buggy/covInfo
done

proj=Time
currentdir=${rootdir}/$proj

for bug in $(seq 1 27)
do
	rm -rf ${currentdir}/${bug}/buggy/covInfo
done

