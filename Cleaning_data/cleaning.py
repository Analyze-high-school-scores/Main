import pandas as pd
import requests
from io import StringIO
from datetime import datetime, timedelta
import os

# Đường dẫn file
DATA_FILE_PATH = 'https://andyanh.id.vn/index.php/s/AQrkaif3HWgs9ke/download'
TINH_FILE_PATH = 'https://andyanh.id.vn/index.php/s/zbHTAjksBekNB4M/download'
CLEANED_DATA_PATH = "C:/Users/admin/Nextcloud4/andyanh/Data-Project-Student-Manager/Cleaning Data"
RAW_DATA_API = 'https://andyanh.id.vn/index.php/s/p7XMy828G8NKiZp/download'

def fetch_csv_from_api(api_url):
    cache_file = 'data_cache.csv' if 'p7XMy' in api_url else 'tinh_cache.csv'
    cache_timeout = timedelta(hours=24)
    
    if os.path.exists(cache_file):
        modified_time = datetime.fromtimestamp(os.path.getmtime(cache_file))
        if datetime.now() - modified_time < cache_timeout:
            print(f"Đang tải dữ liệu từ cache {cache_file}...")
            return pd.read_csv(cache_file)
    
    print(f"Đang tải dữ liệu từ API {api_url}...")
    response = requests.get(api_url)
    if response.status_code == 200:
        df = pd.read_csv(StringIO(response.text))
        df.to_csv(cache_file, index=False)
        return df
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")

def load_data(use_raw_data=False):
    data_file_path = RAW_DATA_API if use_raw_data else DATA_FILE_PATH
    data_df = fetch_csv_from_api(data_file_path)
    tinh_df = fetch_csv_from_api(TINH_FILE_PATH)
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

def main():
    # Hỏi người dùng về lựa chọn file dữ liệu
    choice = input("Bạn muốn dùng file nào để cleaning? (1: Update_Data, 2: Raw_Data): ")
    use_raw_data = choice.strip() == '2'

    try:
        # Load the data
        data_df, tinh_df = load_data(use_raw_data)

        # Clean the data
        cleaned_df = clean_data(data_df, tinh_df)

        # Save the cleaned data
        save_cleaned_data(cleaned_df)
        
    except Exception as e:
        print(f"Lỗi khi xử lý dữ liệu: {e}")
        print("Không thể xử lý dữ liệu. Vui lòng kiểm tra kết nối internet và thử lại.")
        exit()

if __name__ == "__main__":
    main() 