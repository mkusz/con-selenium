import playwright.sync_api as playwright

from src.pom.taiga.dashboard_page import DashboardPage
from src.pom.taiga.home_page import HomePage


class Taiga:
    def __init__(self, page: playwright.Page):
        self.home_page: HomePage = HomePage(page=page)
        self.dashboard_page: DashboardPage = DashboardPage(page=page)
