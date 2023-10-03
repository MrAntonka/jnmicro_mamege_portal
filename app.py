from flask import Flask, render_template

app = Flask(__name__)

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/device_group')
def device_group():
    return render_template('devide_group.html')


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
