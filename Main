import threading
from queue import Queue
from spider import Spider
from domain import *
from skeleton import *

PROJECT_NAME = 'TheSite'
HOME_PAGE = ''  # What page we want to crawl
DOMAIN_NAME = get_domain_name(HOME_PAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8  # Numb of spiders
queue = Queue
Spider(PROJECT_NAME, HOME_PAGE, DOMAIN_NAME)


def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    # Checking if there are links in the file
    if len(queued_links) > 0:
        print(str(len(queued_links)) + 'Links in the queue')
        create_jobs()


def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
        queue.join()
        crawl()


def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()


create_workers()
crawl()
