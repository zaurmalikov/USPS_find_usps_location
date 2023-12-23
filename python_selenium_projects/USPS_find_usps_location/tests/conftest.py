import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome",
    )

    parser.addoption(
        "--url", action="store", default="https://www.usps.com/"
    )

@pytest.fixture(scope="class")
def browser_invocation(request):
    global driver

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")

    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument("--width=1520")
    firefox_options.add_argument("--height=880")

    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        chrome_driver_service = Service("C:/Program Files/Google/Chrome/Application/chromedriver.exe")
        driver = webdriver.Chrome(service=chrome_driver_service, options=chrome_options)
    elif browser_name == "firefox":
        firefox_driver_service = Service("C:/Users/Zaur Malikov/OneDrive/Desktop/Desktop 2023/ASO/automation, python, selenium/Rahul Shetty course notes/drivers/geckodriver.exe")
        driver = webdriver.Firefox(service=firefox_driver_service, options=firefox_options)

    request.cls.driver = driver

    driver.implicitly_wait(3)

    url = request.config.getoption("url")
    if url == "QA":
        driver.get("https://www.usps.com/")
    elif url == "Prod":
        driver.get("https://www.usps.com/")

    yield
    driver.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)   #it will capture screenshot only if there is an error