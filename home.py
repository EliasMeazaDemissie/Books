from flask import Flask, render_template , request
# from flask_sqlalchemy import SQLAlchemy
import psycopg2

app = Flask(__name__) 

DATABASE_HOST = "localhost"
DATABASE_NAME = "information"
DATABASE_USER = "postgres"
DATABASE_PASSWORD = "eliasmz"


@app.route("/")
def home():
    return render_template('home.html')



@app.route('/home' , methods=['POST'])
def getvalue():
    id=request.form['id']
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(host=DATABASE_HOST, database=DATABASE_NAME, user=DATABASE_USER, password=DATABASE_PASSWORD)
        cur = conn.cursor()

        # Define the SQL query to retrieve data
        sql = "SELECT * FROM infotable WHERE id_num = "+id+";"  

        # Execute the query
        cur.execute(sql)

        # Fetch all rows as a list of dictionaries
        data = cur.fetchall()
       

        # Close the connection
        cur.close()
        conn.close()

        # Render the HTML template with dataå
        return render_template("pass.html", data=data)

    except Exception as e:
        # Handle connection errors or other exceptions
        return f"Error: {e}"


if __name__=="__main__": 
    app.run(debug=True) 