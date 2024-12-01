import pandas as pd
import requests
from io import StringIO
from datetime import datetime, timedelta
import os

# Đường dẫn files
cleaned_file_path = "https://andyanh.id.vn/index.php/s/psPTAMbDrzzMnWk/download"
Summary_Result_By_Year = "https://andyanh.id.vn/index.php/s/49ZJgJxeMe5GfSA/download"


def fetch_csv_from_api(api_url, cache_name):
    cache_file = f"{cache_name}_cache.csv"
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
        raise Exception(f"Không thể tải dữ liệu: {response.status_code}")


# Tải dữ liệu với cache
try:
    df = fetch_csv_from_api(cleaned_file_path, "cleaned_data")
    df_2 = fetch_csv_from_api(Summary_Result_By_Year, "summary_data")
    print("Đã tải dữ liệu thành công")

    # Lọc dữ liệu theo năm
    df_years = {2018: df[df["Year"] == 2018], 2019: df[df["Year"] == 2019]}
except Exception as e:
    print(f"Lỗi khi tải dữ liệu: {e}")
    print("Không thể tải dữ liệu. Vui lòng kiểm tra kết nối internet và thử lại.")
    exit()
cached = "cleaned_data_cache.csv"
history_file="history.csv"
def save_history(row, status):
    """
    Ghi lại thông tin dòng bị xóa hoặc cập nhật vào file CSV.
    :param row: Dòng dữ liệu (Series) từ DataFrame.
    :param status: Trạng thái thay đổi (Ví dụ: "XÓA", "CẬP NHẬT").
    """
    # Sao chép dòng để tránh cảnh báo SettingWithCopyWarning
    row_copy = row.copy()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Thêm các cột mới vào bản sao
    row_copy["TrangThai"] = status
    row_copy["Timestamp"] = timestamp
    
    # Tạo một DataFrame từ bản sao
    history_df = pd.DataFrame([row_copy])
    
    try:
        # Đọc dữ liệu cũ từ file CSV
        existing_data = pd.read_csv(history_file)
        
        # Gộp dữ liệu mới với dữ liệu cũ
        history_df = pd.concat([existing_data, history_df], ignore_index=True)
    except FileNotFoundError:
        # Nếu file không tồn tại, tạo mới
        print(f"File '{history_file}' không tồn tại. Tạo file mới.")
    
    # Ghi lại dữ liệu vào file CSV
    history_df.to_csv(history_file, index=False)
    print(f"Lịch sử đã được ghi vào file '{history_file}'.")

print(df.dtypes)
