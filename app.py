from flask import Flask,render_template,url_for,request
import smtplib
from email.message import EmailMessage
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/send_email',methods=['POST'])
def send_email():
    name = request.form.get('name')
    email = request.form.get('email')
    subject = request.form.get('subject')
    message = request.form.get('message')

    msg = EmailMessage()
    msg['From'] = email
    msg['To'] = 'sukhmeets111@gmail.com'
    msg['Subject'] = subject
    if msg is None:
        msg = "No message provided"
    msg.set_content(message)

    with smtplib.SMTP("smtp.gmail.com",587) as server:
        server.starttls()
        server.login("abc@gmail.com",'abc')
        server.send_message(msg)
        return render_template('index.html')

    

if __name__ == '__main__':
    app.run(debug=True)