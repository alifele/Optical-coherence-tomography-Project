#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Jan 24, 2020 04:01:02 PM +0330  platform: Linux

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import gui_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    gui_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    gui_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'

        top.geometry("600x450+335+164")
        top.minsize(1, 1)
        top.maxsize(1351, 738)
        top.resizable(1, 1)
        top.title("New Toplevel")

        self.Amplitude_label = tk.Label(top)
        self.Amplitude_label.place(relx=0.117, rely=0.244, height=15, width=186)
        self.Amplitude_label.configure(text='''Please enter the Amplitude''')

        self.Frequency_label = tk.Label(top)
        self.Frequency_label.place(relx=0.117, rely=0.356, height=15, width=186)
        self.Frequency_label.configure(text='''Please Enter the Frequency''')

        self.amplitude = tk.Entry(top)
        self.amplitude.place(relx=0.5, rely=0.244,height=17, relwidth=0.243)
        self.amplitude.configure(background="white")
        self.amplitude.configure(font="TkFixedFont")

        self.Frequency = tk.Entry(top)
        self.Frequency.place(relx=0.5, rely=0.356,height=17, relwidth=0.243)
        self.Frequency.configure(background="white")
        self.Frequency.configure(font="TkFixedFont")

        self.show_button = tk.Button(top, command = self.plot)
        self.show_button.place(relx=0.4, rely=0.467, height=25, width=119)
        self.show_button.configure(activebackground="#d9d9d9")
        self.show_button.configure(text='''Show the plot''')

if __name__ == '__main__':
    vp_start_gui()





