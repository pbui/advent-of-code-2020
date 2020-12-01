#!/bin/sh

awk '
    {
    	difference = 2020 - $1

	if ($1 in differences) {
	    print difference * $1
	} else {
	    differences[difference] = $1
	}
    }
'
