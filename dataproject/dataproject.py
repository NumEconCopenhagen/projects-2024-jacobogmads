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

# define the plot_e function
def plot_a(df, category1, category2): 
    # Filter the DataFrame for each category
    I1 = df['Category'] == category1
    I2 = df['Category'] == category2
    
    # Initialize the plot with specified figure size
    plt.figure(figsize=(20, 12))
    
    # Plot the first category
    plt.plot(df.loc[I1, 'year'], df.loc[I1, 'Value'], '-o', label=category1)
    
    # Plot the second category on the same axes
    plt.plot(df.loc[I2, 'year'], df.loc[I2, 'Value'], '-o', label=category2, color='red')

    # Add a vertical line at year 2015
    plt.axvline(2015, color='black', linestyle='--', linewidth=0.5, label='Index 2015=100')
    
    # Enhance the plot with legend, labels, and title
    plt.legend()
    plt.xlabel('year')
    plt.ylabel('Value')
    plt.title('Comparative Plot of Categories')
    
    # Show the plot
    plt.show()



def plot_c(df1, df2, category, vehicle):
    # Filter each DataFrame for the specified category
    I1 = df1['Category'] == category
    I2 = df2['vehicle'] == vehicle
    
    # Initialize the plot with specified figure size
    plt.figure(figsize=(20, 12))
    
    # Plot the first category from the first dataframe
    plt.plot(df1.loc[I1, 'year'], df1.loc[I1, 'Value'], '-o', label=f'{category} (DF1)')
    
    # Plot the second category from the second dataframe
    plt.plot(df2.loc[I2, 'year'], df2.loc[I2, 'personkm_pr_cap'], '-o', label=f'{vehicle} (DF2)', color='red')

    # Add a vertical line at year 2015
    plt.axvline(2015, color='black', linestyle='--', linewidth=0.5, label='Index 2015=100')
    
    # Enhance the plot with legend, labels, and title
    plt.legend()
    plt.xlabel('year')
    plt.ylabel('Index')
    plt.title('Comparative Plot of Categories from Different DataFrames')
    
    # Show the plot
    plt.show()