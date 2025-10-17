from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen

# Load the KV file
Builder.load_file("simple.kv")

# Define screens
class HomeScreen(Screen):
    pass

class ProfileScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

# Main App
class SimpleApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"
        return Builder.load_file("simple.kv")

if __name__ == "__main__":
    SimpleApp().run()
