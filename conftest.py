import pytest
from dotenv import load_dotenv
import os

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://www.saucedemo.com")
STANDARD_USER = os.getenv("STANDARD_USER", "standard_user")
LOCKED_USER = os.getenv("LOCKED_USER", "locked_out_user")
PROBLEM_USER = os.getenv("PROBLEM_USER", "problem_user")
PASSWORD = os.getenv("PASSWORD", "secret_sauce")


def pytest_addoption(parser):
    parser.addoption("--headless-mode", action="store", default="true",
                     help="Run in headless mode: true/false")


@pytest.fixture(scope="session")
def browser_type_launch_args(pytestconfig):
    headless = pytestconfig.getoption("--headless-mode").lower() == "true"
    return {"headless": headless, "slow_mo": 100}


@pytest.fixture(scope="session")
def browser_context_args():
    ctx = {"viewport": {"width": 1280, "height": 720}}
    if os.getenv("RECORD_VIDEO"):
        ctx["record_video_dir"] = "reports/videos/"
    return ctx


@pytest.fixture(scope="session")
def base_url():
    return BASE_URL


@pytest.fixture
def credentials():
    return {
        "standard": {"username": STANDARD_USER, "password": PASSWORD},
        "locked": {"username": LOCKED_USER, "password": PASSWORD},
        "problem": {"username": PROBLEM_USER, "password": PASSWORD},
    }
