#!/usr/bin/env python

import requests


def get_volta_data(url):
    d_metrics = dict()
    req = requests.get(url)
    site_metrics = req.json()
    d_metrics['size'] = len(site_metrics)
    print "No. of sites :", d_metrics['size']


def main():
    site_metrics_url = 'https://api.voltaapi.com/v1/sites-metrics'
    get_volta_data(site_metrics_url);


if __name__ == "__main__": main()
