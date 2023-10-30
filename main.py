from flask import Flask, render_template, request
import util

# create an application instance
app = Flask(__name__)

# global variables
# can be placed in a config file
username='raywu1990'
password='test'
host='127.0.0.1'
port='5432'
database='dvdrental'

@app.route('/')
def index():
    # this is index page
    cursor, connection = util.connect_to_db(username,password,host,port,database)
    rule = request.url_rule

    if 'update_basket_a' in rule.rule:
        record = util.run_and_fetch_sql(cursor, "INSERT INTO basket_a (a, fruit_a) VALUES (5, 'Cherry');")
        # if response is ok, print "Success!"
        # else, print error
    elif 'unique' in rule.rule:
        record = util.run_and_fetch_sql(cursor, "SELECT UNIQUE fruit_a FROM basket_a, basket_b;")
        log = record
        # show log in an HTML table
        # print error if necessary



    # disconnect from database
    util.disconnect_from_db(connection,cursor)
    # using render_template function, Flask will search
    # the file named index.html under templates folder
    return render_template('index.html', log_html = log)


if __name__ == '__main__':
	# set debug mode
    app.debug = True
    # your local machine ip
    ip = '127.0.0.1'
    app.run(host=ip)

