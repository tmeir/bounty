#!/bin/bash

cat $@ |urldedupe |grep -e "\.php\|\.asp\|\.htm\|\.txt\|\.xml\|\.asm\|\.jsp\|\.shtm" > ~/Bounty/params/files-found/$@-files.txt
cat $@ |urldedupe |grep -e "\.js" > ~/Bounty/params/files-found/$@-jsfiles.txt
cat $@ |urldedupe |grep "=" > ~/Bounty/params/all-$@-params.txt
cat $@ |urldedupe |grep -Eav ".js|.css|.jpg|.avi|.png|.jpeg|.webp|.woff|.bmp" |grep "=" >~/Bounty/params/$@-params.txt

