import tkinter as tk
# import tkinter.font as tkFont
# from random import randint
# from time import time


class GUI:
    def __init__(self):
        root = tk.Tk()
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        root.geometry(f"{screen_width}x{screen_height}")
        root.minsize(600, 500)
        root.configure(background="lightgray")
        root.title("tkinter_testing.py")

        label = tk.Label(root, text="Hello world!", bg="gray")
        label.pack()

        frame = tk.Frame(root)
        frame.configure(bg="blue", relief=tk.RAISED)

        score_2 = tk.Canvas(frame, bg="lightgray")
        score_2.pack(side=tk.TOP)
        # score_2.grid(row=0)

        leaderboard_w = tk.Canvas(frame, bg="lightgray")
        leaderboard_w.pack(side=tk.TOP)

        # game_w = tk.Canvas(root, cursor="cross", bg="white")
        # game_w.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)

        subframe = tk.Frame(frame, bg="blue")

        button_1 = tk.Button(subframe, text="button", bg="red")
        button_1.pack(side=tk.LEFT, padx=(0, 30))
        # button_1.grid(row=1, column=0)

        button_2 = tk.Button(subframe, text="anotha1", bg="red")
        # button_2.grid(row=1, column=1)
        button_2.pack(side=tk.RIGHT, padx=(30, 0))

        subframe.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        frame.pack(side=tk.RIGHT, fill='y')

        game_w = tk.Canvas(root, cursor="cross", bg="white")
        game_w.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)

        root.mainloop()


if __name__ == "__main__":
    GUI()
