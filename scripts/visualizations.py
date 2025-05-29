import matplotlib.pyplot as plt
import seaborn as sns

def plot_column_distribution(df, column_name):
    """
    Plots the distribution of a specific column in the dataframe using seaborn.

    Parameters:
    df (pd.DataFrame): The input DataFrame
    column_name (str): The column name to visualize
    """
    plt.figure(figsize=(10, 6))
    sns.histplot(df[column_name].dropna(), kde=True)
    plt.title(f'Distribution of ESG Data for {column_name}')
    plt.xlabel(column_name)
    plt.ylabel('Frequency')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
