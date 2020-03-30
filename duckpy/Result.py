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
