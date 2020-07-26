#!/usr/bin/env python
from bs4 import BeautifulSoup
from functools import reduce
from statistics import mean, median, stdev

def load_html_doc(path):
    with open(path) as f:
        doc = f.read()
    return doc

def normalize(doc):
    soup = BeautifulSoup(doc, 'html.parser')
    total_row = int(soup.find(id='rowtol').get('value'))

    records = []
    for i in range(1, total_row + 1):
        row = soup.find(id=i)
        detailed = row.next_sibling.next_sibling

        address = row.find(id='Address_{}'.format(i - 1)).string.split('-').pop()
        trade_year, trade_month = row.find('td', {'class': 'text_row2'}).string.strip().split('/')
        total_price = row.find(id='TotalPrice_{}'.format(i - 1)).string.strip().replace(',', '')
        area = row.find('td', {'class': 'text_row5'}).string.strip()
        age = row.find('td', {'class': 'text_row8'}).string.strip()
        floor, total_floor = row.find('td', {'class': 'text_row9'}).string.strip().split('/')
        car_pool = detailed.find('table', {'class':'det_section_r'}).find('tr').find_all('td')[1].find_all('span')[7].string

        result = {
            'address': address,
            'trade_year': int(trade_year),
            'trade_month': int(trade_month),
            'total_price': int(total_price),
            'area': float(area),
            'age': int(age),
            'floor': int(floor),
            'total_floor': int(total_floor),
            'car_pool': int(car_pool),
            'avg': int(total_price) / float(area)
        }
        records.append(result)
    return records

def calculate(data):
    sample = len(data)
    avg = round(mean(map(lambda x: x['avg'], data)), 3)
    mid = round(median(map(lambda x: x['avg'], data)), 3)
    std = round(stdev(map(lambda x: x['avg'], data)), 3) if len(data) > 1 else 'N/A'
    return sample, avg, mid, std 

def year(year, records):
    year_data = list(filter(lambda x: x['trade_year'] == year, records))
    return calculate(year_data) if len(year_data) > 0 else ('N/A', 'N/A', 'N/A', 'N/A')

def year_car_pool(year, records, car_pool):
    year_data = list(filter(lambda x: x['trade_year'] == year and x['car_pool'] == car_pool, records))
    return calculate(year_data) if len(year_data) > 0 else ('N/A', 'N/A', 'N/A', 'N/A')

def year_floor(year, records, floor):
    year_data = list(filter(lambda x: x['trade_year'] == year and x['floor'] == floor, records))
    return calculate(year_data) if len(year_data) > 0 else ('N/A', 'N/A', 'N/A', 'N/A')

def pretty(records, year_range):
    for i in year_range:
        sample, avg, mid, std = year(i, records)
        print('{}年({}): 平均 {} 萬/坪, 中位數: {} 萬/坪, 標準差: {} 萬/坪'.format(i, sample, avg, mid, std)) 

    # Car pool reference
    for i in range(0, 3):
        print('{} 車位: {} {}'.format('=' * 5, i, '=' * 5))
        for j in year_range:
            sample, avg, mid, std = year_car_pool(j, records, i)
            print('{}年({}): 平均 {} 萬/坪, 中位數: {} 萬/坪, 標準差: {} 萬/坪'.format(j, sample, avg, mid, std))

    # Floor reference
    for i in range(1, records[0]['total_floor'] + 1):
        print('{} {}樓 {}'.format('=' * 5, i, '=' * 5))
        for j in year_range:
            sample, avg, mid, std = year_floor(j, records, i)
            print('{}年({}): 平均 {} 萬/坪, 中位數: {} 萬/坪, 標準差: {} 萬/坪'.format(j, sample, avg, mid, std)) 

doc = load_html_doc('./data')
records = normalize(doc)
pretty(records, range(105, 109 + 1))
