
# coding: utf-8

# In[1]:

import json
from flask import Flask
from flask import Markup
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////resources/tweets.db'
db = SQLAlchemy(app)


from models import Topic

 
@app.route("/" , methods =["POST" , "GET"])
def main():

	tt = Topic.query.all()
	print(tt)


	labels = ["January","February","March","April","May","June","July","August"]
	topic_tweets_sentement = [10,9,8,7,6,4,7,8]
	user_tweets_sentement = [1,2,3,4,5,6,7,8]

	users = [{'id':1 , 'name':'option 1'},{'id':2 , 'name':'option 2'},{'id':3 , 'name':'option 3'}]
	topics = [{'id':1 , 'name':'option 1'},{'id':2 , 'name':'option 2'},{'id':3 , 'name':'option 3'}]

	selected_user = "u"
	selected_topic = "t"

	if request.method == "POST":
		selected_user = request.form.get('user')
		selected_topic = request.form.get('topic')
		print(selected_user , selected_topic)


	return render_template('index.html',selected_user=selected_user,selected_topic=selected_topic,users = users ,
	 topics = topics, topic_tweets_sentement=topic_tweets_sentement, user_tweets_sentement=user_tweets_sentement,
	  labels=labels)
 







###########      topic routes





@app.route("/admin/topic/show" , methods =["GET"])
def showtopic():
	topics = [{'id':1,'name':'sport' , 'words':'("a","b")'}]
	return render_template('admin/topic/show.html',topics=topics)

@app.route("/admin/topic/delete/<id>" , methods =["GET"])
def deletetopic(id):
	print("deleted " , id)
	return redirect('/admin/topic/show')

@app.route("/admin/topic/edit/<id>" , methods =["GET" , "POST"])
def edittopic(id):
	print(id)
	# edit
	if request.method == "POST":
		name = request.form.get('name')
		words = request.form.get('words')
		print(name,words)
		return redirect('/admin/topic/show')
	# show  one row
	elif request.method == "GET":
		topic = {'id':1,'name':'sport' , 'words':'("a","b")'}
		return render_template('/admin/topic/edit.html',item = topic)
	return "404"


@app.route("/admin/topic/create" , methods =["GET" , "POST"])
def createtopic():
	# edit
	if request.method == "POST":
		name = request.form.get('name')
		words = request.form.get('words')
		print(name,words)
		return redirect('/admin/topic/show')
	# show  one row
	elif request.method == "GET":
		return render_template('/admin/topic/create.html')
	return "404"







###########      user routes





@app.route("/admin/user/show" , methods =["GET"])
def showuser():
	users = [{'id':1,'name':'sport' , 'words':'("a","b")'}]
	return render_template('admin/user/show.html',users=users)

@app.route("/admin/user/delete/<id>" , methods =["GET"])
def deleteuser(id):
	print("deleted " , id)
	return redirect('/admin/user/show')

@app.route("/admin/user/edit/<id>" , methods =["GET" , "POST"])
def edituser(id):
	print(id)
	# edit
	if request.method == "POST":
		name = request.form.get('name')
		words = request.form.get('words')
		print(name,words)
		return redirect('/admin/user/show')
	# show  one row
	elif request.method == "GET":
		user = {'id':1,'name':'sport' , 'words':'("a","b")'}
		return render_template('/admin/user/edit.html',item = user)
	return "404"


@app.route("/admin/user/create" , methods =["GET" , "POST"])
def createuser():
	# edit
	if request.method == "POST":
		name = request.form.get('name')
		words = request.form.get('words')
		print(name,words)
		return redirect('/admin/user/show')
	# show  one row
	elif request.method == "GET":
		return render_template('/admin/user/create.html')
	return "404"







if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)

