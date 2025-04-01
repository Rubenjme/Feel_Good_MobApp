from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file("design.kv") # Carga el archivo kv

class LoginScreen(Screen): # Pantalla de inicio de sesión
    pass

class RootWidget(ScreenManager): # Pantalla principal que contiene todas las pantallas
    pass

class MainApp(App): # Clase principal de la app
    def build(self):
        return RootWidget()
    

if __name__ == "__main__": 
    MainApp().run()
