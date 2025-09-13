from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.graphics.vertex_instructions import Rectangle
from kivy.graphics.context_instructions import Color
from kivymd.uix.label import MDLabel
from kivy.uix.gridlayout import GridLayout

class Principal(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.ecuacion = ''
        
        with self.canvas:
            Color(0.6, 0.6, 0.6, 0.9)
            self.rect = Rectangle(size=(0, 0), pos=(0, 0))
    
        self.muestra = MDLabel(text="0", bold=True, halign="right", pos_hint={'center_x': 0.5, 'center_y': 0.925}, font_style="H4")
        self.add_widget(self.muestra)
        
        self.botones = GridLayout(cols=4, rows=5, spacing=5, padding=10, pos_hint={'center_x': 0.5, 'top': 0.82}, size_hint=(1, 0.7))
        
        # Botones de la calculadora
        botones_texto = [
            'C', '/', '*', '-',
            '7', '8', '9', '+',
            '4', '5', '6', '%',
            '1', '2', '3', '=',
            '0', '.', '(', ')',
        ]
        
        for texto in botones_texto:
            if texto == '=':
                btn = Button(text=texto, on_press=self.calcular, background_color='lightblue')
            elif texto == 'C':
                btn = Button(text=texto, on_press=self.borrar, background_color='lightblue')
            else:
                btn = Button(text=texto, on_press=lambda x, t=texto: self.presiona(t), background_color='lightblue')
            self.botones.add_widget(btn)

        self.add_widget(self.botones)
            
    def on_size(self, *args):
        self.rect.size = (self.size[0], 0.15 * self.size[1])
        self.rect.pos = (0, 0.85 * self.height)
            
    def presiona(self, valor):
        self.ecuacion += valor
        self.muestra.text = self.ecuacion
        
    def borrar(self, instance):
        self.ecuacion = ''
        self.muestra.text = '0'
    
    def calcular(self, instance):
        try:
            resultado = str(eval(self.ecuacion))
            self.muestra.text = resultado
            self.ecuacion = resultado
        except Exception:
            self.muestra.text = "Error"
            self.ecuacion = ""
    
class MiApp(MDApp):
    def build(self):
        sc = ScreenManager()
        sc.add_widget(Principal(name='Principal'))
        return sc

MiApp().run()