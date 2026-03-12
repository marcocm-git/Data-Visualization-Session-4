import streamlit as st
import pandas as pd

st.title("Exercise 3")

st.title("Titanic Survivors by Age")

df = pd.read_csv('titanic.csv')
df_clean = df.dropna(subset=['Age'])

age_range = st.slider(
    "Select Age Range",
    min_value=int(df_clean['Age'].min()),
    max_value=int(df_clean['Age'].max()),
    value=(int(df_clean['Age'].min()), int(df_clean['Age'].max()))
)

df_filtered = df_clean[(df_clean['Age'] >= age_range[0]) & (df_clean['Age'] <= age_range[1])]

survivors_by_age = df_filtered.groupby('Age')['Survived'].sum().reset_index()
survivors_by_age.columns = ['Age', 'Number of Survivors']

st.subheader("Number of Survivors by Age")
st.bar_chart(survivors_by_age.set_index('Age'))

st.subheader("Statistics")
total_passengers = len(df_filtered)
total_survivors = df_filtered['Survived'].sum()
st.write(f"**Total Passengers in selected age range:** {total_passengers}")
st.write(f"**Total Survivors in selected age range:** {total_survivors}")
st.write(f"**Survival Rate:** {(total_survivors/total_passengers*100):.1f}%")

