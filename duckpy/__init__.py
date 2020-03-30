from .DuckDuckGo import DuckDuckGo


def query(q):
    return DuckDuckGo.query(q)


__all__ = ["DuckDuckGo", "query"]
