import bs4
import json

class Parser:
    def __init__(self, source):
        self.list = []
        self.source = source
        self.dict = {}

    def parse(self):
        with open(self.source, encoding="utf-8", mode = "r") as f:
            soup = bs4.BeautifulSoup(f, 'html.parser')
            table = soup.find_all("table", attrs={"class": "sc-beb003d5-3 ieTeVa cmc-table"})[0]
            table = table.find_all("tr")

            i = 1
            for coin in table:
                curr = []
                curr_1 = []
                rank = coin.find(class_="sc-4984dd93-0 ihZPK")
                name = coin.find(class_="coin-item-symbol")
                price = coin.find(class_="sc-2bfe2fdb-0 HgnCe")
                market_cap = coin.find(class_="sc-edc9a476-1 gqomIJ")
                volume_24h = coin.find(class_="sc-4984dd93-0 jZrMxO")
                supply = coin.find(class_="sc-4984dd93-0 WfVLk")
                if name:
                    curr.append("NFT rank = " + rank.text)
                    curr.append("Name - " + name.text)
                    curr.append("Price = " + price.text)
                    curr.append("Market cap = " + market_cap.text)
                    curr.append("Volume(24h) = " + f"${volume_24h.text.split('$')[1]}")
                    curr.append("Supply = " + supply.text)
                    curr_1.append(rank.text)
                    curr_1.append(name.text)
                    curr_1.append(price.text)
                    curr_1.append(market_cap.text)
                    curr_1.append(f"${volume_24h.text.split('$')[1]}")
                    curr_1.append(supply.text)
                    self.list.append(curr_1)
                    self.dict[i] = curr
                    i+=1
            return self.dict

    def get_data(self):
        return self.list

    def save(self, path):
        with open(path, "w", encoding = "utf-8") as f:
            json.dump(self.dict, f, ensure_ascii=False, indent = 4)



'''FILE_PATH = "crypto.html"
PARSED_FILE_PATH = "crypto.json"

parser = Parser(source=FILE_PATH)

dict = parser.parse()           
parser.save(PARSED_FILE_PATH, dict)
data = parser.get_data()'''
