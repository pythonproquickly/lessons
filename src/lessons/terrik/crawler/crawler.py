import logging
import re
from urllib.parse import urlparse
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests
import lxml

logger = logging.getLogger(__name__)

class Crawler:
    """
    This class is responsible for scraping urls from the next available link in frontier and adding the scraped links to
    the frontier
    """

    def __init__(self, frontier, corpus):
        self.frontier = frontier
        self.corpus = corpus

        # Analytics 1: keep track of subdomains and count how many different URLs
        self.subdomain = { } # key : sub domain; value = number of links in that sub-domain

        # Analytics 2: Find page with the most valid out links
        self.page_with_most_out_links = ""

        # Analytics 3: List of Downloaded URLs & Identified Traps
        self.downloaded_urls = []
        self.identified_traps = []

        # Analytic #3: What is the longest page in terms of number of words
        self.page_with_most_words = ""

        # Analytic 4: What is the 50 most common words
        self.top_50_words = []

        # Analytic 5: Longest page in terms of number of words (excludes HTML)
        self.longest_page= { "URL": None, "word_count": 0}
        self.stop_words = self.stop_words = ['a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and', 'any', 'are', "aren't", 'as', 'at', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', "can't", 'cannot', 'could', "couldn't", 'did', "didn't", 'do', 'does', "doesn't", 'doing', "don't", 'down', 'during', 'each', 'few', 'for', 'from', 'further', 'had', "hadn't", 'has', "hasn't", 'have', "haven't", 'having', 'he', "he'd", "he'll", "he's", 'her', 'here', "here's", 'hers', 'herself', 'him', 'himself', 'his', 'how', "how's", 'i', "i'd", "i'll", "i'm", "i've", 'if', 'in', 'into', 'is', "isn't", 'it', "it's", 'its', 'itself', "let's", 'me', 'more', 'most', "mustn't", 'my', 'myself', 'no', 'nor', 'not', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'ought', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 'same', "shan't", 'she', "she'd", "she'll", "she's", 'should', "shouldn't", 'so', 'some', 'such', 'than', 'that', "that's", 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', "there's", 'these', 'they', "they'd", "they'll", "they're", "they've", 'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up', 'very', 'was', "wasn't", 'we', "we'd", "we'll", "we're", "we've", 'were', "weren't", 'what', "what's", 'when', "when's", 'where', "where's", 'which', 'while', 'who', "who's", 'whom', 'why', "why's", 'with', "won't", 'would', "wouldn't", 'you', "you'd", "you'll", "you're", "you've", 'your', 'yours', 'yourself', 'yourselves']

    def start_crawling(self):
        """
        This method starts the crawling process which is scraping urls from the next available link in frontier and adding
        the scraped links to the frontier
        """
        print("Does it go in?")
        while self.frontier.has_next_url():
            print("went in")
            url = self.frontier.get_next_url()
            print("url is : " , url)
            logger.info("Fetching URL %s ... Fetched: %s, Queue size: %s", url, self.frontier.fetched, len(self.frontier))
            url_data = self.corpus.fetch_url(url)

            for next_link in self.extract_next_links(url_data):
                if self.is_valid(next_link):
                    if self.corpus.get_file_name(next_link) is not None:
                        self.frontier.add_url(next_link)

    # convert relative URLs to absolute
    def relative_to_absolute(self, source_url, relative_url):
        return urljoin(source_url, relative_url)

    def uri_validator(self,url):
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except:
            return False

    def extract_next_links(self, url_data):
        """
        The url_data coming from the fetch_url method will be given as a parameter to this method. url_data contains the
        fetched url, the url content in binary format, and the size of the content in bytes. This method should return a
        list of urls in their absolute form (some links in the content are relative and needs to be converted to the
        absolute form). Validation of links is done later via is_valid method. It is not required to remove duplicates
        that have already been fetched. The frontier takes care of that.

        Suggested library: lxml
        """
        outputLinks = []
        if url_data["size"] > 0 and url_data['http_code'] < 400:
            if url_data["content"] is not None:
                content = url_data["content"]
                soup = BeautifulSoup(content.decode("utf-8"), 'lxml')
                try:
                    for link in soup.find_all('a'):
                        if 'href' in link.attrs:
                            href_url = link.attrs['href']
                            if url_data['is_redirected']:
                                outputLinks.append(self.relative_to_absolute(url_data['final_url'],(href_url)))
                            else:
                                outputLinks.append(self.relative_to_absolute(url_data['url'],(href_url)))
                        else:
                            outputLinks.append(href_url)
                except KeyError:
                    pass
        # print("url_data dictionary", url_data)

        print("number of links: ", len(outputLinks))
        print("number of link: ", outputLinks)
        return outputLinks


    def is_valid(self, url):
        """
        Function returns True or False based on whether the url has to be fetched or not. This is a great place to
        filter out crawler traps. Duplicated urls will be taken care of by frontier. You don't need to check for duplication
        in this method
        """
        # check 1. default start of http and https
        parsed = urlparse(url)
        if parsed.scheme not in set(["http", "https"]):
            return False

        # check 2: check for length of the URL
        if len(url) > 150:
            return False
        # check 3: check for all the extensions which are not HTML (exclude binary data)
        try:
            return ".ics.uci.edu" in parsed.hostname \
                   and not re.match(".*\.(css|js|bmp|gif|jpe?g|ico" + "|png|tiff?|mid|mp2|mp3|mp4" \
                                    + "|wav|avi|mov|mpeg|ram|m4v|mkv|ogg|ogv|pdf" \
                                    + "|ps|eps|tex|ppt|pptx|doc|docx|xls|xlsx|names|data|dat|exe|bz2|tar|msi|bin|7z|psd|dmg|iso|epub|dll|cnf|tgz|sha1" \
                                    + "|thmx|mso|arff|rtf|jar|csv" \
                                    + "|rm|smil|wmv|swf|wma|zip|rar|gz|pdf)$", parsed.path.lower())

        except TypeError:
            print("TypeError for ", parsed)
            return False
        # check 4: calendar

        # check 5: check the arguments

        # check 6: dynamic URL

        # check 7: repeating directory (pictures)

        # final check: rely on urlparse function
        is_it_a_valid_url = self.uri_validator(url)
        return is_it_a_valid_url



