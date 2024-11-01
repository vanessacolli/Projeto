from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    
    page = {
        'title': 'CRUDTrecos'
    }
    
    return render_template('_template.html', **page)


if __name__ == '__main__':
    app.run(debug=True)
