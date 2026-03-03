import tkinter as tk
from tkinter import messagebox
import random

# --------------------- KBC COLORS --------------------- #
BG_COLOR = "#001f3f"       # Dark royal blue
BTN_COLOR = "#003d7a"      # Button blue
BTN_HOVER = "#005bb5"      # Button hover
TEXT_COLOR = "white"
ACCENT = "#ffcc00"         # Gold

# --------------------- 50 QUESTIONS --------------------- #
questions = [
    ["On which date International Literacy Day is celebrated?", 
     "8 SEP", "28 NOV", "2 MAY", "22 SEP", 1],

    ["Which of these are names of national parks located in Madhya Pradesh?",
     "Krishna & Kanhaiya", "Kanha & Madhav", "Ghanshyam & Murari", "Girdhar & Gopal", 2],

    ["In the game of Ludo the tokens are of how many colours?",
     "ONE", "TWO", "FOUR", "SIX", 3],

    ["Which battle in 1757 marked the beginning of British occupation in India?",
     "Plassey", "Assaye", "Buxar", "Cuddalore", 1],

    ["In which sports is the term ‘free hit’ used?",
     "Football, Squash", "Badminton, Tennis", "Badminton, Cricket", "Hockey, Cricket", 4],

    ["Who created C programming Language?",
     "Ken Thompson", "Dennis Ritchie", "Robin Milner", "Frieder Nake", 2],

    ["Which language is used to create Facebook?",
     "Python", "French", "JavaScript", "PHP", 4],

    ["Who invented Java?", 
     "James Gosling", "Guido Rossum", "Bill Gates", "Steve Jobs", 1],

    ["What is the national flower of India?",
     "Lily", "Lotus", "Rose", "Marigold", 2],
     
    ["Which continent has the most countries?",
     "Asia", "Africa", "Europe", "South America", 2],

    ["Who discovered Gravity?",
     "Newton", "Einstein", "Tesla", "Edison", 1],

    ["Which gas do plants release at night?",
     "Oxygen", "CO2", "Nitrogen", "Helium", 2],

    ["Which is the largest ocean?",
     "Atlantic", "Indian", "Pacific", "Arctic", 3],

    ["Where is Taj Mahal located?",
     "Delhi", "Mumbai", "Agra", "Jaipur", 3],

    ["HTML is used for?",
     "Styling", "Structure", "Backend", "Database", 2],

    ["Which is fastest memory?",
     "RAM", "Cache", "ROM", "SSD", 2],

    ["What does CPU stand for?",
     "Central Process Unit", "Central Processing Unit", "Control Power Unit", "None", 2],

    ["Python was created by?",
     "Dennis Ritchie", "James Gosling", "Guido van Rossum", "Mark Zuckerberg", 3],

    ["India’s national animal?",
     "Lion", "Tiger", "Elephant", "Horse", 2],

    ["Missile Man of India?",
     "APJ Abdul Kalam", "CV Raman", "Homi Bhabha", "Vikram Sarabhai", 1],

    ["Planet closest to the Sun?",
     "Venus", "Earth", "Mercury", "Mars", 3],

    ["Instrument to measure earthquake?",
     "Seismograph", "Thermometer", "Barometer", "Hygrometer", 1],

    ["Land of Rising Sun?",
     "China", "Japan", "Korea", "Thailand", 2],

    ["Largest desert?",
     "Sahara", "Gobi", "Arabian", "Antarctica", 4],

    ["Metal liquid at RT?",
     "Mercury", "Gold", "Iron", "Copper", 1],

    ["Capital of Australia?",
     "Sydney", "Melbourne", "Canberra", "Perth", 3],

    ["Largest organ?",
     "Skin", "Heart", "Brain", "Liver", 1],

    ["Smallest prime number?",
     "0", "1", "2", "3", 3],

    ["National fruit of India?",
     "Banana", "Apple", "Mango", "Orange", 3],

    ["Who wrote Ramayana?",
     "Kalidas", "Valmiki", "Ved Vyas", "Tulsidas", 2],

    ["Longest river in India?",
     "Ganga", "Yamuna", "Brahmaputra", "Godavari", 1],

    ["Largest planet?",
     "Mars", "Earth", "Saturn", "Jupiter", 4],

    ["First month of year?",
     "January", "March", "April", "June", 1],

    ["Who invented Telephone?",
     "Tesla", "Bell", "Newton", "Einstein", 2],

    ["Which animal gives wool?",
     "Cow", "Sheep", "Horse", "Goat", 2],

    ["2 + 2 = ?",
     "2", "4", "6", "8", 2],

    ["What is H2O?",
     "Water", "Salt", "Acid", "Base", 1],

    ["Sun rises in the?",
     "North", "South", "East", "West", 3],

    ["How many days in leap year?",
     "365", "366", "364", "360", 2],

    ["What is RGB?",
     "Red Green Blue", "Red Gold Black", "Rain Glow Bright", "None", 1],

    ["Founder of Microsoft?",
     "Bill Gates", "Steve Jobs", "Pichai", "Bezos", 1],

    ["National bird of India?",
     "Eagle", "Sparrow", "Peacock", "Parrot", 3],

    ["Who invented Electricity?",
     "Einstein", "Newton", "Thomas Edison", "None", 3],

    ["King of Jungle?",
     "Elephant", "Tiger", "Lion", "Leopard", 3],

    ["Which stores data?",
     "Mouse", "Keyboard", "Monitor", "Hard Disk", 4],

    ["HTML full form?",
     "Hyper Type Multi Language", "Hyper Text Markup Language", "Home Tool Multi Language", "None", 2],

    ["Capital of India?",
     "Mumbai", "Kolkata", "Chennai", "New Delhi", 4],
]

random.shuffle(questions)

levels = [
    1000, 2000, 3000, 5000, 10000,
    20000, 40000, 80000, 160000, 320000,
    640000, 1250000, 2500000, 5000000, 10000000
]

current_q = 0
earned_money = 0


# --------------------- GUI FUNCTIONS --------------------- #
def load_question():
    global current_q
    if current_q >= len(levels):
        messagebox.showinfo("Winner", f"🎉 You Won ₹{earned_money}!")
        root.destroy()
        return

    q = questions[current_q]
    question_label.config(text=f"Q{current_q+1}: {q[0]}")
    btn1.config(text=f"A. {q[1]}")
    btn2.config(text=f"B. {q[2]}")
    btn3.config(text=f"C. {q[3]}")
    btn4.config(text=f"D. {q[4]}")
    prize_label.config(text=f"Prize: ₹{levels[current_q]}")


def check_answer(ans):
    global current_q, earned_money
    correct = questions[current_q][-1]

    if ans == correct:
        earned_money = levels[current_q]
        messagebox.showinfo("Correct!", f"✔ Correct! You won ₹{earned_money}")
        current_q += 1
        load_question()
    else:
        messagebox.showerror("Wrong!", f"❌ Wrong Answer!\nYou take home ₹{earned_money}")
        root.destroy()


def quit_game():
    global earned_money
    messagebox.showinfo("Quit", f"You quit!\nTake home money: ₹{earned_money}")
    root.destroy()


# --------------------- BUTTON HOVER EFFECT --------------------- #
def on_enter(e):
    e.widget['background'] = BTN_HOVER

def on_leave(e):
    e.widget['background'] = BTN_COLOR


# --------------------- GUI WINDOW --------------------- #
root = tk.Tk()
root.title("KBC – Kaun Banega Crorepati")
root.geometry("700x550")
root.config(bg=BG_COLOR)

title_label = tk.Label(root, text="🎉 KAUN BANEGA CROREPATI 🎉",
                       font=("Arial", 28, "bold"), fg=ACCENT, bg=BG_COLOR)
title_label.pack(pady=20)

prize_label = tk.Label(root, text="", font=("Arial", 18, "bold"), 
                       fg="cyan", bg=BG_COLOR)
prize_label.pack()

question_label = tk.Label(root, text="", wraplength=650, justify="center",
                          font=("Arial", 18), fg="white", bg=BG_COLOR)
question_label.pack(pady=30)

# ------------------- OPTION BUTTONS ------------------- #
btn1 = tk.Button(root, text="", font=("Arial", 16), width=30,
                 bg=BTN_COLOR, fg=TEXT_COLOR,
                 command=lambda: check_answer(1))
btn1.pack(pady=5)

btn2 = tk.Button(root, text="", font=("Arial", 16), width=30,
                 bg=BTN_COLOR, fg=TEXT_COLOR,
                 command=lambda: check_answer(2))
btn2.pack(pady=5)

btn3 = tk.Button(root, text="", font=("Arial", 16), width=30,
                 bg=BTN_COLOR, fg=TEXT_COLOR,
                 command=lambda: check_answer(3))
btn3.pack(pady=5)

btn4 = tk.Button(root, text="", font=("Arial", 16), width=30,
                 bg=BTN_COLOR, fg=TEXT_COLOR,
                 command=lambda: check_answer(4))
btn4.pack(pady=5)

# Hover effect
for btn in (btn1, btn2, btn3, btn4):
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

quit_btn = tk.Button(root, text="QUIT GAME", font=("Arial", 16, "bold"), 
                     bg="red", fg="white", width=15, command=quit_game)
quit_btn.pack(pady=25)

load_question()
root.mainloop()
