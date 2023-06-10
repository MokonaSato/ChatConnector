from flask import Flask, render_template, request
import time
from models.models import ConvContent
from models.database import init_db, db_session
from gpt2.conv_model import generate_reply

app = Flask(__name__)

# getのときの処理
@app.route('/', methods=['GET'])
def get():
	return render_template('index.html')

# postのときの処理
@app.route('/', methods=['POST'])
def post():
    comment = request.form.get('comment')

    #databaseに入力を登録
    conv = ConvContent(name = "あなた", text = comment)
    db_session.add(conv)
    db_session.commit()

    reply = generate_reply(comment)
    
    #databaseに出力を登録
    conv = ConvContent(name = "もこな", text = reply)
    db_session.add(conv)
    db_session.commit()

    all_conv = ConvContent.query.all()
    time.sleep(2)
    return render_template('index.html', all_conv = all_conv)

if __name__ == '__main__':
    init_db()
    db_session.query(ConvContent).delete()
    db_session.commit()
    app.run(debug=True)