rootdir=/localtmp/feng/Checkedout
# mkdir $rootdir

# proj=Chart
# currentdir=${rootdir}/$proj
# mkdir $currentdir
# for bug in $(seq 1 26)
# do 
# 	mkdir ${currentdir}/$bug

# 	defects4j checkout -p $proj -v ${bug}b -w ${currentdir}/$bug/buggy 
	
# 	defects4j checkout -p $proj -v ${bug}f -w ${currentdir}/$bug/fix
# done

proj=Closure
currentdir=${rootdir}/$proj
# mkdir $currentdir
for bug in $(seq 24 133)
do 
	mkdir ${currentdir}/$bug

	defects4j checkout -p $proj -v ${bug}b -w ${currentdir}/$bug/buggy 
	
	defects4j checkout -p $proj -v ${bug}f -w ${currentdir}/$bug/fix
done

proj=Lang
currentdir=${rootdir}/$proj
mkdir $currentdir
for bug in $(seq 1 65)
do 
	mkdir ${currentdir}/$bug

	defects4j checkout -p $proj -v ${bug}b -w ${currentdir}/$bug/buggy 
	
	defects4j checkout -p $proj -v ${bug}f -w ${currentdir}/$bug/fix
done

proj=Math
currentdir=${rootdir}/$proj
mkdir $currentdir
for bug in $(seq 1 106)
do 
	mkdir ${currentdir}/$bug

	defects4j checkout -p $proj -v ${bug}b -w ${currentdir}/$bug/buggy 
	
	defects4j checkout -p $proj -v ${bug}f -w ${currentdir}/$bug/fix
done

proj=Time
currentdir=${rootdir}/$proj
mkdir $currentdir
for bug in $(seq 1 27)
do 
	mkdir ${currentdir}/$bug

	defects4j checkout -p $proj -v ${bug}b -w ${currentdir}/$bug/buggy 
	
	defects4j checkout -p $proj -v ${bug}f -w ${currentdir}/$bug/fix
done
