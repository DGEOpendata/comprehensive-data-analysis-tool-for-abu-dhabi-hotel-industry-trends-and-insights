python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'Abu_Dhabi_Hotels_Open_Dataset.xlsx'
df = pd.read_excel(file_path, sheet_name='Hotel Occupancy Rates by Month and Zone')

# Data cleaning and preparation
df['Month'] = pd.to_datetime(df['Month'], format='%Y-%m')
df = df.sort_values(by='Month')

# Example Analysis: Average Occupancy Rate by Zone
zone_avg_occupancy = df.groupby('Zone')['Occupancy Rate'].mean().reset_index()

# Plotting the average occupancy rate by zone
plt.figure(figsize=(10, 6))
sns.barplot(data=zone_avg_occupancy, x='Zone', y='Occupancy Rate', palette='viridis')
plt.title('Average Hotel Occupancy Rate by Zone')
plt.xlabel('Zone')
plt.ylabel('Average Occupancy Rate')
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
plt.savefig('average_occupancy_rate_by_zone.png')
plt.show()

# Filter data for a specific year and zone
year = 2023
zone = 'Downtown'
filtered_data = df[(df['Month'].dt.year == year) & (df['Zone'] == zone)]

# Plotting monthly occupancy rate for the selected year and zone
plt.figure(figsize=(12, 6))
sns.lineplot(data=filtered_data, x='Month', y='Occupancy Rate', marker='o', label=zone)
plt.title(f'Monthly Occupancy Rate for {zone} in {year}')
plt.xlabel('Month')
plt.ylabel('Occupancy Rate')
plt.legend()
plt.grid()
plt.tight_layout()

# Save the plot
plt.savefig(f'monthly_occupancy_rate_{year}_{zone}.png')
plt.show()
