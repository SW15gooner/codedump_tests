import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.text = tk.Text(self, wrap="word", height=20)
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.text.yview)
        self.text.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side="right", fill="y")
        self.text.pack(side="left", fill="both", expand=True)

        self.text.bind("<Return>", self.process_input)
        self.prompt = ">>> "

        self.insert_prompt()

    def insert_prompt(self):
        # make sure the last line ends with a newline; remember that
        # tkinter guarantees a trailing newline, so we get the
        # character before this trailing newline ('end-1c' gets the
        # trailing newline, 'end-2c' gets the char before that)
        c = self.text.get("end-2c")
        if c != "\n":
            self.text.insert("end", "\n")
        self.text.insert("end", self.prompt, ("prompt",))

        # this mark lets us find the end of the prompt, and thus
        # the beggining of the user input
        self.text.mark_set("end-of-prompt", "end-1c")
        self.text.mark_gravity("end-of-prompt", "left")

    def process_input(self, event=None):
        # if there is an event, it happened before the class binding,
        # thus before the newline actually got inserted; we'll
        # do that here, then skip the class binding.
        self.text.insert("end", "\n")
        command = self.text.get("end-of-prompt", "end-1c")
        self.text.insert("end", "You asked '%s'" % command)
        self.text.see("end")
        self.insert_prompt()

        # this prevents the class binding from firing, since we 
        # inserted the newline in this method
        return "break"

root = tk.Tk()
root.wm_geometry("400x400")
app = Application(root).pack(side="top", fill="both", expand=True)
root.wm_attributes("-topmost", 1)
root.focus_force()
root.mainloop()