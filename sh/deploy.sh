#!/bin/bash

#echo $1

if [ "$1" == "all" ]; then
#       install_all
do_all
elif [ "$1" == "lamp" ]; then
    yum -y install httpd mysql mariadb-server php php-mysql samba
else
    printf "Usage:\n. deploy.sh all \n. deploy.sh lamp \n"
fi

do_all(){
#install_all
ignite_daemon
create_soft_links
change_ls_color
}

install_all(){
yum -y install net-tools zip unzip vim elinks tree wget git curl nss libcurl\
httpd mysql mariadb-server php php-mysql samba \
yum -y install epel-release
yum -y install phpmyadmin python36
}

ignite_daemon(){
chkconfig smb on ; service smb start
chkconfig httpd on ; chkconfig mariadb on
service httpd start ; service mariadb start
firewall-cmd --permanent --zone=public --add-service=http
firewall-cmd --permanent --zone=public --add-service=samba
firewall-cmd --reload
}

create_soft_links(){
mkdir ~/config_files
ln -s /etc/httpd  ~/config_files
ln -s /etc/httpd/conf/httpd.conf ~/config_files
ln -s /etc/samba/smb.conf ~/config_files
}


change_ls_color(){
cmd="LS_COLORS=\$LS_COLORS:'di=0;35:' ; export LS_COLORS"

if grep -q "LS_COLORS=" ~/.bashrc
then
printf 'no'
else
printf $cmd >> ~/.bashrc
fi

}
