import numpy as np
import pandas as pd
import streamlit as st
from sklearn import metrics
from sklearn.metrics import mean_squared_error
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import  StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def predict():
    dataframe = pd.read_csv(r'hdb_resale.csv')
    townDict = {'ANG MO KIO': 1, 'BEDOK': 2, 'BISHAN': 3, 'BUKIT BATOK': 4, 'BUKIT MERAH': 5, 'BUKIT PANJANG': 6,
                'BUKIT TIMAH': 7, 'CENTRAL AREA': 8, 'CHOA CHU KANG': 9, 'CLEMENTI': 10, 'GEYLANG': 11, 'HOUGANG': 12,
                'JURONG EAST': 13, 'JURONG WEST': 14, 'KALLANG/WHAMPOA': 15, 'MARINE PARADE': 16, 'PASIR RIS': 17,
                'PUNGGOL': 18, 'QUEENSTOWN': 19, 'SEMBAWANG': 20, 'SENGKANG': 21, 'SERANGOON': 22, 'TAMPINES': 23,
                'TOA PAYOH': 24, 'WOODLANDS': 25, 'YISHUN': 26, 'LIM CHU KANG':27}
    flat_typeDict = {'1 ROOM': 1, '2 ROOM': 2, '3 ROOM': 3, '4 ROOM': 4, '5 ROOM': 5, 'EXECUTIVE': 6,
                     'MULTI-GENERATION': 7, 'MULTI GENERATION': 7 }

    latitude = {"ANG MO KIO": 1.3700803, "BEDOK": 1.3239765, "BISHAN": 29.5730296, "BUKIT BATOK": 1.3490572,
                "BUKIT MERAH": 5.0421261,
                "BUKIT PANJANG": 1.3791486, "BUKIT TIMAH": 1.3546901, "CENTRAL AREA": 36.5070827,
                "CHOA CHU KANG": 1.3853167, "CLEMENTI": 1.3151003,
                "GEYLANG": 1.3181862, "HOUGANG": 1.3708011, "JURONG EAST": 1.333108, "JURONG WEST": 1.3434392,
                "KALLANG/WHAMPOA": 1.329832,
                "LIM CHU KANG": 1.4342172, "MARINE PARADE": 1.3026889, "PASIR RIS": 1.3730307, "PUNGGOL": 1.4054248,
                "QUEENSTOWN": -45.0321923,
                "SEMBAWANG": 1.4490928, "SENGKANG": 1.3916536, "SERANGOON": 1.34976105, "TAMPINES": 1.3546528,
                "TOA PAYOH": 1.3353906,
                "WOODLANDS": 54.3558467, "YISHUN": 1.4293839
                }
    longitude = {"ANG MO KIO": 103.8495228, "BEDOK": 103.930216, "BISHAN": 106.1686627, "BUKIT BATOK": 103.7495906,
                 "BUKIT MERAH": 100.6535879, "BUKIT PANJANG": 103.761413, "BUKIT TIMAH": 103.7763724,
                 "CENTRAL AREA": -79.7447575,
                 "CHOA CHU KANG": 103.744325, "CLEMENTI": 103.7652311, "GEYLANG": 103.8870563, "HOUGANG": 103.8925443,
                 "JURONG EAST": 103.7422939, "JURONG WEST": 103.7058663, "KALLANG/WHAMPOA": 103.862424,
                 "LIM CHU KANG": 103.7149872,
                 "MARINE PARADE": 103.9073952, "PASIR RIS": 103.949255, "PUNGGOL": 103.9017967, "QUEENSTOWN": 168.661,
                 "SEMBAWANG": 103.8200555, "SENGKANG": 103.8953636, "SERANGOON": 103.8736841, "TAMPINES": 103.9435712,
                 "TOA PAYOH": 103.8497414, "WOODLANDS": -115.2252675, "YISHUN": 103.8350282
                 }

    dataframe['town'] = dataframe['town'].replace(townDict, regex=True)
    dataframe['flat_type'] = dataframe['flat_type'].replace(flat_typeDict, regex=True)


    dataframe = dataframe.drop('block', axis=1)
    dataframe = dataframe.drop('month', axis=1)
    dataframe = dataframe.drop('street_name', axis=1)
    dataframe = dataframe.drop('address', axis=1)
    dataframe = dataframe.drop('flat_model', axis=1)
    dataframe = dataframe.drop('storey_range', axis=1)
    dataframe = dataframe.drop('max_storey', axis=1)
    dataframe = dataframe.drop('remaining_lease', axis=1)



    tab1, tab2=st.tabs(["Model predictions perfomance", "Predict"])
    with tab1:
        X = dataframe.drop('resale_price', axis=1).values
        y = dataframe['resale_price'].values


        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)
        s_scaler = StandardScaler()
        X_train = s_scaler.fit_transform(X_train.astype(np.float64))
        X_test = s_scaler.transform(X_test.astype(np.float64))


        col1, col2 = st.columns([2, 1])
        with col1:
            regressor = LinearRegression()
            regressor.fit(X_train, y_train)

            # st.write("Intercept:",regressor.intercept_)
            # st.write("Coeff:",regressor.coef_)

            y_pred = regressor.predict(X_test)
            coeff_df = pd.DataFrame(regressor.coef_, dataframe.drop('resale_price', axis=1).columns, columns=['Coefficient'])

            y_pred = regressor.predict(X_test)
            df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
            # st.write('MAE:', metrics.mean_absolute_error(y_test, y_pred))
            # st.write('MSE:', metrics.mean_squared_error(y_test, y_pred))
            st.title("LinearRegression:")
            st.write('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
            # st.write('VarScore:', metrics.explained_variance_score(y_test, y_pred))
            st.write(df)

        with col2:
            knn = KNeighborsRegressor(algorithm='brute')
            knn.fit(X_train, y_train)
            predictions = knn.predict(X_test)

            mse = mean_squared_error(y_test, predictions)
            rmse = mse ** (1 / 2)
            st.title("K-Nearest Neighbour:")
            st.write('RMSE:',rmse)

            df = pd.DataFrame({'Actual': y_test, 'Predicted': predictions})
            df1 = df.head(20)
            st.write(df1)



    with tab2:
        with st.form("my_form"):
            col1, col2, col3 = st.columns([2, 1, 1])
            with col1:
                town = st.selectbox("Choose town",
                                    options=["ANG MO KIO", "BEDOK", "BISHAN", "BUKIT BATOK", "BUKIT MERAH",
                                             "BUKIT PANJANG",
                                             "BUKIT TIMAH", "CENTRAL AREA", "CHOA CHU KANG", "CLEMENTI", "GEYLANG",
                                             "HOUGANG",
                                             "JURONG EAST", "JURONG WEST", "KALLANG/WHAMPOA", "LIM CHU KANG",
                                             "MARINE PARADE",
                                             "PASIR RIS", "PUNGGOL", "QUEENSTOWN", "SEMBAWANG", "SENGKANG", "SERANGOON",
                                             "TAMPINES",
                                             "TOA PAYOH", "WOODLANDS", "YISHUN"], key=1)
                floor_area_sqm = st.slider("floor_area_sqm", min_value=28.0, max_value=307.0)
                lease_commence_date = st.slider("lease_commence_date", min_value=1966, max_value=2022)

            with col2:
                flat_type = st.selectbox("Choose town",
                                             options=['1 ROOM', '2 ROOM', '3 ROOM', '4 ROOM', '5 ROOM', 'EXECUTIVE',
                                                      'MULTI-GENERATION', 'MULTI GENERATION'])
                min_storey = st.slider("min_storey", min_value=1, max_value=49)



            submitted = st.form_submit_button("predict")




        if submitted:
            latitude = latitude[town]
            longitude = longitude[town]
            df={"town": town, "floor_area_sqm": floor_area_sqm,"lease_commence_date": lease_commence_date,
            "min_storey": min_storey,"flat_type":flat_type,"latitude":latitude,"longitude":longitude}
            dataframe=pd.DataFrame(df, index=[0])
            dataframe['town'] = dataframe['town'].replace(townDict, regex=True)
            dataframe['flat_type'] = dataframe['flat_type'].replace(flat_typeDict, regex=True)
            # s_scaler = StandardScaler()
            # X_test = s_scaler.fit_transform(dataframe.astype(np.float64))
            X_test=dataframe
            predictions = knn.predict(X_test)
            predictions=pd.DataFrame(predictions)
            st.write("Re-sale price:",predictions[0][0])


