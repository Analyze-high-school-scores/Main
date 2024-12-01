from tkinter import *
from tkinter import messagebox
from data import cached,df,save_history
def create_update_window(parent):
    """
    Hàm tạo giao diện cập nhật thông tin (module con).
    :param parent: Cửa sổ chính (root)
    """
    global df  # Sử dụng biến toàn cục

    # Tạo cửa sổ con
    update_window = Toplevel(parent)
    update_window.title("Cập Nhật Thông Tin")
    update_window.geometry("400x400")

    # Hàm cập nhật thông tin dựa trên SBD và Year
    def update_entry():
        global df  # Chỉ rõ rằng sẽ sử dụng biến toàn cục data
        sbd = entry_sbd.get().strip()
        year = entry_year.get().strip()

        # Kiểm tra đầu vào
        if not sbd or not year:
            messagebox.showerror("Lỗi", "Vui lòng nhập cả Số báo danh và Năm!", parent=update_window)
            return

        try:
            sbd = int(sbd)  # Chuyển đổi SBD sang int
            year = int(year)  # Chuyển đổi Year sang int
        except ValueError:
            messagebox.showerror("Lỗi", "Số báo danh và Năm phải là số!", parent=update_window)
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

        # Tìm dòng cần cập nhật
        condition = (df["SBD"] == sbd) & (df["Year"] == year)
        if condition.any():
            # Hiển thị hộp xác nhận trước khi cập nhật
            def confirm_update():
                update_row = df.loc[condition] 
                if not update_row.empty:
                    row = update_row.iloc[0]
                    save_history(row, "CẬP NHẬT")
                # Cập nhật điểm các môn
                if new_toan:
                    df.loc[condition, "Toan"] = float(new_toan)
                if new_van:
                    df.loc[condition, "Van"] = float(new_van)
                if new_ly:
                    df.loc[condition, "Ly"] = float(new_ly)
                if new_sinh:
                    df.loc[condition, "Sinh"] = float(new_sinh)
                if new_ngoai_ngu:
                    df.loc[condition, "Ngoai ngu"] = float(new_ngoai_ngu)
                if new_hoa:
                    df.loc[condition, "Hoa"] = float(new_hoa)
                if new_lich_su:
                    df.loc[condition, "Lich su"] = float(new_lich_su)
                if new_dia_ly:
                    df.loc[condition, "Dia ly"] = float(new_dia_ly)
                if new_gdcd:
                    df.loc[condition, "GDCD"] = float(new_gdcd)

                # Ghi lại vào file CSV
                df.to_csv(cached, index=False)
                messagebox.showinfo("Thành công", f"Đã cập nhật thông tin cho SBD {sbd} và Năm {year}.\n Khởi động lại chương trình để xem cập nhật", parent=update_window)

            # Hộp xác nhận
            if messagebox.askokcancel("Xác nhận cập nhật", f"Bạn có chắc chắn muốn cập nhật thông tin cho SBD {sbd} và Năm {year}?", parent=update_window):
                confirm_update()
        else:
            messagebox.showwarning("Không tìm thấy", f"Không tìm thấy SBD {sbd} với Năm {year}.", parent=update_window)

    # Nhãn và ô nhập cho SBD và Year
    Label(update_window, text="Số Báo Danh (SBD):").grid(row=0, column=0, padx=10, pady=5, sticky="e")
    entry_sbd = Entry(update_window)
    entry_sbd.grid(row=0, column=1, padx=10, pady=5)

    Label(update_window, text="Năm:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    entry_year = Entry(update_window)
    entry_year.grid(row=1, column=1, padx=10, pady=5)

    # Nhãn và ô nhập cho các môn
    Label(update_window, text="Điểm Toán:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
    entry_toan = Entry(update_window)
    entry_toan.grid(row=2, column=1, padx=10, pady=5)

    Label(update_window, text="Điểm Văn:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
    entry_van = Entry(update_window)
    entry_van.grid(row=3, column=1, padx=10, pady=5)

    Label(update_window, text="Điểm Lý:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
    entry_ly = Entry(update_window)
    entry_ly.grid(row=4, column=1, padx=10, pady=5)

    Label(update_window, text="Điểm Sinh:").grid(row=5, column=0, padx=10, pady=5, sticky="e")
    entry_sinh = Entry(update_window)
    entry_sinh.grid(row=5, column=1, padx=10, pady=5)

    Label(update_window, text="Điểm Ngoại ngữ:").grid(row=6, column=0, padx=10, pady=5, sticky="e")
    entry_ngoai_ngu = Entry(update_window)
    entry_ngoai_ngu.grid(row=6, column=1, padx=10, pady=5)

    Label(update_window, text="Điểm Hoa:").grid(row=7, column=0, padx=10, pady=5, sticky="e")
    entry_hoa = Entry(update_window)
    entry_hoa.grid(row=7, column=1, padx=10, pady=5)

    Label(update_window, text="Điểm Lịch sử:").grid(row=8, column=0, padx=10, pady=5, sticky="e")
    entry_lich_su = Entry(update_window)
    entry_lich_su.grid(row=8, column=1, padx=10, pady=5)

    Label(update_window, text="Điểm Địa lý:").grid(row=9, column=0, padx=10, pady=5, sticky="e")
    entry_dia_ly = Entry(update_window)
    entry_dia_ly.grid(row=9, column=1, padx=10, pady=5)

    Label(update_window, text="Điểm GDCD:").grid(row=10, column=0, padx=10, pady=5, sticky="e")
    entry_gdcd = Entry(update_window)
    entry_gdcd.grid(row=10, column=1, padx=10, pady=5)

    # Nút Cập nhật
    update_button = Button(update_window, text="Cập nhật", command=update_entry, bg="green")
    update_button.grid(row=11, column=0, columnspan=2, pady=10)

    # Đảm bảo người dùng không thể mở nhiều cửa sổ cập nhật
    update_window.transient(parent)  # Đặt cửa sổ con phía trước cửa sổ chính
    update_window.grab_set()  # Chặn tương tác với các cửa sổ khác cho đến khi đóng cửa sổ này
