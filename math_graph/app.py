import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np

# st.title tạo tiêu đề cho ứng dụng Streamlit, căn giữa và có kích thước lớn
st.title("Keeptrack Day 07: Streamlit", anchor="center")

# df là DataFrame chứa dữ liệu về hóa đơn và tiền tip từ bộ dữ liệu "tips" của Seaborn
df = sns.load_dataset("tips")

# fig và ax là đối tượng của Matplotlib để tạo biểu đồ
# sns.scatterplot tạo biểu đồ scatter plot với dữ liệu từ DataFrame df, 
# sử dụng cột "total_bill" làm trục x và cột "tip" làm trục y

st.write("Đây là ứng dụng Streamlit đơn giản")
fig, ax = plt.subplots()
sns.scatterplot(data=df, x="total_bill", y="tip", ax=ax)
# st.pyplot(fig) hiển thị biểu đồ đã tạo trên ứng dụng Streamlit
st.pyplot(fig)

st.write("Bài 1: Vẽ đồ thị hàm số cơ bản")
#  Tạo dữ liệu đầu vào cho x và y
#  
x = np.linspace(-4 * np.pi, 4 * np.pi, 1000)
y = np.sin(x)

# 3. Vẽ biểu đồ bằng Matplotlib
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(x, y, color='blue', linewidth=2, label='$y = \sin(x)$')
ax.set_title("Đồ thị hàm số Sin", fontsize=14)
ax.set_xlabel("Trục X", fontsize=12)
ax.set_ylabel("Trục Y", fontsize=12)
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend()
st.pyplot(fig)

# Bài 2: So sánh 2 hàm số exp, log trên cùng một biểu đồ
x = np.linspace(0.1, 10, 1000)
y_exp = np.exp(x)
y_log = np.log(x)
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(x, y_exp, color='red', linewidth=2, label='$y = e^x$')
ax.plot(x, y_log, color='green', linewidth=2, label='$y = \log(x)$')
ax.set_title("So sánh hàm số exp và log", fontsize=14)
ax.set_xlabel("Trục X", fontsize=12)
ax.set_ylabel("Trục Y", fontsize=12)
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend()
st.pyplot(fig)

# Bài 3: Vẽ đồ thị hàm bậc 2
# Yêu cầu: Nhập hệ số a, b, c cho phương trình y = ax2 + bx + c và vẽ đồ thị tương ứng.
# Bài 4: Tương tác với Slider để khảo sát đồ thị
# Yêu cầu: Dùng st.slider để điều chỉnh giá trị của a, b, c và cập nhật đồ thị theo thời gian thực.
a = st.slider("Hệ số a", -10.0, 10.0, 1.0)
b = st.slider("Hệ số b", -10.0, 10.0, 0.0)
c = st.slider("Hệ số c", -10.0, 10.0, 0.0)
x = np.linspace(-10, 10, 1000)
y = a * x**2 + b * x + c
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(x, y, color='purple', linewidth=2, label=f'$y ={a}x^2 + {b}x + {c}$')
ax.set_title("Đồ thị hàm bậc 2", fontsize=14)
ax.set_xlabel("Trục X", fontsize=12)
ax.set_ylabel("Trục Y", fontsize=12)
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend()
st.pyplot(fig)

# Bài 5: Vẽ Heatmap cho hàm z = x2 + y2
# Yêu cầu: Dùng sns.heatmap để vẽ biểu đồ nhiệt của hàm z = x2 + y2
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(Z, ax=ax, cmap='viridis')
ax.set_title("Heatmap của hàm z = x^2 + y^2", fontsize=14)
ax.set_xlabel("Trục X", fontsize=12)
ax.set_ylabel("Trục Y", fontsize=12)
st.pyplot(fig)
