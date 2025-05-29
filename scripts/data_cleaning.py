import pandas as pd

def load_and_clean_data():
    # Full path to the Excel file
    filepath = r"C:\Users\shrav\OneDrive\Desktop\sustainable-supply-chains-esg-analysis\data\P_Data_Extract_From_Environment_Social_and_Governance_(ESG)_Data (1).xlsx"
    
    # Load Excel file
    df = pd.read_excel(filepath, engine='openpyxl')
    
    # Basic cleaning: Drop completely empty rows/columns
    df.dropna(how='all', inplace=True)
    df.dropna(axis=1, how='all', inplace=True)

    # Example: fill missing values (customize as needed)
    df.fillna(method='ffill', inplace=True)

    return df

# Example usage
if __name__ == "__main__":
    df = load_and_clean_data()
    print(df.head())
