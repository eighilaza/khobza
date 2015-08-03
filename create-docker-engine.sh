#!/bin/bash

if [ -z $1 ]; then
        echo "usage: ./create-docker-engine.sh machineName"
        exit
fi

echo "Please enter your Openstack password:"
read -sr PASSWORD_INPUT

LOG_FILE=$(date '+%Y-%m-%d-%R')-create-docker-engine.log
touch $LOG_FILE

docker-machine --debug create \
--driver openstack \
--openstack-auth-url http://10.*.*.*:5000/v2.0 \
--openstack-username admin \
--openstack-password $PASSWORD_INPUT \
--openstack-tenant-name admin \
--openstack-flavor-id 2 \
--openstack-image-id e074cc61-fb01-4766-9d8a-efb034efbb26 \
--openstack-net-name net04 \
--openstack-sec-groups all-ports-open \
--openstack-floatingip-pool net04_ext \
--openstack-ssh-user ubuntu \
$1 | tee -a $LOG_FILE

if [[  $?==0 ]]; then
        echo "Provision succeeded. Please wait while image is being pulled."
        docker-machine ssh $1 "sudo echo 'export http_proxy=\"http://10.*.*.*:****/\"' | sudo tee -a /etc/default/docker > /dev/null"
        docker-machine ssh $1 "sudo service docker restart" | tee -a $LOG_FILE
        docker-machine ssh $1 "sudo docker run -d --name jenkins -u jenkins -p 8080:8080 -p 50000:50000 -v /home/ubuntu:/var/jenkins_home jenkins" | tee -a $LOG_FILE
        eval "$(docker-machine env $1)"
        echo "Script terminated"
else
        echo "Provision failed"
fi
