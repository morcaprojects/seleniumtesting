
import streamlit as st

with st.echo():
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from webdriver_manager.core.os_manager import ChromeType

    @st.cache_resource
    def get_driver():
        return webdriver.Chrome(
            service=Service(
                ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
            ),
            options=options,
        )

    options = Options()
    options.add_argument("--disable-gpu")
    options.add_argument("--headless")

    driver = get_driver()
    driver.get("https://edition.cnn.com")

    

    matches = driver.find_elements('xpath', '//div[@data-open-link]')
    links = []

    st.code(matches)

    for i in range(len(matches)):
       links.append(web + matches[i].get_attribute('data-open-link'))
       st.markdown(links[i])
    
