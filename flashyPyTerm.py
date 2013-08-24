import tkinter as tk
from tkinter import ttk
import subprocess
import sys, os

class FlashyPyTerm (tk.Tk) :
	def __init__ (self):
		
		# SETTINGS
		screenWidth = 1920
		screenHeight = 1080
		path = os.path.realpath('>')
		systemFont = ('Dotimatrix 7',20)
		# ********
		
		# Make fullscreen
		tk.Tk.__init__(self)
		self.wm_state('zoomed')
		self.overrideredirect(1)
		self.attributes('-topmost', True)
		
		# Create background image
		self.canvas_image = tk.PhotoImage(file='terminal_logo_sm.gif')	
		
		# Create canvas and insert image and text
		self.canvas = tk.Canvas(self, highlightthickness=0, bg='black')
		self.canvas.create_image(screenWidth/2,screenHeight/2, anchor='center', image=self.canvas_image)	
		self.canvas.create_text(5,1075, anchor='sw', font=systemFont, fill='green')
		self.canvas.place(anchor='center', relx=0.5,rely=0.5, relwidth=1, relheight=1)
	
		# Add current path label
		self.currentPathLabel = tk.Label(self, text=path, font=systemFont, fg='green', bg='black')
		self.currentPathLabel.place(anchor='sw', relx=0, rely=1)
		
		# Add command entry
		self.commandVar = tk.StringVar()
		self.commandEntry = tk.Entry(self, borderwidth=0, font=systemFont, fg='green', bg='black', textvariable=self.commandVar)
		self.commandEntry.bind('<Return>', self.handleInput)
		self.commandEntry.focus_set()
		self.commandEntry.place(anchor='sw', x=self.currentPathLabel.winfo_reqwidth()+10, rely=1)
		
		# Add global key bindings
		# TODO: Add ctrl-c escape for running programs
	
	def handleInput(self, a=None):
		command = self.commandVar.get().split(' ')
		
		if (command[0] == 'exit'):
			sys.exit("Hack the planet")
		
		proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		self.commandEntry.delete(0, 999)
		
		for line in iter(proc.stdout.readline, ''):
			if (line):
				self.canvas.insert(2,'end', line.rstrip())
				self.canvas.insert(2,'end', '\n')
				tk.Tk().update_idletasks()
			else:
				break

if __name__ == "__main__":	
	app = FlashyPyTerm()
	app.mainloop()