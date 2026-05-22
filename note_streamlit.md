# Ghi chú Streamlit cơ bản

## 1. Streamlit là gì?

Streamlit là thư viện Python dùng để tạo web app nhanh, đặc biệt phù hợp cho:

- Dashboard dữ liệu.
- Demo machine learning.
- Hiển thị bảng, biểu đồ, kết quả tính toán.
- Làm app nhỏ mà không cần viết HTML, CSS, JavaScript.

Ví dụ, thay vì phải học frontend phức tạp, ta có thể viết app web chỉ bằng Python.

## 2. Cài đặt Streamlit

Cài Streamlit bằng pip:

```powershell
pip install streamlit
```

Kiểm tra Streamlit đã cài thành công chưa:

```powershell
streamlit --version
```

## 3. Tạo app Streamlit đầu tiên

Tạo file `app.py`:

```python
import streamlit as st

st.title("My First Streamlit App")
st.write("Xin chào Streamlit!")
```

Chạy app:

```powershell
streamlit run app.py
```

Sau khi chạy, app thường mở tại:

```text
http://localhost:8501
```

## 4. Cấu trúc project đơn giản

Một project Streamlit cơ bản có thể gồm:

```text
my_app/
|-- app.py
|-- requirements.txt
|-- README.md
`-- .gitignore
```

Ý nghĩa:

- `app.py`: file chính của ứng dụng.
- `requirements.txt`: danh sách thư viện cần cài.
- `README.md`: mô tả project và cách chạy.
- `.gitignore`: danh sách file không đưa lên GitHub.

## 5. Các lệnh hiển thị cơ bản

Import Streamlit:

```python
import streamlit as st
```

Hiển thị tiêu đề:

```python
st.title("Tiêu đề lớn")
st.header("Tiêu đề cấp 2")
st.subheader("Tiêu đề nhỏ")
```

Hiển thị văn bản:

```python
st.write("Đây là nội dung văn bản")
st.text("Văn bản thường")
st.markdown("**Văn bản in đậm**")
```

Hiển thị code:

```python
st.code("print('Hello')", language="python")
```

Hiển thị thông báo:

```python
st.success("Thành công")
st.info("Thông tin")
st.warning("Cảnh báo")
st.error("Lỗi")
```

## 6. Nhận input từ người dùng

Ô nhập chữ:

```python
name = st.text_input("Nhập tên của bạn")
st.write("Xin chào", name)
```

Ô nhập số:

```python
age = st.number_input("Nhập tuổi", min_value=0, max_value=120)
```

Nút bấm:

```python
if st.button("Bấm vào đây"):
    st.write("Bạn vừa bấm nút")
```

Checkbox:

```python
show = st.checkbox("Hiển thị dữ liệu")

if show:
    st.write("Dữ liệu đang được hiển thị")
```

Selectbox:

```python
choice = st.selectbox("Chọn môn học", ["Python", "SQL", "AI"])
st.write("Bạn đã chọn:", choice)
```

Slider:

```python
score = st.slider("Chọn điểm", 0, 10, 5)
st.write("Điểm đã chọn:", score)
```

## 7. Hiển thị dữ liệu dạng bảng

Ví dụ dùng Pandas:

```python
import pandas as pd
import streamlit as st

df = pd.DataFrame({
    "name": ["An", "Bình", "Chi"],
    "score": [8, 9, 10]
})

st.dataframe(df)
```

Nếu muốn bảng tĩnh:

```python
st.table(df)
```

## 8. Vẽ biểu đồ đơn giản

Streamlit có sẵn một số hàm vẽ biểu đồ nhanh.

Line chart:

```python
st.line_chart(df)
```

Bar chart:

```python
st.bar_chart(df)
```

Vẽ bằng Matplotlib:

```python
import matplotlib.pyplot as plt
import streamlit as st

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [2, 4, 6])

st.pyplot(fig)
```

## 9. Upload file

Cho phép người dùng upload file CSV:

```python
import pandas as pd
import streamlit as st

uploaded_file = st.file_uploader("Chọn file CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)
```

## 10. Sidebar

Sidebar là thanh bên trái, thường dùng để đặt bộ lọc hoặc tùy chọn.

```python
st.sidebar.title("Cài đặt")

option = st.sidebar.selectbox("Chọn chế độ", ["A", "B", "C"])
st.write("Chế độ:", option)
```

## 11. Chia layout thành cột

```python
col1, col2 = st.columns(2)

with col1:
    st.write("Nội dung cột 1")

with col2:
    st.write("Nội dung cột 2")
```

## 12. requirements.txt

Khi deploy app, Streamlit Cloud sẽ đọc file `requirements.txt` để biết cần cài thư viện nào.

Ví dụ:

```text
streamlit
pandas
numpy
matplotlib
seaborn
```

Nếu app import thư viện nào thì nên thêm thư viện đó vào `requirements.txt`.

Ví dụ app có:

```python
import seaborn as sns
```

Thì `requirements.txt` cần có:

```text
seaborn
```

Nếu thiếu, app có thể bị lỗi:

```text
ModuleNotFoundError
```

## 13. Deploy app lên Streamlit Cloud

Các bước cơ bản:

1. Push code lên GitHub.
2. Vào Streamlit Community Cloud.
3. Chọn repository.
4. Chọn branch, thường là `main`.
5. Chọn file app, ví dụ `app.py`.
6. Bấm Deploy.

Trang deploy:

```text
https://share.streamlit.io/
```

## 14. Một số lỗi thường gặp

Lỗi thiếu thư viện:

```text
ModuleNotFoundError
```

Cách xử lý:

- Kiểm tra thư viện đang import trong code.
- Thêm thư viện đó vào `requirements.txt`.
- Commit và push lại lên GitHub.
- Reboot app trên Streamlit Cloud.

Lỗi sai đường dẫn file app:

```text
File not found
```

Cách xử lý:

- Kiểm tra file app nằm ở đâu.
- Khi deploy, nhập đúng đường dẫn, ví dụ `math_graph/app.py`.

Lỗi đọc file dữ liệu:

```text
FileNotFoundError
```

Cách xử lý:

- Kiểm tra file dữ liệu đã được push lên GitHub chưa.
- Dùng đường dẫn tương đối thay vì đường dẫn tuyệt đối trên máy cá nhân.

## 15. Mẫu app hoàn chỉnh cho người mới

```python
import streamlit as st

st.title("Ứng dụng tính bình phương")

number = st.number_input("Nhập một số", value=2)

if st.button("Tính"):
    result = number ** 2
    st.success(f"Bình phương của {number} là {result}")
```

Chạy app:

```powershell
streamlit run app.py
```

## 16. Ghi nhớ nhanh

- Luôn bắt đầu bằng `import streamlit as st`.
- Dùng `st.title()` để tạo tiêu đề.
- Dùng `st.write()` để hiển thị nội dung.
- Dùng `st.button()` để tạo nút bấm.
- Dùng `st.number_input()` hoặc `st.text_input()` để nhận dữ liệu.
- Dùng `st.dataframe()` để hiển thị bảng.
- Dùng `st.pyplot()` để hiển thị biểu đồ Matplotlib.
- Chạy app bằng lệnh `streamlit run app.py`.
- Khi deploy, nhớ cập nhật `requirements.txt`.
