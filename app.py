import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import streamlit as st

data = pd.read_csv("/home/hardick-harass/Documents/MLProjects/creditcard.csv")


legit = data[data.Class==0]
fraud = data[data['Class'] == 1]

legit_sample = legit.sample(n=81)
data =pd.concat([legit_sample,fraud],axis=0)


X = data.drop("Class",axis=1)
Y =  data["Class"]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

model = LogisticRegression()
model.fit(X_train,Y_train)
ypred =  model.predict(X_test)

accuracy_score(ypred,Y_test)

train_acc = accuracy_score(model.predict(X_train), Y_train)
test_acc =  accuracy_score(model.predict(X_test), Y_test)

#create strealit app
st.title("Credit Card Fraud Detection Model")
st.write("Enter the following features to check if the transaction is legitmate or fraudlent: ")

input_df = st.text_input('Input All features')
input_df_lst =  input_df.split(',')

submit = st.button("Submit")

if submit:
    features = np.array(input_df_lst, dtype=np.float64)
    prediction = model.predict(features.reshape(1, -1))

    if prediction[0] == 0:
        st.write("Legitimate transaction")

    else:
        st.write("Fraudulent transaction")