#!/bin/bash

python_program="$1"
rm Result.txt
rm GoodResult.txt
touch Result.txt
touch error.txt
touch temp.txt
touch GoodResult.txt

echo "FILENAME:MEMORYPEAK:EXECUTIONTIME" >> GoodResult.txt

for filename in Pythontest2/*;

	do scalene ${filename} > temp.txt 2>error.txt;

	temporary=$(cat error.txt)

	if [[ $temporary == "" ]]
	then

		#echo "temporary =" $temporary
		echo $filename

		temptemp=$(grep ' MB,' temp.txt | awk -F'[[:space:](]+' '{print $6}')
		temptemptemp=$(grep '% (' temp.txt | awk -F'[(]|[)]' '{print $2}')

		if [[ $temptemptemp == "" ]]
		then
			temptemptemp=$(grep ' out of' temp.txt | awk -F'[(]|[)]' '{print $2}')
		fi


		if [[ $temptemp == "" ]]
		then
			echo "Programme trop court"
			echo -e $filename 'est trop court' >> Result.txt
		else
			echo "Programme OK"
			echo -e $filename":"$temptemp":"$temptemptemp >> Result.txt
			echo -e $filename":"$temptemp":"$temptemptemp >> GoodResult.txt
                        echo -e '\n' >> Result.txt
fi

		#echo "No problemo"
	else
		#echo "temporary = " $temporary
		echo $filename
		echo "Programme ERROR"
		echo -e $filename ": \t \t " "ERROR" >> Result.txt
		echo -e '\t Error : ' $temporary >> Result.txt 
		echo -e '\n' >> Result.txt
		#echo "Yes problemo"
	fi


	#cat temp.txt;
 done





#scalene $python_program
