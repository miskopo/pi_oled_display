class Paginator:
    __slots__ = '_number_of_pages', '_current_page'

    def __init__(self, number_of_pages: int):
        self._number_of_pages = number_of_pages
        self._current_page = 1

    @property
    def current_page(self) -> int:
        return self._current_page

    @current_page.setter
    def current_page(self, value: int):
        if value <= 0 or value > self._number_of_pages:
            raise AttributeError("Current page can't be less then 1 or greater than total number of pages")
        self._current_page = value

    @property
    def number_of_pages(self) -> int:
        return self._number_of_pages

    @number_of_pages.setter
    def number_of_pages(self, value: int):
        if value <= 0:
            raise AttributeError("Total number of pages can't be less then 1")

    def __str__(self):
        full_circle = u"\u25CF"  # ●
        empty_circle = u"\u25CB"  # ○
        return "{}{}{}".format(
            ( self.current_page - 1) * empty_circle,
            full_circle,
            (self.number_of_pages - self.current_page) * empty_circle)
