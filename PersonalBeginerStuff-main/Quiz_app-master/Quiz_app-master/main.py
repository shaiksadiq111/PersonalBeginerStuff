import tkinter
import requests
import html
questions = []
answers = []
bg_color = "#a4ebf3"
style = ("Courier", 20, "bold")
question_no = 0

score = 0


def display_score(score_):
    score_label = tkinter.Label()
    score_label.config(text=f"Score: {score_}", font=style, bg=bg_color)
    score_label.place(x=500, y=60)


def create_database():
    api = requests.get(url="https://opentdb.com/api.php?amount=20&difficulty=easy&type=boolean")
    api.raise_for_status()
    data = api.json()
    status = True
    counter = 0
    while status:

        question = data["results"][counter]["question"]
        question = html.unescape(question)
        questions.append(question)
        answer = data["results"][counter]["correct_answer"]
        answers.append(answer)
        counter += 1
        if counter == 10:
            status = False


window = tkinter.Tk()
window.title("Quiz App")
window.config(bg=bg_color, width=800, height=700)

question_label = tkinter.Label()
question_label.configure(bg=bg_color, font=style)
question_label.place(x=50, y=100)


def display_question(i):
    question_label.configure(text=questions[i])
    display_score(score)


def true_function():
    global question_no
    global score
    global bg_color
    if answers[question_no] == "True":
        print("correct answer")
        bg_color = "#a4ebf3"
        score += 1
    else:
        print("wrong answer")
        bg_color = "red"
        score -= 0.5
    question_no += 1
    if question_no == 10:
        questions.clear()
        answers.clear()
        question_no = 0
        create_database()
    display_question(question_no)


def false_function():
    global question_no
    global score
    global bg_color
    if answers[question_no] == "False":
        print("correct answer")
        score += 1
        bg_color = "#a4ebf3"
    else:
        print("wrong answer")
        score -= 0.5
        bg_color = "red"
    question_no += 1
    if question_no == 10:
        questions.clear()
        answers.clear()
        question_no = 0
        create_database()
    display_question(question_no)


create_database()
display_question(question_no)

true_button = tkinter.Button()
true_button.configure(text="True", command=true_function, font=("Arial", 35, "italic"))
true_button.place(x=300, y=400)

false_button = tkinter.Button()
false_button.configure(text="False", command=false_function, font=("Arial", 35, "italic"))
false_button.place(x=300, y=500)

window.mainloop()
