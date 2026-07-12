import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def email_sender(user_name,receiver_email,score,subject,total,status):
    sender_email=""
    app_password=""
    recieve_email=receiver_email
    email_subject="Your Quiz Result"
    body=f"""
    ---------------------------------
             QUIZ RESULT
    ---------------------------------
    Hello {user_name},
    
    Thank You  for participating in the quiz.

    Subject    :  {subject}
    Score      :  {score}/{total}
    percentage :  {(score/total)*100}
    Status     :  {status}

    Keep learning and keep growing!
    
    Regards,
    Quiz Management System
    """
    msg=MIMEMultipart()
    msg["From"]=sender_email
    msg["To"]=recieve_email
    msg["Subject"]=email_subject
    msg.attach(MIMEText(body,"plain"))
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(sender_email,app_password)
    server.send_message(msg)
    server.quit()
    print("="*50)
    print("             Thank You")
    print("="*50)
    print("Your test has been completed successfully.")
    print("📧 Result has been sent to:")
    print(recieve_email)
    print("\n Have a great day!")
    print("="*50)



    
