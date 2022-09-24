#!/bin/bash

cat toManipulate.txt |urldedupe |grep -e "\.php\|\.asp\|\.htm\|\.txt\|\.xml\|\.asm\|\.jsp\|\.shtm" >> ~/Bounty/params/files-found/toManipulate.txt-files.txt
cat toManipulate.txt |urldedupe |grep -e "\.js" >> ~/Bounty/params/files-found/toManipulate.txt-jsfiles.txt
cat toManipulate.txt |urldedupe |grep "=" >> ~/Bounty/params/all-toManipulate.txt-params.txt
cat toManipulate.txt |urldedupe |grep -Eav ".js|.css|.jpg|.avi|.png|.jpeg|.webp|.woff|.bmp" |grep "=" >~/Bounty/params/toManipulate.txt-params.txt

#cat $@ |urldedupe |grep -e "\.php\|\.asp\|\.htm\|\.txt\|\.xml\|\.asm\|\.jsp\|\.shtm" >> /mnt/vmshares/params/files-found/$@-files.txt
#cat $@ |urldedupe |grep -e "\.js" >> /mnt/vmshares/params/files-found/$@-jsfiles.txt
#cat $@ |urldedupe |grep "=" >> /mnt/vmshares/params/all-$@-params.txt
#cat $@ |urldedupe |grep -Eav ".js|.css|.jpg|.avi|.png|.jpeg|.webp|.woff|.bmp" |grep -Eav "^https://www|utm|=="|grep "=" >/mnt/vmshares/params/$@-params.txt
