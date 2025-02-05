import tkinter as tk
from tkinter import ttk, messagebox, Menu
import random
import time

class RPSGameApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Rock Paper Scissors by Kai Piper")
        self.master.minsize(400, 300)
        self.master.resizable(False, False)
        try:
            self.master.iconbitmap('icon.ico')
        except Exception:
            pass
        self.master.geometry("+300+300")
        self.master.config(cursor="dot")
        self.master.attributes("-topmost", True)
        
        # Game settings
        self.game_mode = tk.StringVar(value="Standard")  # or "Best of 3"
        self.rounds_to_win = 2  # Only used in Best of 3 mode

        # Score variables
        self.wins = tk.IntVar(value=0)
        self.losses = tk.IntVar(value=0)
        self.draws = tk.IntVar(value=0)
        
        # Result text variable
        self.result_var = tk.StringVar(value="Welcome to RPS!")
        
        # Create main container frame using ttk
        self.container = ttk.Frame(master, padding=10)
        self.container.grid(row=0, column=0, sticky="nsew")
        
        # Create UI sections
        self.create_header()
        self.create_game_buttons()
        self.create_result_display()
        self.create_scoreboard()
        self.create_status_bar()
        self.create_menu()
        
    def create_header(self):
        header = ttk.Frame(self.container)
        header.grid(row=0, column=0, sticky="ew", pady=(0,10))
        header.columnconfigure(1, weight=1)
        # Use an emoji for logo
        self.logo_label = ttk.Label(header, text="✊📄✂️", font=("Helvetica", 32))
        self.logo_label.grid(row=0, column=0, padx=5)
        self.title_label = ttk.Label(header, text="Rock Paper Scissors", font=("Helvetica", 20, "bold"))
        self.title_label.grid(row=0, column=1, sticky="w")
        # Settings button to open Game Mode settings
        self.settings_btn = ttk.Button(header, text="Settings", command=self.open_settings)
        self.settings_btn.grid(row=0, column=2, padx=5)
        
    def create_game_buttons(self):
        btn_frame = ttk.Frame(self.container)
        btn_frame.grid(row=1, column=0, pady=10)
        # Load images (ensure these files exist in the working directory)
        try:
            self.rock_img = tk.PhotoImage(file="rock.gif")
        except Exception:
            self.rock_img = None
        try:
            self.paper_img = tk.PhotoImage(file="paper.gif")
        except Exception:
            self.paper_img = None
        try:
            self.scissors_img = tk.PhotoImage(file="scissors.gif")
        except Exception:
            self.scissors_img = None
        
        self.btn_rock = ttk.Button(btn_frame, text="Rock", image=self.rock_img,
                                     compound="top", command=lambda: self.play_round(1))
        self.btn_rock.grid(row=0, column=0, padx=5)
        self.btn_paper = ttk.Button(btn_frame, text="Paper", image=self.paper_img,
                                     compound="top", command=lambda: self.play_round(2))
        self.btn_paper.grid(row=0, column=1, padx=5)
        self.btn_scissors = ttk.Button(btn_frame, text="Scissors", image=self.scissors_img,
                                     compound="top", command=lambda: self.play_round(3))
        self.btn_scissors.grid(row=0, column=2, padx=5)
        
        # Bind right-click (Button-3) to show context menu on each button
        self.context_menu = Menu(self.master, tearoff=0)
        self.context_menu.add_command(label="Select Rock", command=lambda: self.play_round(1))
        self.context_menu.add_command(label="Select Paper", command=lambda: self.play_round(2))
        self.context_menu.add_command(label="Select Scissors", command=lambda: self.play_round(3))
        for btn in (self.btn_rock, self.btn_paper, self.btn_scissors):
            btn.bind("<Button-3>", self.do_popup)
    
    def do_popup(self, event):
        try:
            self.context_menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.context_menu.grab_release()
    
    def create_result_display(self):
        result_frame = ttk.Frame(self.container)
        result_frame.grid(row=2, column=0, pady=10, sticky="ew")
        self.result_label = ttk.Label(result_frame, textvariable=self.result_var, font=("Helvetica", 14, "italic"))
        self.result_label.pack()
    
    def create_scoreboard(self):
        score_frame = ttk.Frame(self.container)
        score_frame.grid(row=3, column=0, pady=10)
        ttk.Label(score_frame, text="Score:", font=("Helvetica", 14, "bold")).grid(row=0, column=0, padx=5)
        ttk.Label(score_frame, text="Wins:", font=("Helvetica", 12)).grid(row=1, column=0, sticky="e", padx=5)
        ttk.Label(score_frame, textvariable=self.wins, font=("Helvetica", 12)).grid(row=1, column=1, sticky="w", padx=5)
        ttk.Label(score_frame, text="Losses:", font=("Helvetica", 12)).grid(row=2, column=0, sticky="e", padx=5)
        ttk.Label(score_frame, textvariable=self.losses, font=("Helvetica", 12)).grid(row=2, column=1, sticky="w", padx=5)
        ttk.Label(score_frame, text="Draws:", font=("Helvetica", 12)).grid(row=3, column=0, sticky="e", padx=5)
        ttk.Label(score_frame, textvariable=self.draws, font=("Helvetica", 12)).grid(row=3, column=1, sticky="w", padx=5)
        reset_btn = ttk.Button(score_frame, text="Reset Score", command=self.reset_score)
        reset_btn.grid(row=4, column=0, columnspan=2, pady=5)
    
    def create_status_bar(self):
        self.status_var = tk.StringVar(value="Ready")
        self.status_bar = ttk.Label(self.master, textvariable=self.status_var, relief="sunken",
                                    anchor="w", font=("Helvetica", 10), padding=5)
        self.status_bar.grid(row=4, column=0, sticky="ew")
    
    def create_menu(self):
        self.menu = Menu(self.master)
        file_menu = Menu(self.menu, tearoff=0)
        file_menu.add_command(label="About", command=self.show_about)
        file_menu.add_command(label="Exit", command=self.master.destroy)
        self.menu.add_cascade(label="File", menu=file_menu)
        help_menu = Menu(self.menu, tearoff=0)
        help_menu.add_command(label="Contact", command=lambda: messagebox.showinfo("Contact", "Email: kai9987kai@gmail.com"))
        self.menu.add_cascade(label="Help", menu=help_menu)
        self.master.config(menu=self.menu)
    
    def play_round(self, user_choice):
        # user_choice: 1 = Rock, 2 = Paper, 3 = Scissors
        computer_choice = random.randrange(1, 4)
        result_text = ""
        # For best-of-3 mode, check if game mode is selected
        if self.game_mode.get() == "Best of 3":
            series_over = False
            if self.wins.get() == self.rounds_to_win or self.losses.get() == self.rounds_to_win:
                series_over = True
            if series_over:
                result_text = "Series complete! Reset score to play again."
                self.result_var.set(result_text)
                self.set_status("Series complete")
                return

        # Determine outcome
        if user_choice == computer_choice:
            result_text = "It's a draw. No points."
            self.draws.set(self.draws.get() + 1)
        elif (user_choice == 1 and computer_choice == 3) or \
             (user_choice == 2 and computer_choice == 1) or \
             (user_choice == 3 and computer_choice == 2):
            result_text = self.get_choice_text(user_choice, computer_choice) + "\nYou win!"
            self.wins.set(self.wins.get() + 1)
        else:
            result_text = self.get_choice_text(user_choice, computer_choice) + "\nYou lose!"
            self.losses.set(self.losses.get() + 1)
        
        # Simulate a brief delay before updating result (animation-like effect)
        self.master.after(200, lambda: self.result_var.set(result_text))
        self.set_status("Round played")
    
    def get_choice_text(self, user, computer):
        choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
        return f"You chose {choices.get(user)}, I chose {choices.get(computer)}."
    
    def reset_score(self):
        self.wins.set(0)
        self.losses.set(0)
        self.draws.set(0)
        self.set_status("Score reset")
    
    def show_about(self):
        about_text = (
            "Rock Paper Scissors v3.0\nDeveloped by Kai Piper\n\n"
            "This game is a modern, feature-rich version of Rock Paper Scissors.\n"
            "Features include: context menus, score tracking, game modes (Standard/Best of 3),\n"
            "and a settings dialog for advanced options."
        )
        messagebox.showinfo("About", about_text)
    
    def set_status(self, text):
        self.status_var.set(text)
    
    def open_settings(self):
        settings_win = tk.Toplevel(self.master)
        settings_win.title("Settings")
        settings_win.transient(self.master)
        settings_win.grab_set()
        settings_win.resizable(False, False)
        settings_win.geometry("")  # Auto-size based on content
        ttk.Label(settings_win, text="Settings", font=("Helvetica", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10)
        
        ttk.Label(settings_win, text="Game Mode:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        mode_combo = ttk.Combobox(settings_win, textvariable=self.game_mode, state="readonly", 
                                  values=["Standard", "Best of 3"])
        mode_combo.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        
        ttk.Button(settings_win, text="Close", command=settings_win.destroy).grid(row=2, column=0, columnspan=2, pady=10)
    
    def check_auto_refresh(self):
        # Placeholder for future auto-refresh feature in advanced options.
        self.master.after(self.refresh_interval, self.check_auto_refresh)
    
    def do_popup(self, event):
        try:
            self.context_menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.context_menu.grab_release()
    
    # History and Favorites functions
    def get_history(self):
        if os.path.exists("history.txt"):
            try:
                with open("history.txt", "r") as f:
                    return f.read().splitlines()
            except Exception:
                return []
        return []
    
    def save_history(self, history):
        try:
            with open("history.txt", "w") as f:
                f.write("\n".join(history))
        except Exception as e:
            print("Error saving history:", e)
    
    def add_history(self, query):
        history = self.get_history()
        if query not in history:
            history.insert(0, query)
            history = history[:10]
            self.save_history(history)
            self.load_history()
    
    def load_history(self):
        history = self.get_history()
        self.history_listbox.delete(0, tk.END)
        for item in history:
            self.history_listbox.insert(tk.END, item)
    
    def clear_history(self):
        if messagebox.askyesno("Clear History", "Are you sure you want to clear history?"):
            if os.path.exists("history.txt"):
                os.remove("history.txt")
            self.load_history()
            self.set_status("History cleared")
    
    def on_history_double_click(self, event):
        selection = self.history_listbox.curselection()
        if selection:
            text = self.history_listbox.get(selection[0])
            self.ip_entry.delete(0, tk.END)
            self.ip_entry.insert(0, text)
    
    def get_favorites(self):
        if os.path.exists("favorites.txt"):
            try:
                with open("favorites.txt", "r") as f:
                    return f.read().splitlines()
            except Exception:
                return []
        return []
    
    def save_favorites(self, favs):
        try:
            with open("favorites.txt", "w") as f:
                f.write("\n".join(favs))
        except Exception as e:
            print("Error saving favorites:", e)
    
    def add_favorite(self):
        text = self.ip_entry.get().strip()
        if text:
            favs = self.get_favorites()
            if text not in favs:
                favs.insert(0, text)
                favs = favs[:10]
                self.save_favorites(favs)
                self.load_favorites()
                self.set_status("Added to favorites")
            else:
                self.set_status("Already in favorites")
        else:
            messagebox.showerror("Input Error", "Enter text to add as favorite.")
    
    def load_favorites(self):
        favs = self.get_favorites()
        self.fav_listbox.delete(0, tk.END)
        for fav in favs:
            self.fav_listbox.insert(tk.END, fav)
    
    def clear_favorites(self):
        if messagebox.askyesno("Clear Favorites", "Are you sure you want to clear favorites?"):
            if os.path.exists("favorites.txt"):
                os.remove("favorites.txt")
            self.load_favorites()
            self.set_status("Favorites cleared")
    
    def on_fav_double_click(self, event):
        selection = self.fav_listbox.curselection()
        if selection:
            fav = self.fav_listbox.get(selection[0])
            self.ip_entry.delete(0, tk.END)
            self.ip_entry.insert(0, fav)
    
    def export_data(self):
        # Exports the latest game result and scores as JSON
        data = {
            "result": self.result_var.get(),
            "wins": self.wins.get(),
            "losses": self.losses.get(),
            "draws": self.draws.get()
        }
        try:
            with open("rps_export.json", "w") as f:
                json.dump(data, f, indent=2)
            messagebox.showinfo("Export", "Data exported to rps_export.json")
            self.set_status("Export successful")
        except Exception as e:
            messagebox.showerror("Export Error", f"Error exporting data: {str(e)}")
    
    def create_menu(self):
        self.menu = tk.Menu(self.master)
        file_menu = tk.Menu(self.menu, tearoff=0)
        file_menu.add_command(label="About", command=self.show_about)
        file_menu.add_command(label="Reset Score", command=self.reset_score)
        file_menu.add_command(label="Export Data", command=self.export_data)
        file_menu.add_command(label="Exit", command=self.master.destroy)
        self.menu.add_cascade(label="File", menu=file_menu)
        help_menu = tk.Menu(self.menu, tearoff=0)
        help_menu.add_command(label="Contact", command=lambda: messagebox.showinfo("Contact", "Email: kai9987kai@gmail.com"))
        self.menu.add_cascade(label="Help", menu=help_menu)
        self.master.config(menu=self.menu)
    
    def set_status(self, text):
        self.status_var.set(text)
    
    def show_about(self):
        about_text = (
            "Rock Paper Scissors v3.0\nDeveloped by Kai Piper\n\n"
            "This game features advanced score tracking, game mode settings (Standard/Best of 3),\n"
            "context menus on buttons, history and favorites management, and export options."
        )
        messagebox.showinfo("About", about_text)
    
    def play_round(self, user_choice):
        # If Best of 3 mode is enabled, check series status
        if self.game_mode.get() == "Best of 3":
            if self.wins.get() == self.rounds_to_win or self.losses.get() == self.rounds_to_win:
                self.result_var.set("Series complete! Please reset the score to play again.")
                self.set_status("Series complete")
                return
        
        computer_choice = random.randrange(1, 4)
        outcome = ""
        if user_choice == computer_choice:
            outcome = "It's a draw. No points awarded."
            self.draws.set(self.draws.get() + 1)
        elif (user_choice == 1 and computer_choice == 3) or \
             (user_choice == 2 and computer_choice == 1) or \
             (user_choice == 3 and computer_choice == 2):
            outcome = self.get_choice_text(user_choice, computer_choice) + "\nYou win!"
            self.wins.set(self.wins.get() + 1)
        else:
            outcome = self.get_choice_text(user_choice, computer_choice) + "\nYou lose!"
            self.losses.set(self.losses.get() + 1)
        # Animate result update (simulate a brief delay)
        self.master.after(200, lambda: self.result_var.set(outcome))
        self.set_status("Round played")
    
    def get_choice_text(self, user, computer):
        choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
        return f"You chose {choices.get(user)}, I chose {choices.get(computer)}."
    
    def reset_score(self):
        self.wins.set(0)
        self.losses.set(0)
        self.draws.set(0)
        self.set_status("Score reset")
    
    def threaded_wrapper(self, func, *args):
        threading.Thread(target=lambda: func(*args), daemon=True).start()
    
    def threaded_fetch_info(self):
        self.threaded_wrapper(self.fetch_info)
    
    def threaded_process(self):
        self.threaded_wrapper(self.play_round, 1)  # Not used here; use play_round from button commands

if __name__ == "__main__":
    root = tk.Tk()
    app = RPSGameApp(root)
    root.bind("<Escape>", lambda e: root.destroy())
    root.mainloop()
