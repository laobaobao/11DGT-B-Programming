# Author: Leo Xu
# Date: 17 September 2024
# Fully functioning multichoice quiz version 4

# CHANGES / EDITIONS
# Version 1:
    # Barebones quiz exactly as followed from the tutorial
    # Created quiz_data tab with a set of 20 questions
# Version 2:
    # Added the default styling option
    # Created the game window
    # Tested functionality of the quiz_data set
# Version 3:
    # Experimented with splash screens, it didn't work
    # Played around with the different styling options
    # Brought up lots of formatting issues
# Version 4:
    # Corrected formatting issues
    # Deleted splash screen
    # Made buttons the same size
    # Rearranged code to be in a more appropriate order
    # Checked for formatting issues in the code and corrected these.


import tkinter as tk
from tkinter import messagebox, ttk
from ttkbootstrap import Style
from quiz_data import quiz_data


# Create the game window
root = tk.Tk()
root.title("Quiz Launcher")
root.geometry("600x550")
style = Style()

# Function to display the current question and choices
def show_question():
    # Get the current question from the quiz_data list
    question = quiz_data[current_question]
    qs_label.config(text=question["question"], justify="center")

    # Display the choices on the buttons
    choices = question["choices"]
    for i in range(4):
        choice_btns[i].config(text=choices[i], state="normal") # Reset button state

    # Clear the feedback label and disable the next button
    feedback_label.config(text = "")
    next_btn.config(state = "disabled")

# Function to check the selected answer and provide feedback
def check_answer(choice):
    # Get the current question from the quiz_data list
    question = quiz_data[current_question]
    selected_choice = choice_btns[choice].cget("text")

    # Check if the selected choice matches the correct answer
    if selected_choice == question["answer"]:
        # Update the score and display it
        global score
        score += 1
        score_label.config(text="Score: {}/{}".format(score, len(quiz_data)))
        feedback_label.config(text="Correct!", foreground="green")
    else:
        feedback_label.config(text="Incorrect!\nCorrect Answer: "+ question["answer"], foreground="red", justify="center")
    
    # Disable all choice buttons and enable the next button
    for button in choice_btns:
        button.config(state = "disabled")
        next_btn.config(state = "normal")

# Function to move to the next question
def next_question():
    global current_question
    current_question += 1

    if current_question < len(quiz_data):
        # If there are more questions, show the next question
        show_question()
    else:
        # If all questions have been answered, display the final score and end the quiz
        messagebox.showinfo("Quiz Completed",
                            "Quiz Completed! Final score: {}/{}".format(score, len(quiz_data)))
        root.destroy()


# Configure the font size for the question and choice buttons
style.configure("TLabel", font = ("Helvetica", 20))
style.configure("TButton", font = ("Helvetica", 16))


# Create the question label
qs_label = ttk.Label(
    root,
    anchor = "center",
    wraplength = 500,
    padding = 5
)
qs_label.pack(pady = 10)

# Create the choice buttons
choice_btns = []
for i in range(4):
    button = ttk.Button(
        root, width = 10,
        command = lambda i = i: check_answer(i),
    )
    button.pack(pady = 5)
    choice_btns.append(button)

# Create the feedback label
feedback_label = ttk.Label(
    root,
    anchor = "center",
    padding = 5
)
feedback_label.pack(pady = 10)

# Initialize the score
score = 0

# Create the score label
score_label = ttk.Label(
    root,
    text = "Score: 0/{}".format(len(quiz_data)),
    anchor = "center",
    padding = 5
)
score_label.pack(pady = 10)

# Create the next button
next_btn = ttk.Button(
    root,
    text = "Next",
    command = next_question,
    state = "disabled"
)
next_btn.pack(pady = 10)

# Initialize the current question index
current_question = 0

# Show the first question
show_question()

# Start the main event loop
root.mainloop()