# Cleaning_data/main.py
from Cleaning_data import cleaner


def main():
    # Hỏi người dùng về lựa chọn file dữ liệu
    choice = input("Bạn muốn dùng file nào để cleaning? (1: Update_Data, 2: Raw_Data): ")
    use_raw_data = choice.strip() == '2'

    # Load the data
    data_df, tinh_df = cleaner.load_data(use_raw_data)

    # Clean the data
    cleaned_df = cleaner.clean_data(data_df, tinh_df)

    # Save the cleaned data
    cleaner.save_cleaned_data(cleaned_df)


if __name__ == "__main__":
    main()
