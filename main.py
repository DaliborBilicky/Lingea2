import tkinter
import config


def main():
    root = tkinter.Tk()
    window = config.WindowHandler(root, 500, 500, "white")
    window.display()


    root.mainloop()

if __name__ == "__main__":
    main()