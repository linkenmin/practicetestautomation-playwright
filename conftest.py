import pytest
from utils.browser_utils import init_playwright, launch_browser

def pytest_addoption(parser):
    parser.addoption(
        "--browsers",
        action="store",
        default="chromium,firefox,webkit",
        help="Comma-separated list of browsers to test, e.g. chromium,firefox,webkit"
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run browsers in headless mode"
    )

@pytest.fixture(scope="session")
def playwright():
    pw = init_playwright()
    yield pw
    pw.stop()

@pytest.fixture(scope="session")
def browser_instances(playwright, request):
    raw = request.config.getoption("--browsers")
    names = [b.strip() for b in raw.split(",") if b.strip()]
    instances = {}
    for name in names:
        instances[name] = launch_browser(
            playwright,
            name,
            headless=request.config.getoption("--headless")
        )
    yield instances

    for br in instances.values():
        br.close()

def pytest_generate_tests(metafunc):
    if "browser_context" in metafunc.fixturenames:
        raw = metafunc.config.getoption("--browsers")
        names = [b.strip() for b in raw.split(",") if b.strip()]
        metafunc.parametrize(
            "browser_context",
            names,
            indirect=True,
            ids=names
        )

@pytest.fixture(scope="function")
def browser_context(browser_instances, request):
    browser_name = request.param
    browser = browser_instances[browser_name]
    context = browser.new_context(viewport={"width": 1920, "height": 1080})
    page = context.new_page()
    yield page
    context.close()
