#!/usr/bin/env python

import requests
import plotly
import plotly.plotly as py

plotly.tools.set_credentials_file(username='pmettu', api_key='19dQNYZz6M9Co4KsVDtk')


class SiteMap(object):
    def __init__(self, site_metrics, d_metrics):
        self.site_metrics = site_metrics
        self.d_metrics = d_metrics
        self.site_status = {'latitude': [], 'longitude': [], 'text': []}
        self.map_site_metrics_data()

    def get_site_metrics(self, url):
        r = requests.get(url)
        self.site_metrics = r.json()
        self.d_metrics['size'] = len(self.site_metrics)
        self.map_site_metrics_data()

    def map_site_metrics_data(self):
        _count = 0
        for site in self.site_metrics:
            _name = ''
            _text = ''
            _latitude = 0
            _longitude = 0
            _count = _count + 1
            if 'name' in site and not (site['name'] is None):
                _name = site['name']
                _text = ('Site :', _name)
                print
                print ("Site # {}, Name :{}".format(_count, _name))

            if 'location' in site and not (site['location'] is None):
                _latitude = site['location']['coordinates'][1]
                self.site_status['latitude'].append(_latitude)
                _longitude = site['location']['coordinates'][0]
                self.site_status['longitude'].append(_longitude)
                print ("Location :({}, {})".format(_latitude, _longitude))

            if 'chargers' in site and not (site['chargers'] is None):
                _total_chargers = (site['chargers'][0]['total'])
                _available_chargers = (site['chargers'][0]['available'])
                _text = _text + ('Total :', _total_chargers)
                _text = _text + ('Available :', _available_chargers)
                print ("Total chargers :{}; Available chargers :{}".format(_total_chargers, _available_chargers))
            else:
                _text = _text + ('Total :', 0)
                _text = _text + ('Available :', 0)
                print ("Total chargers :{}; Available chargers :{}".format(0, 0))

            if 'stations' in site and not (site['stations'] is None):
                for count in range(len(site['stations'])):
                    _station = site['stations'][count]['name']
                    _media = str(site['stations'][count]['has_media_issue'])
                    _text = _text + ('Station :', _station)
                    _text = _text + ('; Media issues :', _media)
                    print ("\tStation :{}; has media issues :{}".format(_station, _media))
                self.site_status['text'].append(_text)

    # plotting the site data on the map
    # build the data and the layout for the plotly api.
    # thanks to https://plot.ly/python/scatter-plots-on-maps/
    def plot_site_data(self):
        _data = [dict(
            type='scattergeo',
            locationmode='USA-states',
            lon=self.site_status.get('longitude'),
            lat=self.site_status.get('latitude'),
            text=self.site_status.get('text'),
            mode='markers',
            marker=dict(
                size=8,
                opacity=0.8,
                reversescale=True,
                autocolorscale=False,
                symbol='circle',
                line=dict(
                    width=1,
                    color='rgba(102, 102, 102)'
                )
            )
        )]
        _layout = dict(
            title='Charging Station Metrics',
            colorbar=False,
            geo=dict(
                scope='usa',
                projection=dict(type='albers usa'),
                showland=True,
                landcolor="rgb(250, 250, 250)",
                subunitcolor="rgb(217, 217, 217)",
                countrycolor="rgb(217, 217, 217)",
                countrywidth=0.5,
                subunitwidth=0.5,
                resolution=50,
                lonaxis=dict(
                    showgrid=True,
                    gridwidth=0.5,
                    range=[-140.0, -55.0],
                    dtick=5
                ),
                lataxis=dict(
                    showgrid=True,
                    gridwidth=0.5,
                    range=[20.0, 60.0],
                    dtick=5
                )
            ),
        )
        figure = dict(data=_data, layout=_layout)
        py.plot(figure, validate=False, filename='Site-Metrics')


sites = SiteMap(dict(), dict())
sites.get_site_metrics("https://api.voltaapi.com/v1/sites-metrics")
sites.plot_site_data()
