from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('hello.html')
@app.route('/a')
def a():
    return 'Hello, A!'

@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == 'GET':
        return "GET으로 전달"
    else:
        # 버튼으로 이미지 url 받기
        # 관상 코드 실행
        url = request.form["url"]
        return f"POST로 전달 <img src = '{url}'>"
if __name__ == '__main__':
    app.run(debug=True)
