#!/bin/bash
sed -i '5c\    bot = Sign("123456", "123456", "御坂美琴")  # Sign(账号，密码，老师名称)' main.py
sed -i '6c\    bot.set_location(114.35283115090016, 30.610761641896637)  # 打卡所需经纬度，在地图上获取' main.py
# 修改上面的Sign()和经纬度
nohup python main.py&
