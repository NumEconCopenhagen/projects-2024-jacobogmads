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