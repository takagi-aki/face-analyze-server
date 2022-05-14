# FACE ANALYZE SERVER

## 概要

顔写真を受け取って分析した結果を返すのアプリケーションサーバ  

言語: python  
サーバ: uvicorn  
フレームワーク: FastAPI  
その他いろいろ

## 準備

### 顔分析モジュールのDL

'''
cd ./server
git clone https://github.com/takagi-aki/face-emotion-checker.git fec
cd ../
'''

https://github.com/takagi-aki/face-emotion-checker  
の必要モデルを手動DL

その他必要モジュールをpipインストールする。

### ゲームコードのDL

別のフォルダで以下を実行

'''
git clone https://github.com/takagi-aki/fly-js.git new_foldername
cd new_foldername
npm install
npm build-release
'''

new_foldername/distディレクトリのgame.jsをこのレポジトリのgameフォルダ以下にコピーする。

## 実行

```
py ./server/main.py
```
