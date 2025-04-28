from tkinter import Tk
from ui.ui import UI


def main():
    """Alustaa ja käynnistää käyttöliittymän.
    """
    window = Tk()
    window.title("Battleship game")

    ui_view = UI(window)
    ui_view.start()

    window.mainloop()


if __name__ == "__main__":
    main()
