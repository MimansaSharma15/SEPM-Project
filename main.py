from flask import (
    Flask,
    redirect,
    request,
    render_template,
    session,
    g,
)

from medrec.models import (
    users
)

secret_key = 'i love you'
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

app.secret_key = secret_key

users.make_db()


@app.before_request
def security():
    """
    function to check user password for every post \
    request made
    """
    g.user = None
    for i in session:
        print(session[i])
    if 'user_email' in session:
        emails = users.getemail()
        try:
            useremail = [email for email in emails if email[0] == session['user_email']][0]
            g.user = useremail
        except Exception as e:
            print("failed")


@app.route('/', methods=['GET', 'POST'])
def login():
    """

    Returns:
        object:
    """
    g.user = None
    session.pop('user_email', None)
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['pass']

        if users.check_pwd(email, password):
            session['user_email'] = email
            return redirect('/index')
        else:
            return render_template('login.html', error='Wrong Password')

    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['pass']
        email = request.form['email']
        repeat_password = request.form['repeat_password']

        if not password == repeat_password:
            return render_template('signup.html', error="Passwords don't match")
        try:
            users.insert(name=name, password=password, email=email)
            return redirect('/index')

        except Exception as e:
            print(Exception)

    return render_template('signup.html')


@app.route('/index')
def home():
    if g.user:
        return render_template('home.html')
    return redirect('/')


@app.route('/allo')
def allo():
    if g.user:
        return render_template('allopathic.html')
    return redirect('/')


@app.route('/ayur')
def ayur():
    if g.user:
        return render_template('ayurvedic.html')
    return redirect('/')


if __name__ == '__main__':
    app.run(port=5000, debug=True)