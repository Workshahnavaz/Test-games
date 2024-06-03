x = [

    [
        "What the Use of language in your perception ?"
    ],
    [
        "How well you are interms of healthcare ?"
    ],
    [
        "Why USA?"
    ],
    [
        "What's your future goal ?"
    ],
]

y = [
    [
        "To communicate", "To interacte", "To creat bounding", "To express feeling"
    ],
    [
        "Very Healthy", "Good", "Extremly well&good", "It's not your business"
    ],
    [
        "To study", "To earn", "To explore", "To settle"
    ],
    [
        "To be successfull", "To be wealthy", "To be Modi", "To get what I want"
    ],
]

Question_number = q = [1,2,3,4]
for i in range(0,len(y[0])):
    question = x[i]
    option = y[i]
    print(f"{q[i]}.{x[i]}")
    print(f"A.{y[i][0]}                          B.{y[i][1]}")
    print(f"C.{y[i][2]}                          D.{y[i][3]}")

    reply = str(input("Share your thoughts..."))
    if reply == reply:
        print("thanks please go forward")
        continue
    elif reply == x[4]:
        print("Thank you for showing your intreste in our website")
    else:
        print("error")
        break;