# First Streamlit App

Đây là project thực hành Streamlit đầu tiên. Repo hiện có 2 app Streamlit riêng biệt:

- `math_graph`: app vẽ biểu đồ toán học và biểu đồ dữ liệu.
  => **https://keeptrack-math-graph.streamlit.app/**
  
- `factorial_app`: app tính giai thừa với giao diện tối.
=> **https://keeptrack-factorial-app.streamlit.app/**
  

## Nội dung project

```text
.
|-- requirements.txt
|-- note_streamlit.md
|-- streamlit.ipynb
|-- math_graph/
|   `-- app.py
`-- factorial_app/
    |-- app.py
    `-- factorial.py
```

Trong đó:

- `math_graph/app.py`: app Streamlit vẽ scatter plot, đồ thị sin, so sánh exp/log, đồ thị bậc 2 và heatmap.
- `factorial_app/app.py`: giao diện Streamlit dark theme để tính giai thừa.
- `factorial_app/factorial.py`: hàm xử lý logic tính giai thừa.
- `requirements.txt`: danh sách thư viện cần cài đặt.
- `note_streamlit.md`: ghi chú kiến thức Streamlit bằng tiếng Việt.

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

## Chạy Factorial App

Factorial App là app tính giai thừa với giao diện tối, có sidebar chọn số, hiển thị số chữ số của kết quả và phần ghi chú công thức.

Chạy lệnh:

```powershell
streamlit run factorial_app/app.py
```

Nếu port `8501` đang được dùng, có thể chạy bằng port khác:

```powershell
streamlit run factorial_app/app.py --server.port 8502
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
   - Factorial App: `factorial_app/app.py`
6. Bấm Deploy.

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

## Lưu ý

- Không push file chứa API key, password hoặc token lên GitHub.
- Nếu dùng secrets, hãy lưu local trong `.streamlit/secrets.toml` và thêm file này vào `.gitignore`.
- Khi thêm thư viện mới, cần cập nhật `requirements.txt`.
- Nên chạy thử local trước khi deploy.
