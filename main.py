from login import login_user
from quiz import start_quiz
from result import result
from questions import python_questions,java_questions,dsa_questions
from email_sender import email_sender
print("="*50)
print("         EMAIL MCQ TEST APPLICATION")
print("="*50)
print("1.Login")
print("2.Exit")
print("="*50)
ch=int(input("Enter your choice:"))
if ch==1:
    print("="*50)
    print("              EMAIL MCQ TEST SYSTEM")
    print("="*50)
    print("                    LOGIN PAGE")
    print("="*50)
    user=login_user()
    if user :
        user_name,email=user
        print("             SELECT SUBJECT")
        print("="*50)
        print("1.🐍 Python")
        print("2.☕ Java")
        print("3.📚 Dsa")
        print("="*50)
        choice=int(input("Enter your choice:"))
        subject=""
        if choice==1:
            subject="python"
            selected_question=python_questions
        elif choice==2:
            subject="Java"
            selected_question=java_questions
        elif choice==3:
            subject="DSA"
            selected_question=dsa_questions
        else:
            print("Invalid Choice")
        score,total,status=start_quiz(selected_question)
        total=len(selected_question)
        result(user_name,subject,score,total,status)
        print("="*50)
        print("           QUIZ COMPLETED")
        print("="*50)
        print("\n Do you want to receive your result by email?")
        print("1.Yes")
        print("2.No")
        email_choice=input("Enter your choice (yes/no):")
        if email_choice=='yes' or email_choice=='y':
            email_sender(user_name,email,score,subject,total,status)
        else:
            print("Email Sending skipped.")
            print("Thank you for taking test.")

elif ch==2:
    print("Thank you")
    exit()
