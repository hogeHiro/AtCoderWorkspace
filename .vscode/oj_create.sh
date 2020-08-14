#!/bin/bash
# atCoderからプロジェクトファイルを作るためのシェルスクリプト

workspaceDir="workspace"

cd $workspaceDir
read -p "Input Contest ID (Ex: abc101):" id
acc new --template python "${id}"
