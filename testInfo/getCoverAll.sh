# after acquire the list of all test methods within their test class name, use this script to run the coverage of each individual test method

predir=/localtmp/feng/testInfo

currentBugId=a # a marker to store the current bugID

targetBugId=$1

for proj in Chart #Closure Time Lang Math
do
	# bugIndex=1
	file=${predir}/${proj}TestMethods_data.txt
	proj_dir=/localtmp/feng/Checkedout/${proj}
	cov_dir=${proj_dir}/covInfoAll
		# echo $file
		# echo ${file%SourceName.txt} # "Source" 
	if [ ! -d $cov_dir ]; then
		mkdir $cov_dir
	fi
	while read line
	do 
		# echo "File:${line}"
		read -a split <<< $line
		# echo ${#split[@]}
		# echo $split
		bugindex=${split[0]}
		if [ $bugindex != $targetBugId ];then
		continue
		fi
		# echo $bugindex

	#	if [ $bugindex = 5 ]
	#	then
			
			IFS=:: read -r -a testnames <<< "${split[1]}"
			# declare -i pathnum
			#pathnum=${#testnames[@]}
			#echo $pathnum

			currentrootdir=${proj_dir}/${bugindex}

			classname=${testnames[0]}
			methodname=${testnames[2]}
			echo $classname
			echo $methodname
			currentbuggydir=${currentrootdir}/buggy
			# currentfixdir=$currentfixdir/$filename

			echo "project : " $proj
			echo "bug No : " $bugindex
			# echo "file name : " $currentbuggydir
			# diff $currentbuggydir $currentfixdir

			cd $currentbuggydir
			# echo $pwd
			

			if [ "${bugIndex}" != "${currentBugId}" ]
			then
				rm coverage.xml
				defects4j coverage
				#defects4j compile
				mv coverage.xml full_coverage.xml
			fi


			if [ -f "cobertura.ser" ]
			then
				rm cobertura.ser
			fi

			if [ -d ".classes_instrumented" ]
			then
				rm -rf .classes_instrumented
			fi

			currentBugId=${bugIndex}
			ant -f /localtmp/feng/defects4j/framework/projects/defects4j.build.xml -Dd4j.home=/localtmp/feng/defects4j -Dbasedir=$currentbuggydir -Dbuild.compiler=javac1.7 compile.tests 2>&1
			

			ant -f /localtmp/feng/defects4j/framework/projects/defects4j.build.xml -Dd4j.home=/localtmp/feng/defects4j -Dbasedir=$currentbuggydir -Dbuild.compiler=javac1.7 coverage.instrument 2>&1

			ant -f /localtmp/feng/defects4j/framework/projects/defects4j.build.xml -Dd4j.home=/localtmp/feng/defects4j -Dbasedir=$currentbuggydir -Dbuild.compiler=javac1.7 -Dtest.entry.class=$classname -Dtest.entry.method=$methodname run.dev.tests 2>&1
			ant -f /localtmp/feng/defects4j/framework/projects/defects4j.build.xml -Dd4j.home=/localtmp/feng/defects4j -Dbasedir=$currentbuggydir -Dbuild.compiler=javac1.7 coverage.report 2>&1
			
			mv coverage.xml ${cov_dir}/${bugindex}_${classname}_${methodname}.xml
	#		mv ${bugindex}_${classname}_${methodname}.xml /covInfo/ 
			echo
			echo "---------------------------------------------"
			echo
	#	fi



	done < $file
done
