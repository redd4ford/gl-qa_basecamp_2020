from ui.config import Config
from ui.pages.google import GoogleSearchPage


def test_can_find_song():
    google_search_page = GoogleSearchPage(Config.DRIVER)
    google_results_page = google_search_page.search_by_phrase('степан гіга найкращі пісні')
    google_results_page.open_result_that_contains_in_link('www.youtube.com')
    assert Config.DRIVER.current_url == 'https://www.youtube.com/watch?v=UxCSDQTRcIg'
