# AtCoderWorkspace

AtCoder の作業環境。  
Docker と VSCode (VS Code Remote Development導入済み) があればどこでも環境を再現できる(はず)。

## 初回準備

1. `.devcontainer/.env_` を開き、AtCoder のユーザー名とパスワードを記入する。
1. `.devcontainer/.env` にリネームする。

## 使い方

1. フォルダごと VSCode で開く
1. VSCode左下のマークで、Container でフォルダが開かれていることを確認する。
    * 開かれていなかった場合は、クリックして表示されるメニューから「Remote-Containers: Reopen in Container」を選ぶ。
1. `cd workspace`
1. `acc new --template python <contestID>` でコンテンスト用のディレクトリを作成する。
1. `cd <contestID>/<ID>`
1. main.py ファイルを開き問題を解く。
1. テストを実施する。`oj t -c " python3 ./main.py"`
1. コードを提出する。`acc submit main.py`
    * カレントディレクトリから問題番号等を推測するので注意。

## 環境設定

* `.devcontainer` に VS Code Remote Development の設定ファイルが含まれる。
* `.devcontainer/Dockerfile` で仮想環境が定義されている。
    * npm や apk add したい場合はここに追加。
* `.devcontainer/devcontainer.json` で 起動設定が行わている。
    * Container 側の VSCode の設定を変えたい場合はここに追加/修正。
* `requirements.txt` で pip のパッケージが定義されている。
    * Container 作成時に pip install される。
