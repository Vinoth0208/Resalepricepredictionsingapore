import sys
import numpy as np
sys.path.insert(1, r'SingaporeResaleFlatPricesPredicting\venv\Lib\site-packages')
import pandas as pd
import streamlit as st
from geopy.geocoders import Nominatim



def Data():

    data2 = pd.read_csv(
        r'ResaleFlatPricesBasedonApprovalDate2000Feb2012.csv')
    data1 = pd.read_csv(
        r'ResaleFlatPricesBasedonApprovalDate19901999.csv')
    data3 = pd.read_csv(
        r'ResaleFlatPricesBasedonRegistrationDateFromMar2012toDec2014.csv')
    data4 = pd.read_csv(
        r'ResaleFlatPricesBasedonRegistrationDateFromJan2015toDec2016.csv')
    data5 = pd.read_csv(
        r'ResaleflatpricesbasedonregistrationdatefromJan2017onwards.csv')
    Data = pd.concat([data1, data2, data3, data4, data5], ignore_index=True)
    print(Data)
    print(Data.info())
    print(Data.isnull().sum())
    Data['month'] = pd.to_datetime(Data['month'])
    Data['month'] = pd.to_datetime(Data['month'], format='%Y%m%d')
    Data['remaining_lease'] = Data['lease_commence_date'] + 99 - Data['month'].dt.year
    Data.isnull().sum()

    min_storey = []
    max_storey = []
    for i in range(len(Data['storey_range'])):
        min_storey.append(Data['storey_range'][i].split(" ")[0])
        max_storey.append(Data['storey_range'][i].split(" ")[2])

    storey = {
        'max_storey': max_storey,
        'min_storey': min_storey
    }
    d = pd.DataFrame(storey)

    town = [x for x in Data['town'].unique().tolist()
            if type(x) == str]
    latitude = []
    longitude = []
    for i in range(0, len(town)):
        try:
            geolocator = Nominatim(user_agent="ny_explorer")
            loc = geolocator.geocode(town[i])
            latitude.append(loc.latitude)
            longitude.append(loc.longitude)
            print('The geographical coordinate of location are {}, {}.'.format(loc.latitude, loc.longitude))
        except:
            latitude.append(np.nan)
            longitude.append(np.nan)

    df_ = pd.DataFrame({'town': town,
                        'latitude': latitude,
                        'longitude': longitude})
    Data = Data.merge(df_, on='town', how='left')

    Data['min_storey'] = d['min_storey']
    Data['max_storey'] = d['max_storey']

    Data['address'] = Data['block'].map(str) + ', ' + Data['street_name'].map(str) + ', Singapore'
    Data['flat_type'] = Data['flat_type'].replace({'MULTI-GENERATION': 'MULTI GENERATION' }, regex=True)
    Data=Data.head(611595)
    Data.to_csv('hdb_resale.csv',index=False)

    st.write(Data)
    data = pd.read_csv(r'hdb_resale.csv')

    File = data.to_csv()
    st.download_button(
        label="Download data as CSV",
        data=File,
        file_name='hdb_resale_data.csv',
        mime='text/csv', )



