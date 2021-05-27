import subprocess
import tkinter as tk
from reset import main as reset
from typing import Union


class OBSCountdownController:
    def __init__(self):
        self.process: Union[None, subprocess.Popen] = None

    @classmethod
    def main(cls):
        control = cls()
        control.render()

    def handle_start(self):
        self.process = subprocess.Popen(['python', 'start.py'], stdout=subprocess.PIPE, shell=True)

    def handle_stop(self):
        if self.process is not None:
            subprocess.call(['taskkill', '/F', '/T', '/PID', str(self.process.pid)])
            self.process = None

    def render(self):
        window = tk.Tk()
        window.title('OBS Countdown Overlay')
        window.rowconfigure(0, minsize=50, weight=1)
        window.columnconfigure([0, 1, 2], minsize=50, weight=1)

        start_button = tk.Button(master=window, text='start', width=25, height=5, command=self.handle_start)
        start_button.grid(row=0, column=0, sticky='nsew')

        stop_button = tk.Button(master=window, text='stop', width=25, height=5, command=self.handle_stop)
        stop_button.grid(row=0, column=1, sticky='nsew')

        reset_button = tk.Button(master=window, text='reset', width=25, height=5, command=reset)
        reset_button.grid(row=0, column=2, sticky='nsew')

        window.mainloop()


if __name__ == '__main__':
    OBSCountdownController.main()
