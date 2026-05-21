# Ghi chú Streamlit

## 1. Streamlit là gì?

Streamlit là một framework Python dùng để xây dựng ứng dụng web nhanh cho data science, machine learning, dashboard và các demo tương tác.

Điểm mạnh của Streamlit:

- Viết app bằng Python, không cần biết HTML, CSS hoặc JavaScript.
- Phù hợp để hiển thị bảng dữ liệu, biểu đồ, mô hình machine learning và file upload.
- Có thể chạy local trên máy tính và deploy lên Streamlit Community Cloud.
- Tự động reload app khi code thay đổi.

## 2. Cài đặt Streamlit

Nên tạo môi trường ảo trước khi cài thư viện:

```powershell
python -m venv .venv
.\.venv\Scripts\activate
```

Cài Streamlit:

```powershell
pip install streamlit
```

Kiểm tra phiên bản:

```powershell
streamlit --version
```

## 3. Cấu trúc project cơ bản

Một project Streamlit đơn giản thường có cấu trúc:

```text
my_streamlit_app/
|-- app.py
|-- requirements.txt
|-- README.md
`-- .gitignore
```

Trong đó:

- `app.py`: file chính chứa code ứng dụng.
- `requirements.txt`: danh sách thư viện cần cài khi deploy.
- `README.md`: mô tả project và hướng dẫn sử dụng.
- `.gitignore`: bỏ qua các file không cần đưa lên GitHub.

## 4. Chạy ứng dụng Streamlit

Nếu file chính là `app.py`, chạy lệnh:

```powershell
streamlit run app.py
```

Sau khi chạy, Streamlit sẽ mở app ở địa chỉ dạng:

```text
http://localhost:8501
```

Nếu trình duyệt không tự mở, copy địa chỉ trên và dán vào browser.

## 5. Các lệnh hiển thị nội dung cơ bản

Import Streamlit:

```python
import streamlit as st
```

Tiêu đề:

```python
st.title("Tiêu đề ứng dụng")
```

Văn bản:

```python
st.write("Nội dung hiển thị")
st.text("Văn bản thường")
st.markdown("**Văn bản Markdown**")
```

Tiêu đề nhỏ:

```python
st.header("Header")
st.subheader("Subheader")
```

Hiển thị code:

```python
st.code("print('Hello Streamlit')", language="python")
```

## 6. Làm việc với dữ liệu

Hiển thị DataFrame:

```python
import pandas as pd
import streamlit as st

df = pd.DataFrame({
    "name": ["Alice", "Bob"],
    "score": [8, 9]
})

st.dataframe(df)
```

Hiển thị bảng tĩnh gọn:

```python
st.table(df)
```

Hiển thị metric:

```python
st.metric(label="Doanh thu", value="10M", delta="5%")
```

## 7. Vẽ biểu đồ

Streamlit hỗ trợ nhiều cách hiển thị biểu đồ.

Line chart:

```python
st.line_chart(df)
```

Bar chart:

```python
st.bar_chart(df)
```

Dùng Matplotlib:

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [4, 5, 6])
st.pyplot(fig)
```

Dùng Seaborn:

```python
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

fig, ax = plt.subplots()
sns.scatterplot(data=df, x="total_bill", y="tip", ax=ax)
st.pyplot(fig)
```

## 8. Tạo input từ người dùng

Text input:

```python
name = st.text_input("Nhập tên của bạn")
st.write("Xin chào", name)
```

Number input:

```python
age = st.number_input("Nhập tuổi", min_value=0, max_value=120)
```

Slider:

```python
score = st.slider("Chọn điểm", 0, 10, 5)
```

Selectbox:

```python
option = st.selectbox("Chọn môn học", ["Python", "SQL", "Machine Learning"])
```

Checkbox:

```python
show_data = st.checkbox("Hiển thị dữ liệu")

if show_data:
    st.write(df)
```

Button:

```python
if st.button("Chạy"):
    st.write("Đã bấm nút")
```

## 9. Upload file

Người dùng có thể upload file CSV:

```python
uploaded_file = st.file_uploader("Chọn file CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)
```

## 10. Sidebar

Sidebar giúp đưa các bộ lọc và tùy chọn sang bên trái app:

```python
st.sidebar.title("Cài đặt")

choice = st.sidebar.selectbox("Chọn chế độ", ["A", "B", "C"])
st.write("Bạn đã chọn:", choice)
```

## 11. Layout cơ bản

Chia cột:

```python
col1, col2 = st.columns(2)

with col1:
    st.write("Cột 1")

with col2:
    st.write("Cột 2")
```

Dùng tabs:

```python
tab1, tab2 = st.tabs(["Dữ liệu", "Biểu đồ"])

with tab1:
    st.write("Nội dung tab dữ liệu")

with tab2:
    st.write("Nội dung tab biểu đồ")
```

## 12. Session State

`st.session_state` dùng để lưu trạng thái giữa các lần app rerun.

Ví dụ đếm số lần bấm nút:

```python
if "count" not in st.session_state:
    st.session_state.count = 0

if st.button("Tăng"):
    st.session_state.count += 1

st.write("Số lần bấm:", st.session_state.count)
```

## 13. Cache trong Streamlit

Streamlit rerun toàn bộ file khi người dùng tương tác. Để tránh tính toán lại các hàm tốn thời gian, có thể dùng cache.

Cache dữ liệu:

```python
@st.cache_data
def load_data():
    return pd.read_csv("data.csv")

df = load_data()
```

Cache tài nguyên như model:

```python
@st.cache_resource
def load_model():
    model = ...
    return model
```

## 14. File requirements.txt

Khi deploy, Streamlit Cloud đọc file `requirements.txt` để cài thư viện.

Ví dụ:

```text
streamlit
pandas
numpy
matplotlib
seaborn
scikit-learn
```

Nếu app import thư viện nào mà `requirements.txt` thiếu thư viện đó, app deploy có thể bị lỗi `ModuleNotFoundError`.

## 15. Deploy Streamlit lên GitHub và Streamlit Cloud

Quy trình cơ bản:

```powershell
git init
git add .
git commit -m "Initial Streamlit app"
git branch -M main
git remote add origin https://github.com/USERNAME/REPO_NAME.git
git push -u origin main
```

Sau đó vào Streamlit Community Cloud:

```text
https://share.streamlit.io
```

Chọn:

- Repository: repo GitHub của project.
- Branch: `main`.
- Main file path: `app.py`.

## 16. Quản lý secrets

Không nên đưa API key, password hoặc token lên GitHub.

Ở local, có thể tạo file:

```text
.streamlit/secrets.toml
```

Ví dụ:

```toml
API_KEY = "your_api_key"
```

Đọc secrets trong app:

```python
api_key = st.secrets["API_KEY"]
```

Khi deploy lên Streamlit Cloud, khai báo secrets trong phần Settings của app.

Nên thêm file này vào `.gitignore`:

```gitignore
.streamlit/secrets.toml
```

## 17. Một số lỗi thường gặp

Lỗi thiếu thư viện:

```text
ModuleNotFoundError
```

Cách xử lý:

- Kiểm tra app đang import thư viện nào.
- Thêm thư viện đó vào `requirements.txt`.
- Commit và push lại lên GitHub.
- Reboot app trên Streamlit Cloud.

Lỗi sai file chính:

```text
File not found: app.py
```

Cách xử lý:

- Kiểm tra tên file chính.
- Khi deploy, điền đúng `Main file path`.

Lỗi đọc file dữ liệu:

```text
FileNotFoundError
```

Cách xử lý:

- Đảm bảo file dữ liệu đã được push lên GitHub.
- Dùng đường dẫn tương đối thay vì đường dẫn tuyệt đối trên máy local.

## 18. Best practices

- Đặt file chính là `app.py` hoặc đặt tên rõ ràng như `dashboard.py`.
- Luôn cập nhật `requirements.txt` khi thêm thư viện mới.
- Không push môi trường ảo `.venv` lên GitHub.
- Không push secrets lên GitHub.
- Nên test local bằng `streamlit run app.py` trước khi deploy.
- Nên viết README rõ ràng để người khác biết cách cài đặt và chạy app.
- Nên chia code thành hàm nếu app dài.
- Nên dùng `st.cache_data` cho bước load dữ liệu nặng.
- Nên dùng sidebar cho filter, input và control.

## 19. Mẫu app Streamlit đơn giản

```python
import streamlit as st
import pandas as pd

st.title("My First Streamlit App")

st.write("Đây là ứng dụng Streamlit đầu tiên của tôi.")

name = st.text_input("Nhập tên của bạn")

if name:
    st.success(f"Xin chào {name}!")

df = pd.DataFrame({
    "x": [1, 2, 3, 4],
    "y": [10, 20, 15, 30]
})

st.dataframe(df)
st.line_chart(df.set_index("x"))
```

Chạy app:

```powershell
streamlit run app.py
```
