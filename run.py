from flask import Flask, request
#インスタンスを作成、引数には__name__を使用する
app = Flask(__name__)
#ルーティングを定義しいる
#ここでは'/'にアクセスされると、hello_worldという関数を実行する
@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/flask')
def hello_sample():
    return "Hello Flask."

@app.route('/user/<user_id>')
def hello_person(user_id):
    return "Hello " + user_id

@app.route('/test', methods=['GET', 'POST'])
def post_test():
    if request.method == 'GET':
        pass
    else:
        pass
    return '0'

#最後に上記の通り定義したアプリケーションを起動しています。
if __name__ == '__main__':
    app.run()