import itchat
import requests


# 上传获得消息内容到图灵机器人

# api_key里面填你在图灵机器人里面获得的机器人的apiKey

class wechatRobot:
    api_key = ['51a1337c2b9d4031b89460045ddec3b7', 'c6118b8873b34a4c86f437dff774dd80',
               '0326ee3b436540ceabd1884207700eb5',
               '6d95987adc144da0a19883d15afe905c', '00535128abb0472ca48ca7e801cf7b0b']
    flag = 0

    success_code = [100000, 200000]
    error_code = [40001]

    def setApikey(self, api_key):
        wechatRobot.api_key = api_key
        return wechatRobot

    @staticmethod
    def getMessage(msg):
        apiURL = 'https://www.tuling123.com/openapi/api'
        data = {'key': wechatRobot.api_key[wechatRobot.flag],
                'info': msg,
                'userid': 'yancy'
                }
        r = requests.post(apiURL, data=data).json()
        print(str(r))
        # 重试
        if r.get('code') not in wechatRobot.success_code:
            wechatRobot.flag += 1  # api标志位+1
            if wechatRobot.flag == len(wechatRobot.api_key) - 1:
                wechatRobot.flag = 0
                return 0
            data = {'key': wechatRobot.api_key[wechatRobot.flag],
                    'info': msg,
                    'userid': 'yancy'
                    }
            r = requests.post(apiURL, data=data).json()
        rst = r.get('text')
        print('答text：' + str(r))
        if r.get('url'):
            rst = r.get('text') + "\n" + r.get('url')
        print('rst====：' + rst)
        print('flag：' + str(wechatRobot.flag))
        return {'code': r.get('code'), 'data': rst}

    # 监听个人微信聊天
    @staticmethod
    @itchat.msg_register(itchat.content.TEXT)
    def return_message(msg):
        try:
            print('问：' + msg['Text'])
        except Exception as e:
            print(e)
        return wechatRobot.getMessage(msg['Text'])


# 监听微信群聊天
# @itchat.msg_register([itchat.content.TEXT],isGroupChat=True)
# def return_message(msg):
#   print('问：'+msg['Text'])
#   return getMessage(msg['Text'])

if __name__ == '__main__':
    wechatRobot()
    itchat.auto_login(hotReload=True)
    itchat.run()
