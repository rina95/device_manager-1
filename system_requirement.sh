#!/bin/sh

# run by command: ./system_requirement.sh
echo "---> sudo apt-get update";\
sudo apt-get update

echo "---> sudo apt-get -y install libpq-dev postgresql postgresql-contrib";\
sudo apt-get -y install libpq-dev postgresql postgresql-contrib
