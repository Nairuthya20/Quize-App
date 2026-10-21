import random
import tkinter as tk
from datetime import datetime
from pathlib import Path
from tkinter import messagebox, ttk


QUESTIONS = [
    {
        "question": "Which function is used to display output in Python?",
        "options": ["A. input()", "B. print()", "C. display()", "D. output()"],
        "answer": "B"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. function", "B. def", "C. fun", "D. define"],
        "answer": "B"
    },
    {
        "question": "Which data type stores True or False?",
        "options": ["A. String", "B. Integer", "C. Boolean", "D. Float"],
        "answer": "C"
    },
    {
        "question": "Which symbol is used to write a comment in Python?",
        "options": ["A. //", "B. <!-- -->", "C. #", "D. **"],
        "answer": "C"
    },
    {
        "question": "Which data structure is used to store an ordered collection of items?",
        "options": ["A. List", "B. Boolean", "C. Integer", "D. Float"],
        "answer": "A"
    },
    {
        "question": "Which loop is commonly used to go through items in a list?",
        "options": ["A. if", "B. for", "C. def", "D. try"],
        "answer": "B"
    },
    {
        "question": "Which function is used to get input from the user?",
        "options": ["A. get()", "B. scan()", "C. input()", "D. read()"],
        "answer": "C"
    },
    {
        "question": "Which keyword is used to handle possible errors?",
        "options": ["A. error", "B. catch", "C. try", "D. stop"],
        "answer": "C"
    },
    {
        "question": "Which file mode is normally used to write new content to a file?",
        "options": ["A. r", "B. w", "C. x", "D. a"],
        "answer": "B"
    },
    {
        "question": "Which library function can randomly shuffle a list?",
        "options": [
            "A. random.shuffle()",
            "B. random.sort()",
            "C. random.change()",
            "D. random.order()"
        ],
        "answer": "A"
    }
]

BACKGROUND = "#f3f6fc"
CARD = "#ffffff"
NAVY = "#172554"
BLUE = "#2563eb"
TEXT = "#334155"
MUTED = "#64748b"


def calculate_result(score, total):
    """Return percentage and grade for the quiz score."""
    percentage = (score / total) * 100

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "Fail"

    return percentage, grade


def save_result(name, score, total, percentage, grade):
    """Append a quiz result beside this script."""
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    results_file = Path(__file__).resolve().with_name("quiz_results.txt")

    with results_file.open("a", encoding="utf-8") as file:
        file.write("\n" + "=" * 40 + "\n")
        file.write("QUIZ RESULT\n")
        file.write("=" * 40 + "\n")
        file.write(f"Name: {name}\n")
        file.write(f"Score: {score}/{total}\n")
        file.write(f"Percentage: {percentage:.2f}%\n")
        file.write(f"Grade: {grade}\n")
        file.write(f"Date and Time: {current_time}\n")


class QuizApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Application")
        self.root.geometry("800x650")
        self.root.minsize(640, 560)
        self.root.configure(bg=BACKGROUND)

        style = ttk.Style()
        style.configure(
            "Quiz.Horizontal.TProgressbar",
            troughcolor="#e2e8f0",
            background=BLUE,
            bordercolor="#e2e8f0",
            lightcolor=BLUE,
            darkcolor=BLUE
        )
        style.configure(
            "Quiz.TButton",
            font=("Segoe UI", 11, "bold"),
            padding=(18, 10)
        )
        style.configure(
            "Quiz.TRadiobutton",
            background=CARD,
            foreground=TEXT,
            font=("Segoe UI", 12),
            padding=10
        )
        style.map(
            "Quiz.TRadiobutton",
            background=[("active", "#eff6ff")],
            foreground=[("active", NAVY)]
        )

        self.page = tk.Frame(root, bg=BACKGROUND)
        self.page.pack(fill="both", expand=True, padx=36, pady=28)

        self.name = ""
        self.questions = []
        self.question_index = 0
        self.score = 0
        self.answer_var = tk.StringVar()
        self.show_home()

    def clear_page(self):
        for widget in self.page.winfo_children():
            widget.destroy()

    def show_home(self):
        self.clear_page()

        tk.Label(
            self.page,
            text="QUIZ APPLICATION",
            bg=BACKGROUND,
            fg=NAVY,
            font=("Segoe UI", 27, "bold")
        ).pack(pady=(55, 8))
        tk.Label(
            self.page,
            text="Test your Python knowledge",
            bg=BACKGROUND,
            fg=MUTED,
            font=("Segoe UI", 13)
        ).pack(pady=(0, 30))

        card = tk.Frame(self.page, bg=CARD, padx=36, pady=32)
        card.pack(fill="x", padx=70)

        tk.Label(
            card,
            text="Ready to begin?",
            bg=CARD,
            fg=NAVY,
            font=("Segoe UI", 18, "bold")
        ).pack(anchor="w")
        tk.Label(
            card,
            text="Enter your name to start a 10-question multiple-choice quiz.",
            bg=CARD,
            fg=MUTED,
            font=("Segoe UI", 11),
            wraplength=540,
            justify="left"
        ).pack(anchor="w", pady=(8, 22))
        tk.Label(
            card,
            text="Your name",
            bg=CARD,
            fg=TEXT,
            font=("Segoe UI", 10, "bold")
        ).pack(anchor="w", pady=(0, 7))

        self.name_entry = ttk.Entry(card, font=("Segoe UI", 12))
        self.name_entry.pack(fill="x", ipady=7)
        self.name_entry.bind("<Return>", self.handle_name_entry_enter)

        ttk.Button(
            card,
            text="Start Quiz",
            style="Quiz.TButton",
            command=self.start_quiz
        ).pack(anchor="w", pady=(22, 0))

        tk.Label(
            self.page,
            text="Answer each question, then review your result at the end.",
            bg=BACKGROUND,
            fg=MUTED,
            font=("Segoe UI", 10)
        ).pack(pady=22)
        self.name_entry.focus_set()

    def handle_name_entry_enter(self, event):
        if event.keysym == "Return":
            self.start_quiz()

    def start_quiz(self):
        name = self.name_entry.get().strip()
        if not name:
            messagebox.showwarning("Name required", "Please enter your name to start.")
            self.name_entry.focus_set()
            return

        self.name = name
        self.questions = QUESTIONS.copy()
        random.shuffle(self.questions)
        self.question_index = 0
        self.score = 0
        self.show_question()

    def show_question(self):
        self.clear_page()
        question_number = self.question_index + 1
        item = self.questions[self.question_index]
        self.answer_var = tk.StringVar()

        tk.Label(
            self.page,
            text="PYTHON KNOWLEDGE QUIZ",
            bg=BACKGROUND,
            fg=NAVY,
            font=("Segoe UI", 21, "bold")
        ).pack(anchor="w", pady=(12, 4))
        tk.Label(
            self.page,
            text=f"Question {question_number} of {len(self.questions)}",
            bg=BACKGROUND,
            fg=MUTED,
            font=("Segoe UI", 11)
        ).pack(anchor="w", pady=(0, 10))

        progress = ttk.Progressbar(
            self.page,
            style="Quiz.Horizontal.TProgressbar",
            maximum=len(self.questions),
            value=question_number
        )
        progress.pack(fill="x", pady=(0, 24))

        card = tk.Frame(self.page, bg=CARD, padx=30, pady=28)
        card.pack(fill="both", expand=True)
        tk.Label(
            card,
            text=item["question"],
            bg=CARD,
            fg=NAVY,
            font=("Segoe UI", 16, "bold"),
            wraplength=660,
            justify="left",
            anchor="w"
        ).pack(fill="x", pady=(0, 20))

        for option in item["options"]:
            answer_key = option[0]
            ttk.Radiobutton(
                card,
                text=option,
                value=answer_key,
                variable=self.answer_var,
                style="Quiz.TRadiobutton"
            ).pack(fill="x", anchor="w", pady=3)

        self.feedback = tk.Label(
            card,
            text="",
            bg=CARD,
            fg=TEXT,
            font=("Segoe UI", 11, "bold"),
            anchor="w"
        )
        self.feedback.pack(fill="x", pady=(16, 4))

        self.submit_button = ttk.Button(
            card,
            text="Submit Answer",
            style="Quiz.TButton",
            command=self.submit_answer
        )
        self.submit_button.pack(anchor="e", pady=(14, 0))

    def submit_answer(self):
        answer = self.answer_var.get()
        if not answer:
            messagebox.showinfo("Choose an answer", "Select an option before continuing.")
            return

        item = self.questions[self.question_index]
        if answer == item["answer"]:
            self.score += 1
            self.feedback.configure(text="Correct answer!", fg="#15803d")
        else:
            self.feedback.configure(
                text=f"Not quite. The correct answer is {item['answer']}.",
                fg="#b91c1c"
            )

        for child in self.feedback.master.winfo_children():
            if isinstance(child, ttk.Radiobutton):
                child.configure(state="disabled")

        button_text = (
            "View Results"
            if self.question_index == len(self.questions) - 1
            else "Next Question"
        )
        self.submit_button.configure(text=button_text, command=self.next_question)

    def next_question(self):
        self.question_index += 1
        if self.question_index < len(self.questions):
            self.show_question()
        else:
            self.show_result()

    def show_result(self):
        self.clear_page()
        total = len(self.questions)
        percentage, grade = calculate_result(self.score, total)

        try:
            save_result(self.name, self.score, total, percentage, grade)
            saved_message = "Your result has been saved to quiz_results.txt."
        except OSError as error:
            saved_message = f"Could not save your result: {error}"

        tk.Label(
            self.page,
            text="QUIZ COMPLETE",
            bg=BACKGROUND,
            fg=NAVY,
            font=("Segoe UI", 25, "bold")
        ).pack(pady=(48, 22))

        card = tk.Frame(self.page, bg=CARD, padx=42, pady=32)
        card.pack(fill="x", padx=75)
        tk.Label(
            card,
            text=f"Well done, {self.name}!",
            bg=CARD,
            fg=NAVY,
            font=("Segoe UI", 18, "bold")
        ).pack(pady=(0, 20))
        tk.Label(
            card,
            text=f"{self.score} / {total}",
            bg=CARD,
            fg=BLUE,
            font=("Segoe UI", 36, "bold")
        ).pack()
        tk.Label(
            card,
            text=f"Score     {percentage:.2f}%\nGrade     {grade}",
            bg=CARD,
            fg=TEXT,
            font=("Segoe UI", 14),
            justify="left"
        ).pack(pady=16)
        tk.Label(
            card,
            text=saved_message,
            bg=CARD,
            fg=MUTED,
            font=("Segoe UI", 10),
            wraplength=540
        ).pack()

        actions = tk.Frame(self.page, bg=BACKGROUND)
        actions.pack(pady=24)
        ttk.Button(
            actions,
            text="Try Again",
            style="Quiz.TButton",
            command=self.show_home
        ).pack(side="left", padx=8)
        ttk.Button(
            actions,
            text="Exit",
            style="Quiz.TButton",
            command=self.root.destroy
        ).pack(side="left", padx=8)


def main():
    root = tk.Tk()
    QuizApplication(root)
    root.mainloop()


if __name__ == "__main__":
    main()
