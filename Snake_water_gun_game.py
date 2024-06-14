import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
import random

kivy.require('1.11.1')

def game(comp, you):
    if comp == you:
        return None
    elif comp == 'S':
        if you == 'W':
            return False
        elif you == 'G':
            return True
    elif comp == 'W':
        if you == 'S':
            return True
        elif you == 'G':
            return False
    elif comp == 'G':
        if you == 'S':
            return False
        elif you == 'W':
            return True

class SnakeWaterGunGame(App):
    def build(self):
        self.title = 'Snake Water Gun Game'
        self.layout = BoxLayout(orientation='vertical')

        self.label = Label(text="Comp's turn: Snake, Water, Gun", font_size=24)
        self.layout.add_widget(self.label)

        self.result_label = Label(text="", font_size=24)
        self.layout.add_widget(self.result_label)

        button_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.2))

        snake_button = Button(text='Snake', on_press=self.player_choice)
        button_layout.add_widget(snake_button)

        water_button = Button(text='Water', on_press=self.player_choice)
        button_layout.add_widget(water_button)

        gun_button = Button(text='Gun', on_press=self.player_choice)
        button_layout.add_widget(gun_button)

        self.layout.add_widget(button_layout)

        return self.layout

    def player_choice(self, instance):
        choices = ['S', 'W', 'G']
        comp_choice = random.choice(choices)
        user_choice = instance.text[0]  # First letter of the button's text (S, W, G)

        result = game(comp_choice, user_choice)
        comp_choice_full = {'S': 'Snake', 'W': 'Water', 'G': 'Gun'}[comp_choice]

        result_text = f"Comp chose {comp_choice_full}\n"

        if result is None:
            result_text += "It's a Tie!"
        elif result:
            result_text += "You Win!"
        else:
            result_text += "You Lose!"

        self.result_label.text = result_text

if __name__ == '__main__':
    SnakeWaterGunGame().run()
