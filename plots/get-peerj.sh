#!/bin/bash
for i in $(seq 1429)
do
	mkdir 10.7717%2Fpeerj.$i
	cd 10.7717%2Fpeerj.$i
	wget https://peerj.com/articles/$i/ -O fulltext.html
	grep 'data-rel="supplement' fulltext.html | tr ""\" "\n" | grep -E 'https' > suppdatalinks.txt
	wget -w 1 -i suppdatalinks.txt
	cd /home/ross/suppdata/manualpeerj
	sleep 1
done
