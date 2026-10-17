from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

Window.clearcolor = (0.04, 0.05, 0.10, 1)


class WinMusic(App):
    def build(self):
        self.title = "Win Music"

        root = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=16
        )

        root.add_widget(Label(
            text="[b]WIN MUSIC[/b]",
            markup=True,
            font_size="30sp",
            size_hint_y=None,
            height=65
        ))

        root.add_widget(Label(
            text="Your music, your world",
            font_size="16sp",
            size_hint_y=None,
            height=35
        ))

        self.search = TextInput(
            hint_text="Rechercher une chanson...",
            multiline=False,
            size_hint_y=None,
            height=50
        )
        root.add_widget(self.search)

        root.add_widget(Widget())

        root.add_widget(Label(
            text="[b]Aucune chanson sélectionnée[/b]\n\nTa musique t'attend.",
            markup=True,
            halign="center"
        ))

        controls = BoxLayout(
            size_hint_y=None,
            height=65,
            spacing=12
        )

        for symbol in ["|◀", "▶", "▶|"]:
            controls.add_widget(Button(
                text=symbol,
                font_size="24sp",
                background_normal="",
                background_color=(0.25, 0.32, 0.90, 1)
            ))

        root.add_widget(controls)

        root.add_widget(Button(
            text="♥  MES FAVORIS",
            size_hint_y=None,
            height=55,
            background_normal="",
            background_color=(0.65, 0.15, 0.35, 1)
        ))

        root.add_widget(Label(
            text="WIN MUSIC",
            size_hint_y=None,
            height=30
        ))

        return root


if __name__ == "__main__":
    WinMusic().run()
