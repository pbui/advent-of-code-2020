#!/bin/sh

for number in $(cat $1); do
    pair=$(awk -v TARGET=$((2020 - $number)) '
	{
	    difference = TARGET - $1

	    if ($1 in differences) {
		print difference, $1
	    } else {
		differences[difference] = $1
	    }
	}
    ' < $1)
    if [ -n "$pair" ]; then
    	echo $number $pair | tr ' ' '*' | bc
    	break
    fi
done
