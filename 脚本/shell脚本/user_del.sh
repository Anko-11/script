#!/bin/bash

for i in $(seq $2)
do
	userdel $1$i
done

