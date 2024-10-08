from src.pom.base_pom import PageObjectModelBase


class HomePage(PageObjectModelBase):
    @property
    def default_url(self):
        return f"{self._env.taiga_ui_url}"

    def login(self):
        self._page.get_by_role("link", name="Log in").click()
        self._page.get_by_placeholder("Username or email (case").click()
        self._page.get_by_placeholder("Username or email (case").fill(self._env.taiga_user)
        self._page.get_by_placeholder("Username or email (case").press("Tab")
        self._page.get_by_placeholder("Password (case sensitive)").fill(self._env.taiga_pass)
        self._page.get_by_role("button", name="Login").click()
