import toga
from PIL import Image
from toga.handlers import wrapped_handler
from toga.style import Pack
import requests
from pyquery import PyQuery as jQuery


html_doc=""" """

import requests
from wtforms import Form,StringField,validators


class MyForm(Form):
    name = StringField(u' Name', validators=[validators.input_required()])
    email = StringField(u'Email', validators=[validators.optional()])
    subject = StringField(u'Subject', validators=[validators.input_required()])
    message = StringField(u'Message', validators=[validators.optional()])
    



form = MyForm()


    
class WebViewApp(toga.App):
   def startup(self):
        payload = {'name': form.name.data, 'email': form.email.data,'subject':form.subject.data,'message':form.message.data}

        
        
        # Create a WebView widget and set the URL to load

       
        link ="contact.html"

        
        nr = requests.get("http://localhost/static")
        
        nwebview =toga.WebView(url=nr.url)
        doc= jQuery(url ="http://localhost/static")
       
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html_doc, 'html.parser')
        print(soup.div)

        # Create a main window and set the content as the WebView
        self.main_window = toga.MainWindow(self.formal_name)
        
        self.main_window.content = nwebview
        
        self.main_window.show()

def main():
    return WebViewApp('Odibaba Hub', 'org.chase.webview')
    


if __name__ == '__main__':
    main().main_loop()
   
    
