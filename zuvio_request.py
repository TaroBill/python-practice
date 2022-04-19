import requests 
import json

#from bs4 import BeautifulSoup 
#from time import localtime, strftime 
#r = requests.get('https://irs.zuvio.com.tw/irs/login', auth=('bill890914@gmail.com', 'TaroBill0914'))
r = requests.get("https://irs.zuvio.com.tw/course/listStudentCurrentCourses?user_id=1872576&accessToken=d446a9f72ce77c5f629afda24d809e30f82b39fb")
print(r.status_code)
#print(r.text)
output = json.loads(r.text)
for i in output["courses"]:
    print(i["course_name"],i["course_id"])
