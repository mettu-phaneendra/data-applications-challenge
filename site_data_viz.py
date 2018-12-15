#!/usr/bin/env python

import requests
import plotly
import plotly.plotly as py
plotly.tools.set_credentials_file(username='pmettu', api_key='19dQNYZz6M9Co4KsVDtk')


def get_volta_data(url):
    d_metrics = dict()
    req = requests.get(url)
    site_metrics = req.json()
    d_metrics['size'] = len(site_metrics)
    print "No. of sites :", d_metrics['size']

    # build the site metrics data from resulted json
    _count = 0
    for site in site_metrics:
        _name = ''
        _latitude = 0
        _longitude = 0
        _count = _count + 1
        if 'name' in site and not (site['name'] is None):
            _name = site['name']
            print
            print ("Site # {}, Name :{}".format(_count, _name))

        if 'location' in site and not (site['location'] is None):
            _latitude = site['location']['coordinates'][0]
            _longitude = site['location']['coordinates'][1]
            print ("Location :({}, {})".format(_latitude, _longitude))

        if 'chargers' in site and not (site['chargers'] is None):
            _total_chargers = (site['chargers'][0]['total'])
            _available_chargers = (site['chargers'][0]['available'])
            print ("Total chargers :{}; Available chargers :{}".format(_total_chargers, _available_chargers))
        else:
            print ("Total chargers :{}; Available chargers :{}".format(0, 0))

        if 'stations' in site and not (site['stations'] is None):
            for count in range(len(site['stations'])):
                _station = site['stations'][count]['name']
                _media = str(site['stations'][count]['has_media_issue'])
                print ("\tStation :{}; has media issues :{}".format(_station, _media))

        # plotting the site data on the map
        # build the data and the layout for the plotly api.
        # thanks to https://plot.ly/python/scatter-plots-on-maps/

        _data = [dict(
            type='scattergeo',
            locationmode='USA-states',
            lon=_longitude,
            lat=_latitude,
            text=_name,
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
            title='Volta sites location and metrics',
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
        py.iplot(figure, validate=False, filename='Site-Metrics')

def main():
    site_metrics_url = 'https://api.voltaapi.com/v1/sites-metrics'
    get_volta_data(site_metrics_url);


if __name__ == "__main__": main()
