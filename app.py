from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id' : 1,
        'title' : 'Data Analyst',
        'location' : 'Nairobi, Kenya',
        'salary' : 'Ksh. 56,550 '
    },
    {
        'id': 2,
        'title': 'Backend Developer',
        'location': 'Mombasa, Kenya',
        'salary': 'Ksh. 44,455 - 154,378'
    },
    {
        'id': 3,
        'title': 'Front End Developer',
        'location': 'Eldoret, Kenya',
        'salary': 'Ksh 45,033 '
    },
    {
        'id': 5,
        'title': 'Remote Software Developer',
        'location': 'Kenya (remote)',
        'salary': 'ksh 83,647'
    },
    {
        'id': 6,
        'title': 'Cyber Security Analyst',
        'location': 'remote'
    }
]

@app.route("/")
def hello_jovian():
    return render_template("home.html", jobs=JOBS)

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

if __name__== "__main__":
    app.run('0.0.0.0', debug=True)