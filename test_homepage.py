from selenium import webdriver
from selenium.common.exceptions import WebDriverException

def test_homepage():
    driver = None
    try:
        print("Starting WebDriver...")
        driver = webdriver.Firefox()
        print("WebDriver started successfully.")

        print("Navigating to http://localhost:5000...")
        driver.get("http://localhost:5000")
        print("Page loaded successfully.")

        print("Checking for 'Mean Value' in page source...")
        assert "Mean Value" in driver.page_source
        print("'Mean Value' found in page source!")

    except WebDriverException as e:
        print(f"Selenium WebDriverException: {e}")

    finally:
        if driver:
            driver.quit()
            print("WebDriver quit successfully.")

if __name__ == "__main__":
    test_homepage()
