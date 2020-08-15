#!/bin/bash
# pythonファイルをAtCoderに提出するシェルスクリプト
# sh cptest.sh <対象ファイル>


filePath=$1
fileName=$(basename $1)
parentDir=$(dirname ${filePath})

echo $parentDir
fileInfo=$(file ${filePath})
if [ "`echo $fileInfo | grep 'Python script'`" ]; then
    cd $parentDir
    acc submit
else
    echo "This file is not Python script"
fi
