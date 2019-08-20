#!/bin/bash

OLD_PATH=$PWD

cd $NAV_HOME/src 

if python3 main.py $OLD_PATH; then 
	source $NAV_HOME/tmp/navigate_to.sh
	rm $NAV_HOME/tmp/navigate_to.sh
else
	# Program ended with exception	
	cd $OLD_PATH
fi
