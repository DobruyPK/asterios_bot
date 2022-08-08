import requests
from html.parser import HTMLParser
from data_store import dataSaver

data_l = dataSaver()


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        dataSaver.update_tag(data_l, tag)

    def handle_data(self, data):
        if dataSaver.get_target_tag(data_l) == 'a':
            dataSaver.update_data(data_l, data)


def start_parse():
    url = 'https://asterios.tm/index.php?cmd=rss&serv=3&filter=all'
    saite_request = requests.get(url)
    parser = MyHTMLParser()
    parser.feed(saite_request.text)


# while True:
#     x = input()
#     if x == 'q':
#         url = 'https://asterios.tm/index.php?cmd=rss&serv=3&filter=all'
#         saite_request = requests.get(url)
#         parser = MyHTMLParser()
#         parser.feed(saite_request.text)
#         print(dataSaver.get_data(data_l))
#     if x == "Orfen":
#         print(dataSaver.get_data(data_l)[x])

# тесты
# parser.feed(saite_request.text)
# print(dataSaver.get_data(data_l))
# print(dataSaver.get_unic_bos(data_l))

# for boss_name, time in data_l._data.items():
#     datetime.datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
