# ChatConnector
## 概要 (Overview)
自前でファインチューニングしたrinnaの日本語GPT-2モデルと対話するためのインターフェースとなるWebアプリケーションです。  
The Interface: A Web Application for Interacting with a Custom Fine-Tuned rinna Japanese GPT-2 model. 

## 使用言語など (Language)
- Python 3.8.14
- Flask 2.2.3
- Flask-SQLAlchemy 3.0.3
- transformers 4.23.1

## 使い方 (Usage)
`git clone https://github.com/MokonaSato/ChatConnector.git`でカレントディレクトリにダウンロードします。   
Please use code `git clone https://github.com/MokonaSato/ChatConnector.git` to download files to the current directory.

`pip install -r requirements.txt`でrequirements.txtに記載されたライブラリをダウンロードします。   
Please use code `pip install -r requirements.txt` to download libraries written in requirements.txt.  

staticディレクトリ配下にcat.pngという名前の画像ファイルを格納してください。  
Please store an image file named 'cat.png' under the 'static' directory.

gpt2ディレクトリ配下にoutputという名前のファインチューニング済みモデルを格納してください。  
Please store a Fine-Tuned model named 'output' under the 'gpt2' directory.

`python3 app.py`でapp.pyを実行してください。
Please use code`python3 app.py` to execute this application.

## 使用規約（License）
The source code is licensed MIT, see LICENSE.
