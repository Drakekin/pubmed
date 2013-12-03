from requests import get
from sys import argv
from lxml import html


def main(url):
    source = get(url).text.encode("utf8")
    page = html.document_fromstring(source)
    abstract = page.cssselect(".rprt.abstract")[0]
    title, authors = [tag.text_content() for tag in abstract.getchildren()[1:3]]
    print title
    print "Authors:", authors


if __name__ == "__main__":
    main(*argv[1:])
