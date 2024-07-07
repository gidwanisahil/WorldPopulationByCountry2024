import pandas as pd

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

# Now you can proceed to train your model
from sklearn.linear_model import LinearRegression

X = df[['Population 2023', 'Area (km2)', 'Density (/km2)', 'Growth Rate', 'World %', 'World Rank']]
y = df['Population 2024']

model = LinearRegression()
model.fit(X, y)

# Example prediction
prediction = model.predict([[1428627663, 3e6, 485.0, 0.0092, 0.1801, 1]])
print(f'Predicted Population in 2024: {prediction[0]}')
