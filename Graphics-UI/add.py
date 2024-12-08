from tkinter import *
from tkinter import messagebox
from data import cached,df,save_history
import pandas as pd
from datetime import datetime
def create_add_window(parent):
    """
    Hàm tạo cửa sổ con để thêm một dòng dữ liệu mới.
    :param parent: Cửa sổ chính (root)
    """
    # Tạo cửa sổ con
    add_window = Toplevel(parent)
    add_window.title("Thêm Dữ Liệu Mới")
    add_window.geometry("400x500")

    # Hàm thêm dữ liệu vào DataFrame
    def add_entry():
        global df  # Sử dụng biến toàn cục df
        # Lấy giá trị từ các ô nhập liệu
        sbd = entry_sbd.get().strip()
        year = entry_year.get().strip()
        ma_tinh = entry_ma_tinh.get().strip()
        ten_tinh = entry_ten_tinh.get().strip()
        
        # Kiểm tra đầu vào
        if not sbd or not year or not ma_tinh or not ten_tinh:
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin!", parent=add_window)
            return

        try:
            sbd = int(sbd)  # Chuyển đổi SBD sang int
            year = int(year)  # Chuyển đổi Year sang int
            ma_tinh = int(ma_tinh)  # Mã tỉnh là kiểu int
        except ValueError:
            messagebox.showerror("Lỗi", "Số báo danh, Năm và Mã tỉnh phải là số!", parent=add_window)
            return
        if not df[(df["SBD"] == sbd) & (df["Year"] == year)].empty:
            messagebox.showerror("Lỗi", f"Số báo danh {sbd} cho năm {year} đã tồn tại!", parent=add_window)
            return

        # Lấy các điểm mới từ các ô nhập
        new_toan = entry_toan.get().strip()
        new_van = entry_van.get().strip()
        new_ly = entry_ly.get().strip()
        new_sinh = entry_sinh.get().strip()
        new_ngoai_ngu = entry_ngoai_ngu.get().strip()
        new_hoa = entry_hoa.get().strip()
        new_lich_su = entry_lich_su.get().strip()
        new_dia_ly = entry_dia_ly.get().strip()
        new_gdcd = entry_gdcd.get().strip()

        # Kiểm tra và chuyển đổi các điểm thi, nếu không có điểm thì mặc định là NaN
        def convert_to_float(value):
            try:
                diem = float(value)
                return diem if diem >= 0 else -1
            except ValueError:
                return -1
        # Tạo dictionary mới với dữ liệu người dùng nhập
        new_data = {
            "SBD": sbd,
            "Toan": convert_to_float(new_toan),
            "Van": convert_to_float(new_van),
            "Ly": convert_to_float(new_ly),
            "Sinh": convert_to_float(new_sinh),
            "Ngoai ngu": convert_to_float(new_ngoai_ngu),
            "Year": year,
            "Hoa": convert_to_float(new_hoa),
            "Lich su": convert_to_float(new_lich_su),
            "Dia ly": convert_to_float(new_dia_ly),
            "GDCD": convert_to_float(new_gdcd),
            "MaTinh": ma_tinh,
            "TenTinh": ten_tinh
        }

        # Chuyển dữ liệu mới thành DataFrame
        new_data_df = pd.DataFrame([new_data])
                       
        if not new_data_df.empty:
            row = new_data_df.iloc[0]
            save_history(row, "THÊM MỚI")
        # Dùng pd.concat để kết hợp DataFrame mới với DataFrame cũ
        df = pd.concat([df, new_data_df], ignore_index=True)
        # Lưu lại DataFrame vào file CSV
        df.to_csv(cached, index=False)

        # Thông báo thành công 
        messagebox.showinfo("Thành công", f"Đã thêm dữ liệu cho SBD {sbd}.\n Khởi động lại chương trình để xem cập nhật", parent=add_window)

    # Nhãn và ô nhập cho các trường
    Label(add_window, text="Số Báo Danh (SBD):").grid(row=0, column=0, padx=10, pady=5, sticky="e")
    entry_sbd = Entry(add_window)
    entry_sbd.grid(row=0, column=1, padx=10, pady=5)

    Label(add_window, text="Năm:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    entry_year = Entry(add_window)
    entry_year.grid(row=1, column=1, padx=10, pady=5)

    Label(add_window, text="Mã Tỉnh:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
    entry_ma_tinh = Entry(add_window)
    entry_ma_tinh.grid(row=2, column=1, padx=10, pady=5)

    Label(add_window, text="Tên Tỉnh:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
    entry_ten_tinh = Entry(add_window)
    entry_ten_tinh.grid(row=3, column=1, padx=10, pady=5)

    # Nhãn và ô nhập cho các môn
    Label(add_window, text="Điểm Toán:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
    entry_toan = Entry(add_window)
    entry_toan.grid(row=4, column=1, padx=10, pady=5)

    Label(add_window, text="Điểm Văn:").grid(row=5, column=0, padx=10, pady=5, sticky="e")
    entry_van = Entry(add_window)
    entry_van.grid(row=5, column=1, padx=10, pady=5)

    Label(add_window, text="Điểm Lý:").grid(row=6, column=0, padx=10, pady=5, sticky="e")
    entry_ly = Entry(add_window)
    entry_ly.grid(row=6, column=1, padx=10, pady=5)

    Label(add_window, text="Điểm Sinh:").grid(row=7, column=0, padx=10, pady=5, sticky="e")
    entry_sinh = Entry(add_window)
    entry_sinh.grid(row=7, column=1, padx=10, pady=5)

    Label(add_window, text="Điểm Ngoại ngữ:").grid(row=8, column=0, padx=10, pady=5, sticky="e")
    entry_ngoai_ngu = Entry(add_window)
    entry_ngoai_ngu.grid(row=8, column=1, padx=10, pady=5)

    Label(add_window, text="Điểm Hoa:").grid(row=9, column=0, padx=10, pady=5, sticky="e")
    entry_hoa = Entry(add_window)
    entry_hoa.grid(row=9, column=1, padx=10, pady=5)

    Label(add_window, text="Điểm Lịch sử:").grid(row=10, column=0, padx=10, pady=5, sticky="e")
    entry_lich_su = Entry(add_window)
    entry_lich_su.grid(row=10, column=1, padx=10, pady=5)

    Label(add_window, text="Điểm Địa lý:").grid(row=11, column=0, padx=10, pady=5, sticky="e")
    entry_dia_ly = Entry(add_window)
    entry_dia_ly.grid(row=11, column=1, padx=10, pady=5)

    Label(add_window, text="Điểm GDCD:").grid(row=12, column=0, padx=10, pady=5, sticky="e")
    entry_gdcd = Entry(add_window)
    entry_gdcd.grid(row=12, column=1, padx=10, pady=5)

    # Nút Thêm
    add_button = Button(add_window, text="Thêm Dữ Liệu", command=add_entry, bg="blue")
    add_button.grid(row=13, column=0, columnspan=2, pady=10)

    # Đảm bảo người dùng không thể mở nhiều cửa sổ thêm dữ liệu
    add_window.transient(parent)  # Đặt cửa sổ con phía trước cửa sổ chính
    add_window.grab_set() 