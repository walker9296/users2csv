# users2csv
discord的bot程序，以csv格式输出服务器/频道用户的一览表

# 前提条件
- python 3.6+
- 安装discord.py
```
pip install -U discord.py
```
- 在 [discord](https://discord.com/developers/applications/) 创建bot
- 选择discord服务器给bot授权

# 启动bot后台程序
```
#python userlistbot.py [bot's TOKEN]

python userlistbot.py XXXXXXXXODcwNzQ1Mjg4NzU2.X05mIA.6NzSx3ec6azsGAqogaLPiKpLbX8
```

# 在discord执行bot的命令

- help命令： <br>
![](https://github.com/walker9296/users2csv/blob/master/img/help.png?raw=true "help命令") <br>

- info命令： <br>
![](https://github.com/walker9296/users2csv/blob/master/img/info.png?raw=true "info命令") <br>

- lists命令输出当前discord服务器的用户一览(需要频道Admin权限)： <br>
![](https://github.com/walker9296/users2csv/blob/master/img/lists.png?raw=true "lists命令(需要频道Admin权限)") <br>

- listc命令输出当前discord频道的用户一览： <br>
![](https://github.com/walker9296/users2csv/blob/master/img/listc.png?raw=true "listc命令") <br>

- lists命令和listc命令的输出结果： <br>
![](https://github.com/walker9296/users2csv/blob/master/img/result.png?raw=true) <br>
