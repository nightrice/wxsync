# wxsync

[py35]: https://img.shields.io/badge/python-3.5-red.svg

![py35][py35]

Wechat message synchronized - 微信多群消息同步

原作者忘记时谁了,在网上搜了下发现了这些现成的代码,自己小改了一下.

## 安装

```
git clone https://github.com/Lyttoni/wxsync.git
cd wxsync
python -m pip install itchat
```

## 使用

1. 添加作为机器人的小号到两个需要同步消息的群。
2. 修改sync_bot.py中的group_name为群名关键字。
3. python sync_bot.py 运行并扫码登录微信。