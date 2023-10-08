#!/bin/bash

tail -n +2 grade.txt |while read id name subject grade
do
	if (($grade>70));then
		echo $name $subject $grade
	fi
done 
