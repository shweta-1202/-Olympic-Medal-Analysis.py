# Olympic Medals Dashboard

This project provides a data analysis and visualization tool for Olympic medals data. It consists of several Python scripts that handle data reading, cleaning, exception handling, and visualization. The project also includes a Streamlit-based web application for interactive data exploration.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Modules](#modules)
   - [exception.py](#exceptionpy)
   - [file_handling.py](#file_handlingpy)
   - [datacleaning.py](#datacleaningpy)
   - [visualization.py](#visualizationpy)
   - [analysis.py](#analysispy)
4. [Streamlit Dashboard](#streamlit-dashboard)

## Installation

1. Install the required packages:
   pip install -r requirements.txt

## Usage
To run the data cleaning and saving script:
python analysis.py

To start the Streamlit dashboard:
streamlit run dashboard.py

## Modules

### `exception.py`

Defines custom exceptions for data cleaning errors.

#### Class `DataCleaningError`
- **Attributes**:
  - `message`: Error message.

### `file_handling.py`

Handles reading from and writing to CSV files.

#### Functions
- `read_csv(file_name)`: Reads a CSV file and returns a DataFrame.
- `write_csv(file_name, df)`: Writes a DataFrame to a CSV file.

### `datacleaning.py`

Contains functions for loading and cleaning data.

#### Functions
- `load_data(file_name)`: Loads a CSV file and returns a DataFrame, handling potential errors.
- `clean_data(df)`: Cleans the DataFrame by handling missing values and duplicates.

### `visualization.py`

Provides functions for visualizing the Olympic medals data using Matplotlib and Streamlit.

#### Functions
- `plot_medals_by_countries(df, countries)`: Plots the number of medals won by selected countries.
- `plot_medal_distribution(df)`: Plots the distribution of medal types (gold, silver, bronze).

### `analysis.py`

1. **Basic Data Cleaning and Saving**:
   - Imports required modules.
   - Reads a CSV file (`olympic_medals.csv`).
   - Cleans the data and handles exceptions.
   - Writes the cleaned data to a new CSV file (`clean_olympic_medals.csv`).

2. **Streamlit Dashboard**:
   - Sets up the Streamlit dashboard for interactive data exploration.
   - Loads and cleans the data.
   - Provides data overview and visualizations based on user-selected countries.

## Streamlit Dashboard

The Streamlit dashboard allows users to interactively explore the Olympic medals data. Users can:
- View a data overview.
- Select specific countries to visualize their medals.
- See additional plots, such as the distribution of medals by type.

To run the Streamlit dashboard, execute:
streamlit run dashboard.py
