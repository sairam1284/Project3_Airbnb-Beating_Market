import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split
import folium
from folium.plugins import MarkerCluster
import seaborn as sns

st.title('Getting the most out of your Airbnb')
# Load some data


# Create a text element and let the reader know the data is loading.
#st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
df = pd.read_pickle('cleaned_full_dataframe.pkl')


cmap = sns.cubehelix_palette(rot=-.2, as_cmap=True)

fig, ax = plt.subplots(figsize=(12,7))
ax = sns.scatterplot(x="accommodates", y="price", sizes=(5, 400), size='monthly_cash_flow', hue='monthly_cash_flow',
                      palette=cmap,  data=df)

plt.title('\nEffect of Accommodation Bedrooms on Monthly Cash Flow \n', fontsize=14, fontweight='bold')

# putting legend out of the plot
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.);

st.write(fig)


st.write(df.sample(5))


#st.map(df.sample(1000))

#
# feat3 = ['accommodates', 'bathrooms', 'bedrooms', 'price', 'cleaning_fee','guests_included', 'distance(km)',
#          'size', 'beds','review_scores_rating', 'host_is_superhost', 'amen_patio', 'amen_dryer',
#          'amen_parking', 'amen_tv', 'count_amenities',
#          'host_response_time_within an hour',
#          'cancellation_policy_flexible', 'room_type_Entire home/apt', 'len_desc', 'len_space',
#          'neighbourhood_labels']
# X = df[feat3]
# y = df['target']
# X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=12)


feat_test = ['accommodates', 'bathrooms','distance(km)', 'bedrooms', 'size', 'room_type_Entire home/apt', 'price', 'neighbourhood_labels',
'review_scores_rating', 'len_desc', 'len_space']
X1 = df[feat_test]
y1 = df['target']
#X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, random_state=12)


rfc = RandomForestClassifier(n_estimators=60)
rfc = rfc.fit(X1, y1)
# pred_te = rfc.predict(X1_test)
# accuracy = metrics.accuracy_score(y1_test, pred_te)
# precision = metrics.precision_score(y1_test, pred_te)
# recall = metrics.recall_score(y1_test, pred_te)

st.sidebar.write('## Modeling Inputs')
st.sidebar.write('### Factors you cannot control')

bathrooms = st.sidebar.number_input('Number of bathrooms', value=1)
rooms = st.sidebar.number_input('Number of bedrooms', value=2)
sqrm = 75
distance = st.sidebar.number_input('Distance to City Center(km)', value = 2)
home_type = 1 #st.selectbox('What kind of Home',('Entire Home', 'Private Room'))
neighbourhood_labels = 4 #This is Mitte which is Downtown

st.sidebar.write('## Things you have control over')
# rooms = st.number_input('Number of Bedrooms', value=2)
accom = st.sidebar.number_input('How many people does it accommodate', value=5)
price = st.sidebar.number_input('How much are you charging', value=100)
review_scores_rating = 95
len_desc = st.sidebar.number_input('How long is your description', value=100)
len_space = 100

input_data = pd.DataFrame({'accommodates': [accom], 'bathrooms': [bathrooms],'distance(km)': [distance],
'bedrooms': [rooms], 'size': [sqrm], 'room_type': [home_type], 'price': [price],
'neighbourhood_labels': [neighbourhood_labels], 'review_scores_rating': [review_scores_rating],
'len_desc': [len_desc], 'len_space':[len_space]})

pred = rfc.predict(input_data)[0]
pred_prob = rfc.predict_proba(input_data)[0]
st.write(
# f'Predicted Sale Price of House: {pred}, {pred_prob}'
)

if pred==1:
    st.write(f'## You have a {pred_prob[1]*100:.1f}% probability of beating the market!!')
else:
    st.write(f'## There is a {pred_prob[0]*100:.1f}% that you are not doing quite as good as the average.  See if you can tweak some parameters to increase your profits!')
