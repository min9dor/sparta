from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html')

## API 역할을 하는 부분
@app.route('/mypage')       # 같은 URL 내 함수명이 같으면 안됨.
def mypage():
   return 'This is Mypage!'

@app.route('/test', methods=['POST'])
def test_post():
   title_receive = request.form['title_give']
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 POST!'})

@app.route('/test', methods=['GET'])
def test_get():
   title_receive = request.args.get('title_give')
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 GET!'})

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)  # debuging mode가 켜져 있으면, 저장할 때마다 코드를 자동으로 재실행.