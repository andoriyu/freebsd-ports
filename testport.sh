#!/bin/sh
PORTS="system"
ZSET="eden"
JAIL="freebsd_12_2-amd64"
JAIL_OLD="freebsd_12_1-amd64"


sudo poudriere testport -J 4:16 -j ${JAIL} -p $PORTS -z $ZSET $1
