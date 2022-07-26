from csv import writer
from bs4 import BeautifulSoup
import requests
import csv

url = 'https://www.akchabar.kg/ru/exchange-rates/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'lxml')


table1 = soup.find_all('tbody')
tables_of_currencies_and_banks = table1[4]

list_buying_selling = soup.find_all('thead')
buying_and_selling = list_buying_selling[4]
buy_prod = ['Банк'] + ['Покупка', 'Продажа'] * 4

list_val = []

for pim in buying_and_selling.findAll('span', class_='dib'):
    list_val.append(pim.text)

data_val = soup.find('span', class_='refresh')
name_file = data_val.text[22:]
with open('{}.csv'.format(name_file), 'w') as pul:
    writer = csv.writer(pul)


currency_name = ['Наличные курсы']

i = 0
while i != 4:
    currency_name.append(list_val[i])
    currency_name.append('')
    i += 1    

with open('{}.csv'.format(name_file), 'a') as pul:
    writer = csv.writer(pul)
    writer.writerow(currency_name)
    writer.writerow(buy_prod)


list_banks_currencies =  []
for one_bank in tables_of_currencies_and_banks.findAll('tr'): 
    one_element_list = []
    for bank in one_bank.findAll('td'):
        one_element_list.append(bank.text)
    list_banks_currencies.append(one_element_list)


with open('{}.csv'.format(name_file), 'a') as pul:
    writer = csv.writer(pul)
    for bank_list_write in list_banks_currencies:
        writer.writerow(bank_list_write)

    
 

