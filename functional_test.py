from selenium import webdriver

driver_dir = r'D:\安装包\chromedriver_win32\chromedriver.exe'
browser = webdriver.Chrome(executable_path=driver_dir)
browser.get('http://localhost:8000')
assert 'Django' in browser.title