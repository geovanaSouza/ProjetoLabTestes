from src.calculadora_biz import CalculadoraBiz
import PySimpleGUI as sg
import os
import json

class Calculadora:

    def __init__(self):
        self.args = {}

    def show(self): 
        layout = [
            [sg.Input(
                key="result",
                disabled=True,
                size=(28, 30))],
            [
                sg.Submit("7", key="7", size=(2, 2)),
                sg.Submit("8", key="8", size=(2, 2)),
                sg.Submit("9", key="9", size=(2, 2)),
                sg.Submit("X", key="x", size=(2, 2), button_color=("black", "green"))
            ],
            [
                sg.Submit("4", key="4", size=(2, 2)),
                sg.Submit("5", key="5", size=(2, 2)),
                sg.Submit("6", key="6", size=(2, 2)),
                sg.Submit("%", key="/", size=(2, 2), button_color=("black", "green"))
            ],
            [
                sg.Submit("1", key="1", size=(2, 2)),
                sg.Submit("2", key="2", size=(2, 2)),
                sg.Submit("3", key="3", size=(2, 2)),
                sg.Submit("+", key="+", size=(2, 2), button_color=("black", "green"))
            ],
            [                
                sg.Submit("C", key="c", size=(2, 2), button_color=("black", "red")),
                sg.Submit("0", key="0", size=(2, 2)),
                sg.Submit("=", key="=", size=(2, 2), button_color=("black", "green")),
                sg.Submit("-", key="-", size=(2, 2), button_color=("black", "green"))
            ],
        ]
        window = sg.Window('Calculadora', layout)
        
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancel':
                break

            window['result'].update(values['result'] + event)

            if event == "c":
                self.args = {}
                window['result'].update("")

            if "action" in self.args:                                
                if event == "=":
                    self.args["b"] = float(values['result'].split(self.args["action"])[1])
                    aux = CalculadoraBiz().action(**self.args)
                    self.args = {}
                    window['result'].update(str(aux))
                    self.args["a"] = aux
                elif event in [ "+", "-", "/", "x"]:
                    window['result'].update(values['result'].replace(self.args["action"], event))
                    self.args["action"] = event
            elif event in [ "+", "-", "/", "x"]:
                self.args["action"] = event
                self.args["a"] = float(values['result'])
                window['result'].update(values['result'] + event)


if __name__ == '__main__':
    calc = Calculadora()
    calc.show()
