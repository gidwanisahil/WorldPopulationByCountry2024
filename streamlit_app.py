import streamlit as st
import pandas as pd
import re
import plotly.express as px
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('population data.csv')

# Function to convert area to numeric, handling cases like '3M'
def convert_area(area):
    if isinstance(area, str):
        area = area.replace(',', '').replace(' ', '')
        if 'M' in area:
            return float(area.replace('M', '')) * 1_000_000
        elif 'K' in area:
            return float(area.replace('K', '')) * 1_000
        else:
            return float(re.sub(r'[^\d.]', '', area))
    return float(area)

# Apply the conversion function to the 'Area (km2)' column
df['Area (km2)'] = df['Area (km2)'].apply(convert_area)

# Fill missing values in 'World %'
df['World %'] = df['World %'].fillna(df['World %'].mean())

# Convert columns to appropriate data types
df['Population 2024'] = pd.to_numeric(df['Population 2024'], errors='coerce').astype('Int64')  # Handle missing values
df['Population 2023'] = pd.to_numeric(df['Population 2023'], errors='coerce').astype('Int64')  # Handle missing values
df['Density (/km2)'] = pd.to_numeric(df['Density (/km2)'], errors='coerce')
df['Growth Rate'] = pd.to_numeric(df['Growth Rate'], errors='coerce')
df['World %'] = pd.to_numeric(df['World %'], errors='coerce')

# Ensure Growth Rate values are non-negative for visualization
df['Growth Rate'] = df['Growth Rate'].abs()

# Streamlit app code to display the processed data
st.title('Population Data Analysis')

# Display data types
st.write("### Data Types")
st.write(df.dtypes)

# Display processed data
st.write("### Processed Data")
st.write(df.head())

# Function to convert area to numeric, handling cases like '3M'
def convert_area(area):
    if isinstance(area, str):
        area = area.replace(',', '').replace(' ', '')
        if 'M' in area:
            return float(area.replace('M', '')) * 1_000_000
        elif 'K' in area:
            return float(area.replace('K', '')) * 1_000
        else:
            return float(re.sub(r'[^\d.]', '', area))
    return float(area)


# Load the dataset
df = pd.read_csv('population data.csv')

# Apply the conversion function to the 'Area (km2)' column
df['Area (km2)'] = df['Area (km2)'].apply(convert_area)

# Fill missing values in 'World %'
df['World %'] = df['World %'].fillna(df['World %'].mean())

# Ensure correct data types
df['Population 2024'] = df['Population 2024'].astype(int)
df['Population 2023'] = df['Population 2023'].astype(int)
df['Area (km2)'] = df['Area (km2)'].astype(float)
df['Density (/km2)'] = df['Density (/km2)'].astype(float)
df['Growth Rate'] = df['Growth Rate'].astype(float)
df['World %'] = df['World %'].astype(float)
df['World Rank'] = df['World Rank'].astype(int)

# Ensure Growth Rate values are non-negative for visualization
df['Growth Rate'] = df['Growth Rate'].abs()

# Streamlit app code to display the processed data and plot
st.title('Population Data Analysis')

# Display data types
st.write("### Data Types")
st.write(df.dtypes)

# Display processed data
st.write("### Processed Data")
st.write(df.head())

# Create 3D scatter plot using Plotly Express
fig = px.scatter_3d(df, 
                    x='Area (km2)', 
                    y='Population 2024', 
                    z='Density (/km2)', 
                    color='World %', 
                    size='Growth Rate', 
                    hover_name='Country', 
                    title='3D Visualization of Population Data')

# Display the plot in Streamlit
st.plotly_chart(fig)


# Load the dataset
df = pd.read_csv('population data.csv')

# Streamlit app code to display the processed data and plot
st.title('Population Data Analysis')

# Display data types
st.write("### Data Types")
st.write(df.dtypes)

# Display processed data
st.write("### Processed Data")
st.write(df.head())

# Create choropleth map using Plotly Express
fig = px.choropleth(df, 
                    locations="Country", 
                    locationmode='country names',
                    color="Population 2024", 
                    hover_name="Country", 
                    title="World Population Map 2024",
                    projection="natural earth")

# Display the choropleth map in Streamlit
st.plotly_chart(fig)


# Extract relevant columns for time series analysis
time_series_data = df[['Country', 'Population 2023', 'Population 2024']]

# Melt the dataframe to convert it to long format for easier plotting
time_series_data_melted = pd.melt(time_series_data, id_vars=['Country'], 
                                  var_name='Year', value_name='Population')

# Convert 'Year' column to integer for correct sorting and plotting
time_series_data_melted['Year'] = time_series_data_melted['Year'].str.split().str[-1].astype(int)

# Sort by 'Country' and 'Year' for consistent plotting
time_series_data_melted = time_series_data_melted.sort_values(by=['Country', 'Year'])

# Streamlit app code to display the processed data and plot
st.title('Population Trends Over Time (2023-2024)')

# Display data types
st.write("### Data for Time Series Analysis")
st.write(time_series_data_melted.head())

# Plotting using Plotly
fig = px.line(time_series_data_melted, x='Year', y='Population', color='Country',
              line_group='Country', hover_name='Country',
              title='Population Trends Over Time (2023-2024)',
              labels={'Population': 'Population Count', 'Year': 'Year'})

# Display the plot in Streamlit
st.plotly_chart(fig)


# Function to convert area to numeric, handling cases like '3M', '770.9K', '< 1', etc.
def convert_area(area):
    if isinstance(area, str):
        area = area.replace(',', '').replace(' ', '')
        if 'M' in area:
            return float(area.replace('M', '')) * 1_000_000
        elif 'K' in area:
            return float(area.replace('K', '')) * 1_000
        elif '<' in area:
            return 0  # Handle cases like '< 1' as 0
        else:
            try:
                return float(re.sub(r'[^\d.]', '', area))
            except ValueError:
                return None  # Return None for cases that can't be converted
    return float(area)
# Apply the conversion function to the 'Area (km2)' column
df['Area (km2)'] = df['Area (km2)'].apply(convert_area)

# Streamlit app code
st.title('Population Data Analysis')

# Display the processed dataframe
st.write("### Processed Data")
st.write(df)

# Calculate summary statistics (example)
summary_stats = df[['Population 2023', 'Population 2024', 'Area (km2)', 'Density (/km2)']].describe()

# Display summary statistics
st.write("### Summary Statistics:")
st.write(summary_stats)

correlation_matrix = df[['Population 2023', 'Population 2024', 'Area (km2)', 'Density (/km2)', 'Growth Rate']].corr()
