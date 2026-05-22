# KeepTrack Day 07 - Streamlit Apps

Đây là project thực hành Streamlit trong ngày 07. Repo hiện có 2 app Streamlit riêng biệt:

- `math_graph`: app vẽ biểu đồ toán học và biểu đồ dữ liệu bằng Streamlit, NumPy, Matplotlib và Seaborn.

**=> https://keeptrack-math-graph.streamlit.app/**

- `streamlit_basic`: app guideline hướng dẫn cú pháp Streamlit cơ bản và một số tính năng nâng cao cho người mới bắt đầu.

**=> https://keeptrack-streamlit-basic.streamlit.app/**

## Nội dung project

```text
.
|-- requirements.txt
|-- note_streamlit.md
|-- note_streamlit.pdf
|-- streamlit.ipynb
|-- math_graph/
|   `-- app.py
`-- streamlit_basic/
    `-- app.py
```

Trong đó:

- `math_graph/app.py`: app Streamlit vẽ scatter plot, đồ thị sin, so sánh exp/log, đồ thị bậc 2 bằng slider và heatmap.
- `streamlit_basic/app.py`: app guideline với ví dụ code rõ ràng cho các cú pháp Streamlit cơ bản như `st.title`, `st.write`, `st.button`, `st.number_input`, `st.dataframe`, `st.line_chart`.
- `requirements.txt`: danh sách thư viện cần cài đặt.
- `note_streamlit.md`: ghi chú kiến thức Streamlit bằng tiếng Việt.
- `note_streamlit.pdf`: bản PDF của ghi chú Streamlit.

## Nội dung chính của từng app

### Math Graph App

App này minh họa cách dùng Streamlit để hiển thị biểu đồ:

- Scatter plot từ dataset `tips` của Seaborn.
- Đồ thị hàm số sin.
- So sánh hàm `exp` và `log`.
- Đồ thị hàm bậc 2 với các hệ số điều chỉnh bằng slider.
- Heatmap cho hàm `z = x^2 + y^2`.

### Streamlit Basic App

App này đóng vai trò như một guideline học Streamlit trực tiếp trên giao diện web:

- Hiển thị nội dung: `st.title`, `st.header`, `st.write`, `st.markdown`, `st.code`.
- Nhận input: `st.text_input`, `st.number_input`, `st.slider`, `st.selectbox`, `st.checkbox`.
- Button và điều kiện: `st.button`.
- Hiển thị dữ liệu: `st.dataframe`, `st.table`.
- Vẽ biểu đồ: `st.line_chart`, `st.bar_chart`.
- Layout: `st.columns`, `st.tabs`, sidebar.
- Upload file: `st.file_uploader`.
- Tính năng nâng cao: `st.session_state`, `st.cache_data`, `st.metric`, `st.expander`, `st.download_button`.

## Cài đặt môi trường

Tạo môi trường ảo:

```powershell
python -m venv .venv
```

Kích hoạt môi trường ảo trên Windows:

```powershell
.\.venv\Scripts\activate
```

Cài đặt thư viện:

```powershell
pip install -r requirements.txt
```

## Chạy Math Graph App

Chạy lệnh:

```powershell
streamlit run math_graph/app.py
```

Sau đó mở trình duyệt tại:

```text
http://localhost:8501
```

## Chạy Streamlit Basic App

Streamlit Basic App là app nhập môn, minh họa cách dùng các cú pháp Streamlit thông qua ví dụ code trực tiếp trên giao diện.

Chạy lệnh:

```powershell
streamlit run streamlit_basic/app.py
```

Nếu port `8501` đang được dùng, có thể chạy bằng port khác:

```powershell
streamlit run streamlit_basic/app.py --server.port 8502
```

## Thư viện sử dụng

Các thư viện chính:

- `streamlit`
- `pandas`
- `numpy`
- `seaborn`
- `matplotlib`

## Deploy lên Streamlit Community Cloud

Các bước cơ bản:

1. Push code lên GitHub.
2. Vào Streamlit Community Cloud.
3. Chọn repository cần deploy.
4. Chọn branch `main`.
5. Chọn file chính:
   - Math Graph App: `math_graph/app.py`
   - Streamlit Basic App: `streamlit_basic/app.py`
6. Bấm Deploy.

Nếu muốn deploy cả 2 app, hãy tạo 2 app riêng trên Streamlit Cloud, mỗi app trỏ tới một `Main file path` khác nhau.

Link Streamlit Community Cloud:

```text
https://share.streamlit.io/
```

## Các lệnh Git thường dùng

Kiểm tra trạng thái:

```powershell
git status
```

Thêm file vào commit:

```powershell
git add .
```

Tạo commit:

```powershell
git commit -m "Update Streamlit app"
```

Push lên GitHub:

```powershell
git push
```

Nếu vừa đổi tên folder hoặc xóa file, nên dùng:

```powershell
git add -A
git commit -m "Update Streamlit apps"
git push
```

## Lưu ý

- Không push file chứa API key, password hoặc token lên GitHub.
- Nếu dùng secrets, hãy lưu local trong `.streamlit/secrets.toml` và thêm file này vào `.gitignore`.
- Khi thêm thư viện mới, cần cập nhật `requirements.txt`.
- Nên chạy thử local trước khi deploy.
