from urllib.parse import quote
from urllib.request import urlopen, Request
from user_agent import generate_navigator_js
from bs4 import BeautifulSoup

from .Result import Result


def make_soup(data):
    return BeautifulSoup(data, features="lxml", parser="lxml")


class DuckDuckGo(object):
    @staticmethod
    def query(q, debug=False):
        req = Request(quote("https://duckduckgo.com/lite/?q={0}".format(q), ':/?='))
        req.add_header("User-Agent", generate_navigator_js()["userAgent"])
        try:
            return Result.get_all(make_soup(urlopen(req).read()))
        except Exception as e:
            if debug:
                print(e)
        return None
