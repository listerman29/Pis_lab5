from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    login = request.args.get('login')
    if not login:
        return 'Введіть ваш логін у Moodle у адресний рядок'
    return f'Ваш логін у Moodle: {login}'

@app.route('/is-33fiot-23-148')
def student_info():
    return 'Трофімчук Максим, 2 курс, ІС-33'

if __name__ == '__main__':
    app.run(port=8080)