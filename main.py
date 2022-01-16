from replit import web
import flask
import time
import sqlite3

from wtforms.validators import DataRequired
import roommate_matching as rm
app = flask.Flask(__name__)

users = web.UserStore()

db = sqlite3.connect('users_and_appts.db')
cursor = db.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS apartment_likes (apartment INTEGER PRIMARY KEY, name TEXT)')
db.commit()
db.close()

traits = ['quality1', 'quality2', 'quality3', 'quality4', 'quality5', 'quality6', 'quality7', 'quality8', 'quality9', 'quality10', 'quality 11']

#@web.authenticated
@app.route("/")
#def is_mod(username):
# Check whether a user has moderator priveleges
#return web.auth.name in ("Scoder12", "Your_username_here")
def index():
    #if web.auth.name:
    #    return web.local_redirect("/home")
    return flask.render_template("index.html")


@app.route("/api/login", methods=["GET", "POST"])
def login():
  return flask.render_template('login.html')
  ''''
    error = None
    if flask.request.method == 'POST':
        if flask.request.form["username"] != "admin" or flask.request.form[
                "password"] != "admin":
            error = "Incorrect Username or Password, try again."
        else:
            return flask.redirect(flask.url_for("/home"))
            
    return flask.render_template('login.html', error=error)
    '''
 

@app.route("/home")
def home():
    #if not web.auth.is_authenticated:
    #    return web.local_redirect("/")
    return flask.render_template("home.html")
    #MOD=is_mod(web.auth.name))


@app.route("/api/listing", methods=["POST", "GET"])
@web.params("body")
def api_listing(body):
    if len(body) == 0:
        return {"error": "Must have something in listing"}, 400
    newlisting = dict(body=body, ts=int(time.time() * 1000), rating=[])
    users.current.get("listings", []).append(newlisting)
    print(f"{web.auth.name} created a new listing: {body!r}")

@app.route('/api/apartment_likes', methods = ["POST", "GET"])
def api_apartment_likes():
  # need to display apartments with their descriptions, and allow the user to "like" their favorite
  return flask.render_template('apartment_likes.html')

users = []

@app.route('/api/questionnaire1', methods=["POST", "GET"])
def questform1():
  user1 = rm.User()
  if flask.request.method == 'POST':
    name = flask.request.form.get('name')

    age = flask.request.form.get('age')


    sex = flask.request.form.get('sex')

    traits_input = []

    for t in traits:
      trait = flask.request.form.get(t)
      if trait.checked == True:
        traits_input.append(t)

    user1.personal(name, age, sex, traits_input)

    flask.session['my_var'] = user1
  
  return flask.render_template('personal_questionnaire.html')
    
@app.route('/api/questionnaire2', methods=["POST", "GET"])
def questform2():
  user1 = flask.session.get('my_var', None)
  if flask.request.method == 'POST':
    name = flask.request.form.get('name')

    age = flask.request.form.get('age')


    sex = flask.request.form.get('sex')

    traits_input = []

    for t in traits:
      trait = flask.request.form.get(t)
      if trait.checked == True:
        traits_input.append(t)

    user1.pref(name, age, sex, traits_input)

    users.append(user1)

  return flask.render_template('roommate_questionnaire.html', title = 'Submit')


#not really sure how to link this part properly to the inputs in the html file, same 
@app.route("/api/signup")
def signup():
   # user_email = EmailField(id="email", validators = [Email()])
   # user_name = StringField(id="username", validators = [DataRequired()])
   # user_pass = PasswordField(id="pass", validators = [InputRequired(), EqualTo('confirm', message='Passwords must match')])
   # confirm = PasswordField("repeat password")
    return flask.render_template("signup.html", title="Sign Up")

@app.route("/load_data")
def load_data():
  return flask.render_template('final_page.html')
    

if __name__ == '__main__':
  web.run(app, debug=True)