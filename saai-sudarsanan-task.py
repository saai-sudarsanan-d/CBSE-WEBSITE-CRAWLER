# Importing required libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sqlite3 as sql
import time

# Create and Connect to database
conn = sql.connect('cbse.db')
conn.execute('''
CREATE TABLE SCHOOLS
(
SRL   INT NOT NULL,
AFFL    TEXT    PRIMARY KEY    NOT NULL,
NAME    TEXT    NOT NULL,
PRNAME  TEXT    NOT NULL,
STATUS  TEXT    NOT NULL,
ADDR    CHAR(200) NOT NULL,
PHNO    TEXT,
EMAIL   TEXT,
WEBSITE TEXT
);
''')
# Connect to URL
url = "http://cbseaff.nic.in/cbse_aff/schdir_Report/userview.aspx"

driver = webdriver.Chrome()
driver.get(url)

# Browse one by one in alphabetical Order
lex = "zy,zz" # "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z" -> Sample Input since, the process is large
lex = lex.split(",")
print(lex)
# Select Keywise in Radio Button Field 
radio1 = driver.find_element_by_id("optlist_0")
radio1.click()

# Function to extract the results from a page
def extract(page):
    i=0
    while i < len(page):
        row = []
        for n in range(10):
            row.append(page[i].text)
            i+=1
        # Get the values from the page
        sr = int(row[0])
        affl = str(row[1].split(".")[1])
        name = str(row[3].split(":")[1])
        pr = str(row[4].split(":")[1])
        stat = str(row[5].split(":")[1])
        addr = str(row[7].split(":")[1])
        phno = str(row[8].split(":")[1])
        email = str(row[9].split("\n")[0].split(":")[1])
        web = str("".join(row[9].split("\n")[1].split(":")[1:]))
        # Print Results for debugging
        print([sr,affl,name,pr,stat,addr,phno,email,web]) # This line is not essential
        # Insert values into the database
        conn.execute("INSERT INTO SCHOOLS (SRL,AFFL,NAME,PRNAME,STATUS,ADDR,PHNO,EMAIL,WEBSITE)\
            VALUES {}".format((sr,affl,name,pr,stat,addr,phno,email,web)))
        conn.commit()
# Search and traverse through the database page by page
for ch in lex:
    search = driver.find_element_by_id("keytext")
    search.clear()
    search.send_keys(ch)
    search.send_keys(Keys.RETURN)
    page = driver.find_elements_by_class_name(name="repItem")
    extract(page)
    # Once we reach end of page click next button, if not break and search next character
    while True:
        try:
            button = driver.find_element_by_id(id_="Button1")
            button.send_keys(Keys.RETURN)
            page = driver.find_elements_by_class_name(name = "repItem")
            extract(page)
        except:
            break
time.sleep(5)
driver.quit()