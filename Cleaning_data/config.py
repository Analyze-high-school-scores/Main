# Cleaning_data/config.py
import requests
import pandas as pd
from io import StringIO

# Đường dẫn file
DATA_FILE_PATH = 'https://andyanh.id.vn/index.php/s/AQrkaif3HWgs9ke/download'
TINH_FILE_PATH = 'https://andyanh.id.vn/index.php/s/zbHTAjksBekNB4M/download'
CLEANED_DATA_PATH = "C:/Users/admin/Nextcloud4/andyanh/Data-Project-Student-Manager/Cleaning Data" # dùng địa chỉ thư mục này để đẩy thẳng vào cloud

def fetch_csv_from_api(api_url):
    from datetime import datetime, timedelta
    import os
    
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

# Tải dữ liệu từ API
try:
    data_df = fetch_csv_from_api(DATA_FILE_PATH)
    tinh_df = fetch_csv_from_api(TINH_FILE_PATH)
    print("Đã tải dữ liệu thành công từ API")
except Exception as e:
    print(f"Lỗi khi tải dữ liệu từ API: {e}")
    print("Không thể tải dữ liệu. Vui lòng kiểm tra kết nối internet và thử lại.")
    exit()

