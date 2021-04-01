import tkinter as tk
from random import randint, choices
from time import time


class ScoreKeeper:
    """
    Works as a counter. Has option to add to leaderboard but doesn't check logic of add.
    """

    def __init__(self, name_length, length=5):
        self.__length = length
        self.__name_length = name_length
        self.__leaderboard = [(35, "Jack")] + (self.__length - 1) * [(0, self.__name_length * "-")]
        self.__curr_score = 0

    def increment(self):
        self.__curr_score += 1

    def reset_curr_score(self):
        self.__curr_score = 0

    def reset_leaderboard(self):
        self.__leaderboard = self.__length * [(0, self.__name_length * "-")]

    def insert_score(self, score, name):
        """
        You must check that score is >= last element yourself.
        I do not want to have to bring up an enter name window just for the name to not get displayed.
        """

        self.__leaderboard.pop()
        self.__leaderboard.append((score, name[:self.__name_length]))
        self.__leaderboard.sort(reverse=True)

    @property
    def curr_score(self):
        return self.__curr_score

    @property
    def leaderboard(self):
        return self.__leaderboard

    @property
    def min_score(self):
        return self.__leaderboard[-1][0]


class Stopwatch:
    def __init__(self):
        self.__time1 = 0
        self.__time2 = 0

    def start(self):
        self.__time1 = time()

    def stop(self):
        self.__time2 = time()

    def reset(self):
        self.__time1 = 0
        self.__time2 = 0

    @property
    def time(self):
        return self.__time2 - self.__time1


class GUI:
    def __init__(self):
        """ Made methods for the creation/packing of each of the principal widgets in the GUI to be neater. """

        self.__name_length = 10

        self.__stopwatch = Stopwatch()
        self.__scorekeeper = ScoreKeeper(self.__name_length)

        self.__config_root()
        self.__config_info_display()
        self.__config_game_window()

        self.__root.mainloop()

    def __config_root(self):
        """ Starts the application and initial window size + other attributes. """

        self.__root = tk.Tk()
        screenwidth = self.__root.winfo_screenwidth()
        screenheight = self.__root.winfo_screenheight()
        self.__root.geometry(f"{screenwidth}x{screenheight}")
        self.__root.configure(bg="lightgray")
        self.__root.title("OConnor_Jack.py")
        self.__root_label = tk.Label(self.__root, text="Square clicky game", font=("Times New Roman", 14))
        self.__root_label.configure(bg="#0055FF", border=2, relief=tk.RAISED)
        self.__root_label.pack(side=tk.TOP, fill='x')
        self.__root.minsize(800, 600)

    def __config_info_display(self):
        """ Handles the right-hand side portion of the window."""

        width = 46  # width of info display in mm (I think).

        # StringVar objects for updating score and leaderboard automatically.
        self.__leaderboard = self.__LeaderboardVar(self.__name_length)
        self.__score_display = self.__ScoreVar()

        # Frame for right-hand side.
        self.__i_display = tk.Frame(self.__root, bg="gray")
        self.__i_display.configure(border=4, relief=tk.RAISED)
        self.__i_display.pack(side=tk.RIGHT, fill='y', expand=False)

        # The top right box
        self.__leaderboard_w = tk.Label(self.__i_display, bg="lightgray",
                                        textvariable=self.__leaderboard)
        self.__leaderboard_w.configure(cursor="arrow", width=width)
        self.__leaderboard_w.pack(side=tk.TOP, fill='y', expand=True)

        # The middle portion of info_display.
        self.__score_and_refresh_canvas = tk.Frame(self.__i_display, bg="lightgray", width=width)
        self.__score_label = tk.Label(self.__score_and_refresh_canvas, bg="yellow",
                                      textvariable=self.__score_display)
        self.__reset_canvas_b = tk.Button(self.__score_and_refresh_canvas, text="Reset", bg="red",
                                          fg="white", activebackground="pink", command=self.__start_screen)
        self.__score_label.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.__reset_canvas_b.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.__score_and_refresh_canvas.pack(fill=tk.BOTH)

        # The bottom right game description.
        info = "This is a square clicking game. Click squares for points.\n\n" \
               "There are 3 types of coloured square:\n" \
               "- Blue squares must be clicked within 2 seconds\n" \
               "- Green squares must be clicked within 1.45 seconds\n" \
               "- Red squares must be clicked within 0.9 seconds.\n\n" \
               "The likelihood of green and red squares increases with the user's score.\n\n" \
               "The reset button resets the canvas to the game start screen, if it gets wonky on resizing."

        self.__game_description = tk.Text(self.__i_display, bg="lightgray")
        self.__game_description.pack()
        self.__game_description.insert(tk.END, info)
        self.__game_description.configure(state="disable", cursor="arrow", width=width,
                                          relief=tk.SUNKEN)  # disabled so user can't enter text into box

    def __config_game_window(self):
        """ Prep needed for the canvas the game is played on. """

        # for deciding random square properties
        self.__square_colour_times = {"blue": 2, "green": 1.45, "red": 0.9}
        self.__square_colours = ["blue", "green", "red"]
        self.__curr_square_colour = "blue"

        # the canvas for playing the game
        self.__game_w = tk.Canvas(self.__root, bg="white", borderwidth=4)
        self.__game_w.configure(cursor="cross", relief=tk.SUNKEN)
        self.__game_w.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)

        # tags here so tag_bind only called once and not set multiple times
        self.__game_w.tag_bind("random_square", "<ButtonPress-1>", func=self.__square_clicked, add='+')
        self.__game_w.tag_bind("random_square", "<ButtonPress-1>", func=lambda event: self.__Update_ScoreVar(), add='+')
        self.__game_w.tag_bind("start_square", "<ButtonPress-1>", func=self.__create_random_square, add='+')
        self.__game_w.tag_bind("start_square", "<ButtonPress-1>",
                               func=lambda event: self.__scorekeeper.reset_curr_score(), add='+')
        self.__game_w.tag_bind("start_square", "<ButtonPress-1>", func=lambda event: self.__Update_ScoreVar(), add='+')

        self.__start_screen()

    def __start_screen(self):
        """ Draw start screen on the canvas, with a start option. """

        self.__game_w.delete(tk.ALL)

        square_length, canvas_width, canvas_height = self.__square_and_canvas_dimensions()
        self.__create_start_square(square_length, canvas_width, canvas_height)

        self.__game_w.create_text(canvas_width // 2, canvas_height // 2 - square_length, anchor="center",
                                  font=("Times New Roman", square_length),
                                  text="Click Square To Start")

    def __create_random_square(self, event=None):
        """ Handles the creation of the different square types. """

        self.__stopwatch.reset()
        self.__stopwatch.start()

        self.__game_w.delete(tk.ALL)

        if self.__scorekeeper.curr_score < 20:
            self.__curr_square_colour = choices(self.__square_colours,
                                                weights=[100 - 5 * self.__scorekeeper.curr_score,
                                                         4 * self.__scorekeeper.curr_score,
                                                         1 * self.__scorekeeper.curr_score])[0]
        else:
            self.__curr_square_colour = choices(self.__square_colours,
                                                weights=[0, 20, 80])[0]

        square_length, canvas_width, canvas_height = self.__square_and_canvas_dimensions()
        x = randint(0, canvas_width - square_length)
        y = randint(0, canvas_height - square_length)
        self.__game_w.create_rectangle(x, y, x + square_length, y + square_length,
                                       fill=self.__curr_square_colour, tags="random_square")

    def __square_clicked(self, event=None):
        """ Used in __create_random_square to determine outcome of user clicking square. """

        self.__stopwatch.stop()
        if self.__stopwatch.time < self.__square_colour_times[self.__curr_square_colour]:
            self.__scorekeeper.increment()
            self.__create_random_square()
        else:
            self.__game_over()

    def __game_over(self, event=None):
        """
        If a square isn't pushed within the required time limit the game ends.
        The game over screen is displayed and the leaderboard is updated if necessary.
        """

        self.__game_w.delete(tk.ALL)

        if self.__scorekeeper.curr_score >= self.__scorekeeper.min_score:
            self.__name_entry_window()
            self.__Update_LeaderboardVar(self.__name_length)

        square_length, canvas_width, canvas_height = self.__square_and_canvas_dimensions()
        self.__create_start_square(square_length, canvas_width, canvas_height)

        self.__game_w.create_text(canvas_width // 2, canvas_height // 2 - square_length, anchor="center",
                                  font=("Times New Roman", square_length),
                                  text="You Lost - Click Square To Try Again")

    def __create_start_square(self, square_length, canvas_width, canvas_height):
        """
        Pressing this square starts the game.
        Also resets scorekeeper current score to zero.
        """

        self.__game_w.create_rectangle((canvas_width - square_length) // 2,
                                       canvas_height // 2 + square_length,
                                       (canvas_width + square_length) // 2,
                                       canvas_height // 2 + 2 * square_length,
                                       fill="blue", tags="start_square")

    def __name_entry_window(self):
        """
        Create new window for name entry, if a person makes it onto the leaderboard.
        Return: String
        """

        self.__entry_box_w = tk.Toplevel(self.__root)
        self.__entry_box_w.title(f"Top Score! Enter name up to {self.__name_length} letters long.")
        self.__entry_box_w.attributes("-topmost", 'true')  # window stays in front of root

        self.__entry_box = tk.Text(self.__entry_box_w, width=60, height=1)
        self.__entry_box.pack(side=tk.LEFT)

        self.__enter_button = tk.Button(self.__entry_box_w, text="Enter", bg="green", fg="white",
                                        command=self.__get_text_destroy_entry_window)
        self.__enter_button.pack(side=tk.RIGHT)

    def __get_text_destroy_entry_window(self, event=None):
        """
        Only called when user finished entering name by clicking enter button.

        :param event: sometimes needed because of event callbacks
        """
        name = self.__entry_box.get("1.0", "end-1c")
        self.__scorekeeper.insert_score(self.__scorekeeper.curr_score, name)
        self.__Update_LeaderboardVar(self.__name_length)
        self.__entry_box_w.destroy()

    def __LeaderboardVar(self, name_length):
        """
        This could probably be a class but I can only go so deep down the rabbit hole.

        :return: tk.StringVar to automatically update leaderboard when leaderboard changed.
        """

        leaderboard = tk.StringVar()
        string = "LEADERBOARD\n\n"
        for score, name in self.__scorekeeper.leaderboard:
            while len(name) < name_length:
                name = ' ' + name
            string += f"{name}:\t{score}\n\n"
        leaderboard.set(string)
        return leaderboard

    def __Update_LeaderboardVar(self, name_length):
        """ Should probably be a method for the above function. """

        string = "LEADERBOARD\n\n"
        for score, name in self.__scorekeeper.leaderboard:
            name = name.strip()
            while len(name) < name_length:
                name = ' ' + name
            string += f"{name}:\t{score}\n\n"
        self.__leaderboard.set(string)

    def __ScoreVar(self):
        """ return: modified tk.Stringvar """

        score_var = tk.StringVar()
        score_var.set(f"Score: {self.__scorekeeper.curr_score}")
        return score_var

    def __Update_ScoreVar(self):
        """ To be called every time random square clicked in under the time limit. """

        self.__score_display.set(f"Score: {self.__scorekeeper.curr_score}")

    def __square_and_canvas_dimensions(self):
        """
        For convenience. Used when drawing on canvas.

        :return: updated square and canvas dimensions.
        """

        self.__game_w.update()
        canvas_width = self.__game_w.winfo_width()
        canvas_height = self.__game_w.winfo_height()
        square_length = min(canvas_width, canvas_height) // 20
        return square_length, canvas_width, canvas_height


if __name__ == "__main__":
    GUI()
