# here is how we pull in python libraries
from flask import Flask, render_template, request
import sqlite3

# create database
conn = sqlite3.connect("myDatabase.db")
cursor = conn.cursor()

# create table - but after you turn the app on the first time, then comment this out
# cursor.execute('''DROP TABLE IF EXISTS inputs''') #debug feature only - don't put in live file, will blow out
# cursor.execute('''CREATE TABLE inputs(calc_value_a TEXT, calc_value_b TEXT)''')

# open up index file
# f = open("templates/index.html", "a")
# f.truncate(0) #debug - do not put on live file, will blow out
# create html,
# f.write('''
# ''')
# f.close()

# setup flask framework
app = Flask(__name__) # set up flask app
@app.route('/') # python decorator
def index():
  return render_template('index.html')

# route flask functions and allow GET and POST requests
@app.route('/', methods=['GET', 'POST']) # python decorator
def main(): # run main function
  conn = sqlite3.connect("myDatabase.db")
  cursor = conn.cursor()
  if request.method == 'POST': # identify request method
    calc_value_a = request.form['input_a'] # gather the post request data
    calc_value_b = request.form['input_b'] # gather the post request data
    cursor.execute('''INSERT INTO inputs (calc_value_a, calc_value_b) VALUES(?,?)''', (calc_value_a, calc_value_b))
    conn.commit() # when commit, the journal entries disappear
    # retrieve data to confirm
    cursor.execute('''SELECT calc_value_a, calc_value_b FROM inputs''')
    data1 = cursor.fetchall()[-1] # [0] fetches first record, [-1] fetches last record
    cursor.execute('''SELECT count(*) FROM inputs''')
    count = cursor.fetchone()
    return "Data Values '" + data1[0] + " & " + \
    data1[1] + "' Saved to Database | Number of Records in Table = " + str(count[0])
  if request.method == 'GET': # identify request method
    return render_template('index.html')

app.run('0.0.0.0', 8080, debug=True)