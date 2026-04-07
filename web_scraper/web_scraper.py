from bs4 import BeautifulSoup
import requests
import random
import os

class WebScraper:

    def __init__(self):
        self.desktop_user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0',
        'Mozilla/5.0 (X11; CrOS x86_64 14541.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.3.1 Safari/605.1.15',
        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1'
        ]
        self.base_url = 'https://static.slov-lex.sk'
        self.overview_url = self.base_url + '/static/SK/ZZ/2011/404/'
        self.last_update = ''
        self.law_online_url = ''
        self.law_pdf_url = ''

    def get_law_online_url(self):
        overview_html = requests.get(self.overview_url, headers={'User-Agent': random.choice(self.desktop_user_agents)})
        laws = BeautifulSoup(overview_html.text, 'html.parser').find_all('tr')
        versions = []
        for law in laws:
            date = law.get("data-ucinnostod")
            if date is None or date == '':
                continue
            versions.append(date)
        self.last_update = max(versions)

        for law in laws:
            date = law.get("data-ucinnostod")
            if date == self.last_update:
                link_tag = law.find('a')
                if link_tag:
                    self.law_online_url = self.overview_url + link_tag.get("href")
                    print(self.law_online_url)

    def get_law_pdf_url(self):
        if self.law_online_url is None:
            print("Link with online law is not available")
            return
        html_online_law = requests.get(self.law_online_url, headers={'User-Agent': random.choice(self.desktop_user_agents)})
        short_url_pdf = BeautifulSoup(html_online_law.text, 'html.parser').find(id='sidebar-button-download').parent.get('href')
        self.law_pdf_url = self.base_url + short_url_pdf[7:]
        print(self.law_pdf_url)

    def save_pdf_locally(self):
        if self.law_pdf_url is None:
            print("Link for downloading PDF is not available")
            return
        response = requests.get(self.law_pdf_url, headers={'User-Agent': random.choice(self.desktop_user_agents)})
        base_dir = os.path.dirname(__file__)
        file_path = os.path.join(base_dir, 'law404.pdf')
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print("PDF saved")

    def get_date_last_version(self):
        base_dir = os.path.dirname(__file__)
        file_path = os.path.join(base_dir, 'last_date_version.txt')
        with open(file_path, 'r') as file:
            return file.read()

    def scrape(self):
        print("Check if there is a new version...")
        self.get_law_online_url()
        base_dir = os.path.dirname(__file__)
        file_path = os.path.join(base_dir, 'law404.pdf')
        if self.get_date_last_version() != self.last_update or self.is_valid_pdf(file_path) == False:
            print("Updating PDF")
            file_path = os.path.join(base_dir, 'last_date_version.txt')
            with open(file_path, 'w') as file:
                file.write(str(self.last_update))
            self.get_law_pdf_url()
            self.save_pdf_locally()
        else:
            print("No new version")

    def is_valid_pdf(self, file_path):
        with open(file_path, "rb") as f:
            if f.read(4) != b"%PDF":
                print("There isn't a PDF file")
                return False
        return True

