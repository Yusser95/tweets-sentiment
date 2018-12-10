
# coding: utf-8

# In[1]:
import os
import json
from flask import Flask
from flask import Markup
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc

app = Flask(__name__)

cwd = os.getcwd()
print(cwd)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+cwd+'/resources/tweets.db'
db = SQLAlchemy(app)


from models import *

 
@app.route("/" , methods =["POST" , "GET"])
def main():
	

	ss = Sentiment.query.order_by(Sentiment.date).all()

	tw = Tweet.query.group_by(Tweet.root_id).all()




	labels =[s.date for s in ss] #["January","February","March","April","May","June","July","August"]
	topic_tweets_sentement =  [s.score for s in ss] #[s.score for s in ss] #[10,9,8,7,6,4,7,8]
	user_tweets_sentement = [s.score for s in ss] #[1,2,3,4,5,6,7,8]



	users = [{'id':t.root_id , 'name':t.root_id} for t in tw] #[{'id':1 , 'name':'option 1'},{'id':2 , 'name':'option 2'},{'id':3 , 'name':'option 3'}]


	tt= Topic.query.all()
	topics = [{'id':t.id , 'name':t.name} for t in tt] #[{'id':1 , 'name':'option 1'},{'id':2 , 'name':'option 2'},{'id':3 , 'name':'option 3'}]

	selected_user = "u"
	selected_topic = "tـ4"

	if request.method == "POST":
		selected_user = request.form.get('user')
		selected_topic = request.form.get('topic')
		print(selected_user[2:] , selected_topic[2:])

		ss= Sentiment.query.filter_by(topic_id=selected_topic[2:]).order_by(Sentiment.date).all()
		topic_tweets_sentement = [s.score for s in ss]
		
		tw = Tweet.query.all()
		selected_tweets = [t.id for t in tw if str(t.root_id) == selected_user[2:]]
		
		print(selected_tweets)
		ss= Sentiment.query.filter(Sentiment.tweet_id.in_(selected_tweets)).order_by(Sentiment.date).all()
		user_tweets_sentement = [s.score for s in ss]



	return render_template('index.html',selected_user=selected_user,selected_topic=selected_topic,users = users ,
	 topics = topics, topic_tweets_sentement=topic_tweets_sentement, user_tweets_sentement=user_tweets_sentement,
	  labels=labels)
 






@app.route("/admin" , methods =["GET"])
def admin():
	return render_template('admin.html')


###########      topic routes





@app.route("/admin/topic/show" , methods =["GET"])
def showtopic():
	# topics = [{'id':1,'name':'sport' , 'words':'("a","b")'}]
	tt= Topic.query.all()
	topics = [{'id':t.id , 'name':t.name , 'words':t.words} for t in tt]
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
		# topic = {'id':1,'name':'sport' , 'words':'("a","b")'}

		t= Topic.query.filter_by(id=id).first()
		topic = {'id':t.id , 'name':t.name , 'words':t.words}
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
    # app.run(host='0.0.0.0', port=5001)
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True, threaded=True)

