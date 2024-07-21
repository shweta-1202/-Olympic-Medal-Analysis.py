import streamlit as st
import file_handling
import data_cleaning
import visualization

def load_and_clean_data():
    df = file_handling.read_csv('olympic_medals.csv')
    df = data_cleaning.clean_data(df)
    return df

def main():
    st.title("Olympic Medals Dashboard")
    
    # Load and clean data
    df = load_and_clean_data()

    st.header("Data Overview")
    st.write(df.head())

    selected_countries = st.multiselect("Select countries", df['country_name'].unique())

    # Button to trigger visualization
    if st.button("Visualize Medals"):
        if selected_countries:
            # Filter data based on selected countries
            filtered_df = df[df['country_name'].isin(selected_countries)]
            
            st.header("Medals by Selected Countries")
            
            # Plotting medals by selected countries using visualization function
            visualization.plot_medals_by_countries(filtered_df, selected_countries)
        else:
            st.warning("Please select one or more countries.")
    
    # Additional plots based on user selection or default display
    st.header("Additional Plots")
    # Plot medal distribution
    st.subheader("Medal Distribution")
    visualization.plot_medal_distribution(df)

main()
