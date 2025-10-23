# COVID-19 Data Visualization Project

import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# 1️⃣ Load Dataset
df = pd.read_csv("covid_19_data.csv")

# 2️⃣ Clean and Prepare Data
df['ObservationDate'] = pd.to_datetime(df['ObservationDate'])
df.rename(columns={'Country/Region': 'Country'}, inplace=True)

# 3️⃣ Global Summary
global_summary = df.groupby('ObservationDate')[['Confirmed', 'Deaths', 'Recovered']].sum().reset_index()

# 4️⃣ Plot Global Trends (Matplotlib)
plt.figure(figsize=(12, 6))
plt.plot(global_summary['ObservationDate'], global_summary['Confirmed'], label='Confirmed')
plt.plot(global_summary['ObservationDate'], global_summary['Deaths'], label='Deaths')
plt.plot(global_summary['ObservationDate'], global_summary['Recovered'], label='Recovered')
plt.title('Global COVID-19 Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Cases')
plt.legend()
plt.grid(True)
plt.show()

# 5️⃣ Top 10 Affected Countries (Latest Date)
latest_date = df['ObservationDate'].max()
latest_data = df[df['ObservationDate'] == latest_date]
top_countries = latest_data.groupby('Country')['Confirmed'].sum().sort_values(ascending=False).head(10).reset_index()

# Bar Chart
plt.figure(figsize=(10, 5))
plt.barh(top_countries['Country'], top_countries['Confirmed'], color='orange')
plt.gca().invert_yaxis()
plt.title('Top 10 Countries by Confirmed Cases')
plt.xlabel('Confirmed Cases')
plt.show()

# 6️⃣ Interactive World Map (Plotly)
world_data = latest_data.groupby('Country')['Confirmed'].sum().reset_index()

fig = px.choropleth(
    world_data,
    locations='Country',
    locationmode='country names',
    color='Confirmed',
    hover_name='Country',
    color_continuous_scale='reds',
    title='COVID-19 Confirmed Cases Worldwide'
)
fig.show()

# 7️⃣ Country-wise Trend Example
country_name = "India"
india_data = df[df['Country'] == country_name].groupby('ObservationDate')[['Confirmed', 'Deaths', 'Recovered']].sum().reset_index()

plt.figure(figsize=(12, 6))
plt.plot(india_data['ObservationDate'], india_data['Confirmed'], label='Confirmed')
plt.plot(india_data['ObservationDate'], india_data['Deaths'], label='Deaths')
plt.plot(india_data['ObservationDate'], india_data['Recovered'], label='Recovered')
plt.title(f'COVID-19 Trend in {country_name}')
plt.xlabel('Date')
plt.ylabel('Number of Cases')
plt.legend()
plt.grid(True)
plt.show()
