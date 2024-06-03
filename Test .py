Q =[
    [
        "who is the of Dubai's prime minister ?", "A) Habibi", "B) Seikh AI", "C) Rashid ", "D) Zayed Sheikh", "d"
    ],
    [
        "Who is the most famous Chai Wala in India ?", "A) MBA Chail wala", "B) Pychics Wala", "C) Dolly Chaiwalla", "D) YOU", "c"
    ],
    [
        "What's new treand in India ?", "A) Digital transformation", "B) Cleaness city's", "C) SportsIndia", "D) Infulancers rights", "a"
    ],
    [
        "python main framework ?", "A) Django", "B) Java script", "C) VS code", "D) IDK", "a"
    ]
]

levels = ["10k","20k","30k","40k"]

for i in range(len(Q)):
    question = Q[i]
    print(f"Question for ${levels[i]} is {Q[i][0]}")
    print(f".{Q[i][1]}         .{Q[i][2]}")
    print(f".{Q[i][3]}         .{Q[i][4]}")

    reply = str(input("Enter your Answer :"))
    if (reply == Q[i][5]):
        print(f"Congratulation / you have wined {levels[i]}")
    else:
        print(" Wrong Answer, Better luck for next question ")
        continue;