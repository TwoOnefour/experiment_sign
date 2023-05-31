#!/bin/bash
sed -i '5c\    bot = Sign("123456", "123456", "御坂美琴")  # Sign(账号，密码，老师名称)' main.py
# 修改上面的Sign()
nohup python main.py&
