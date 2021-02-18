from Question import Question

Question_prompts = [
    "Which animal is an invertebrate?:\n(a)Dog\n(b)Cat\n(c)Snake\n(d)Cow\n",
    "What color are Watermelons?: \n(a)Red\n(b)Green\n(c)Orange\n(d)Blue\n",
    "What type of state is ice in?: \n(a)Solid(b)Liquid(c)Gas(d)Runny"
]

questions = [
    Question(Question_prompts[0], "c"),
    Question(Question_prompts[1], "b"),
    Question(Question_prompts[2], "a"),
]

def test(questions):
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            print("Correct!")
        else:
            print("Wrong!")

test(questions)