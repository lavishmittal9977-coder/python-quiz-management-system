import random
def start_quiz(questions):
    score=0
    question_list=list(questions.keys())
    total=len(questions)
    random.shuffle(question_list)
    for count,i in enumerate(question_list,start=1):
        print("="*50)
        print(f"\nQuestion {count} of {len(question_list)}")
        print("="*50)
        print(questions[i]["question"])
        for option,text in questions[i]["option"].items():
            print(option,":",text)
        print("-"*50)
        user_answer=input("Enter the answer(A/B/C/D):").upper()
        while user_answer not in ['A','B','C','D']:
            print("Invalid choice ")
            user_answer=input("Enter the answer(A/B/C/D):").upper()
        if user_answer==questions[i]["answer"]:
            print(f"✅ Correct Answer")
            score+=1
        else:
            print(f"❌ Incorrect Answer")
            print("correct Answer is:",questions[i]["answer"])
    if score>=5:
        status="PASS"
    else:
        status="FAIL"
    return score,total,status    
