#GUI Version of TIC-TAC-TOE using kivy
import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from algo import Algo

my_algo = Algo()
AI_mode = False
player_name = ['X','O']
player_sign = ['X','O']

#Login Page
class Login(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(font_size = 40, text="Tic Tac Toe"))
        self.add_widget(Label(text="---RS_Games", font_size=20))
        self.add_widget(Label(text="Player X:", font_size=20))
        self.player_x = TextInput(multiline=False, font_size=20)
        self.add_widget(self.player_x)
        self.add_widget(Label(text="Player O:", font_size=20))
        self.player_o = TextInput(text="Computer", multiline=False, font_size=20)
        self.add_widget(self.player_o)
        self.add_widget(Label())
        self.start = Button(text="Start")
        self.start.bind(on_press=self.start_game)
        self.add_widget(self.start)

    def start_game(self, button):
        player_name[0] = self.player_x.text
        player_name[1] = self.player_o.text
        if player_name[1]=="Computer":
            global AI_mode
            AI_mode = True 
        my_app.game.message.text = "{} to play".format(player_name[my_app.game.current_player])
        my_app.screen_manager.current = "game"

#Game Page
class Game(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 3
        self.buttons = []
        for x in range(0,9):
            button = Button(text='-', font_size=30)
            button.number = x
            button.bind(on_press=self.button_press)
            self.add_widget(button)
            self.buttons.append(button)
        self.message = Label(font_size=30)
        self.add_widget(self.message)
        self.play = True
        self.add_widget(Label())
        self.replay = Button(text="Replay")
        self.replay.bind(on_press=self.restart)
        self.current_player = 0

    def button_press(self, button):
        if button.text == '-' and self.play:
            button.text = player_sign[self.current_player]
            my_algo.board[button.number] = player_sign[self.current_player]
            if my_algo.check_win():
                self.message.text = "{} won".format(player_name[self.current_player])
                self.play = False
                self.add_widget(self.replay)
                if self.current_player == 0:
                    self.current_player = 1
                else:
                    self.current_player = 0
            elif my_algo.check_draw():
                self.message.text = "Draw"
                self.play = False
                self.add_widget(self.replay)
                if self.current_player == 0:
                    self.current_player = 1
                else:
                    self.current_player = 0
            else:
                if self.current_player == 0:
                    self.current_player = 1
                else:
                    self.current_player = 0
                self.message.text = "{} to play".format(player_name[self.current_player])

        #AI decision
        if AI_mode and self.play and self.current_player==1:
            choice = my_algo.ai_choice()
            self.button_press(self.buttons[choice])

    def restart(self, button):
        for x in range(0,9):
            my_algo.board[x] = '-'
            for x in self.buttons:
                x.text = '-'
                self.message.text = "{} to play".format(player_name[self.current_player])
        self.remove_widget(self.replay)
        self.play = True

        #AI decision when it has the first move
        if AI_mode and self.play and self.current_player==1:
            choice = my_algo.ai_choice()
            self.button_press(self.buttons[choice])

class MyApp(App):
    def build(self):
        self.title = "TIC-TAC-TOE"
        self.screen_manager = ScreenManager()
        self.login_screen = Screen(name="login")
        self.login_screen.add_widget(Login())
        self.screen_manager.add_widget(self.login_screen)
        self.game_screen = Screen(name="game")
        self.game = Game()
        self.game_screen.add_widget(self.game)
        self.screen_manager.add_widget(self.game_screen)
        return self.screen_manager

if __name__ == "__main__":
    my_app = MyApp()
    my_app.run()
