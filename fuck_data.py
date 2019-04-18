#!/usr/bin/env python
from functools import reduce

def display_stats(data):
    print('Sample({}) 平均 = {}'.format(len(data),
        reduce(lambda x, y: x + y['avg'], data, 0) / len(data) if data else 0))
    one_car_pool = list(filter(lambda x: x['car_pool'] == 1, data))
    print('Sample({}) 單車位 平均(扣車位110) = {}'.format(len(one_car_pool),
        reduce(lambda x, y: x + ((y['total'] - 110 * y['car_pool']) / (y['area'] - 9 * y['car_pool'])), one_car_pool, 0) / len(one_car_pool) if one_car_pool else 0))
    two_car_pool = list(filter(lambda x: x['car_pool'] == 2, data))
    print('Sample({}) 雙車位 平均(扣車位110) = {}'.format(len(two_car_pool),
        reduce(lambda x, y: x + ((y['total'] - 110 * y['car_pool']) / (y['area'] - 9 * y['car_pool'])), two_car_pool, 0) / len(two_car_pool) if two_car_pool else 0))

    high_floor = list(filter(lambda x: x['floor'] >= 10, data))
    print('Sample({}) 高樓(>=10F) 平均 = {}'.format(len(high_floor),
        reduce(lambda x, y: x + y['avg'], high_floor, 0) / len(high_floor) if high_floor else 0))
    high_floor_not_13F = list(filter(lambda x: x['floor'] >= 10 and x['floor'] != 13, data))
    print('Sample({}) 高樓(>=10F)非13F 平均 = {}'.format(len(high_floor_not_13F),
        reduce(lambda x, y: x + y['avg'], high_floor_not_13F, 0) / len(high_floor_not_13F) if high_floor_not_13F else 0))
    high_floor_not_top = list(filter(lambda x: x['floor'] >= 10 and x['floor'] != x['total_floor'], data))
    print('Sample({}) 高樓(>=10F)非頂樓 平均 = {}'.format(len(high_floor_not_top),
        reduce(lambda x, y: x + y['avg'], high_floor_not_top, 0) / len(high_floor_not_top) if high_floor_not_top else 0))

    mid_floor = list(filter(lambda x: 4 < x['floor'] < 10, data))
    print('Sample({}) 中樓 平均 = {}'.format(len(mid_floor),
        reduce(lambda x, y: x + y['avg'], mid_floor, 0) / len(mid_floor) if mid_floor else 0))

    low_floor = list(filter(lambda x: x['floor'] <= 4, data))
    print('Sample({}) 低樓(<=4F) 平均 = {}'.format(len(low_floor),
        reduce(lambda x, y: x + y['avg'], low_floor, 0) / len(low_floor) if low_floor else 0))
    low_floor_not_4F = list(filter(lambda x: x['floor'] <= 4 and x['floor'] != 4, data))
    print('Sample({}) 低樓(<=4F)非4F 平均 = {}'.format(len(low_floor_not_4F),
        reduce(lambda x, y: x + y['avg'], low_floor_not_4F, 0) / len(low_floor_not_4F) if low_floor_not_4F else 0))
    low_floor_not_2F = list(filter(lambda x: x['floor'] <= 4 and x['floor'] != 2, data))
    print('Sample({}) 低樓(<=4F)非2F 平均 = {}'.format(len(low_floor_not_2F),
        reduce(lambda x, y: x + y['avg'], low_floor_not_2F, 0) / len(low_floor_not_2F) if low_floor_not_2F else 0))

    one_car_pool = list(filter(lambda x: x['car_pool'] == 1, data))
    print('Sample({}) 單車位 平均 = {}'.format(len(one_car_pool),
        reduce(lambda x, y: x + y['avg'], one_car_pool, 0) / len(one_car_pool) if one_car_pool else 0))
    one_car_pool_high_floor = list(filter(lambda x: x['car_pool'] == 1 and x['floor'] >= 10, data))
    print('Sample({}) 單車位 高樓 平均 = {}'.format(len(one_car_pool_high_floor),
        reduce(lambda x, y: x + y['avg'], one_car_pool_high_floor, 0) / len(one_car_pool_high_floor) if one_car_pool_high_floor else 0))
    one_car_pool_mid_floor = list(filter(lambda x: x['car_pool'] == 1 and 4 < x['floor'] < 10, data))
    print('Sample({}) 單車位 中樓 平均 = {}'.format(len(one_car_pool_mid_floor),
        reduce(lambda x, y: x + y['avg'], one_car_pool_mid_floor, 0) / len(one_car_pool_mid_floor) if one_car_pool_mid_floor else 0))
    one_car_pool_low_floor = list(filter(lambda x: x['car_pool'] == 1 and x['floor'] <= 4, data))
    print('Sample({}) 單車位 低樓 平均 = {}'.format(len(one_car_pool_low_floor),
        reduce(lambda x, y: x + y['avg'], one_car_pool_low_floor, 0) / len(one_car_pool_low_floor) if one_car_pool_low_floor else 0))

    two_car_pool = list(filter(lambda x: x['car_pool'] == 2, data))
    print('Sample({}) 雙車位 平均 = {}'.format(len(two_car_pool),
        reduce(lambda x, y: x + y['avg'], two_car_pool, 0) / len(two_car_pool) if two_car_pool else 0))
    two_car_pool_high_floor = list(filter(lambda x: x['car_pool'] == 2 and x['floor'] >= 10, data))
    print('Sample({}) 雙車位 高樓 平均 = {}'.format(len(two_car_pool_high_floor),
        reduce(lambda x, y: x + y['avg'], two_car_pool_high_floor, 0) / len(two_car_pool_high_floor) if two_car_pool_high_floor else 0))
    two_car_pool_mid_floor = list(filter(lambda x: x['car_pool'] == 2 and 4 < x['floor'] < 10, data))
    print('Sample({}) 雙車位 中樓 平均 = {}'.format(len(two_car_pool_mid_floor),
        reduce(lambda x, y: x + y['avg'], two_car_pool_mid_floor, 0) / len(two_car_pool_mid_floor) if two_car_pool_mid_floor else 0))
    two_car_pool_low_floor = list(filter(lambda x: x['car_pool'] == 2 and x['floor'] <= 4, data))
    print('Sample({}) 雙車位 低樓 平均 = {}'.format(len(two_car_pool_low_floor),
        reduce(lambda x, y: x + y['avg'], two_car_pool_low_floor, 0) / len(two_car_pool_low_floor) if two_car_pool_low_floor else 0))


if __name__ == '__main__':
    with open('data', 'r') as f:
        line = list(map(lambda x: x.strip(), f.readlines()))
        line = list(filter(lambda x: x != '車', line))

    data = []
    for i in range(int(len(line) / 6)):
        _data = dict()
        
        _data['addr'] = line.pop(0)
        _data['car_pool'] = int(line.pop(0))
        _data['date'] = line.pop(0)
        _data['total'] = int(line.pop(0).replace(',', ''))
        _data['avg'] = float(line.pop(0))

        _d = line.pop(0).split('\t')

        _data['area'] = float(_d[0])
        _data['floor'] = int(_d[-1].split('/')[0])
        _data['total_floor'] = int(_d[-1].split('/')[1])

        data.append(_data)

    print('=' * 12 + ' 過去三年 ' + '=' * 13)
    display_stats(data)

    print('=' * 15 + ' 107 ' + '=' * 15)

    data_107 = list(filter(lambda x: x['date'].startswith('107'), data))
    display_stats(data_107)

    print('=' * 15 + ' 106 ' + '=' * 15)

    data_106 = list(filter(lambda x: x['date'].startswith('106'), data))
    display_stats(data_106)

    print('=' * 15 + ' 105 ' + '=' * 15)

    data_105 = list(filter(lambda x: x['date'].startswith('105'), data))
    display_stats(data_105)
