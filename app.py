from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbTest                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index2.html')

## API 역할을 하는 부분
@app.route('/order', methods=['POST'])
def order_apply():
    customer_name = request.form['customer_name']
    order_count = request.form['order_count']
    address = request.form['address']
    phon_num = request.form['phon_num']

    doc = {
        'customer_name': customer_name,
        'order_count': order_count,
        'address': address,
        'phon_num': phon_num
    }
    #디비 어디 테이블에 넣어줄 것인지.
    db.orders.insert_one(doc)
    return jsonify({'result':'success', 'msg': '주문이 성공적으로 작성되었습니다.'})


@app.route('/orderList', methods=['GET'])
def read_orderList():
    orderList = list(db.orders.find({},{'_id':0}))
    return jsonify({'result':'success', 'msg': '리뷰를 받아왔습니다.!','orderList': orderList})


if __name__ == '__main__':
    app.run('localhost', port=5000, debug=True)