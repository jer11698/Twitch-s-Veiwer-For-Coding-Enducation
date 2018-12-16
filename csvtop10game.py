import pandas as pd
import numpy as np
import list_2015_02_01 as li1
import list_2015_02_02 as li2
import list_2015_02_03 as li3
import list_2015_02_04 as li4
import list_2015_02_05 as li5
import list_2015_02_06 as li6
import list_2015_02_07 as li7
import pygal


def main():
    """ เริ่มจากตรงนี้ """
    for i in [li1, li2, li3, li4, li5, li6, li7]:  # รายชื่อข้อมูลแต่ละวันมาทำที่ละไฟล์
        dic = {}  # ไว้เก็บข้อมูลที่รวมไว้แล้ว
        name, date = i.list_name()  # รายชื่อข้อมูลแต่ละเวลาของ li1-7
        for i in name:  # ไฟลข้อมูลรายชื่อของแต่ละเวลาของ li1-7 ทำทีละไฟล์
            data = pd.read_csv(i, sep="\t", header=None,
                               quotechar=None, quoting=3)
            data.columns = ["s_id", "current_views", "created", "g_name", "b_id", "b_name", "delay", "follower",
                            "status", "b_language", "total_views", "language", "b_created", "playback", "resolution", "var"]
            dic = cal(data, dic)  # เรียกใช้ฟังก์ชัน
        graph = chart(dic, date)
        # ทำเป็นตารางแล้วเรนเดอร์เป็นไฟล์ csv
        data_filter = pd.DataFrame(
            {'game': pd.Categorical(dic), 'views': pd.Categorical(dic.values())})
        data_filter.to_csv(date+'.csv')
        # เรนเดอร์เป็นกราฟ
        graph.render_to_file(date+".svg")


def cal(data, dic):
    """ ส่วนรวมข้อมูล """
    # เลือกดึงตารางข้อมูลออกมา
    view = data["current_views"].tolist()
    game = data["g_name"].tolist()
    # ส่วนของการรวมยอดวิวแต่ละเกม
    for i in range(len(game)):
        if game[i] not in dic:
            dic[game[i]] = view[i]
        else:
            dic[game[i]] += view[i]
    return dic


def chart(dic, date):
    """ ส่วนทำกราฟ """
    # สลับข้อมูลและคีย์
    dic2 = {}
    for i in dic:
        dic2[dic[i]] = i
    # ได้เวลาทำกราฟ
    graph = pygal.Pie()
    graph.title = "Top 10 GAME view "+date
    count = 0
    for i in sorted(dic.values())[::-1]:
        graph.add(dic2[i], i)
        count += 1
        if count == 10:
            break
    return graph


main()
