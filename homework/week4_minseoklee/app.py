from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

# HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

# API 역할을 하는 부분
@app.route('/orders', methods=['POST'])
def write_order():
    Name_receive = request.form['Name_give']
    Quantity_receive = request.form['Quantity_give']
    Address_receive = request.form['Address_give']
    Contacts_receive = request.form['Contacts_give']

    # DB에 삽입할 order 만들기
    order = {
       'Name': Name_receive,
       'Quantity': Quantity_receive,
       'Address': Address_receive,
       'Contacts': Contacts_receive,
    }
    # DB orders에 order 저장하기
    db.orders.insert_one(order)

    return jsonify({'result': 'success'})

@app.route('/orders', methods=['GET'])
def read_orders():
    # 1. 모든 orders의 문서를 가져온 후 list로 변환합니다.
    orders = list(db.orders.find({},{'_id':0}))
    # 2. 요청을 성공하면 orders 데이터를 보냅니다.
    return jsonify({'result': 'success', 'orders': orders})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)