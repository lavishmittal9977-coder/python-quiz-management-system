def result(name,subject,score,total,status):
    wrong=total-score
    correct=total-wrong
    percentage=(score/total)*100
    print("="*50)
    print("                QUIZ RESULT")
    print("="*50)
    print(f"{'User':<20}:{name}")
    print(f"{'Subject':<20}:{subject}")
    print(f"{'Total Questions':<20}:{total}")
    print(f"{'Wrong Answer':<20}:{wrong}")
    print(f"{'percentage':<20}:{percentage:.2f}%")
    print(f"="*50)
    print(f"{'status':<20}:{status}")
    print("="*50)
    if status=="PASS":
        print("🎉 Congratulations! You Passed the Quiz")
    else:
        print("📚 Better Luck Next Time. Keep Practicing!")
    print("="*50)



