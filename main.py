from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index/<word>')
@app.route('/<word>')
def mars(word):
    return render_template('base.html', title=word)

@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', spec=prof)

@app.route('/list_prof/<lk>')
def list_prof(lk):
    return render_template('list.html', param=lk)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')