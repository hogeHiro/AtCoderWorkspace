#!/bin/bash
# AtCoderのツール類のログインを行うスクリプト

if [ $# -ne 2 ]; then
  echo "指定された引数は$#個です。"
  echo "sh login.sh <USER_NAME> <PASSWORD>"
  exit 1
fi

USER=$1
PASS=$2

echo "🚀🚀🚀Login ACC"
expect -c "
set timeout 10
spawn acc login
expect \"username:\"
send \"${USER}\n\"
expect \"password:*\"
send \"${PASS}\n\"
expect \"OK\"
exit 0
"

echo "🚀🚀🚀Login ACC"
expect -c "
spawn oj login https://beta.atcoder.jp/
expect \"Username:\" 
send \"${USER}\n\"
expect \"Password:\"
send \"${PASS}\n\"
expect \"*Welcome*\"
exit 0
"
