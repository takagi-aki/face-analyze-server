# FACE ANALYZE SERVER

## 概要

顔写真を受け取って分析した結果を返すのアプリケーションサーバ  

言語: python  
サーバ: uvicorn  
フレームワーク: FastAPI  
その他いろいろ

## 利用

顔分析モジュールのDL
'''
cd ./server
git clone https://github.com/takagi-aki/face-emotion-checker.git fec
cd ../
'''

https://github.com/takagi-aki/face-emotion-checker  
の必要モデルを手動DL

その他必要モジュールをpipインストールする。

## 実行

```
py ./server/main.py
```
