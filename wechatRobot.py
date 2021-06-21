import itchat
import requests
#上传获得消息内容到图灵机器人

#api_key里面填你在图灵机器人里面获得的机器人的apiKey
api_key = []
flag = 0
def getMessage(msg,flag):
  apiURL='http://www.tuling123.com/openapi/api'
  data={'key':api_key[flag],
     'info':msg,
     'userID':'yancy'
     }
  r=requests.post(apiURL, data=data).json()
  if r.get('code') != '100000':
    flag += 1
  if r.get('code') != '100000' and flag == len(api_key):
    return "yancy是个猛1"
  print('答text：'+r.get('text'))
  print('答all：'+str(r))
  return r.get('text')

#监听个人微信聊天
@itchat.msg_register(itchat.content.TEXT)
def return_message(msg):
  try:
    print('问：'+msg['Text'])
  except Exception as e:
    print(e)
  return getMessage(msg['Text'],flag)

#监听微信群聊天
@itchat.msg_register([itchat.content.TEXT],isGroupChat=True)
def return_message(msg):
  print('问：'+msg['Text'])
  return getMessage(msg['Text'],flag)

if __name__=='__main__':
  itchat.auto_login(hotReload=True)
  itchat.run()