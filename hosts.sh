#!/bin/bash

BASEDIR=$(dirname "$0")
HOSTS_PATH=$(grep HOSTS_PATH $BASEDIR/.env | cut -d '"' -f2)

vi $HOSTS_PATH