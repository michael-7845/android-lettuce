@echo off
rem ftp服务器ip地址
set server=10.120.2.242
rem ftp服务器上文件所在目录
set remote=/home/ckt/lettuce/viewer
rem 保存到本地的目录
set local=d:\tmp__\viewer

echo root>>ftp.txt
echo 123123>>ftp.txt
echo binary>>ftp.txt
echo lcd %local%>>ftp.txt
echo prompt>>ftp.txt
echo mget %remote% >>ftp.txt
echo bye>>ftp.txt

ftp -s:"ftp.txt" %server%
del ftp.txt
