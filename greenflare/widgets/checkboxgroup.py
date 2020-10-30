from tkinter import W, ttk, IntVar


class CheckboxGroup(ttk.LabelFrame):

    def __init__(self, parent, text, boxes, settings, column):
        s = ttk.Style()
        s.configure('Green.TFrame', background='green')
        s.configure('Blue.TFrame', background='blue')

        self.parent = parent
        self.boxes = boxes
        self.text = text
        self.settings = settings
        self.column = column

        ttk.LabelFrame.__init__(
            self, self.parent, text=self.text, width=25, height=50)

        self.widgets = []
        self.vars = []

        self.populate_checkboxes()

    def checkbox_clicked(self):
        for i, e in enumerate(self.widgets):
            value = self.vars[i].get()
            setting = self.widgets[i]['text']
            column = self.text_to_column(setting)
            if value == 1 and column not in self.settings[self.column]:
                self.settings[self.column].append(column)
            elif value == 0 and column in self.settings[self.column]:
                self.settings[self.column].remove(column)

    def text_to_column(self, txt):
        return txt.lower().replace(" ", "_").replace(".", "_").replace("-", "_")

    def populate_checkboxes(self):
        for i, e in enumerate(self.boxes):
            if self.text_to_column(e) in self.settings[self.column]:
                self.vars.append(IntVar())
                self.vars[-1].set(1)
            else:
                self.vars.append(IntVar())
            self.widgets.append(ttk.Checkbutton(
                self, text=e, onvalue=1, offvalue=0, variable=self.vars[-1], command=self.checkbox_clicked, width=22))
            self.widgets[-1].pack(side='top', anchor='w', padx=5, pady=2)
