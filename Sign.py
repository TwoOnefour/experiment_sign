import requests
import time

import urllib3

urllib3.disable_warnings()


class Sign:
    def __init__(self, username, password, teacher):
        self.latitude = None
        self.longitude = None
        self.username = username
        self.password = password
        self.teacher = teacher
        self.session = requests.session()
        self.baseurl = "https://whut-experiment.hooook.com"
        self.course_dict = {}
        self.api = {
            "login": "/api/minipro/login",  # 请求方法POST, 需要数据 json = {"type": "student","student_number": self.username,"password": self.password}
            "logout": "/api/minipro/student/logout",  # 需要数据 Authorization , 返回 json={"status": "success", "code": 200, "data": "已退出登录"}
            "list_index": "/api/minipro/student/index",  # 需要数据 json={"longitude": 114, "latitude": 30}
            "check_in": "/api/minipro/student/cherk_in"
        }

    def set_location(self, longitude, latitude):
        self.latitude = latitude
        self.longitude = longitude

    def list_course(self):
        try:
            res = self.session.post(f"{self.baseurl}{self.api['list_index']}", json={
                "latitude": self.latitude,
                "longitude": self.longitude
            }, verify=False)
            res_json = res.json()
            # print(res)
            for i in res_json["data"]["list"]:
                # self.course_dict[i["id"]] = i["project_name"]
                for j in i["teacher_name"]:
                    if j == self.teacher:
                        self.check_in(i["id"])
            return True
        except Exception as e:
            return False

    def check_in(self, patch_id):
        res = self.session.post(f"{self.baseurl + self.api['check_in']}", json={
            "patch_id": patch_id,
            "created_at": ""
        }, verify=False)

    def login(self):
        res = self.session.post(f"{self.baseurl}{self.api['login']}", json={
            "type": "student",
            "student_number": self.username,
            "password": self.password
        }, verify=False)
        result_json = res.json()
        if result_json["code"] == 200:
            self.session.headers["Authorization"] = result_json["data"]["access_token"]
            print(self.session.headers["Authorization"])
            return True
        else:
            return False

    def logout(self):
        res = self.session.post(f"{self.baseurl}{self.api['logout']}", verify=False)
        print(res.json()["data"])

    def run(self):
        if self.login():
            while True:
                if not self.list_course():
                    self.logout()
                    break
                time.sleep(30)
