from spellchecker import SpellChecker
import re
from nltk.corpus import wordnet
from bs4 import BeautifulSoup
import requests
from selenium import webdriver


command = "from kaggle download a dataset on 'indian stock market'"

useless_text = ["a","an","the","is","on","in","for","of","and","be","should"]

main_command = re.findall(r'\w+', command)   #SEPERATING ALL THE WORDS

# corrected_command = [SpellChecker().correction(x) for x in main_command]   #CORRECTING MISPELLED WORDS
corrected_command = []

main_command_lower = [x.lower() for x in main_command if x.lower() not in useless_text]  #REMOVING USELESS WORDS AND CONVERTING THEM TO LOWER TEXT

for x in main_command_lower:
    if SpellChecker().correction(x)!=None:
        corrected_command.append(SpellChecker().correction(x))
    else:
        corrected_command.append(x)

words_interest = ["csv","xlsx","txt","ipynb","json","md","py","parquet","xls","kaggle","size","small","large","medium","relevant","newest","latest","topic","filetype","dataset","datatype"]

filtered_command = [x for x in main_command_lower if x in words_interest]

# print(filtered_command)

size = ["small","medium","large"]
filetype = ["csv","xlsx","txt","ipynb","json","md","py","parquet","xls"]
type_data = {"relevance":"relevance","relevant":"relevance","latest":"date","newest":"date"}

final_size = ""
final_filetype = ""
final_type_data = ""

pattern = r"'(.*?)'"
topic_name = re.findall(pattern, command)
seperated_topic_words = re.findall(r'\w+', topic_name[0])

if len(seperated_topic_words)>=2:
    final_topic = "+".join(seperated_topic_words)
elif len(seperated_topic_words)==1:
    final_topic = topic_name[0]

if "dataset" in filtered_command:
    for x in filtered_command:
        if x in size:
            final_size = x
        elif x in filetype:
            final_filetype = x
        elif x in type_data.keys():
            final_type_data = type_data[x]
    
    # print(final_size)
    # print(final_filetype)
    # print(final_type_data)

    primary_url = f'https://www.kaggle.com/search?q={final_topic}+in%3Adatasets'

    if final_size != "":
        size_url = f'datasetSize%3A{final_size}'
    else:
        size_url = ""

    if final_type_data != "":
        if final_type_data == "relevance":
            pass
        elif final_type_data=="date":
            type_data_url = 'sortBy%3Adate'
    else:
        type_data_url = ""

    if final_filetype!="":
        file_type_url = f'datasetFileTypes%3A{final_filetype}'
    else:
        file_type_url = ""

    final_url = primary_url + "+" + size_url + "+" + type_data_url + "+" + file_type_url

    print(final_url)

    driver = webdriver.Chrome (executable_path="C:\chromedriver.exe")
    driver.maximize_window()
    driver.get(final_url)
    
    lnks=driver.find_elements_by_tag_name("a")
    
    for lnk in lnks:
    
        print(lnk.get_attribute(href))
    driver.quit()

    # response = requests.get(final_url)

    # print(response.status_code)

    # if response.status_code == 200:
    #     html_content = response.text

    #     print(html_content)
        
    #     soup = BeautifulSoup(html_content, "html.parser")

    # requests.get(final_url)

    # soup_object1 = BeautifulSoup(final_url , 'html.parser')

    # m=soup_object1.prettify()

    # print(m)
    # for div in soup_object1.findAll('div', attrs={'class':'sc-fmKFGs sc-imiRDh cynhGK gvrsOC'}):
    #     txt = div.text
    #     # file.write(div.text)
    #     print(div.text)
    #     print("------------------------------------------------------------------------------------------------")

    # link = soup.find('div', class_='example').a['href']

    # print(link)

    # url = 'https://www.kaggle.com/search?q=stock+market+in%3Adatasets+datasetSize%3Amedium++datasetFileTypes%3Acsv'
    # reqs = requests.get(url)
    # soup = BeautifulSoup(reqs.text, 'html.parser')
    
    # urls = []
    # for link in soup.find_all('a'):
    #     print(link.get('href'))


