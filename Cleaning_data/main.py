# Cleaning_data/main.py
from Cleaning_data import cleaner


def main():
    # Load the data
    data_df, tinh_df = cleaner.load_data()

    # Clean the data
    cleaned_df = cleaner.clean_data(data_df, tinh_df)

    # Save the cleaned data
    cleaner.save_cleaned_data(cleaned_df)


if __name__ == "__main__":
    main()
