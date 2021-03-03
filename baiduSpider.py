import requests

from urllib import parse
from uuid import uuid4
import os
import time
s = input("请输入要爬取的图片：")
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'Cookie': 'uuid_tt_dd=10_19687710960-1595772699005-801112; UserName=m0_46697844; UserInfo=991e4e570ffa43dfac975d44182f7224; UserToken=991e4e570ffa43dfac975d44182f7224; UserNick=m0_46697844; AU=321; UN=m0_46697844; BT=1603771556805; p_uid=U010000; Hm_up_6bcd52f51e9b3dce32bec4a3997715ac=%7B%22islogin%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isonline%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isvip%22%3A%7B%22value%22%3A%220%22%2C%22scope%22%3A1%7D%2C%22uid_%22%3A%7B%22value%22%3A%22m0_46697844%22%2C%22scope%22%3A1%7D%7D; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=6525*1*10_19687710960-1595772699005-801112!5744*1*m0_46697844; UM_distinctid=175d98d376a3f7-075dfe99815695-3a65420e-151800-175d98d376b5a4; CNZZDATA1259587897=209855807-1605670023-https%253A%252F%252Fwww.baidu.com%252F%7C1605670023; Hm_lvt_e5ef47b9f471504959267fd614d579cd=1609669885; TY_SESSION_ID=abebe609-79f7-4880-ba6c-2f232700977e; c_first_ref=www.baidu.com; c_segment=8; dc_sid=0bce2731200ca6c24f53a46fb40b1133; c_pref=https%3A//www.baidu.com/link; announcement-new=%7B%22isLogin%22%3Atrue%2C%22announcementUrl%22%3A%22https%3A%2F%2Fblog.csdn.net%2Fblogdevteam%2Farticle%2Fdetails%2F112280974%3Futm_source%3Dgonggao_0107%22%2C%22announcementCount%22%3A0%2C%22announcementExpire%22%3A3600000%7D; dc_session_id=10_1614532119027.719948; c_first_page=https%3A//blog.csdn.net/qq_43361381/article/details/89677329; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1614519393,1614529512,1614532127,1614532175; log_Id_click=333; c_ref=https%3A//blog.csdn.net/qq_43361381/article/details/89677329; c_utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.control; c_page_id=default; dc_tos=qp910a; log_Id_pv=734; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1614532187; log_Id_view=1991; __gads=ID=1992f177261043e3-22c850ae32c60031:T=1614532189:RT=1614532189:S=ALNI_MaPRjemuvfzKDkKZ_SlYTkN-Lrh9Q',
    'Referer': 'http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=%E4%B8%89%E4%B8%8A%E6%82%A0%E4%BA%9A'
}
session = requests.session()
session.headers = headers


def getHTMLText(url):
    html = session.get(url)

    if html.status_code == 200:
        parse_html(html.json())
    else:
        print("访问网页错误")


def parse_html(html):
    data = html['data']
    for i in data:
        try:
            img = i['middleURL']
            print(img)
            download(img)
        except:
            pass


def download(img_url):
    time.sleep(3);
    html = session.get(img_url)
    filename = s
    if not os.path.exists(filename):
        os.makedirs(filename)
    with open('./{}/{}.jpg'.format(filename,uuid4()),'wb') as f:
        f.write(html.content)


if __name__ == "__main__":

    name = parse.quote(s)
    for i in range(1, 12, 1):
        url = 'http://image.baidu.com/search/acjson?tn=resultjson_com' \
              '&ipn=rj&ct=201326592&is=&fp=result&queryWord={}' \
              '&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=' \
              '&hd=&latest=&copyright=&word={}&s=&se=&tab=&width=' \
              '&height=&face=&istype=&qc=&nc=1&fr=&expermode=' \
              '&force=&pn={}&rn=30'.format(name, name, i)

        getHTMLText(url)
