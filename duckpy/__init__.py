from bs4 import BeautifulSoup
from urllib.parse import quote
from urllib.request import urlopen, Request
from user_agent import generate_navigator_js


def make_soup(data):
    return BeautifulSoup(data, features="lxml", parser="lxml")


def query(q):
    return DuckDuckGo.query(q)


class Result(object):
    url = None
    title = None

    def __init__(self, url, title):
        self.url = url
        self.title = title

    @staticmethod
    def get_all(tr_list):
        r = []
        for a in tr_list.find_all("a", {"class": "result-link"}, href=True):
            r.append(Result(a["href"], a.get_text()))
        return r

    def print(self):
        print(self.__dict__)


class DuckDuckGo(object):
    @staticmethod
    def query(q):
        req = Request(quote("https://duckduckgo.com/lite/?q={0}".format(q), ':/?='))
        req.add_header("User-Agent", generate_navigator_js()["userAgent"])
        r = urlopen(req)
        return Result.get_all(make_soup(r.read()))


__all__ = ["DuckDuckGo", "query"]
