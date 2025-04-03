from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json
from datetime import datetime

Builder.load_file("design.kv") # Carga el archivo kv

class LoginScreen(Screen): # Pantalla de inicio de sesión
    def sign_up(self):
        self.manager.current = "sign_up_screen" # Cambia a la pantalla de registro


class RootWidget(ScreenManager): # Pantalla principal que contiene todas las pantallas
    pass


class SignUpScreen(Screen):
    def add_user(self, uname, pword):
        with open("users.json") as file:
            users = json.load(file)

        users[uname] = {"username": uname, "password": pword, 
                        "created": datetime.now().strftime("%Y-%m-%d %H-%M-%S")}
        
        with open("users.json", "w") as file: # Guardo los datos introducidos en el archivo json
            json.dump(users, file)
        self.manager.current = "sign_up_screen_success"


class SignUpScreenSuccess(Screen):
    def go_to_login(self):
        self.manager.current = "login_screen"


class MainApp(App): # Clase principal de la app
    def build(self):
        return RootWidget()



if __name__ == "__main__": 
    MainApp().run()
