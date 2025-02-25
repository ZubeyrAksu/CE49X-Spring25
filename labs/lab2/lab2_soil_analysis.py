import pandas as pd
import numpy as np

def load_data(file_path):
    """Load dataset and handle file not found error."""
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

def clean_data(df):
    """Handle missing values by filling with column mean."""
    df.fillna(df.mean(numeric_only=True), inplace=True)
    return df

def compute_statistics(df, column):
    """Compute and print descriptive statistics for a given column."""
    if column not in df.columns:
        print(f"Error: Column '{column}' not found in dataset.")
        return

    stats = {
        "Minimum": df[column].min(),
        "Maximum": df[column].max(),
        "Mean": df[column].mean(),
        "Median": df[column].median(),
        "Standard Deviation": df[column].std()
    }
    
    print(f"\nStatistics for '{column}':")
    for key, value in stats.items():
        print(f"{key}: {value:.2f}")

if __name__ == "__main__":
    file_path = "../../datasets/soil_test.csv"  # Adjust path if needed
    df = load_data(file_path)

    if df is not None:
        df = clean_data(df)
        compute_statistics(df, "soil_ph")  # Ensure column exists



