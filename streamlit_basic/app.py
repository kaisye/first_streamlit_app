import pandas as pd
import streamlit as st


# Cấu hình thông tin cơ bản của trang Streamlit.
st.set_page_config(
    page_title="Streamlit Basic Guideline",
    page_icon="📘",
    layout="wide",
)


# Tiêu đề chính của ứng dụng.
st.title("Streamlit Basic Guideline")

# Mô tả ngắn về mục tiêu của app.
st.write(
    "Ứng dụng này tổng hợp các cú pháp Streamlit cơ bản cho người mới bắt đầu. "
    "Mỗi phần đều có ví dụ code rõ ràng để bạn có thể copy và chạy thử."
)


# Sidebar dùng để tạo mục lục điều hướng.
st.sidebar.title("Mục lục")

section = st.sidebar.radio(
    "Chọn nội dung muốn học:",
    [
        "1. Hiển thị nội dung",
        "2. Nhận input",
        "3. Button và điều kiện",
        "4. Hiển thị bảng dữ liệu",
        "5. Vẽ biểu đồ",
        "6. Layout cơ bản",
        "7. Upload file",
        "8. App mẫu hoàn chỉnh",
        "9. Các tính năng nâng cao",
    ],
)


if section == "1. Hiển thị nội dung":
    st.header("1. Hiển thị nội dung")

    st.write("Streamlit thường bắt đầu bằng cách import thư viện:")

    st.code(
        """
import streamlit as st
""",
        language="python",
    )

    st.subheader("Các cú pháp hiển thị thường dùng")

    st.code(
        """
st.title("Tiêu đề lớn")
st.header("Tiêu đề cấp 2")
st.subheader("Tiêu đề nhỏ")
st.write("Hiển thị văn bản hoặc dữ liệu")
st.text("Hiển thị văn bản thường")
st.markdown("**Văn bản in đậm bằng Markdown**")
st.code("print('Hello Streamlit')", language="python")
""",
        language="python",
    )

    st.subheader("Kết quả minh họa")

    st.title("Tiêu đề lớn")
    st.header("Tiêu đề cấp 2")
    st.subheader("Tiêu đề nhỏ")
    st.write("Đây là nội dung được hiển thị bằng st.write().")
    st.text("Đây là nội dung được hiển thị bằng st.text().")
    st.markdown("**Đây là nội dung Markdown in đậm.**")


elif section == "2. Nhận input":
    st.header("2. Nhận input từ người dùng")

    st.write("Streamlit có nhiều widget để nhận dữ liệu từ người dùng.")

    st.code(
        """
name = st.text_input("Nhập tên của bạn")
age = st.number_input("Nhập tuổi", min_value=0, max_value=120, value=18)
score = st.slider("Chọn điểm", min_value=0, max_value=10, value=5)
subject = st.selectbox("Chọn môn học", ["Python", "SQL", "AI"])
is_student = st.checkbox("Tôi là học viên")

st.write("Tên:", name)
st.write("Tuổi:", age)
st.write("Điểm:", score)
st.write("Môn học:", subject)
st.write("Là học viên:", is_student)
""",
        language="python",
    )

    st.subheader("Kết quả minh họa")

    name = st.text_input("Nhập tên của bạn")
    age = st.number_input("Nhập tuổi", min_value=0, max_value=120, value=18)
    score = st.slider("Chọn điểm", min_value=0, max_value=10, value=5)
    subject = st.selectbox("Chọn môn học", ["Python", "SQL", "AI"])
    is_student = st.checkbox("Tôi là học viên")

    st.write("Tên:", name)
    st.write("Tuổi:", age)
    st.write("Điểm:", score)
    st.write("Môn học:", subject)
    st.write("Là học viên:", is_student)


elif section == "3. Button và điều kiện":
    st.header("3. Button và điều kiện")

    st.write("`st.button()` tạo nút bấm. Code trong `if` chỉ chạy khi người dùng bấm nút.")

    st.code(
        """
st.write('Đây là button tên "Chạy chương trình"')

if st.button("Chạy chương trình"):
    st.success("Bạn vừa bấm nút!")
    st.balloons()
""",
        language="python",
    )

    st.subheader("Kết quả minh họa")

    st.write('Đây là button tên "Chạy chương trình"')

    if st.button("Chạy chương trình"):
        st.success("Bạn vừa bấm nút!")
        st.balloons()


elif section == "4. Hiển thị bảng dữ liệu":
    st.header("4. Hiển thị bảng dữ liệu")

    st.write("Có thể dùng Pandas để tạo bảng dữ liệu, sau đó hiển thị bằng Streamlit.")

    st.code(
        """
import pandas as pd
import streamlit as st

df = pd.DataFrame({
    "Tên": ["An", "Bình", "Chi"],
    "Điểm": [8, 9, 10],
    "Môn học": ["Python", "SQL", "AI"]
})

st.dataframe(df)
st.table(df)
""",
        language="python",
    )

    st.subheader("Kết quả minh họa")

    df = pd.DataFrame(
        {
            "Tên": ["An", "Bình", "Chi"],
            "Điểm": [8, 9, 10],
            "Môn học": ["Python", "SQL", "AI"],
        }
    )

    st.write("Hiển thị bằng st.dataframe():")
    st.dataframe(df)

    st.write("Hiển thị bằng st.table():")
    st.table(df)


elif section == "5. Vẽ biểu đồ":
    st.header("5. Vẽ biểu đồ")

    st.write("Streamlit có thể vẽ nhanh line chart và bar chart từ DataFrame.")

    st.code(
        """
import pandas as pd
import streamlit as st

chart_data = pd.DataFrame({
    "Ngày": [1, 2, 3, 4, 5],
    "Doanh thu": [10, 15, 13, 20, 25]
})

st.line_chart(chart_data, x="Ngày", y="Doanh thu")
st.bar_chart(chart_data, x="Ngày", y="Doanh thu")
""",
        language="python",
    )

    st.subheader("Kết quả minh họa")

    chart_data = pd.DataFrame(
        {
            "Ngày": [1, 2, 3, 4, 5],
            "Doanh thu": [10, 15, 13, 20, 25],
        }
    )

    st.line_chart(chart_data, x="Ngày", y="Doanh thu")
    st.bar_chart(chart_data, x="Ngày", y="Doanh thu")


elif section == "6. Layout cơ bản":
    st.header("6. Layout cơ bản")

    st.write("Streamlit hỗ trợ chia giao diện thành cột, tab và sidebar.")

    st.subheader("Chia cột")

    st.code(
        """
col1, col2 = st.columns(2)

with col1:
    st.write("Nội dung cột 1")

with col2:
    st.write("Nội dung cột 2")
""",
        language="python",
    )

    col1, col2 = st.columns(2)

    with col1:
        st.info("Nội dung cột 1")

    with col2:
        st.success("Nội dung cột 2")

    st.subheader("Dùng tabs")

    st.code(
        """
tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])

with tab1:
    st.write("Nội dung tab 1")

with tab2:
    st.write("Nội dung tab 2")
""",
        language="python",
    )

    tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])

    with tab1:
        st.write("Nội dung tab 1")

    with tab2:
        st.write("Nội dung tab 2")


elif section == "7. Upload file":
    st.header("7. Upload file")

    st.write("`st.file_uploader()` cho phép người dùng tải file lên app.")

    st.code(
        """
uploaded_file = st.file_uploader("Chọn file CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)
else:
    st.info("Hãy upload một file CSV.")
""",
        language="python",
    )

    uploaded_file = st.file_uploader("Chọn file CSV", type=["csv"])

    if uploaded_file is not None:
        uploaded_df = pd.read_csv(uploaded_file)
        st.dataframe(uploaded_df)
    else:
        st.info("Hãy upload một file CSV để xem dữ liệu.")


elif section == "8. App mẫu hoàn chỉnh":
    st.header("8. App mẫu hoàn chỉnh")

    st.write("Dưới đây là một app Streamlit nhỏ, phù hợp để người mới copy và chạy thử.")

    st.code(
        """
import streamlit as st

st.title("Ứng dụng tính bình phương")

number = st.number_input("Nhập một số", value=2)

if st.button("Tính bình phương"):
    result = number ** 2
    st.success(f"Bình phương của {number} là {result}")
""",
        language="python",
    )

    st.subheader("Kết quả minh họa")

    number = st.number_input("Nhập một số", value=2)

    if st.button("Tính bình phương"):
        result = number**2
        st.success(f"Bình phương của {number} là {result}")


elif section == "9. Các tính năng nâng cao":
    st.header("9. Các tính năng nâng cao")

    st.write(
        "Sau khi đã quen với các lệnh cơ bản, bạn có thể học thêm một số tính năng "
        "giúp app Streamlit mạnh hơn và chuyên nghiệp hơn."
    )

    st.subheader("9.1. st.session_state")

    st.write(
        "`st.session_state` dùng để lưu trạng thái trong quá trình người dùng tương tác với app."
    )

    st.code(
        """
if "count" not in st.session_state:
    st.session_state.count = 0

if st.button("Tăng số"):
    st.session_state.count += 1

st.write("Số hiện tại:", st.session_state.count)
""",
        language="python",
    )

    if "count" not in st.session_state:
        st.session_state.count = 0

    if st.button("Tăng số"):
        st.session_state.count += 1

    st.write("Số hiện tại:", st.session_state.count)

    st.subheader("9.2. st.cache_data")

    st.write(
        "`st.cache_data` giúp lưu kết quả của hàm, tránh chạy lại các bước tốn thời gian "
        "như đọc file hoặc xử lý dữ liệu lớn."
    )

    st.code(
        """
@st.cache_data
def load_data():
    df = pd.read_csv("data.csv")
    return df

df = load_data()
st.dataframe(df)
""",
        language="python",
    )

    st.info("Ví dụ trên thường dùng khi app cần đọc file CSV hoặc tải dữ liệu.")

    st.subheader("9.3. st.metric")

    st.write("`st.metric` dùng để hiển thị chỉ số quan trọng như doanh thu, điểm số, số lượng.")

    st.code(
        """
st.metric(label="Doanh thu", value="10M", delta="5%")
st.metric(label="Người dùng", value="1,200", delta="-2%")
""",
        language="python",
    )

    metric_col1, metric_col2 = st.columns(2)

    with metric_col1:
        st.metric(label="Doanh thu", value="10M", delta="5%")

    with metric_col2:
        st.metric(label="Người dùng", value="1,200", delta="-2%")

    st.subheader("9.4. st.expander")

    st.write("`st.expander` dùng để ẩn/hiện nội dung chi tiết, giúp giao diện gọn hơn.")

    st.code(
        """
with st.expander("Xem giải thích"):
    st.write("Đây là nội dung chi tiết.")
""",
        language="python",
    )

    with st.expander("Xem giải thích"):
        st.write("Đây là nội dung chi tiết nằm bên trong expander.")

    st.subheader("9.5. st.tabs")

    st.write("`st.tabs` dùng để chia nội dung thành nhiều tab.")

    st.code(
        """
tab1, tab2 = st.tabs(["Dữ liệu", "Biểu đồ"])

with tab1:
    st.write("Nội dung dữ liệu")

with tab2:
    st.write("Nội dung biểu đồ")
""",
        language="python",
    )

    advanced_tab1, advanced_tab2 = st.tabs(["Dữ liệu", "Biểu đồ"])

    with advanced_tab1:
        st.write("Đây là tab dữ liệu.")

    with advanced_tab2:
        st.write("Đây là tab biểu đồ.")

    st.subheader("9.6. st.download_button")

    st.write("`st.download_button` cho phép người dùng tải nội dung từ app về máy.")

    st.code(
        """
text = "Hello Streamlit"

st.download_button(
    label="Tải file text",
    data=text,
    file_name="demo.txt",
    mime="text/plain"
)
""",
        language="python",
    )

    text = "Hello Streamlit"

    st.download_button(
        label="Tải file text",
        data=text,
        file_name="demo.txt",
        mime="text/plain",
    )


st.divider()

st.caption("Gợi ý: chạy app bằng lệnh `streamlit run streamlit_basic/app.py`.")
