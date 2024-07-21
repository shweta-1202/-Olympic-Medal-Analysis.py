import matplotlib.pyplot as plt
import streamlit as st

def plot_medals_by_countries(df, countries):
    """
    Plots the number of medals won by selected countries.

    Parameters:
    - df: DataFrame containing the data
    - countries: List of countries (strings) to plot
    """
    df_selected = df[df['country_name'].isin(countries)]
    if df_selected.empty:
        st.warning("No data found for the selected countries.")
        return
    
    plt.figure(figsize=(10, 6))
    df_selected.groupby('country_name')['medal_type'].value_counts().unstack().plot(kind='bar')
    plt.title('Medals by Countries')
    plt.xlabel('Country')
    plt.ylabel('Number of Medals')
    plt.xticks(rotation=45)
    plt.legend(title='Medal Type')
    # plt.tight_layout()

    # Use st.pyplot() to render the plot in Streamlit
    st.pyplot(plt)


def plot_medal_distribution(df):
    """
    Plots the distribution of medal types (gold, silver, bronze).

    Parameters:
    - df: DataFrame containing the data
    """
    plt.figure(figsize=(8, 5))
    df['medal_type'].value_counts().plot(kind='pie', autopct='%1.1f%%')
    plt.title('Medal Distribution')
    plt.ylabel('')  
    st.pyplot(plt)
