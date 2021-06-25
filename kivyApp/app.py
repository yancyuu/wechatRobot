import os

import itchat
import kivy

kivy.require('1.8.0')
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import RiseInTransition
from kivy.uix.popup import Popup
from kivy.logger import Logger
from kivy.core.audio import SoundLoader
from wechatRobot.wechatRobot import wechatRobot


class LoginScreen(Screen):
    def login(self, instance):
        self.apikey = self.ids.apikey.text
        if not self.apikey:
            Logger.info('LoginScreen: apikey wrong')
        else:
            # 检查apikey
            api_ret = self.test_api(self.apikey)
            if api_ret < 0:
                Logger.info('LoginScreen: apikey wrong')
                exit()
            self.wechat_robot()
            SoundLoader.load('QR.png').play()
            self.manager.current = 'circle'

    def wechat_robot(self):
        ret = self.test_api(self.apikey)
        if not ret:
            return "api error"
        wechatRobot().setApikey(self.api_list)
        itchat.auto_login(hotReload=True,picDir=os.getcwd())
        itchat.run()

    def test_api(self, api):  # 检查api的合法性
        try:
            self.api_list = api.split(',')
            Logger.info('api_list'+str(self.api_list))

            handler = wechatRobot().setApikey(self.api_list)
            ret = handler.getMessage("test")  # 测试所有的api是否正常
            if ret['code'] in wechatRobot.error_code:
                return -1
        except Exception as e:
            print(e)
            return -1
        return 1

    def get_instance(self):
        return self.sm


class MyPopup(Popup):
    pass


class CircleScreen(Screen):
    pass


class MyApp(App):
    def build(self):
        self.icon = 'my.png'
        root = ScreenManager(transition=RiseInTransition())
        root.add_widget(LoginScreen())
        root.add_widget(CircleScreen())
        return root

    def build_config(self, config):
        config.setdefaults('myconfig', {
            'key1': 'value1',
            'key2': '42'})

    def build_settings(self, settings):
        jsondata = '''
            [
                {"type": "options",
                "title": "My first key",
                "desc": "Description of my first key",
                "section": "myconfig",
                "key": "key1",
                "options": ["value1", "value2", "another value"] },
                {"type": "title",
                "title": "Numeric" },
                { "type": "numeric",
                "title": "My second key",
                "desc": "Description of my second key",
                "section": "myconfig",
                "key": "key2" }
            ]'''
        settings.add_json_panel('Settings', self.config, data=jsondata)


if __name__ == '__main__':
    MyApp().run()
