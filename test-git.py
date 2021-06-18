from flask import Flask

app = Flask(__name__)

@app.route('/')
def api_root():
    return 'test-git.py'

if __name__ == '__main__':
    app.run(debug=True)
