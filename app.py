import ttkbootstrap as ttk
from ttkbootstrap.constants import TOP, DANGER, SUCCESS, LEFT, BOTH, YES
from utils._globals import CATEGORIES
from tracker import start_listener, set_activity


class App(ttk.Window):
    def __init__(self, themename):
        super().__init__(themename=themename)

        self.title("Input Tracker")
        self.colors = self.style.colors
        self.theme_list = self.style.theme_names()


class AppButton(ttk.Frame):
    def __init__(self, master, category_selector, **kwargs):
        super().__init__(master, **kwargs)
        self.grid(row=2, column=0, columnspan=2, padx=0)
        self.category_selector = category_selector
        self.create_buttons()

    def create_buttons(self):
        def run_app():
            print(f"Category selected: {self.category_selector.category_selected}")
            set_activity(self.category_selector.category_selected)
            start_listener()

        def exit_app():
            self.master.destroy()

        button_container = ttk.Frame(self)
        button_container.pack(side=TOP, padx=5, pady=5)
        run_button = ttk.Button(
            master=button_container, text="Run", command=run_app, bootstyle=SUCCESS
        )
        run_button.pack(
            side=LEFT,
            padx=5,
            pady=10,
        )

        exit_button = ttk.Button(
            master=button_container, text="Exit", command=exit_app, bootstyle=DANGER
        )
        exit_button.pack(side=LEFT, padx=5, pady=10)


class CategorySelector(ttk.Frame):
    def __init__(self, master, category, **kwargs):
        super().__init__(master, **kwargs)
        self.grid(row=1, column=0, columnspan=2, padx=0)
        self.category_selected = category
        self.container = ttk.Labelframe(self, text="Category")
        self.container.pack(side=TOP, pady=5, fill=BOTH, expand=YES)
        self.create_category_selector()

    def create_category_selector(self, initial_value="general"):
        def my_upd():
            self.category_selected = my_str.get()

        my_str = ttk.StringVar(value=initial_value)

        menu_field_container = ttk.Frame(self.container)
        menu_field_container.pack(
            side=TOP,
            padx=5,
            pady=5,
        )

        menu_label = ttk.Label(
            master=menu_field_container,
            text="Select a category:",
            font="Calibri 12 bold",
        )
        menu_label.pack(side=LEFT, padx=5, pady=10)

        menu = ttk.Menubutton(master=menu_field_container, textvariable=my_str)
        menu.pack(side=LEFT, padx=5, pady=10)

        menu_input = ttk.Menu(menu)
        for x in CATEGORIES.values():
            menu_input.add_radiobutton(
                label=x, variable=my_str, value=x, command=lambda: my_upd()
            )

        menu["menu"] = menu_input


if __name__ == "__main__":
    app = App(themename="superhero")
    category_selector = CategorySelector(master=app, category="general")
    AppButton(
        master=app,
        category_selector=category_selector,
    )
    app.mainloop()
