from Question import Question


questions_prompt = [
    "What color are apples?\n(a)Red\n(b)Yellow\n(c)White\n\n",
    "What color are banana?\n(a)Red\n(b)Green\n(c)Yellow\n\n",
    "What color are peaches\n(a)Voilet\n(b)Orange\n(c)Green\n\n"
]


questions = [
    Question(questions_prompt[0], "a"),
    Question(questions_prompt[1], "c"),
    Question(questions_prompt[2], "c")
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You Scored "+str(score)+"/"+str(len(questions))+" correct")