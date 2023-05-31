

from Sign import Sign

if __name__ == "__main__":
    bot = Sign("", "", "")  # Sign(账号，密码，老师名称)
    bot.set_location(114.35283115090016, 30.610761641896637)  # 打卡所需经纬度，在地图上获取
    bot.run()
