# Volta Code Challenge
> The goal of this challenge is to demonstrate your skills, with a tool of your choice, taking data and turning it into something meaningful.

## Problem
We have a publicly available endpoint, documented here:
http://docs.voltaapi.com/api/#get--stations.
Build an interface that exposes this data in whatever form you like.

### Requirements
- Don't spend too much time on this, focusing on one feature is a plus
- Deliver a product that is easy for us to consume
- Commit history showing your thought/development process is always interesting
- DO NOT fork this repository. Create a new personal repository then email it to us once its complete

If you have any questions do not hesitate to reach out via email or phone. In consideration of your schedule, take as long as you need to return the challenge.

### Some examples/ideas for inspiration:
- Display the stations on a map
- Render a searchable table of the stations
- Aggregate data about the stations and display a high-level metric

## Tips and Tricks
We don't spend much time reinventing wheels here at Volta. Depending on the meaning you would like to derive from our data, find a tool or library that helps you express it without writing an excessive amount of code or re-implementing existing technology.

Conversely, if you already have a tool or library in mind: show off your skills by using something you know when to provide new insight into our data. Engineering hours are expensive so we like to find a middle-ground between correctness and efficiency.

## Technologies or tools used

Python makes perfect sense to quickly plot or map locations on the map.
I am planning on using Matplotlib BaseMap to plot the station metrics on the map.
Keeping the 2 hrs time in mind, I'll keep the documentation to minimal and use intuitive naming 

After a little bit of reviews online, it makes sense to use this new py map module called plotly
Advantage: the plots are posted online, so no dependency to have a massive basemap module installed
Disadvantage: the data is plotted online and public, since some of these api are public information that should not be a problem.
I will try use only those api which doesnt need a auth credentials. 


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Final steps followed to plot this site metrics data:

OS: ubuntu 18.04
Python 2.7.12

setup:
sudo apt install python
sudo apt install python-pip

pip install requests
pip install plotly

plotly account:
user-name : pmettu
key : 19dQNYZz6M9Co4KsVDtk

These above steps needs to be done using a setup py file.
will try to add setup file, as I have run out of time. 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


