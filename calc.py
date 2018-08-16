#!/usr/bin/env python3

from tkinter import *
import re

class Calc(Tk):

    def add(self, x, y):
        return (x + y)

    def sub(self, x, y):
        return (x - y)

    def div(self, x, y):
        if y != 0:
            return (x / y)
        else:
            return ("Division by zero")

    def mult(self, x, y):
        return (x * y)
    
    def equals(self, label):
        if len(self.expression) == 3:
            if re.search("\.", self.expression[0]) or re.search("\.", self.expression[2]):
                self.expression[0] = float(self.expression[0])
                self.expression[2] = float(self.expression[2])
            else:
                self.expression[0] = int(self.expression[0])
                self.expression[2] = int(self.expression[2])

            if self.expression[1] == "+":
                res = self.add(self.expression[0], self.expression[2])
            elif self.expression[1] == "-":
                res = self.sub(self.expression[0], self.expression[2])
            elif self.expression[1] == "*":
                res = self.mult(self.expression[0], self.expression[2])
            elif self.expression[1] == "/":
                res = self.div(self.expression[0], self.expression[2])
            
            res = str(res)
            if re.search("([0-9]+)\.0$", res):
                res = re.sub("([0-9]+)\.0$", r"\1", res)
            label.config(text=res)
            self.expression = []
            if re.search("[0-9\.]+", res):
                self.expression.append(res)
        
    def clear(self, label):
        self.expression = []
        label.config(text="                                                    ")
        
    def enter(self, param, label):
        param = str(param)
        if re.search("[0-9]", param):
            if len(self.expression) == 0:
                self.expression.append(param)
                label.config(text=param)
            elif re.search("[0-9]+", self.expression[len(self.expression) - 1]):
                self.expression[len(self.expression) - 1] += param
                label.config(text=self.expression[len(self.expression) - 1])
            elif re.search("[0-9]+\.", self.expression[len(self.expression) - 1]):
                self.expression[len(self.expression) - 1] += param
                label.config(text=self.expression[len(self.expression) - 1])
            else:
                self.expression.append(param)
                label.config(text=param)
        elif param == ".":
            if len(self.expression) >= 1:
                if re.search("^[0-9]+$", self.expression[len(self.expression) - 1]):
                    self.expression[len(self.expression) - 1] += param
                    label.config(text=self.expression[len(self.expression) - 1])
        elif re.search("[\+\-\*/.]", param):
            if len(self.expression) >= 1 and re.search("[0-9]+$", self.expression[len(self.expression) - 1]):
                label.config(text="                                                    ")
                self.expression.append(param)

    def __init__(self):    
        self.expression = []
        self.result = 0
        calc = Tk()
        calc.title("My calculator")
        calc.geometry("200x200")

        label = Label(calc, text=self.result)
        label.pack(side=TOP)

        #row 1
        row1 = Frame(calc)
        row1.pack(side=TOP)
        btn_sin = Button(calc, text="sin", command="", height=2 , width=4)
        btn_sin.pack(in_=row1, side=LEFT)
        btn_ac = Button(calc, text="AC", command=lambda: self.clear(label), height=2 , width=4)
        btn_ac.pack(in_=row1, side=LEFT)
        btn_signs = Button(calc, text="+/-", command="", height=2 , width=4)
        btn_signs.pack(in_=row1, side=LEFT)
        btn_percent = Button(calc, text="%", command="", height=2 , width=4)
        btn_percent.pack(in_=row1, side=LEFT)
        btn_slash = Button(calc, text="÷", command=lambda: self.enter("/", label), height=2 , width=4)
        btn_slash.pack(in_=row1, side=LEFT)

        #row 2
        row2 = Frame(calc)
        row2.pack(side=TOP)
        btn_cos = Button(calc, text="cos", command="", height=2 , width=4)
        btn_cos.pack(in_=row2, side=LEFT)
        btn_7 = Button(calc, text="7", command=lambda: self.enter(7, label), height=2 , width=4)
        btn_7.pack(in_=row2, side=LEFT)
        btn_8 = Button(calc, text="8", command=lambda: self.enter(8, label), height=2 , width=4)
        btn_8.pack(in_=row2, side=LEFT)
        btn_9 = Button(calc, text="9", command=lambda: self.enter(9, label), height=2 , width=4)
        btn_9.pack(in_=row2, side=LEFT)
        btn_mult = Button(calc, text="x", command=lambda: self.enter("*", label), height=2 , width=4)
        btn_mult.pack(in_=row2, side=LEFT)

        #row 3
        row3 = Frame(calc)
        row3.pack(side=TOP)
        btn_tan = Button(calc, text="tan", command="", height=2 , width=4)
        btn_tan.pack(in_=row3, side=LEFT)
        btn_4 = Button(calc, text="4", command=lambda: self.enter(4, label), height=2 , width=4)
        btn_4.pack(in_=row3, side=LEFT)
        btn_5 = Button(calc, text="5", command=lambda: self.enter(5, label), height=2 , width=4)
        btn_5.pack(in_=row3, side=LEFT)
        btn_6 = Button(calc, text="6", command=lambda: self.enter(6, label), height=2 , width=4)
        btn_6.pack(in_=row3, side=LEFT)
        btn_sub = Button(calc, text="-", command=lambda: self.enter("-", label), height=2 , width=4)
        btn_sub.pack(in_=row3, side=LEFT)

        #row 4
        row4 = Frame(calc)
        row4.pack(side=TOP)
        btn_pow = Button(calc, text="^", command="", height=2 , width=4)
        btn_pow.pack(in_=row4, side=LEFT)
        btn_1 = Button(calc, text="1", command=lambda: self.enter(1, label), height=2 , width=4)
        btn_1.pack(in_=row4, side=LEFT)
        btn_2 = Button(calc, text="2", command=lambda: self.enter(2, label), height=2 , width=4)
        btn_2.pack(in_=row4, side=LEFT)
        btn_3 = Button(calc, text="3", command=lambda: self.enter(3, label), height=2 , width=4)
        btn_3.pack(in_=row4, side=LEFT)
        btn_add = Button(calc, text="+", command=lambda: self.enter("+", label), height=2 , width=4)
        btn_add.pack(in_=row4, side=LEFT)

        #row 5
        row5 = Frame(calc)
        row5.pack(side=TOP)
        btn_sqr = Button(calc, text="√", command="", height=2 , width=4)
        btn_sqr.pack(in_=row5, side=LEFT)
        btn_0 = Button(calc, text="0", command=lambda: self.enter(0, label), height=2 , width=8)
        btn_0.pack(in_=row5, side=LEFT)
        btn_dec = Button(calc, text=".", command=lambda: self.enter(".", label), height=2 , width=4)
        btn_dec.pack(in_=row5, side=LEFT)
        btn_eq = Button(calc, text="=", command=lambda: self.equals(label), height=2 , width=4)
        btn_eq.pack(in_=row5, side=LEFT)

        calc.mainloop()

calc = Calc()