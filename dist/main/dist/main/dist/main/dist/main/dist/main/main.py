from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.checkbox import CheckBox
from kivy.lang import Builder
from kivy.uix.textinput import TextInput

from thecropperclass import thecropperfunction
from thecopierclass import thecoppier
import plyer

Builder.load_file('TheMainPage.kv')

# from kivy.config import Config
# Config.set('graphics', 'width', '150')
# Config.set('graphics', 'height', '10')

from kivy.core.window import Window
Window.size = (396*1.5, 532*1.5)
Window.minimum_width, Window.minimum_height = Window.size

Window.top = 150
Window.left = 600

class RootWidget(ScreenManager):
    pass


class ZerothScreen(Screen):
    def sayfayaal(self):
        self.manager.current = 'first_screen'


class FirstScreen(Screen):

    def sayfaanaya(self):
        self.manager.current = 'zeroth_screen'

    def theformer(self):

        try:

            text = self.ids.theinput.text
            thecropperfunction(text)
            self.ids.formatid.text = "Başarılı, dosyalar oluşturuldu"


        except:

            self.ids.formatid.text = "Doğru bir dizin girmediniz, bir daha deneyin."


    def thecreater(self):
        try:
            text = self.ids.theinput2.text

            filetF = self.ids.filetbox.active
            garsonF = self.ids.garsonbox.active
            patikF = self.ids.patikbox.active
            bebeF = self.ids.bebebox.active
            ilkadimF = self.ids.ilkadimbox.active

            thecoppier(dir_path=text, filetFlag=filetF, patikFlag=patikF, bebeFlag=bebeF, garsonFlag=garsonF, ilkadimFlag=ilkadimF)

            if filetF or patikF or bebeF or garsonF or ilkadimF:
                self.ids.cogaltid.text = "İşlem başarılı"


        except:
            self.ids.cogaltid.text = "Doğru bir dizin girmediniz, bir daha deneyin."

    #
    # def thecopier(self):


class TheTiflani(App):
    def build(self):
        self.icon = "images/thenewlogo.ico"
        self.title = 'Nebim Foto Formatlayıcı'
        return RootWidget()


if __name__ == '__main__':
    TheTiflani().run()
