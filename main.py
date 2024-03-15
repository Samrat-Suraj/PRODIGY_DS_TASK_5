import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random
import plotly.express as px

# Load Dataset
Accidents = pd.read_csv("RTA Dataset.csv")

# Function to handle missing values and encode categorical variables
def preprocess_data(df):
    # Fill missing values
    df.fillna({'Accident_severity': 'Unknown', 'Age_band_of_driver': 'Unknown'}, inplace=True)
    # Encode categorical variables
    categorical_cols = ['Road_surface_conditions', 'Weather_conditions', 'Accident_severity', 'Age_band_of_driver',
                        'Day_of_week', 'Educational_level', 'Types_of_Junction', 'Number_of_vehicles_involved']
    for col in categorical_cols:
        df[col] = df[col].astype('category').cat.codes
    return df

# Preprocess the data
Accidents = preprocess_data(Accidents)

# Time of Day Analysis
Accidents['Time'] = pd.to_datetime(Accidents['Time'])
Accidents['Hour'] = Accidents['Time'].dt.hour
time_of_day_counts = Accidents['Hour'].value_counts().sort_index()
plt.figure(figsize=(12, 6))
plt.bar(time_of_day_counts.index, time_of_day_counts.values, color='skyblue')
plt.xlabel('Hour of the Day')
plt.ylabel('Accident Count')
plt.title('Accidents by Time of Day')
plt.show()

# Road Condition Analysis
plt.figure(figsize=(10, 6))
sns.countplot(x='Road_surface_conditions', data=Accidents, palette='pastel')
plt.xticks(rotation=45)
plt.xlabel('Road Conditions')
plt.ylabel('Accident Count')
plt.title('Accidents by Road Conditions')
plt.show()

# Weather Analysis
plt.figure(figsize=(10, 6))
sns.countplot(x='Weather_conditions', data=Accidents, palette='pastel')
plt.xticks(rotation=45)
plt.xlabel('Weather Conditions')
plt.ylabel('Accident Count')
plt.title('Accidents by Weather Conditions')
plt.show()

# Function to create interactive subplots
def interactive_subplots(df, category_cols, ncols=3):
    nrows = (len(category_cols) + ncols - 1) // ncols
    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(18, 6 * nrows))
    for i, col in enumerate(category_cols):
        sns.countplot(data=df, x=col, ax=axes[i // ncols, i % ncols], palette='pastel')
        axes[i // ncols, i % ncols].set_title(f'Accidents by {col}')
        axes[i // ncols, i % ncols].set_xlabel(col)
        axes[i // ncols, i % ncols].set_ylabel('Accident Count')
        axes[i // ncols, i % ncols].tick_params(axis='x', rotation=45)
    plt.tight_layout()
    plt.show()

# Plot interactive subplots for categorical variables
category_cols = ['Accident_severity', 'Age_band_of_driver', 'Day_of_week', 'Educational_level', 'Types_of_Junction', 'Number_of_vehicles_involved']
interactive_subplots(Accidents, category_cols)

# Contributing Factors Analysis (Interactive Plot)
contributing_factors_counts = Accidents['Cause_of_accident'].value_counts()
fig = px.bar(x=contributing_factors_counts.index, y=contributing_factors_counts.values, labels={'x': 'Contributing Factors', 'y': 'Accident Count'},
             title='Contributing Factors to Accidents')
fig.update_layout(xaxis_tickangle=-45, plot_bgcolor='rgba(0, 0, 0, 0)')
fig.show()

# Defect in Vehicles (Interactive Plot)
defect_count = Accidents['Defect_of_vehicle'].value_counts()
fig = px.bar(x=defect_count.index, y=defect_count.values, labels={'x': 'Defect', 'y': 'Accident Count'},
             title='Defect in Vehicles')
fig.update_layout(xaxis_tickangle=-45, plot_bgcolor='rgba(0, 0, 0, 0)')
fig.show()

# Light Conditions (Interactive Plot)
light_count = Accidents['Light_conditions'].value_counts()
fig = px.bar(x=light_count.index, y=light_count.values, labels={'x': 'Light Conditions', 'y': 'Accident Count'},
             title='Light Conditions')
fig.update_layout(xaxis_tickangle=-45, plot_bgcolor='rgba(0, 0, 0, 0)')
fig.show()

# Driving Experience Analysis
plt.figure(figsize=(10, 6))
sns.countplot(x='Driving_experience', data=Accidents, palette='pastel')
plt.xticks(rotation=45)
plt.xlabel('Experience')
plt.ylabel('Accident Count')
plt.title('Accidents by Driving Experience')
plt.show()

# Age band of Casualty (Interactive Plot)
age_counts = Accidents['Age_band_of_casualty'].value_counts()
fig = px.bar(x=age_counts.index, y=age_counts.values, labels={'x': 'Casualty Age', 'y': 'Accident Count'},
             title='Casualty by Age Band')
fig.update_layout(xaxis_tickangle=-45, plot_bgcolor='rgba(0, 0, 0, 0)')
fig.show()
