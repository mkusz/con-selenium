from playwright.sync_api import expect

from src.pom.base_pom import PageObjectModelBase


class DashboardPage(PageObjectModelBase):
    @property
    def default_url(self):
        return "https://tree.taiga.io/"

    @property
    def is_opened(self) -> bool:
        try:
            expect(self._page.get_by_role("navigation")).to_contain_text("Projects2")
            return True
        except AssertionError:
            return False
