# defining the index function
def index_to_year(df, base_year):
    # Find the column name that matches the base year
    base_year_column = base_year
    
    # Make sure that the base year exists in the DataFrame
    if base_year_column not in df.columns:
        raise ValueError(f"Base year {base_year} not found in DataFrame columns")
    
    # Set the index to 'Category' if it's not already set
    if df.index.name != 'Category':
        df = df.set_index('Category')
    
    # Rebase each row to the base year
    df = df.divide(df[base_year_column], axis=0) * 100
    
    # Reset index to move 'Category' back to a column
    df.reset_index(inplace=True)
    
    return df

import matplotlib.pyplot as plt
import pandas as pd

# define the plot_e function
def plot_e(df, category1, category2): 
    # Filter the DataFrame for each category
    I1 = df['Category'] == category1
    I2 = df['Category'] == category2
    
    # Initialize the plot with specified figure size
    plt.figure(figsize=(20, 12))
    
    # Plot the first category
    plt.plot(df.loc[I1, 'Date'], df.loc[I1, 'Value'], '-o', label=category1)
    
    # Plot the second category on the same axes
    plt.plot(df.loc[I2, 'Date'], df.loc[I2, 'Value'], '-o', label=category2, color='red')

    # Add a vertical line at year 2015
    plt.axvline(2015, color='black', linestyle='--', linewidth=0.5, label='Index 2015=100')
    
    # Enhance the plot with legend, labels, and title
    plt.legend()
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.title('Comparative Plot of Categories')
    
    # Show the plot
    plt.show()