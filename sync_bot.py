#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/25 20:35
# @File    : sync_bot.py
# @Software: PyCharm
import itchat
from itchat.content import *

# 配置
# 这里填写两个群的关键字，比如两个群的名称都是 "Web Security&Pentesting"，就填下面的名称
group_name = "Web Security"


# 自动回复文本等类别消息
# isGroupChat=False表示非群聊消息
@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING], isGroupChat=False)
def text_reply(msg):
    itchat.send('wxsync - 群消息同步功能，代码：https://github.com/Lyttoni/wxsync.git', msg['FromUserName'])


# 自动处理添加好友申请
@itchat.msg_register(FRIENDS)
def add_friend(msg):
    itchat.add_friend(**msg['Text'])  # 该操作会自动将新好友的消息录入，不需要重载通讯录
    itchat.send_msg(u'Hello World.', msg['RecommendInfo']['UserName'])


# 自动回复文本等类别的群聊消息
# isGroupChat=True表示为群聊消息
@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING], isGroupChat=True)
def group_reply_text(msg):
    # 消息来自于哪个群聊
    chatroom_id = msg['FromUserName']
    # 发送者的昵称
    username = msg['ActualNickName']

    # 消息并不是来自于需要同步的群
    if not chatroom_id in chatroom_ids:
        return

    if msg['Type'] == TEXT:
        content = msg['Content']
    elif msg['Type'] == SHARING:
        content = msg['Text']

    # 根据消息类型转发至其他需要同步消息的群聊
    if msg['Type'] == TEXT:
        for item in chatrooms:
            if not item['UserName'] == chatroom_id:
                itchat.send('%s\n%s' % (username, msg['Content']), item['UserName'])
    elif msg['Type'] == SHARING:
        for item in chatrooms:
            if not item['UserName'] == chatroom_id:
                itchat.send('%s:\n%s\n%s' % (username, msg['Text'], msg['Url']), item['UserName'])


# 自动回复图片等类别的群聊消息
# isGroupChat=True表示为群聊消息
@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO], isGroupChat=True)
def group_reply_media(msg):
    # 消息来自于哪个群聊
    chatroom_id = msg['FromUserName']
    # 发送者的昵称
    username = msg['ActualNickName']

    # 消息并不是来自于需要同步的群
    if not chatroom_id in chatroom_ids:
        return

    # 下载图片等文件
    msg['Text'](msg['FileName'])
    # 转发至其他需要同步消息的群聊
    for item in chatrooms:
        if not item['UserName'] == chatroom_id:
            itchat.send("{} 发送:".format(username), item['UserName'])
            itchat.send('@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName']), item['UserName'])


if __name__ == "__main__":
    # enableCmdQR=True时命令行输出二维码
    itchat.auto_login(enableCmdQR=True, hotReload=True)
    # 搜索群
    chatrooms = itchat.search_chatrooms(name=group_name)
    chatroom_ids = [c['UserName'] for c in chatrooms]

    print('正在同步{}个群聊'.format(len(chatrooms)))
    print(' | '.join([item['NickName'] for item in chatrooms]))

    # 开始同步
    itchat.run()
