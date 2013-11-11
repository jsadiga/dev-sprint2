import flask, flask.views
import os
import functools

app = flask.Flask(__name__)

app.secret_key = "jamboo"
users={'sadiga':'jamboo'}

class main(flask.views.MethodView):
	def get(self):
		return flask.render_template('index.html')

	def post(self):
		if 'logout' in flask.request.form:
			flask.session.pop('username',None)
			return flask.redirect(flask.url_for('index'))
		required={'username','passwd'}
		for r in required:
			if r not in flask.request.form:
				flask.flash("Error: {0} is required.".format(r))
				return flask.redirect(flask.url_for('index'))
		username = flask.request.form['username']
		passwd = flask.request.form['passwd']
		if username in users and users[username]== passwd:
			flask.session['username']=username
		else:
			flask.flash("username password incorrect")
		return flask.redirect(flask.url_for('index'))

def login_required(method):
	@functools.wraps(method)
	def wrapper(*args, **kwargs):
		if 'username' in flask.session:
			return method(*args,**kwargs)
		else:
			flask.flash("username and password required")
			return flask.redirect(flask.url_for('index'))
	return wrapper


	

class remote(flask.views.MethodView):
	def get(self):
		return flask.render_template('remote.html')

	def post(self):
		result = eval (flask.request.form['expression'])
		flask.flash(result)
		return self.get()

class music(flask.views.MethodView):
	@login_required
	def get(self):
		songs = os.listdir('static/music/')
		return flask.render_template('music.html',songs=songs)


app.add_url_rule('/'
	, view_func=main.as_view('index'), methods=['GET', 'POST'])
		

app.add_url_rule('/remote/'
	, view_func=remote.as_view('remote'), methods=['GET', 'POST'])

app.add_url_rule('/music/'
	, view_func=music.as_view('music'), methods=['GET'])

app.debug = True
app.run()