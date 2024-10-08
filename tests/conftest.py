import playwright.sync_api as playwright
import pytest

from src.configs import EnvConfig
from src.configs import PlaywrightConfig
from src.pom.taiga_pom import Taiga


@pytest.fixture
def playwright_config() -> PlaywrightConfig:
    """Playwright Config fixture"""
    return PlaywrightConfig()


@pytest.fixture
def env_config() -> EnvConfig:
    """Env Config fixture"""
    return EnvConfig()


@pytest.fixture
def taiga(page: playwright.Page) -> Taiga:
    return Taiga(page=page)
