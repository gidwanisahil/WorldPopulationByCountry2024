import pandas as pd
import streamlit as st
from sklearn.linear_model import LinearRegression

# Load your dataset
file_path = 'population_data.csv'
df = pd.read_csv(file_path)

# Function to convert 'Area (km2)' to numeric
def convert_to_numeric(value):
    try:
        # Handle 'M' for million
        if 'M' in value:
            return float(value.replace('M', '')) * 1e6
        else:
            return float(value)
    except ValueError:
        # Handle unexpected or non-convertible values
        return None  # Or handle as appropriate (e.g., return a default value)

# Apply conversion function to 'Area (km2)' column
df['Area (km2)'] = df['Area (km2)'].apply(convert_to_numeric)

# Convert other numeric columns to numeric type
df['Population 2023'] = pd.to_numeric(df['Population 2023'], errors='coerce')
df['Population 2024'] = pd.to_numeric(df['Population 2024'], errors='coerce')
df['Density (/km2)'] = pd.to_numeric(df['Density (/km2)'], errors='coerce')
df['Growth Rate'] = pd.to_numeric(df['Growth Rate'], errors='coerce')
df['World %'] = pd.to_numeric(df['World %'], errors='coerce')
df['World Rank'] = pd.to_numeric(df['World Rank'], errors='coerce')

# Drop rows with missing values
df.dropna(inplace=True)

# Train the model
X = df[['Population 2023', 'Area (km2)', 'Density (/km2)', 'Growth Rate', 'World %', 'World Rank']]
y = df['Population 2024']
model = LinearRegression()
model.fit(X, y)

# Streamlit app
st.title('Population Prediction for 2024')

# Explain the input fields
st.write("""
### Enter the details below to predict the population for 2024:
- **Population 2023**: The population of the country in 2023.
- **Area (km2)**: The area of the country in square kilometers.
- **Density (/km2)**: The population density of the country (population per square kilometer).
- **Growth Rate**: The annual population growth rate.
- **World %**: The percentage of the world's population that resides in this country.
- **World Rank**: The country's rank in terms of population size.
""")

# Input fields for user to enter data
population_2023 = st.number_input('Population 2023', value=1428627663)
area_km2 = st.number_input('Area (km2)', value=3e6)
density_km2 = st.number_input('Density (/km2)', value=485.0)
growth_rate = st.number_input('Growth Rate', value=0.0092)
world_percentage = st.number_input('World %', value=0.1801)
world_rank = st.number_input('World Rank', value=1)

# Explain the prediction process
st.write("""
### How the Prediction Works:
When you click the 'Predict Population for 2024' button, the model will use the input values to estimate the population for 2024 based on the linear regression model trained on historical data.
""")

# Prediction button
if st.button('Predict Population for 2024'):
    input_data = pd.DataFrame([[population_2023, area_km2, density_km2, growth_rate, world_percentage, world_rank]],
                              columns=['Population 2023', 'Area (km2)', 'Density (/km2)', 'Growth Rate', 'World %', 'World Rank'])
    prediction = model.predict(input_data)
    st.write(f'Predicted Population in 2024: {prediction[0]:,.0f}')
    
    # Explain the result
    st.write("""
    ### Prediction Result:
    The predicted population for 2024 is displayed above. This prediction is based on the linear regression model which considers the provided input values to estimate the future population.
    """)
