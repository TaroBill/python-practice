import requests https://github.com/TaroBill/python-practice/blob/master/zuvio_request.py
import json

#from bs4 import BeautifulSoup 
#from time import localtime, strftime 
#r = requests.get('https://irs.zuvio.com.tw/irs/login', auth=('@gmail.com', 'password'))
r = requests.get("https://irs.zuvio.com.tw/course/listStudentCurrentCourses?user_id=id&accessToken=token")
print(r.status_code)
#print(r.text)
output = json.loads(r.text)
for i in output["courses"]:
    print(i["course_name"],i["course_id"])
