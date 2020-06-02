from urllib.request import urlopen
from link_finder import LinkFinder
from skeleton import *
from domain import *


class Spider:
    # Shared data between spiders for efficiency
    project_name = ''
    base_URL = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()

    def __init__(self, project_name, base_URL, domain_name):
        Spider.project_name = project_name
        Spider.base_URL = base_URL
        Spider.domain_name = domain_name
        Spider.queue_file = project_name + '/queue.txt'
        Spider.crawled_file = project_name + '/crawled.txt'
        self.boot()
        self.crawl_page('First spider', Spider.base_URL)

    @staticmethod
    def boot():  # Creating the project
        create_project_dir(Spider.project_name)
        create_data_files(Spider.project_name, Spider.base_URL)
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)

    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Spider.crawled:  # New URL
            print(thread_name + ' ,Now crawling URL ' + page_url)
            print('Queue' + str(len(Spider.queue))) + ' | Crawled ' + str(len(Spider.crawled))
            Spider.add_links_to_queue(Spider.gather_links(page_url))
            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)
            Spider.update_files()

    @staticmethod
    def add_links_to_queue(links):
        for url in links:  # Making sure URL it isn't present in the queue/crawled and domain_name in domain_name
            if (url in Spider.queue) or (url in Spider.crawled):
                continue
            if Spider.domain_name != get_domain_name(url):
                continue
            Spider.queue.add(url)

    @staticmethod
    def gather_links(page_url):
        html_string = ''
        try:
            response = urlopen(page_url)
            if 'text/html' in response.getheader('Content-Type'):  # Making sure it read text and html only
                html_bytes = response.read()
                html_string = html_bytes.decode("utf-8")
            finder = LinkFinder(Spider.base_URL, page_url)
            finder.feed(html_string)
        except Exception as e:
            print(str(e))
            return set()
        return finder.page_links()

    @staticmethod
    def update_file():
        set_to_file(Spider.queue, Spider.queue_file)
        set_to_file(Spider.crawled, Spider.crawled_file)
