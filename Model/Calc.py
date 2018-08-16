#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#import calculator
import sys
sys.path.append("..")
from tkinter import *
import re
from Python_d03.Controller import controller

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
        
    def __init__(self):    
        self.controller = controller.CalcController(self)
        self.expression = []
        self.result = 0
        self.isRes = 0
        calc = Tk()
        calc.title("My calculator")
        calc.geometry("240x200")

        label = Label(calc, text=self.result)
        label.pack(side=TOP)

        #row 1
        row1 = Frame(calc)
        row1.pack(side=TOP)
        btn_pi = Button(calc, text="π", command=lambda: self.controller.enter("pi", label, self.isRes), height=2 , width=4)
        btn_pi.pack(in_=row1, side=LEFT)
        btn_sin = Button(calc, text="sin", command=lambda: self.controller.operation("sin", label, self.isRes), height=2 , width=4)
        btn_sin.pack(in_=row1, side=LEFT)
        btn_ac = Button(calc, text="AC", command=lambda: self.controller.clear(label, self.isRes), height=2 , width=4)
        btn_ac.pack(in_=row1, side=LEFT)
        btn_signs = Button(calc, text="+/-", command=lambda: self.controller.operation("inv", label, self.isRes), height=2 , width=4)
        btn_signs.pack(in_=row1, side=LEFT)
        btn_percent = Button(calc, text="%", command=lambda: self.controller.operation("%", label, self.isRes), height=2 , width=4)
        btn_percent.pack(in_=row1, side=LEFT)
        btn_slash = Button(calc, text="÷", command=lambda: self.controller.operation("/", label, self.isRes), height=2 , width=4)
        btn_slash.pack(in_=row1, side=LEFT)

        #row 2
        row2 = Frame(calc)
        row2.pack(side=TOP)
        btn_e = Button(calc, text="e", command=lambda: self.controller.enter("e", label, self.isRes), height=2 , width=4)
        btn_e.pack(in_=row2, side=LEFT)
        btn_cos = Button(calc, text="cos", command=lambda: self.controller.operation("cos", label, self.isRes), height=2 , width=4)
        btn_cos.pack(in_=row2, side=LEFT)
        btn_7 = Button(calc, text="7", command=lambda: self.controller.enter(7, label, self.isRes), height=2 , width=4)
        btn_7.pack(in_=row2, side=LEFT)
        btn_8 = Button(calc, text="8", command=lambda: self.controller.enter(8, label, self.isRes), height=2 , width=4)
        btn_8.pack(in_=row2, side=LEFT)
        btn_9 = Button(calc, text="9", command=lambda: self.controller.enter(9, label, self.isRes), height=2 , width=4)
        btn_9.pack(in_=row2, side=LEFT)
        btn_mult = Button(calc, text="x", command=lambda: self.controller.operation("*", label, self.isRes), height=2 , width=4)
        btn_mult.pack(in_=row2, side=LEFT)

        #row 3
        row3 = Frame(calc)
        row3.pack(side=TOP)
        btn_exp = Button(calc, text="exp", command=lambda: self.controller.operation("exp", label, self.isRes), height=2 , width=4)
        btn_exp.pack(in_=row3, side=LEFT)
        btn_tan = Button(calc, text="tan", command=lambda: self.controller.operation("tan", label, self.isRes), height=2 , width=4)
        btn_tan.pack(in_=row3, side=LEFT)
        btn_4 = Button(calc, text="4", command=lambda: self.controller.enter(4, label, self.isRes), height=2 , width=4)
        btn_4.pack(in_=row3, side=LEFT)
        btn_5 = Button(calc, text="5", command=lambda: self.controller.enter(5, label, self.isRes), height=2 , width=4)
        btn_5.pack(in_=row3, side=LEFT)
        btn_6 = Button(calc, text="6", command=lambda: self.controller.enter(6, label, self.isRes), height=2 , width=4)
        btn_6.pack(in_=row3, side=LEFT)
        btn_sub = Button(calc, text="-", command=lambda: self.controller.operation("-", label, self.isRes), height=2 , width=4)
        btn_sub.pack(in_=row3, side=LEFT)

        #row 4
        row4 = Frame(calc)
        row4.pack(side=TOP)
        btn_ln = Button(calc, text="ln", command=lambda: self.controller.operation("ln", label, self.isRes), height=2 , width=4)
        btn_ln.pack(in_=row4, side=LEFT)
        btn_pow = Button(calc, text="pow", command=lambda: self.controller.operation("pow", label, self.isRes), height=2 , width=4)
        btn_pow.pack(in_=row4, side=LEFT)
        btn_1 = Button(calc, text="1", command=lambda: self.controller.enter(1, label, self.isRes), height=2 , width=4)
        btn_1.pack(in_=row4, side=LEFT)
        btn_2 = Button(calc, text="2", command=lambda: self.controller.enter(2, label, self.isRes), height=2 , width=4)
        btn_2.pack(in_=row4, side=LEFT)
        btn_3 = Button(calc, text="3", command=lambda: self.controller.enter(3, label, self.isRes), height=2 , width=4)
        btn_3.pack(in_=row4, side=LEFT)
        btn_add = Button(calc, text="+", command=lambda: self.controller.operation("+", label, self.isRes), height=2 , width=4)
        btn_add.pack(in_=row4, side=LEFT)

        #row 5
        row5 = Frame(calc)
        row5.pack(side=TOP)
        btn_log10 = Button(calc, text="log10", command=lambda: self.controller.operation("log10", label, self.isRes), height=2 , width=4)
        btn_log10.pack(in_=row5, side=LEFT)
        btn_sqr = Button(calc, text="√", command=lambda: self.controller.operation("sqr", label, self.isRes), height=2 , width=4)
        btn_sqr.pack(in_=row5, side=LEFT)
        btn_0 = Button(calc, text="0", command=lambda: self.controller.enter(0, label, self.isRes), height=2 , width=8)
        btn_0.pack(in_=row5, side=LEFT)
        btn_dec = Button(calc, text=".", command=lambda: self.controller.enter(".", label, self.isRes), height=2 , width=4)
        btn_dec.pack(in_=row5, side=LEFT)
        btn_eq = Button(calc, text="=", command=lambda: self.controller.equals(label, self.isRes), height=2 , width=4)
        btn_eq.pack(in_=row5, side=LEFT)

        calc.mainloop()