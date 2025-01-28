import csv
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.amazon.in/")
driver.maximize_window()

# Necessary data lists of laptops
laptop_data = {
    "brand_name": [],
    "model_name": [],
    "screen_size": [],
    "ram": [],
    "storage": [],
    "cpu": [],
    "operating_system": [],
    "price": [],
    "rating": [],
    "reviews": [],
    "graphics": [],
    "card_description": []
}

# Search for laptops
search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.clear()
search_box.send_keys("laptops")
driver.find_element(By.ID, "nav-search-submit-button").click()

# Filter by brands (Dell and HP)
# driver.find_element(By.XPATH, "//span[text()='Dell']").click()
# driver.find_element(By.XPATH, "//span[text()='HP']").click()

# Store the search results page URL
search_results_url = driver.current_url


def extract_text(xpath, default="Null"):
    try:
        return driver.find_element(By.XPATH, xpath).text
    except NoSuchElementException:
        return default


# Function to scrape data from a single page
def scrape_laptop_data():
    laptop_links = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//a[@class='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal']"))
    )
    laptop_urls = [link.get_attribute('href') for link in laptop_links]
    print(f"Total laptops on this page: {len(laptop_urls)}")

    for link in laptop_urls:
        driver.get(link)

        try:
            # Scroll to the table section to ensure visibility
            try:
                # Wait for the table element to be present and scroll to it
                element_to_scroll = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//table[@class='a-normal a-spacing-micro']"))
                )
                driver.execute_script("arguments[0].scrollIntoView(true);", element_to_scroll)
            except TimeoutException:
                print(f"Table element not found on page: {link}")
            except NoSuchElementException:
                print(f"No table element found on page: {link}")

            # Expand sections if necessary
            try:
                # Wait for the expand button to be visible and clickable
                expand_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//a[@class='a-declarative']//i[@class='a-icon a-icon-extender-expand']"))
                )
                driver.execute_script("arguments[0].scrollIntoView(true);", expand_button)  # Scroll into view if necessary
                expand_button.click()
            except TimeoutException:
                print(f"No expandable section found or not clickable on page: {link}")
            except NoSuchElementException:
                print(f"Expand button not found on page: {link}")
            except ElementNotInteractableException:
                print(f"Expand button not interactable on page: {link}")


            laptop_data["brand_name"].append(extract_text("//tr[@class='a-spacing-small po-brand']//span[@class='a-size-base po-break-word']"))
            laptop_data["model_name"].append(extract_text("//tr[@class='a-spacing-small po-model_name']//span[@class='a-size-base po-break-word']"))
            laptop_data["screen_size"].append(extract_text("//tr[@class='a-spacing-small po-display.size']//span[@class='a-size-base po-break-word']"))
            laptop_data["ram"].append(extract_text("//tr[@class='a-spacing-small po-ram_memory.installed_size']//span[@class='a-size-base po-break-word']"))
            laptop_data["storage"].append(extract_text("//tr[@class='a-spacing-small po-hard_disk.size']//span[@class='a-size-base po-break-word']"))
            laptop_data["cpu"].append(extract_text("//tr[@class='a-spacing-small po-cpu_model.family']//span[@class='a-size-base po-break-word']"))
            laptop_data["operating_system"].append(extract_text("//tr[@class='a-spacing-small po-operating_system']//span[@class='a-size-base po-break-word']"))
            laptop_data["price"].append(extract_text("//div[@class='a-section a-spacing-none aok-align-center aok-relative']//span[@class='a-price-whole']"))
            laptop_data["rating"].append(extract_text("//span[@id='acrPopover']//span[@class='a-size-base a-color-base']"))
            laptop_data["reviews"].append(extract_text("//span[@id='acrCustomerReviewText']"))
            laptop_data["graphics"].append(extract_text("//tr[@class='a-spacing-small po-graphics_coprocessor']//span[@class='a-size-base po-break-word']","Not available"))
            laptop_data["card_description"].append(extract_text("//tr[@class='a-spacing-small po-graphics_description']//span[@class='a-size-base po-break-word']"))
        except TimeoutException:
            print(f"Specifications not found for laptop: {link}")
            continue

    # Navigate back to the search results page using the stored URL
    driver.get(search_results_url)


# Loop through pages and scrape data
for page in range(20):  # Adjusted to 20 pages, modify as per your need
    scrape_laptop_data()

    try:
        # Wait for the next button to be clickable
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//a[@class='s-pagination-item s-pagination-next s-pagination-button s-pagination-separator']"))
        )
        next_button.click()  # Click the button to go to the next page
        print(f"Clicked 'Next' button, page {page + 1}")

        # Wait for the page to load completely by checking the presence of laptop links
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH,
                 "//a[@class='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal']"))
        )
        time.sleep(3)  # Adding an extra sleep to ensure the page is fully loaded
        search_results_url = driver.current_url
        print(search_results_url)
    except (NoSuchElementException, TimeoutException):
        print("No more pages available or 'Next' button not found.")
        break

# Write the extracted data into a CSV file
with open('laptop_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(laptop_data.keys())
    writer.writerows(zip(*laptop_data.values()))

print("Data saved to laptop_data.csv")

input("Press Enter to close the browser...")
driver.quit()
