#!/usr/bin/env python3

import re
import math

class CalcController:

    def __init__(self, calc):
        self.expression = []
        self.result = 0
        self.calc = calc

    def equals(self, label, isRes):
        if len(self.expression) == 3:
            if re.search("\.", self.expression[0]) or re.search("\.", self.expression[2]):
                self.expression[0] = float(self.expression[0])
                self.expression[2] = float(self.expression[2])
            else:
                self.expression[0] = int(self.expression[0])
                self.expression[2] = int(self.expression[2])

            if self.expression[1] == "+":
                res = self.calc.add(self.expression[0], self.expression[2])
            elif self.expression[1] == "-":
                res = self.calc.sub(self.expression[0], self.expression[2])
            elif self.expression[1] == "*":
                res = self.calc.mult(self.expression[0], self.expression[2])
            elif self.expression[1] == "/":
                res = self.calc.div(self.expression[0], self.expression[2])
            elif self.expression[1] == "pow":
                res = math.pow(self.expression[0], self.expression[2])
            
            res = str(res)
            if re.search("([-0-9]+)\.0$", res):
                res = re.sub("([-0-9]+)\.0$", r"\1", res)
            label.config(text=res)
            self.expression = []
            if re.search("[-0-9\.]+", res):
                self.expression.append(res)
            self.calc.isRes = 1
        
    def clear(self, label, isRes):
        self.expression = []
        label.config(text="                                                    ")
        isRes = 0
        
    def enter(self, param, label, isRes):
        param = str(param)
        if re.search("[-0-9]", param):
            if len(self.expression) == 0:
                self.expression.append(param)
                label.config(text=param)
            elif re.search("[-0-9\.]+", self.expression[len(self.expression) - 1]):
                if isRes == 0:
                    if re.search("([-0-9\.]+)pow([-0-9\.]+)?$", self.expression[len(self.expression) - 1]):
                        self.expression[len(self.expression) - 1] += param
                        param = re.sub("([-0-9\.]+)pow([-0-9\.]+)?$", r"\2", self.expression[len(self.expression) - 1]) 
                        label.config(text=param)
                    else:
                        self.expression[len(self.expression) - 1] += param
                        label.config(text=self.expression[len(self.expression) - 1])
                elif isRes == 1:
                    self.clear(label, isRes)
                    self.expression = [param]
                    label.config(text=param)
                    self.calc.isRes = 0
            else:
                self.expression.append(param)
                label.config(text=param)
        elif param == "pi":
            if len(self.expression) == 0 or len(self.expression) == 2:
                if isRes == 0:
                    self.expression.append(str(math.pi))
                    label.config(text=math.pi)
                elif isRes == 1:
                    self.clear(label, isRes)
                    self.expression = [str(math.pi)]
                    label.config(text=math.pi)
                    self.calc.isRes = 0
        elif param == "e":
            if len(self.expression) == 0 or len(self.expression) == 2:
                if isRes == 0:
                    self.expression.append(str(math.e))
                    label.config(text=math.e)
                elif isRes == 1:
                    self.clear(label, isRes)
                    self.expression = [str(math.e)]
                    label.config(text=math.e)
                    self.calc.isRes = 0
        elif param == ".":
            if len(self.expression) >= 1:
                if re.search("^[-0-9]+$", self.expression[len(self.expression) - 1]):
                    self.expression[len(self.expression) - 1] += param
                    label.config(text=self.expression[len(self.expression) - 1])

    def operation(self, param, label, isRes):
        param = str(param)
        if param == "%":
            if len(self.expression) >= 1:
                if re.search("^[-0-9]+$", self.expression[len(self.expression) - 1]):
                    self.expression[len(self.expression) - 1] = int(self.expression[len(self.expression) - 1])/100
                    self.expression[len(self.expression) - 1] = str(self.expression[len(self.expression) - 1])
                    label.config(text=self.expression[len(self.expression) - 1])
                    self.calc.isRes = 1
                elif re.search("^[-0-9.]+$", self.expression[len(self.expression) - 1]):
                    self.expression[len(self.expression) - 1] = float(self.expression[len(self.expression) - 1])/100
                    self.expression[len(self.expression) - 1] = str(self.expression[len(self.expression) - 1])
                    label.config(text=self.expression[len(self.expression) - 1])
                    self.calc.isRes = 1
        elif param == "inv":
            if len(self.expression) >= 1:
                if re.search("^[-0-9]+$", self.expression[len(self.expression) - 1]):
                    self.expression[len(self.expression) - 1] = int(self.expression[len(self.expression) - 1]) * (-1)
                    self.expression[len(self.expression) - 1] = str(self.expression[len(self.expression) - 1])
                    label.config(text=self.expression[len(self.expression) - 1])
                    self.calc.isRes = 1
                elif re.search("^[-0-9.]+$", self.expression[len(self.expression) - 1]):
                    self.expression[len(self.expression) - 1] = float(self.expression[len(self.expression) - 1]) * (-1)
                    self.expression[len(self.expression) - 1] = str(self.expression[len(self.expression) - 1])
                    label.config(text=self.expression[len(self.expression) - 1])
                    self.calc.isRes = 1
        elif param == "cos":
            if len(self.expression) >= 1:
                if re.search("^[-0-9]+$", self.expression[len(self.expression) - 1]):
                    self.expression[len(self.expression) - 1] = math.cos(math.radians(int(self.expression[len(self.expression) - 1])))
                    self.expression[len(self.expression) - 1] = str(self.expression[len(self.expression) - 1])
                    label.config(text=self.expression[len(self.expression) - 1])
                    self.calc.isRes = 1
                elif re.search("^[-0-9.]+$", self.expression[len(self.expression) - 1]):
                    self.expression[len(self.expression) - 1] = math.cos(math.radians(float(self.expression[len(self.expression) - 1])))
                    self.expression[len(self.expression) - 1] = str(self.expression[len(self.expression) - 1])
                    label.config(text=self.expression[len(self.expression) - 1])
                    self.calc.isRes = 1
        elif param == "sin":
            if len(self.expression) >= 1:
                if re.search("^[-0-9]+$", self.expression[len(self.expression) - 1]):
                    self.expression[len(self.expression) - 1] = math.sin(math.radians(int(self.expression[len(self.expression) - 1])))
                    self.expression[len(self.expression) - 1] = str(self.expression[len(self.expression) - 1])
                    label.config(text=self.expression[len(self.expression) - 1])
                    self.calc.isRes = 1
                elif re.search("^[-0-9.]+$", self.expression[len(self.expression) - 1]):
                    self.expression[len(self.expression) - 1] = math.sin(math.radians(float(self.expression[len(self.expression) - 1])))
                    self.expression[len(self.expression) - 1] = str(self.expression[len(self.expression) - 1])
                    label.config(text=self.expression[len(self.expression) - 1])
                    self.calc.isRes = 1
        elif param == "tan":
            if len(self.expression) >= 1:
                if re.search("^[-0-9]+$", self.expression[len(self.expression) - 1]):
                    self.expression[len(self.expression) - 1] = math.tan(math.radians(int(self.expression[len(self.expression) - 1])))
                    self.expression[len(self.expression) - 1] = str(self.expression[len(self.expression) - 1])
                    label.config(text=self.expression[len(self.expression) - 1])
                    self.calc.isRes = 1
                elif re.search("^[-0-9.]+$", self.expression[len(self.expression) - 1]):
                    self.expression[len(self.expression) - 1] = math.tan(math.radians(float(self.expression[len(self.expression) - 1])))
                    self.expression[len(self.expression) - 1] = str(self.expression[len(self.expression) - 1])
                    label.config(text=self.expression[len(self.expression) - 1])
                    self.calc.isRes = 1
        elif param == "sqr":
            if len(self.expression) >= 1:
                if re.search("^[-0-9]+$", self.expression[len(self.expression) - 1]):
                    self.expression[len(self.expression) - 1] = math.sqrt(int(self.expression[len(self.expression) - 1]))
                    self.expression[len(self.expression) - 1] = str(self.expression[len(self.expression) - 1])
                    if re.search("([-0-9]+)\.0$", self.expression[len(self.expression) - 1]):
                        self.expression[len(self.expression) - 1] = re.sub("([-0-9]+)\.0$", r"\1", self.expression[len(self.expression) - 1])
                    label.config(text=self.expression[len(self.expression) - 1])
                    self.calc.isRes = 1
                elif re.search("^[-0-9.]+$", self.expression[len(self.expression) - 1]):
                    self.expression[len(self.expression) - 1] = math.sqrt(float(self.expression[len(self.expression) - 1]))
                    self.expression[len(self.expression) - 1] = str(self.expression[len(self.expression) - 1])
                    label.config(text=self.expression[len(self.expression) - 1])
                    self.calc.isRes = 1
        elif param == "exp":
            if len(self.expression) >= 1:
                if re.search("^[-0-9]+$", self.expression[len(self.expression) - 1]):
                    self.expression[len(self.expression) - 1] = math.exp(int(self.expression[len(self.expression) - 1]))
                    self.expression[len(self.expression) - 1] = str(self.expression[len(self.expression) - 1])
                    if re.search("([-0-9]+)\.0$", self.expression[len(self.expression) - 1]):
                        self.expression[len(self.expression) - 1] = re.sub("([-0-9]+)\.0$", r"\1", self.expression[len(self.expression) - 1])
                    label.config(text=self.expression[len(self.expression) - 1])
                    self.calc.isRes = 1
                elif re.search("^[-0-9.]+$", self.expression[len(self.expression) - 1]):
                    self.expression[len(self.expression) - 1] = math.exp(float(self.expression[len(self.expression) - 1]))
                    self.expression[len(self.expression) - 1] = str(self.expression[len(self.expression) - 1])
                    label.config(text=self.expression[len(self.expression) - 1])
                    self.calc.isRes = 1
        elif param == "ln":
            if len(self.expression) >= 1:
                if re.search("^[-0-9]+$", self.expression[len(self.expression) - 1]):
                    self.expression[len(self.expression) - 1] = math.log(int(self.expression[len(self.expression) - 1]))
                    self.expression[len(self.expression) - 1] = str(self.expression[len(self.expression) - 1])
                    if re.search("([-0-9]+)\.0$", self.expression[len(self.expression) - 1]):
                        self.expression[len(self.expression) - 1] = re.sub("([-0-9]+)\.0$", r"\1", self.expression[len(self.expression) - 1])
                    label.config(text=self.expression[len(self.expression) - 1])
                    self.calc.isRes = 1
                elif re.search("^[-0-9.]+$", self.expression[len(self.expression) - 1]):
                    self.expression[len(self.expression) - 1] = math.log(float(self.expression[len(self.expression) - 1]))
                    self.expression[len(self.expression) - 1] = str(self.expression[len(self.expression) - 1])
                    label.config(text=self.expression[len(self.expression) - 1])
                    self.calc.isRes = 1
        elif param == "log10":
            if len(self.expression) >= 1:
                if re.search("^[-0-9]+$", self.expression[len(self.expression) - 1]):
                    self.expression[len(self.expression) - 1] = math.log10(int(self.expression[len(self.expression) - 1]))
                    self.expression[len(self.expression) - 1] = str(self.expression[len(self.expression) - 1])
                    if re.search("([-0-9]+)\.0$", self.expression[len(self.expression) - 1]):
                        self.expression[len(self.expression) - 1] = re.sub("([-0-9]+)\.0$", r"\1", self.expression[len(self.expression) - 1])
                    label.config(text=self.expression[len(self.expression) - 1])
                    self.calc.isRes = 1
                elif re.search("^[-0-9.]+$", self.expression[len(self.expression) - 1]):
                    self.expression[len(self.expression) - 1] = math.log10(float(self.expression[len(self.expression) - 1]))
                    self.expression[len(self.expression) - 1] = str(self.expression[len(self.expression) - 1])
                    label.config(text=self.expression[len(self.expression) - 1])
                    self.calc.isRes = 1
        elif param == "pow":
            if len(self.expression) >= 1 and re.search("[-0-9]+$", self.expression[len(self.expression) - 1]):
                label.config(text="                                                    ")
                self.expression.append(param)
        elif re.search("[\+\-\*/.]", param):
            if len(self.expression) >= 1 and re.search("[-0-9]+$", self.expression[len(self.expression) - 1]):
                label.config(text="                                                    ")
                self.expression.append(param)