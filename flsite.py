from flask import Flask, render_template, url_for


app = Flask(__name__)


@app.route('/')
def registration():
    print(url_for('registration'))
    return render_template('registration.html')

@app.route('/authorization')
def authorization():
    print(url_for('authorization'))
    return render_template('authorization.html')

@app.route('/home_page')
def home_page():
    print(url_for('home_page'))
    return render_template('home_page.html')


if __name__ == '__main__':
    app.run(debug=True)
