import pytest
from selenium import webdriver
from pytest_metadata.plugin import metadata_key


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
        driver.maximize_window()
        print("Launching Chrome browser")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        driver.maximize_window()
        print("Launching FireFox browser")
    elif browser == "edge":
        driver = webdriver.Edge()
        driver.maximize_window()
        print("Launching Edge browser")
    else:
        driver = webdriver.Chrome()
        driver.maximize_window()
        print("Launching Default Chrome browser")

    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

########### pytest HTML Report ################
def pytest_html_report_title(report):
    report.title = "nop Commercer Login DDT Test"

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config.stash[metadata_key]["Project Name"] = "nop Commerce"
    config.stash[metadata_key]["Module Name"] = "Customers"
    config.stash[metadata_key]["Tester"] = "Fawad Ali Khan"

# It is hook for delete/Modify Environment info to HTML Report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)