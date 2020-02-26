#!/bin/bash

#when option 'update' or '-u' is given, crawls data 
if [ $# -eq 1 ] 
then
    if [ $1 == "--update" -o $1 == "-u" ]
    then 
        python ./passmarksynchronizer.py -a
        python ./naversynchronizer.py -a
        echo "Crawling and Synchronization complete"
    fi
#otherwise just synchronizes db with local data
else
	python ./passmarksynchronizer.py -s
    python ./naversynchronizer.py -s
    python ./programsynchronizer.py
    python ./gamesynchronizer.py
    echo "Synchronization complete"
fi
