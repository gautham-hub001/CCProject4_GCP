# import sqlite3

from flask import Flask, request, g, render_template, session
import os

# DATABASE = '/home/gauthampothana007/CCProject4_GCP/example.db'
#DATABASE ='/Users/gauthampothana/Downloads/CCProject4/example.db'
app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = os.urandom(123)

# def connect_to_database():
    # return sqlite3.connect(app.config['DATABASE'])

# def get_db():
#     db = getattr(g, 'db', None)
#     if db is None:
#         db = g.db = connect_to_database()
#     return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

# def execute_query(query, args=()):
#     cur = get_db().execute(query, args)
#     rows = cur.fetchall()
#     cur.close()
#     return rows

# def commit():
#     get_db().commit()

@app.route("/")
def hello():
    # execute_query("DROP TABLE IF EXISTS userstable")
    # execute_query("CREATE TABLE userstable (firstname text,lastname text,email text)")
    return render_template('index.html')


@app.route('/startenquiry', methods =['POST', 'GET'])
def startinquiry():
    message = ''
    if request.method == 'POST' and str(request.form['ufname']) !="" and str(request.form['ulname']) != "" and str(request.form['mail']) != "":
        session['firstname'] = str(request.form['ufname'])
        session['lastname'] = str(request.form['ulname'])
        session['email'] = str(request.form['mail'])
        # result = execute_query("""INSERT INTO userstable (firstname, lastname, email) values (?, ?, ?)""",(firstname, lastname, email))
        # commit()
    elif request.method == 'POST':
        message = 'Please enter all fields.'
    return render_template('chat.html', message = message)

ChatWindowHTMLFirst = """
    <!DOCTYPE html>
    <html>
      <title>College Enquiry Chatbot</title>
      <head>
        <link href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700" rel="stylesheet">
        <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.4.1/css/all.css" integrity="sha384-5sAR7xN1Nv6T6+dT2mhtzEpVJvfS3NScPQTrOxhwjIuvcA67KV2R5Jz6kr4abQsz" crossorigin="anonymous">
        <style>
          html, body {
          display: flex;
          justify-content: center;
          font-family: Roboto, Arial, sans-serif;
          font-size: 15px;
          background-color: grey;
          }
          form {
            background-color: beige;
          border: 5px solid #f1f1f1;
          }
          input[type=text], input[type=password] {
          width: 100%;
          padding: 16px 8px;
          margin: 8px 0;
          display: inline-block;
          border: 1px solid #ccc;
          box-sizing: border-box;
          }
          .icon {
          font-size: 110px;
          display: flex;
          justify-content: center;
          color: #4286f4;
          }
          .send-button {
          background-color: #4286f4;
          color: white;
          padding: 12px 0;
          margin: 10px 0;
          border: none;
          cursor: grab;
          width: 12%;
          }
    	.end-button {
            background-color: #FF0000;
            color: white;
            padding: 4px 0;
            margin: 2px 0;
            border: none;
            cursor: grab;
            width: 24%;
            }
          h1 {
          text-align:center;
          fone-size:18;
          }
          button:hover {
          opacity: 0.8;
          }
          .formcontainer {
          text-align: center;
          margin: 24px 50px 12px;
          }
    	.text-box {
      	font-size: 16px;
     	 display: flex;
     	 width: 100%;
    	}
          .container {
          padding: 16px 0;
          text-align:left;
          }
          span.psw {
          float: right;
          padding-top: 0;
          padding-right: 15px;
          }
          /* Change styles for span on extra small screens */
          @media screen and (max-width: 300px) {
          span.psw {
          display: block;
          float: none;
          }
        </style>
      </head>
      <body>
        <form {{url_for('chatbotsystem')}} method="POST">
          <h1>College Enquiry Chatbot</h1>
          <div class="icon">
    	 <i class="fas fa-user"></i>
          </div>
          <div class="formcontainer">
          <div class="container">
           <label for="ufname"><strong>Hi!! Welcome to College Enquiry portal</strong></label></br></br>
    	  <label for="ufname"><strong>Choose your questions from below list</strong></label></br>
    	  <label for="ufname"><strong>1.Tell me about the college</strong></label></br>
    	  <label for="ufname"><strong>2.what courses are available</strong></label></br>
    	  <label for="ufname"><strong>3.What is the fee structure like?</strong></label></br>
    	  <label for="ufname"><strong>4.Tell me more about location of your college</strong></label></br>
    """

ChatWindowHTMLLast = """
    </div>
    	<div class="text-box">
            <input type="text" name="question" id="message" autocomplete="off" placeholder="Type your Questions here">
    	  <input class="send-button" type="submit" value=">">
          </div>
           <a href='/endchat' align='center'">End Chat</a>
    	</div>
        </form>
      </body>
    </html>
    """


@app.route('/chatbotsystem', methods =['GET', 'POST'])
def chatbotsystem():
    global ChatWindowHTMLFirst
    ChatWindowHTMLMiddle = ''
    if request.method == 'POST' and str(request.form['question']) !="":
        questionasked = str(request.form['question'])
        if(questionasked in "Tell me about the college"):
            ChatWindowHTMLMiddle="""
            </br><label for="ufname" style="color:blue;"><strong>"""+questionasked+"""</strong></label></br>
            <label for ="ufname"><strong> The University of Cincinnati is a public research university in Cincinnati, Ohio. </strong></label></br>
            """
        elif(questionasked in "what courses are available"):
            ChatWindowHTMLMiddle = """
            </br><label for="ufname" style="color:blue;"><strong>""" + questionasked + """</strong></label></br>
            <label for ="ufname"><strong>Courses available: Cloud computing, Advanced Algorithms, Large Scale software engineering, capstone project, Innovation and Design Thinking</strong></label></br>
            """
        elif (questionasked in "What is the fee structure like?"):
            ChatWindowHTMLMiddle = """
            </br><label for="ufname" style="color:blue;"><strong>""" + questionasked + """</strong></label></br>
            <label for ="ufname"><strong> The Cincinnati Tuition Guarantee is a cohort-based program that sets tuition, mandatory fees, and room and board at a consistent rate for up to four or five years</strong></label></br>
            """
        elif (questionasked in "Tell me more about location of your college"):
            ChatWindowHTMLMiddle = """
            </br><label for="ufname" style="color:blue;"><strong>""" + questionasked + """</strong></label></br>
            <label for ="ufname"><strong> UC is located at 2600 Clifton Ave, Cincinnati, OH 45221. Cincinnati is located in the south-west of the Ohio.</strong></label></br>
            """
        else:
            ChatWindowHTMLMiddle = """
            </br><label for="ufname" style="color:blue;"><strong>""" + questionasked + """</strong></label></br>
            <label for ="ufname"><strong> Sorry!! I don't have answer to your question</strong></label></br>
            """

    ChatWindowHTMLFirst=ChatWindowHTMLFirst + ChatWindowHTMLMiddle
    return ChatWindowHTMLFirst+ChatWindowHTMLLast

EndChatHTMLFirst="""
<!DOCTYPE html>
<html>
  <title>Session Closed</title>
  <head>
    <link href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700" rel="stylesheet">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.4.1/css/all.css" integrity="sha384-5sAR7xN1Nv6T6+dT2mhtzEpVJvfS3NScPQTrOxhwjIuvcA67KV2R5Jz6kr4abQsz" crossorigin="anonymous">
    <style>
      html, body {
      display: flex;
      justify-content: center;
      font-family: Roboto, Arial, sans-serif;
      font-size: 15px;
      background-color: grey;
      }
      form {
      border: 5px solid #f1f1f1;
      background-color: beige;
      }
      input[type=text], input[type=password] {
      width: 100%;
      padding: 16px 8px;
      margin: 8px 0;
      display: inline-block;
      border: 1px solid #ccc;
      box-sizing: border-box;
      }
      .icon {
      font-size: 110px;
      display: flex;
      justify-content: center;
      color: #4286f4;
      }
      .send-button {
      background-color: #4286f4;
      color: white;
      padding: 12px 0;
      margin: 10px 0;
      border: none;
      cursor: grab;
      width: 12%;
      }
	.end-button {
      background-color: #FF0000;
      color: white;
      padding: 12px 0;
      margin: 10px 0;
      border: none;
      cursor: grab;
      width: 12%;
      }
      h1 {
      text-align:center;
      fone-size:18;
      }
      button:hover {
      opacity: 0.8;
      }
      .formcontainer {
      text-align: center;
      margin: 24px 50px 12px;
      }
	.text-box {
  	font-size: 16px;
 	 display: flex;
 	 width: 100%;
	}
      .container {
      padding: 16px 0;
      text-align:left;
      }
      span.psw {
      float: right;
      padding-top: 0;
      padding-right: 15px;
      }
      /* Change styles for span on extra small screens */
      @media screen and (max-width: 300px) {
      span.psw {
      display: block;
      float: none;
      }
    </style>
  </head>
  <body>
    <form style="background-color: palegreen">
      <h1>Chat Ended. Bye!</h1>
      
      <div class="formcontainer">
      <div class="container">
        <label for="ufname"><strong>Thank You!</strong></label></br></br>
"""

EndChatHTMLLast="""
 </div>
	</div>
    </form>
  </body>
</html>
"""
@app.route("/endchat", methods=['GET', 'POST'])
def endchat():
    global ChatWindowHTMLFirst
    ChatWindowHTMLFirst = """
        <!DOCTYPE html>
        <html>
          <title>College Enquiry Chatbot</title>
          <head>
            <link href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700" rel="stylesheet">
            <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.4.1/css/all.css" integrity="sha384-5sAR7xN1Nv6T6+dT2mhtzEpVJvfS3NScPQTrOxhwjIuvcA67KV2R5Jz6kr4abQsz" crossorigin="anonymous">
            <style>
              html, body {
              display: flex;
              justify-content: center;
              font-family: Roboto, Arial, sans-serif;
              font-size: 15px;
              }
              form {
              border: 5px solid #f1f1f1;
              }
              input[type=text], input[type=password] {
              width: 100%;
              padding: 16px 8px;
              margin: 8px 0;
              display: inline-block;
              border: 1px solid #ccc;
              box-sizing: border-box;
              }
              .icon {
              font-size: 110px;
              display: flex;
              justify-content: center;
              color: #4286f4;
              }
              .send-button {
              background-color: #4286f4;
              color: white;
              padding: 12px 0;
              margin: 10px 0;
              border: none;
              cursor: grab;
              width: 12%;
              }
        	.end-button {
                background-color: #FF0000;
                color: white;
                padding: 4px 0;
                margin: 2px 0;
                border: none;
                cursor: grab;
                width: 24%;
                }
              h1 {
              text-align:center;
              fone-size:18;
              }
              button:hover {
              opacity: 0.8;
              }
              .formcontainer {
              text-align: center;
              margin: 24px 50px 12px;
              }
        	.text-box {
          	font-size: 16px;
         	 display: flex;
         	 width: 100%;
        	}
              .container {
              padding: 16px 0;
              text-align:left;
              }
              span.psw {
              float: right;
              padding-top: 0;
              padding-right: 15px;
              }
              /* Change styles for span on extra small screens */
              @media screen and (max-width: 300px) {
              span.psw {
              display: block;
              float: none;
              }
            </style>
          </head>
          <body>
            <form {{url_for('chatbotsystem')}} method="POST">
              <h1>College Enquiry Chatbot</h1>
              <div class="icon">
        	 <i class="fas fa-user"></i>
              </div>
              <div class="formcontainer">
              <div class="container">
               <label for="ufname"><strong>Hi! Welcome to college enquiry portal</strong></label></br></br>
        	  <label for="ufname"><strong>You can ask questions from below list:</strong></label></br>
        	  <label for="ufname"><strong>1.Tell me about the college</strong></label></br>
        	  <label for="ufname"><strong>2.what courses are available</strong></label></br>
        	  <label for="ufname"><strong>3.What is the fee structure like?</strong></label></br>
        	  <label for="ufname"><strong>4.Tell me more about location of your college</strong></label></br>
        """
    # result = execute_query("""SELECT firstname,lastname,email  FROM userstable""")
    # result = list()
    # result = firstname
    Userdetails = list()
    # if result:
    #     for row in result:
    #         Userdetails.append(row[0])
    #         Userdetails.append(row[1])
    #         Userdetails.append(row[2])
    Userdetails.append(session.get('firstname'))
    Userdetails.append(session.get('lastname'))
    Userdetails.append(session.get('email'))
    creatordetails= ['Gautham','Pothana','pothangm@mail.uc.edu']
    EndChatHTMLMiddle="""
    <strong>User Details:<br></strong>
    First Name: """+Userdetails[0]+"""</br>Last Name: """+Userdetails[1]+"""</br>Email: """+Userdetails[2]+"""</br>"""+"""</br></br>
    <strong>Chatbot Creator Details:<br></strong>
    First Name: """+creatordetails[0]+"""</br>Last Name: """+creatordetails[1]+"""</br>Email: """+creatordetails[2]+"""</br>"""+"""</br></br>
    """
    return EndChatHTMLFirst+EndChatHTMLMiddle+EndChatHTMLLast

if __name__ == '__main__':
  app.run()