from src.pom.taiga_pom import Taiga


def test_login(taiga: Taiga) -> None:
    taiga.home_page.goto()
    taiga.home_page.login()
    assert taiga.dashboard_page.is_opened
