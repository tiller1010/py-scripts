#!/bin/bash

if [[ $3 == 'x' || $3 == 'xampp' ]]
then
	hosts.py $2 x
	vhost.py $2
else
	hosts.py $2 h
	homestead.py $1 $2
fi
env.py $1 $2