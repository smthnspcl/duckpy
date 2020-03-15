from argparse import ArgumentParser
from duckpy import DuckDuckGo
from json import dump

if __name__ == '__main__':
    p = ArgumentParser()
    p.add_argument("-s", "--search", type=str, help="search query", required=True)
    p.add_argument("-o", "--output", type=str, help="save results as json file")
    a = p.parse_args()

    results = DuckDuckGo.query(a.search)
    if not a.output:
        for r in results:
            r.print()
    else:
        r = []
        for i in results:
            r.append(i.__dict__)
        dump(open(a.output, "wb"), r)
        print("wrote results to {0}".format(a.output))
