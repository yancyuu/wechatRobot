import itchat
import requests

# 上传获得消息内容到图灵机器人

# api_key里面填你在图灵机器人里面获得的机器人的apiKey
api_key = ['51a1337c2b9d4031b89460045ddec3b7', 'c6118b8873b34a4c86f437dff774dd80', '0326ee3b436540ceabd1884207700eb5',
           '6d95987adc144da0a19883d15afe905c', '00535128abb0472ca48ca7e801cf7b0b']
flag = 0


def getMessage(msg):
    global flag
    apiURL = 'https://www.tuling123.com/openapi/api'
    data = {'key': api_key[flag],
            'info': msg,
            'userid': 'yancy'
            }
    r = requests.post(apiURL, data=data).json()
    print(str(r))
    # 重试
    if r.get('code') != 100000:
        flag += 1
        if flag == len(api_key) - 1:
            return "yancy是个猛1"
        data = {'key': api_key[flag],
                'info': msg,
                'userid': 'yancy'
                }
        r = requests.post(apiURL, data=data).json()
    print('flag：' + str(flag))
    print('答text：' + r.get('text'))
    print('答all：' + str(r))
    return r.get('text')


# 监听个人微信聊天
@itchat.msg_register(itchat.content.TEXT)
def return_message(msg):
    try:
        print('问：' + msg['Text'])
    except Exception as e:
        print(e)
    return getMessage(msg['Text'])


# #监听微信群聊天
# @itchat.msg_register([itchat.content.TEXT],isGroupChat=True)
# def return_message(msg):
#   print('问：'+msg['Text'])
#   return getMessage(msg['Text'],flag)

if __name__ == '__main__':
    itchat.auto_login(hotReload=True)
    itchat.run()
