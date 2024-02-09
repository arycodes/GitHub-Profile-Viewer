from flask import Flask, render_template, url_for , redirect
import datamgmt

app = Flask(__name__)

@app.route('/<string:username>')
def userindex(username):
    userdata = datamgmt.fetch_github_user_data(username)
    userrepos = datamgmt.fetch_github_user_repos(username)
    if userdata and userrepos:
        return render_template('index.html', data=userdata , repos = userrepos)
    elif userdata :
        return render_template('ind.html', data=userdata)
    else: 
        return "no username found"

@app.route('/')
def index():
    return redirect(url_for('userindex', username='arycodes'))

if __name__ == "__main__":
    app.run(debug=True)
