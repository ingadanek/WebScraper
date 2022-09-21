import click
import requests
from lxml.html import fromstring


def extract(page_content, xpath):
    """ Accepts page_content as a string and xpath as a string and returns matching elements as a list of strings """


    tree = fromstring(page_content)
    elements = tree.xpath(xpath)
    elements = [e.text_content() for e in elements]
    stripped = [e.strip().replace('\n', ' ') for e in elements]
    return stripped


@click.command()
@click.argument('url')
@click.argument('xpath')
def main(url, xpath):
    page = requests.get(url)
    content = page.text
    elements = extract(content, xpath)
    for element in elements:
        print(element)
    

if __name__ == '__main__':
    main()

# //*[@id="maincontent"]/div[4]/div[1]/div[9]/ol/li[1]/div[2]/strong/a
# //*[@id="maincontent"]/div[4]/div[1]/div[9]/ol/li[2]/div[2]/strong/a
# //*[@id="maincontent"]/div[4]/div[1]/div[9]/ol/li[3]/div[2]/strong/a
