from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.clock import Clock
from functools import partial
from LIFX import LIFX
from kivy.network.urlrequest import UrlRequest
import certifi



class DemoBox(BoxLayout):
    """
    This class demonstrates various techniques that can be used for binding to
    events. Although parts could me made more optimal, advanced Python concepts
    are avoided for the sake of readability and clarity.
    """
    def __init__(self, **kwargs):
        super(DemoBox, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.handler = LIFX()

        # Text Input
        label = Label(text='LIFX API KEY', font_size='20sp')
        self.txt = TextInput()
        self.txt.bind(text=self.on_text)

        btn = Button(text="Power ON", background_color=(1,1,1,1))
        btn.bind(on_press=self.power_on)

        btn2 = Button(text="Power OFF")
        btn2.bind(on_press=self.off)

        btn3 = Button(text="Power PULSE")
        btn3.bind(on_press=self.pulse)

        btn4 = Button(text="Mexicana")
        btn4.bind(on_press=self.mex)

        btn5 = Button(text="Mango")
        btn5.bind(on_press=self.man)

        btn6 = Button(text="Pisces")
        btn6.bind(on_press=self.pis)

        btn7 = Button(text="Hygge")
        btn7.bind(on_press=self.hyg)

        btn8 = Button(text="Blue Haus")
        btn8.bind(on_press=self.blu)

        btn9 = Button(text="Lady Prep")
        btn9.bind(on_press=self.lad)

        btn10 = Button(text="Vday Vibes")
        btn10.bind(on_press=self.vda)

        btn11 = Button(text="Habesha Nation")
        btn11.bind(on_press=self.hab)


        for but in [label, self.txt, btn, btn2, btn3, btn4, btn5, 
        btn6, btn7, btn8, btn9, btn10, btn11]:
            self.add_widget(but)

    def on_text(self, instance, value):
        self.handler.token = self.txt.text
        # self.handler.auth()
        print('Text widget: ', self.txt.text)

    def on(self, instance):
        self.handler.power_on()
        print('Powering ON')

    def off(self, instance):
        self.handler.power_off()
        print('Powering OFF')

    def pulse(self, instance):
        self.handler.pulse()
        print('Pulse Effect')

    def mex(self, instance):
        self.handler.mexicana()
        print('Preset: mexicana')

    def man(self, instance):
        self.handler.mango()
        print('Preset: mango')

    def pis(self, instance):
        self.handler.pisces()
        print('Preset: pisces')

    def hyg(self, instance):
        self.handler.hygge()
        print('Preset: hygge')

    def blu(self, instance):
        self.handler.blue_haus()
        print('Preset: blue haus')

    def lad(self, instance):
        self.handler.lady_prep()
        print('Preset: lady prep')

    def vda(self, instance):
        self.handler.vday_vibes()
        print('Preset: vday vibe')

    def hab(self, instance):
        self.handler.habesha_nation()
        print('Preset: habesha nation')

    def power_on(self, instance):
            token = self.txt.text
            headers = {"Content-Type": "application/json",
                        "Authorization": "Bearer %s" % token}
            payload = {"power": "on"}
            url = 'https://api.lifx.com/v1/lights/all/state'
            req = UrlRequest(url,req_body=payload, req_headers = headers, method="PUT",ca_file=certifi.where())
            # req.wait(delay=7)
            print(req.result) 

class DemoApp(App):
    def build(self):
        return DemoBox()

if __name__ == "__main__":
    DemoApp().run()
