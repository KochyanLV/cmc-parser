from download import Downloader
from parse import Parser
from data import some_logic

def process(url, web_page_path = None, data_path = None):
    downloader = Downloader(url, {})
    web_page_file = downloader.get_html()
    downloader.save(web_page_path)

    parser = Parser(web_page_path)
    parser.parse()
    parser.save(data_path)
    data = parser.get_data()

    some_logic(data)
    print(some_logic(data))

URL = "https://coinmarketcap.com/view/collectibles-nfts/"
FILE_PATH = "crypto.html"
PARSED_FILE_PATH = "crypto.json"
process(URL, FILE_PATH, PARSED_FILE_PATH)
