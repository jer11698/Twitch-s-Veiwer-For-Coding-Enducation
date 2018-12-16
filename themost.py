import pandas as pd
import numpy as np
import pygal
import datetime as dt


def main():
    name = {}  # ไว้เก็บข้อมูลที่แบ่งเป็นหมวดไว้แล้ว
    for i in ("2015-02-01.csv", "2015-02-02.csv", "2015-02-03.csv", "2015-02-04.csv", "2015-02-05.csv", "2015-02-06.csv", "2015-02-07.csv"):
        data = pd.read_csv("nope/"+i, sep=",")
        data.drop(['Unnamed: 0'], axis=1, inplace=True)
        # เลือกดึงตารางข้อมูลออกมา
        game = data['game'].tolist()
        view = data['views'].tolist()
        # คัดยอดวิวเกมมาจัดเป็นหมวดเดียวกัน
        for i in range(len(game)):
            if game[i] not in name:
                name[game[i]] = [view[i]]
            else:
                name[game[i]].append(view[i])
    most(name)


def most(name):
    # เรียงข้อมูลจากมากไปน้อย
    sorted_game = {}
    count = 0
    for i in name:
        sorted_game[i] = sum(name[i])
    sorted_game = sorted(name.items(), key=lambda kv: kv[1], reverse=True)
    # ได้เวลาทำกราฟ
    line_chart = pygal.Line()
    line_chart.title = 'The Most Games\' view in Twitch 2015-02-01 to 2015-02-07'
    line_chart.x_labels = map(lambda d: d.strftime('%Y-%m-%d'), [
        dt.datetime(2015, 2, 1),
        dt.datetime(2015, 2, 2),
        dt.datetime(2015, 2, 3),
        dt.datetime(2015, 2, 4),
        dt.datetime(2015, 2, 5),
        dt.datetime(2015, 2, 6),
        dt.datetime(2015, 2, 7)])
    for i in sorted_game:
        line_chart.add(i[0], name[i[0]])
        print(name[i[0]])
        if count == 14:
            break
        count += 1
    # เรนเดอร์กราฟออกมา
    line_chart.render_to_file('chart.svg')


main()
