predir=buginfo

for proj in Chart Closure Time Lang Math
do
	# bugIndex=1
	file=${predir}/${proj}SourceName.txt
		# echo $file
		# echo ${file%SourceName.txt} # "Source" 
	while read line
	do 
		# echo "File:${line}"
		read -a split <<< $line
		# echo ${#split[@]}
		# echo $split
		bugindex=${split[0]}
		# echo $bugindex
		IFS=. read -r -a pathes <<< "${split[1]}"
		declare -i pathnum
		pathnum=${#pathes[@]}
		# echo $pathnum

		currentrootdir=Checkedout/${proj}/${bugindex}
# Checkedout/Lang/64/buggy/src/main/java/org/apache/commons/lang/enums/ValuedEnum.java
		# pathtest=$currentrootdir/buggy/source
		if [ $proj == "Lang" ];
			then 
			currentbuggydir=$currentrootdir/buggy/src/main/java
			currentfixdir=$currentrootdir/fix/src/main/java
			if [ $bugindex -ge "36" ];
				then
				currentbuggydir=$currentrootdir/buggy/src/java
				currentfixdir=$currentrootdir/fix/src/java
			fi
		elif [ $proj == "Chart" ] 
			then
			currentbuggydir=$currentrootdir/buggy/source
			currentfixdir=$currentrootdir/fix/source
		elif [ $proj == "Closure" ] 
			then
			currentbuggydir=$currentrootdir/buggy/src
			currentfixdir=$currentrootdir/fix/src
		elif [ $proj == "Math" ] 
			then
			currentbuggydir=$currentrootdir/buggy/src/main/java
			currentfixdir=$currentrootdir/fix/src/main/java
			if [ $bugindex -ge "85" ];
				then
				currentbuggydir=$currentrootdir/buggy/src/java
				currentfixdir=$currentrootdir/fix/src/java
			fi
		else #proj == Time
			currentbuggydir=$currentrootdir/buggy/src/main/java
			currentfixdir=$currentrootdir/fix/src/main/java
		fi
		
		for ((i=0; i<$pathnum-2; i++))
		do 
			currentbuggydir=${currentbuggydir}/${pathes[$i]}
			currentfixdir=${currentfixdir}/${pathes[$i]}
		done
		filename=${pathes[$pathnum-2]}.${pathes[$pathnum-1]}
		currentbuggydir=$currentbuggydir/$filename
		currentfixdir=$currentfixdir/$filename

		echo "project : " $proj
		echo "bug No : " $bugindex
		echo "file name : " $currentbuggydir
		diff $currentbuggydir $currentfixdir
		echo
		echo "---------------------------------------------"
		echo
	done < $file
done
