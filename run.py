from flask import Flask, request
#インスタンスを作成、引数には__name__を使用する
app = Flask(__name__)
#ルーティングを定義しいる
#ここでは'/'niにアクセスされると、hello_worldという関数を実行する
@app.route('/')
def hello_world():
    return "Hello World!"
#最後に上記の通り定義したアプリケーションを起動しています。
if __name__ == '__main__':
    app.run()
