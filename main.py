import re

import kivy
import random

from kivy.app import App
from kivy.metrics import sp
from kivy.storage.jsonstore import JsonStore
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

red = [1, 0, 0, 1]
green = [0, 1, 0, 1]
blue = [0, 0, 1, 1]
purple = [1, 0, 1, 1]
db = JsonStore('db.json')


class FloatInput(TextInput):
    non_numbers_pattern = re.compile('[^0-9]')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.font_size = sp(20)

    def insert_text(self, substring, from_undo=False):
        non_numbers_pattern = self.non_numbers_pattern
        if '.' in self.text:
            result_str = re.sub(non_numbers_pattern, '', substring)
        else:
            result_str = '.'.join(
                re.sub(non_numbers_pattern, '', s)
                for s in substring.split('.', 1)
            )
        return super().insert_text(result_str, from_undo=from_undo)


class WelcomeScreen(Screen):
    size_of_rows = 1/5

    def __init__(self, **kw):
        super().__init__(**kw)
        grid = GridLayout(cols=2, padding=sp(30))#, row_default_height=sp(36), col_default_width=sp(200), row_force_default=True, col_force_default=True)
        # grid.pos_hint = {'center_x': .5, 'center_y': .5}
        #grid.size_hint_y = None
        #grid.height = grid.minimum_height
        grid.add_widget(Label(text='Ваш рост:'))
        grid.add_widget(FloatInput(multiline=False, input_type='number', size_hint=(self.size_of_rows, self.size_of_rows)))
        grid.add_widget(Label(text='Ваш возраст:'))
        grid.add_widget(FloatInput(multiline=False, input_type='number'))
        grid.add_widget(Label(text='Ваш текущий вес:'))
        grid.add_widget(FloatInput(multiline=False, input_type='number'))
        grid.add_widget(Label(text='Желаемый вес:'))
        grid.add_widget(FloatInput(multiline=False, input_type='number'))
        self.add_widget(grid)


class MainScreen(Screen):
    pass


# class WelcomeWidget(GridLayout):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.pos_hint = {'center_x': .5, 'center_y': .5}
#         self.cols = 2
#         self.padding = 30
#         self.add_widget(Label(text='Ваш рост:'))
#         inp = FloatInput(multiline=False, input_type='number')
#         inp.font_size = sp(20)
#         inp.size_hint_y = None
#         inp.height = sp(36)
#         inp.pos_hint = {'center_x': .5, 'center_y': .5}
#         self.add_widget(inp)
#         self.add_widget(Label(text='Ваш возраст:'))
#         self.add_widget(FloatInput(multiline=False, input_type='number'))
#         self.add_widget(Label(text='Ваш текущий вес:'))
#         self.add_widget(FloatInput(multiline=False, input_type='number'))
#         self.add_widget(Label(text='Желаемый вес:'))
#         self.add_widget(FloatInput(multiline=False, input_type='number'))


class HBoxLayoutExample(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(WelcomeScreen(name='welcome'))
        sm.add_widget(MainScreen(name='main'))
        sm.current = 'main'
        return sm


if __name__ == "__main__":
    app = HBoxLayoutExample()
    app.run()
