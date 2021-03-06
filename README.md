# wxsync

Wechat message synchronized - 微信多群消息同步

原作者是[张宏伦 - 基于itchat实现微信群消息同步机器人](https://zhuanlan.zhihu.com/p/25445025)


## 安装

```
git clone git@github.com:nightrice/wxsync.git
cd wxsync
python -m pip install itchat
```

## 使用

1. 添加作为机器人的小号到两个需要同步消息的群。
2. 修改sync_bot.py中的group_name为群名关键字。
3. python sync_bot.py 运行并扫码登录微信。


# 更简洁的实现方式 - wxpy

原作者：[牛小强 - 10行代码实现微信群消息同步（wxpy）](https://zhuanlan.zhihu.com/p/33604536)

## 使用方法
```
pythom -m pip install wxpy
python sync.py
```

如果你用的非桌面版服务器运行该脚本，请修改sync.py中的console_qr为True。


提示：最后... 希望你能看到这里的提示，我用了一天以后被禁止登录Web微信了。
