#!/usr/bin/env python

import requests


def get_volta_data(url):
    d_metrics = dict()
    req = requests.get(url)
    site_metrics = req.json()
    d_metrics['size'] = len(site_metrics)
    print "No. of sites :", d_metrics['size']

    # build the site metrics data from resulted json
    _count = 1
    for site in site_metrics:
        _name = ''
        _latitude = 0
        _longitude = 0
        if 'name' in site and not (site['name'] is None):
            _name = site['name']
            print ("Site # {}, name {}:".format(_count, _name))
            _count = _count + 1;
        if 'location' in site and not (site['location'] is None):
            _latitude = site['location']['coordinates'][0]
            _longitude = site['location']['coordinates'][1]
            print ("Location :({}, {})".format(_latitude, _longitude))

def main():
    site_metrics_url = 'https://api.voltaapi.com/v1/sites-metrics'
    get_volta_data(site_metrics_url);


if __name__ == "__main__": main()
