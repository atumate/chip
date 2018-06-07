#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Test urls are valid or not, urls from txt file, results to csv file
remote: https://github.com/nixni/chip/blob/master/py/test_urls.py
"""

import requests
import re 
from pprint import pprint

TIME_OUT_CONNECTION = 2
TIME_OUT_READ = 3


def test_url(targetURL):
    valid_status_codes=[200,302];
    info = '';
    print('checking-> ' + targetURL)

    try:
        response = requests.head(targetURL, timeout=(TIME_OUT_CONNECTION, TIME_OUT_READ))
    except Exception as e:
        # raise e
        info = 'Timeout'
        print(info)
        return targetURL + ',,' + info
    else:
        if response.status_code in valid_status_codes:
            info = 'Valid!'
        else :
            info = 'Not Valid!'
        
        print(str(response.status_code) + ','+ info)
        return targetURL +','+ str(response.status_code) + ',' + info



def format_url(raw_url):
    formatted_url = raw_url
    if not re.match(r'^(http|https)://',raw_url):
        formatted_url = 'http://' + raw_url
    return formatted_url
    

def read_txt(fname):
    with open(fname) as f:
        lines = f.readlines()
    csv_list =[test_url(format_url(x.strip())) for x in lines]
    return csv_list

def write_csv(fname,text_list):
    with open(fname,'w') as file:
        for item in text_list:
            file.write(item)
            file.write('\n')
    return 'ok'




def main():
    print('test_url.py start!')
    print('TIME_OUT_CONNECTION:'+ str(TIME_OUT_CONNECTION) +'s')
    print('TIME_OUT_READ:'+ str(TIME_OUT_READ) +'s' + '\n')
    csv_list_ready=read_txt('ip.txt')
    write_csv('results.csv',csv_list_ready)



if __name__ == "__main__":
    main()
