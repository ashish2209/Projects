from selenium import webdriver
class song():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='C:\Program Files\Google\Chrome\Application\chrome.exe')
        
    def plays(self,query):
        self.query = query
        self.driver.get(url='https://wynk.in/music/detailsearch?q=' + query)
        song = self.driver.find_element_by_xpath('//*[@id="navbar"]/div/div[2]/div[1]/div')
        song.click()

