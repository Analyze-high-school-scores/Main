# Cleaning_data/cleaner.py
import pandas as pd
from Cleaning_data.config import DATA_FILE_PATH, TINH_FILE_PATH, CLEANED_DATA_PATH


def load_data():
    data_df = pd.read_csv(DATA_FILE_PATH)
    tinh_df = pd.read_csv(TINH_FILE_PATH)
    return data_df, tinh_df


def clean_data(data_df, tinh_df):
    # Merge the two datasets on 'MaTinh'
    merged_df = pd.merge(data_df, tinh_df, on="MaTinh", how="left")

    # Fill missing values in score columns with -1 to indicate missing scores
    score_columns = [
        "Toan",
        "Van",
        "Ly",
        "Sinh",
        "Ngoai ngu",
        "Hoa",
        "Lich su",
        "Dia ly",
        "GDCD",
    ]
    merged_df[score_columns] = merged_df[score_columns].fillna(-1)

    # Filter for rows where 'Year' is either 2018 or 2019
    merged_df = merged_df[merged_df["Year"].isin([2018, 2019])]

    # Drop rows where essential columns like 'SBD', 'Year', or 'MaTinh' are missing
    cleaned_df = merged_df.dropna(subset=["SBD", "Year", "MaTinh"])

    return cleaned_df


def save_cleaned_data(cleaned_df):
    cleaned_df.to_csv(CLEANED_DATA_PATH, index=False)
    print(f"Cleaned data saved to {CLEANED_DATA_PATH}")
