#! /bin/bash

cat $@ | cut -d "/" -f 3 |sort|urldedupe >raw-list-hosts.txt
httpx -l raw-list-hosts.txt -sc -o h-list
cat h-list |grep -Eav "\[\]" |cut -d " " -f 1 |cut -d "/" -f 3|sort |urldedupe >>list-hosts.txt
cat list-hosts.txt|urldedupe |sort >r-list-hosts && cat r-list-hosts |urldedupe |sort >list-hosts.txt
