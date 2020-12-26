from MCQ_Class import Question

question_prompt = [
    "what are color apples?\n(a)Red/Green\n(b)Purple\n(c)Orange\n",
    "\nwhat are color bananas?\n(a)Green\n(b)Yellow\n(c)Red\n",
    "\nwhat are color strawberries?\n(a)Pink\n(b)Magenta\n(c)Red\n"
]

question_ans = [
    Question(question_prompt[0],'a'), #creating the object of the Question class and passing
    Question(question_prompt[1],'b'), #two parameter first prompt and second answer.
    Question(question_prompt[2],'c')
]

#first time loop is executed it take first question and its answer
#Second time loop is executed it take second question and its answer and so on.
def run_test(question_ans):
    score = 0
    for quest in question_ans:
        answer = input(quest.prompt)  #first paramter prompt
        if answer == quest.answer:    #Second parameter answer
            score += 1
    print("You got "+str(score)+" /" + str(len(question_ans))+" correct")

print(run_test(question_ans))