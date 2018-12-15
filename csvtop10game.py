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
    for i in [li1, li2, li3, li4, li5, li6, li7]:
        dic = {}
        name, date = i.list_name()
        for i in name:
            data = pd.read_csv(i, sep="\t", header=None, quotechar=None, quoting=3)
            data.columns = ["s_id", "current_views", "created", "g_name", "b_id", "b_name", "delay", "follower",
                            "status", "b_language", "total_views", "language", "b_created", "playback", "resolution", "var"]
            dic = cal(data, dic)
        graph = chart(dic, date)
        data_filter = pd.DataFrame(
            {'game': pd.Categorical(dic), 'views': pd.Categorical(dic.values())})
        # print(data_filter)
        data_filter.to_csv(date+'.csv')
        graph.render_to_file(date+".svg")


def cal(data, dic):
    view = data["current_views"].tolist()
    game = data["g_name"].tolist()
    for i in range(len(game)):
        if game[i] not in dic:
            dic[game[i]] = view[i]
        else:
            dic[game[i]] += view[i]
    return dic


def chart(dic, date):
    dic2 = {}
    for i in dic:
        dic2[dic[i]] = i
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
