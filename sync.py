#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/26 0:18
# @File    : sync.py
# @Software: PyCharm
from wxpy import *

# 配置
# 这里填写两个群的关键字，比如两个群的名称都是 "Web Security&Pentesting"，就填下面的名称
group_name = "Security&Pentesting"

# console_qr=True 命令行输入二维码
bot = Bot(console_qr=False)
bot.groups(update=True, contact_only=False)
my_groups = bot.groups().search(group_name)
my_groups[0].update_group(members_details=True)
my_groups[1].update_group(members_details=True)


@bot.register(my_groups, except_self=False)
def sync_my_groups(msg):
    sync_message_in_groups(msg, my_groups, prefix="Sync-{}:".format(msg.member.name))


bot.join()
