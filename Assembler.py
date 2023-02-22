### pip install selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from riscv_assembler.utils import * # for bltu
tk = Toolkit()

filename = "Game" ### change filename here without file extension

with open(filename+'.s') as file:
    program = file.read().split('\n')

fullcode = []

PATH = "C:\Program Files (x86)\chromedriver.exe" ### path to your chromedriver
driver = webdriver.Chrome(PATH)

for instr in program:

    if instr[0:4]=='bltu': # 'bltu' is unavailable in website
        bltu = instr.replace(',','').split()
        machine_code  = tk.SB_type(bltu[0], bltu[1], bltu[2], bltu[3])

    else:
        driver.get("https://luplab.gitlab.io/rvcodecjs/")
        search = driver.find_element("id","search-input")
        search.send_keys(instr)
        search.send_keys(Keys.RETURN)

        machine_code = ''

        try:
            code = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "binary-data")))
            machine_code = code.text.replace('\n','')
        except:
            driver.quit()

    print(machine_code)  # prints the machine code in the Python Shell
    fullcode.append(machine_code)

length = len(fullcode)
for i in range(256-length):
    fullcode.append("0"*32)
    
driver.quit()

content = '\n'.join(fullcode)
with open('IM_image.mem', 'w') as file:
    file.write(content) # saves the machine code as a txt file
