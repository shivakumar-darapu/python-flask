import random
from builtins import print
from flask import Flask, render_template, url_for, request, redirect
# from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import mysql.connector
import os


app = Flask(__name__)


# app.config['SQLALCHEMY_DATABASE_URI'] =

@app.route('/Hello')
def hello():
    return "Hello World!"


@app.route('/Notebook')
def notebook():
    return render_template('notebook.html')


@app.route('/Index')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        # try:
            mydb = mysql.connector.connect(
                host=os.environ['DATABASE_HOST'],
                user=os.environ['DATABASE_USER'],
                password=os.environ['DATABASE_PASSWORD'],
                database=os.environ['DATABASE_NAME'],
                auth_plugin='mysql_native_password'
            )
            task_content = request.form['content']
            cursor = mydb.cursor()
            add_content = (
                "INSERT INTO `test`.`Todo`(`ID`,`Content`,`Completed`,`Date_Created`) VALUES(%s, %s, %s, %s)")
            task_id = random.randint(11, 999999)
            task_date = datetime.today().strftime('%Y/%m/%d')
            task_data = (task_id, task_content, 0, task_date)
            cursor.execute(add_content, task_data)
            mydb.commit()
            cursor.close()
            mydb.close()
            print(cursor.lastrowid)
            return redirect("/")
        # except:
        #     return 'There was an error while submitting the data'
    else:
        # try:
            mydb1 = mysql.connector.connect(
                host=os.environ['DATABASE_HOST'],
                user=os.environ['DATABASE_USER'],
                password=os.environ['DATABASE_PASSWORD'],
                database=os.environ['DATABASE_NAME'],
                auth_plugin='mysql_native_password'
            )
            query_content = ("SELECT Content, Date_Created from Todo")
            cursor1 = mydb1.cursor(buffered=True)
            cursor1.execute("SELECT Content, Date_Created from Todo")
            tasks = cursor1.fetchall()
            print(tasks)
            # for rw in tasks:
            #     comment = rw[0]
            #     task_date = rw[1]
            #     print("Content is", comment, "& date is ", task_date)
            for content, task_date in tasks:
                print("Content is", content, "& date is ", task_date)
            cursor1.close()
            mydb1.close()
            return render_template('index.html', tasks=tasks)
        # return render_template('home.html')
        # except:
        #     return 'There was an error while submitting the data'


@app.route('/Delete/<string:content>')
def delete(content):
    try:
        print(content)
        mydb = mysql.connector.connect(
                host=os.environ['DATABASE_HOST'],
                user=os.environ['DATABASE_USER'],
                password=os.environ['DATABASE_PASSWORD'],
                database=os.environ['DATABASE_NAME'],
                auth_plugin='mysql_native_password'
            )
        cursor = mydb.cursor(buffered=True)
        delete_query = 'DELETE FROM Todo WHERE Content="' + content + '"'
        print(delete_query)
        cursor.execute(delete_query)
        print(cursor)
        mydb.commit()
        cursor.close()
        mydb.close()
        return redirect("/")
    except:
        return 'There was an error while deleting data'


@app.route('/Update/<string:content>', methods=['POST', 'GET'])
def update(content):
    if request.method == 'POST':
        # try:
        new_content = request.form['content']
        print(new_content)
        mydb = mysql.connector.connect(
                host=os.environ['DATABASE_HOST'],
                user=os.environ['DATABASE_USER'],
                password=os.environ['DATABASE_PASSWORD'],
                database=os.environ['DATABASE_NAME'],
                auth_plugin='mysql_native_password'
            )
        cursor = mydb.cursor(buffered=True)
        task_date = datetime.today().strftime('%Y-%m-%d')
        update_query = 'UPDATE Todo SET Content= "' + new_content + '", Date_Created="' + task_date + '" WHERE Content="' + content + '"'
        print(update_query)
        cursor.execute(update_query)
        print(cursor)
        mydb.commit()
        cursor.close()
        mydb.close()
        return redirect("/")
    # except:
    #     return "Update Failed"
    else:
        old_content = content
        return render_template('update.html', old_content=old_content)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
