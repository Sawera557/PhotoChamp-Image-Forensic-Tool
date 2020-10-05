import os
import random
import webbrowser

import folium

from simple_PIL_code import extractPIL


def map_html(file_path):

    extractPIL(file_path)
    lat = 37.5056
    lon = -111.051119
    browser_path = 'C:\\Program Files\\Opera\\launcher.exe'
    webbrowser.register('opera', None, webbrowser.BackgroundBrowser(browser_path))

    # Get an instance and launch your file
    browser = webbrowser.get('opera')

    my_map3 = folium.Map(location=[lat, lon],
                         zoom_start=15)

    # Pass a string in popup parameter
    folium.Marker([lat, lon],
                  popup='Picture Was Taken Here!').add_to(my_map3)

    head, tail = os.path.split(file_path)
    Maps_path = os.getcwd() + "\\Maps"
    file_number = random.randint(1, 1000)
    Gen_MapName = Maps_path + "\\Map_" + tail + "_" + str(file_number) + ".html"

    my_map3.save(Gen_MapName)
    browser.open(Gen_MapName)
