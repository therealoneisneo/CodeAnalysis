#!/bin/bash

# using this script to get the raw parsing of all related test methods name from the test.class file


# for proj in Chart Closure Time Lang Math
proj=Chart

	# file=${predir}/${proj}TestName.txt
	testinfo_dir=/localtmp/feng/testInfo
	file=${testinfo_dir}"/"${proj}"TestClasses.txt"
	# echo $file
	# proj_dir=/localtmp/feng/Checkedout/${proj}
	# proj_dir=/localTestSet/
	# test_dir=${proj_dir}/testInfo
	# if [ ! -d $test_dir ]; then
	# 	mkdir $test_dir
	# fi
	preindex=0
	while read line
	do
		# echo "File:${line}"
		read -a split <<< $line
		# echo ${#split[@]}
		# echo ${split[1]}
		bugindex=${split[0]}
		if [ $bugindex != $preindex ];then
			echo "----------" # 10 dashes
			echo "bugindex : "$bugindex
			preindex=$bugindex
		fi
		targetclass=${split[1]}
		# IFS=. read -r -a testnames <<< "${split[1]}"
		# testnames[-2]=${testnames[-2]}"Tests"
		# # echo ${testnames[-2]}
		# testnames[-1]="class"
		# # targetclass=localTestSet/buggy/build-tests

		# if [ $proj = "Chart" ]; then

		# 	targetclass=${proj_dir}"/"${bugindex}"/buggy/build-tests"  # specifically for Chart
		# fi

		# if [ $proj = "Closure" ]; then

		# 	targetclass=${proj_dir}"/"${bugindex}"/buggy/build/test"  # specifically for Chart
		# fi

		# for var in ${testnames[@]}
		# do
		# 	if [ $var = ${testnames[-3]} ]; then
		# 		targetclass=$targetclass"/"$var
		# 		if [ $proj = "Chart" ]; then
		# 			targetclass=$targetclass"/junit"
		# 		fi
		# 	else
		# 		if [ $var = "class" ]; then
		# 		targetclass=$targetclass"."$var
		# 		else
		# 		targetclass=$targetclass"/"$var
		# 		fi
		# 	fi
		# done
		
		echo $targetclass
		javap $targetclass
	done < $file


