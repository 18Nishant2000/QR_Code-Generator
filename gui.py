from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from main import generate_qr
from kivy.uix.popup import Popup
from kivy.uix.image import Image


class Layout(BoxLayout):

    def __init__(self):
        super(Layout, self).__init__()
        Layout.orientation = 'vertical'
        self.add_widget(Label(text='WELCOME TO QR CODE GENERATOR'))
        self.add_widget(Label(text='Enter your text to generate QR CODE'))
        self.text = TextInput()
        self.add_widget(self.text)
        self.add_widget(Label(text='Enter file name with extension (.jpg/.png)'))
        self.file_name = TextInput()
        self.add_widget(self.file_name)
        self.submit = Button(text='Submit')
        self.submit.bind(on_press=self.click)
        self.add_widget(self.submit)
    
    def click(self, *args):
        # print('pressed')
        text = self.text.text
        f_name = self.file_name.text
        status = generate_qr(text, f_name)
        
        pop_close = Button(text='Close')
        layout = BoxLayout(orientation='vertical')
        
        if status == 1:
            # print('Success')
            pop_image = Image(source=f'QR_Codes/{f_name}')
            title='QR CODE'
            layout.add_widget(pop_image)
        else:
            pop_label = Label(text='Something went wrong!!')
            layout.add_widget(pop_label)
            title='Error'
        
        layout.add_widget(pop_close)
        popup = Popup(title=f'{title}', content=layout)
        popup.open()
        pop_close.bind(on_press=popup.dismiss)
        self.text.text = ''
        self.file_name.text = ''


class Main(App):

    def build(self):
        return Layout()

if __name__ == '__main__':
    Main().run()

