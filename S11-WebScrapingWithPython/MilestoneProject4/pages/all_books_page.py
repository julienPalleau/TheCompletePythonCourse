from bs4 import BeautifulSoup

from MilestoneProject4.locators.all_books_page import AllBooksPageLocators
from MilestoneProject4.parsers.book_parser import BookParser


class AllBooksPage:
    def __init__(self, page_content):
        self.soup = BeautifulSoup(page_content, 'html.parser')

    @property
    def books(self):
        return [BookParser(e) for e in self.soup.select(AllBooksPageLocators.BOOKS)]
