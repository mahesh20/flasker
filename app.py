from flask import Flask, render_template

#  create a flask instance
app = Flask(__name__)

# create a route decorator
@app.route('/')
def home():
  first_name = "John"
  stuff="This is <strong>bold</strong> text"
  fav_pizza=['cheese','peperoni','pineapple', 'tomato', 30]
  return render_template('index.html', first_name=first_name,stuff=stuff,fav_pizza=fav_pizza)

# eg:localhost:5000/user/mahesh
@app.route('/user/<name>')
def user(name):
  return render_template('user.html',user_name=name)

# invalid URL
@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html'), 404

# Internal Server Error URL
@app.errorhandler(500)
def page_not_found(e):
  return render_template('500.html'), 500




