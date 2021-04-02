from pywinauto.application import Application
from pywinauto import Desktop
import time, json, sys, schedule

class Program:
    def __init__(self, bk, path):
        self.app = Application(backend=bk).start(path)
        self.creditials = {
            'username': None,
            'password': None
        }

    def wait_for_run(self):
        while True:
            time.sleep(1)
            try:
                self.app.Dialog['Użytkownik:Edit'].set_text('')
                break
            except: 
                pass

    def load_creditials(self):
        with open('config.txt') as config:
            try:
                data = json.loads(config.read())
                self.creditials['username'] = data['username']
                self.creditials['password'] = data['password']
            except:
                print('Masz źle skonfigurowany plik config.txt (prawidłowy format: JSON)')

    def run(self):
        self.app.Dialog['Użytkownik:Edit'].set_text(self.creditials['username'])
        self.app.Dialog['Hasło:Edit'].set_text(self.creditials['password'])
        time.sleep(5)
        self.app.Dialog.Zaloguj.click()

def run_app():
    program = Program('uia', 'C:\\Program Files (x86)\\Sage\\Symfonia ERP\\21.0\\AMHMSQL.exe')
    program.load_creditials()
    program.wait_for_run()
    program.run()

if __name__ == '__main__':
    schedule.every().day.at('12:03').do(run_app)
    while True:
        schedule.run_pending()
        time.sleep(1)
