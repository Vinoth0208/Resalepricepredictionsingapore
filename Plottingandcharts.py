import pandas as pd
import plotly.express as px
import streamlit


def plots():
    Data=pd.read_csv(r'hdb_resale.csv')

    df = Data.groupby(['flat_type'], as_index=False)['flat_type'].count()
    flat = Data['flat_type'].unique()
    flat = pd.DataFrame(flat)
    flat.rename(columns={0: 'flat_type'}, inplace=True)
    df = pd.DataFrame(df)
    df.rename(columns={'flat_type': 'count'}, inplace=True)
    df = pd.concat([flat, df], axis=1)


    image = px.bar(df, x='flat_type', y='count', color='flat_type',title='Flat type vs Count')
    streamlit.plotly_chart(image, use_container_width=True)

    df = Data.groupby(['flat_type'], as_index=False)['resale_price'].mean()
    image=px.pie(values=df.resale_price, names=df.flat_type, title='Mean resale price for flat_type')
    streamlit.plotly_chart(image, use_container_width=True)

    df = Data.groupby(['flat_type', 'max_storey'], as_index=False).size()
    image=px.scatter(df, x='max_storey',y='size', hover_data=['flat_type'])
    streamlit.plotly_chart(image, use_container_width=True)

    df = Data.groupby(['flat_type', 'floor_area_sqm'], as_index=False).size()
    image=px.histogram(df, x='floor_area_sqm', y='size', color='floor_area_sqm', title='Floor area sqm vs sum of size')
    streamlit.plotly_chart(image, use_container_width=True)

    df = Data.groupby(['flat_model', 'flat_type'], as_index=False)['flat_type'].size()
    image=px.scatter(df, x='flat_model', y='size', size='size', hover_data=['flat_type'], color='flat_model')
    streamlit.plotly_chart(image, use_container_width=True)

    df = Data.groupby(['flat_model', 'remaining_lease'], as_index=False)['flat_type'].size()
    image=px.bar(df, x='remaining_lease', y='size', color='flat_model', hover_data=['flat_model'])
    streamlit.plotly_chart(image, use_container_width=True)

    image=px.box(Data, x='remaining_lease', y='resale_price', color='remaining_lease')
    streamlit.plotly_chart(image, use_container_width=True)



