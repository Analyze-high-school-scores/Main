from tkinter import *
from tkinter import messagebox
from data import cached,df,df_years,save_history
def create_delete_window(parent):
    """
    Hàm tạo giao diện xóa thông tin (module con).
    :param parent: Cửa sổ chính (root)
    """


    global df  #biến toàn cục

    # Tạo cửa sổ con
    delete_window = Toplevel(parent)
    delete_window.title("Xóa Thông Tin")
    delete_window.geometry("300x150")

    # Hàm xóa thông tin dựa trên SBD và Year
    def delete_entry():
        global df  # Chỉ rõ rằng sẽ sử dụng biến toàn cục data
        sbd = entry_sbd.get().strip()
        year = entry_year.get().strip()

        # Kiểm tra đầu vào
        if not sbd or not year:
            messagebox.showerror("Lỗi", "Vui lòng nhập cả Số báo danh và Năm!", parent=delete_window)
            return

        try:
            sbd = int(sbd)  # Chuyển đổi SBD sang int
            year = int(year)  # Chuyển đổi Year sang int
        except ValueError:
            messagebox.showerror("Lỗi", "Số báo danh và Năm phải là số!", parent=delete_window)
            return

        # Lọc dữ liệu để loại bỏ dòng cần xóa
        initial_length = len(df)
        condition = (df["SBD"] == sbd) & (df["Year"] == year)
        deleted_row = df.loc[condition] 
        df = df[~((df["SBD"] == sbd) & (df["Year"] == year))]
        global df_years
        df_years = {2018: df[df["Year"] == 2018], 2019: df[df["Year"] == 2019]}
        # Kiểm tra xem có dòng nào bị xóa không
        if len(df) < initial_length:
            # Ghi lại vào file CSV # Dòng bị xóa từ DataFrame chính
            if not deleted_row.empty:
                row = deleted_row.iloc[0]
                save_history(row, "XÓA")

            df.to_csv(cached, index=False)
            messagebox.showinfo("Thành công", f"Đã xóa thông tin của SBD {sbd} và Năm {year}.\n Khởi động lại chương trình để xem cập nhật", parent=delete_window)
        else:
            messagebox.showwarning("Không tìm thấy", f"Không tìm thấy SBD {sbd} với Năm {year}.", parent=delete_window)

    # Nhãn và ô nhập
    Label(delete_window, text="Số Báo Danh (SBD):").grid(row=0, column=0, padx=10, pady=5, sticky="e")
    entry_sbd = Entry(delete_window)
    entry_sbd.grid(row=0, column=1, padx=10, pady=5)

    Label(delete_window, text="Năm:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    entry_year = Entry(delete_window)
    entry_year.grid(row=1, column=1, padx=10, pady=5)

    def xacnhan():
        if messagebox.askokcancel("Xóa thông tin", "Bạn có chắc chắn muốn xóa?", parent=delete_window):
            delete_entry()

    # Nút Xóa
    delete_button = Button(delete_window, text="Xóa", command=xacnhan, bg="red",)
    delete_button.grid(row=2, column=0, columnspan=2, pady=10)

    # Đảm bảo người dùng không thể mở nhiều cửa sổ xóa
    delete_window.transient(parent)  # Đặt cửa sổ con phía trước cửa sổ chính
    delete_window.grab_set()  # Chặn tương tác với các cửa sổ khác cho đến khi đóng cửa sổ này
