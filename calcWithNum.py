#!usr/bin/env python
#-*- coding: utf-8 -*-
from tkinter import *
root = Tk()
root.title("CalcPro+-*/")
root.geometry('600x700+378+50')
n = StringVar()
number = ''

def main():
	global number
	if symbol == "+":
		result = float(numberSave1) + float(number)
		number = ''
		n.set("Ответ: " + str(result))
		return number
	elif symbol == '-':
		result = float(numberSave1) - float(number)
		number = ''
		n.set("Ответ: " + str(result))
		return number
	elif symbol == '*':
		result = float(numberSave1) * float(number)
		number = ''
		n.set("Ответ: " + str(result))
		return number
	elif symbol == '/':
		result = float(numberSave1) / float(number)
		number = ''
		n.set("Ответ: " + str(result))
		return number
	else:
		pass


def numberPlusHash():
	global number
	global symbol
	global numberSave1
	numberSave1 = number
	number = ''
	n.set(number)
	symbol = '+'
	return numberSave1
	return number
	return symbol

def numberMinusHash():
	global number
	global symbol
	global numberSave1
	numberSave1 = number
	number = ''
	n.set(number)
	symbol = '-'
	return numberSave1
	return number
	return symbol

def numberSplitHash():
	global number
	global symbol
	global numberSave1
	numberSave1 = number
	number = ''
	n.set(number)
	symbol = '/'
	return numberSave1
	return number
	return symbol

def numberMultiplyHash():
	global number
	global symbol
	global numberSave1
	numberSave1 = number
	number = ''
	n.set(number)
	symbol = '*'
	return numberSave1
	return number
	return symbol

def numberSqr():
	global number
	numberInt = float(number)
	number = str(numberInt ** 2)
	n.set("Ответ: " + number)
	number = ''
	return number

def addNum1():
	global number
	number += '1'
	n.set(number)
	return number

def addNum2():
	global number
	number += "2"
	n.set(number)
	return number

def addNum3():
	global number
	number += "3"
	n.set(number)
	return number

def addNum4():
	global number
	number += '4'
	n.set(number)
	return number

def addNum5():
	global number
	number += '5'
	n.set(number)
	return number

def addNum6():
	global number
	number += "6"
	n.set(number)
	return number

def addNum7():
	global number
	number += '7'
	n.set(number)
	return number

def addNum8():
	global number
	number += '8'
	n.set(number)
	return number

def addNum9():
	global number
	number += '9'
	n.set(number)
	return number

def addNum0():
	global number
	number += '0'
	n.set(number)
	return number

def addDot():
	global number
	number += '.'
	n.set(number)
	return number

def rmNum():
	global number
	number = number[:-1]
	n.set(number)
	return number

def numberClear():
	global number
	number = ''
	n.set(number)
	return number



label = Label(textvariable = n, bg = '#fff', fg = "#000", padx = '10', pady = '10', font = '38')
label.place(x = '0', y = '0', width = '600', height = '100')
btnClear = Button(text = 'C', background = '#ccc', foreground = '#000', highlightcolor = '#fff', command = numberClear)
btnClear.place(height = '50', width = '150', x = '0', y = '100')
btnSqr = Button(text = 'x^2', background = '#ccc', foreground = '#000', highlightcolor = '#fff', command = numberSqr)
btnSqr.place(height = '50', width = '150', x = '150', y = '100')
btnPlus = Button(text = '+', background = '#ccc', foreground = '#000', highlightcolor = '#fff', command = numberPlusHash)
btnPlus.place(height = '50', width = '150', x = '0', y = '150')
btnMinus = Button(text = '-', background = '#ccc', foreground = '#000', highlightcolor = '#fff', command = numberMinusHash)
btnMinus.place(height = '50', width = '150', x = '150', y = '150')
btnSplit = Button(text = '/', background = '#ccc', foreground = '#000', highlightcolor = '#fff', command = numberSplitHash)
btnSplit.place(height = '50', width = '150', x = '300', y = '150')
btnMultiply = Button(text = '*', background = '#ccc', foreground = '#000', highlightcolor = '#fff', command = numberMultiplyHash)
btnMultiply.place(height = '50', width = '150', x = '450', y = '150')
btn1 = Button(text = '1', background = '#ccc', foreground = '#000', highlightcolor = '#fff', command = addNum1)
btn1.place(height = "100", width = "200", x = '0', y = '200')
btn2 = Button(text = '2', background = '#ccc', foreground = '#000', highlightcolor = '#fff', command = addNum2)
btn2.place(height = "100", width = "200", x = '200', y = '200')
btn3 = Button(text = '3', background = '#ccc', foreground = '#000', highlightcolor = '#fff', command = addNum3)
btn3.place(height = "100", width = "200", x = '400', y = '200')
btn4 = Button(text = '4', background = '#ccc', foreground = '#000', highlightcolor = '#fff', command = addNum4)
btn4.place(height = "100", width = "200", x = '0', y = '300')
btn5 = Button(text = '5', background = '#ccc', foreground = '#000', highlightcolor = '#fff', command = addNum5)
btn5.place(height = "100", width = "200", x = '200', y = '300')
btn6 = Button(text = '6', background = '#ccc', foreground = '#000', highlightcolor = '#fff', command = addNum6)
btn6.place(height = "100", width = "200", x = '400', y = '300')
btn7 = Button(text = '7', background = '#ccc', foreground = '#000', highlightcolor = '#fff', command = addNum7)
btn7.place(height = "100", width = "200", x = '0', y = '400')
btn8 = Button(text = '8', background = '#ccc', foreground = '#000', highlightcolor = '#fff', command = addNum8)
btn8.place(height = "100", width = "200", x = '200', y = '400')
btn9 = Button(text = '9', background = '#ccc', foreground = '#000', highlightcolor = '#fff', command = addNum9)
btn9.place(height = "100", width = "200", x = '400', y = '400')
btnDot = Button(text = '.', background = '#ccc', foreground = '#000', highlightcolor = '#fff', command = addDot)
btnDot.place(height = "100", width = "200", x = '0', y = '500')
btn0 = Button(text = '0', background = '#ccc', foreground = '#000', highlightcolor = '#fff', command = addNum0)
btn0.place(height = "100", width = "200", x = '200', y = '500')
btnDel = Button(text = 'DEL', background = '#ccc', foreground = '#000', highlightcolor = '#fff', command = rmNum)
btnDel.place(height = "100", width = "200", x = '400', y = '500')
btnCompile = Button(text = 'Решить', background = '#ccc', foreground = '#000', highlightcolor = '#fff', command = main)
btnCompile.place(height = "100", width = "200", x = '200', y = '600')

root.mainloop()