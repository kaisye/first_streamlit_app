import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np


st.title("Tiêu đề")
st.write("Đây là ứng dụng Streamlit đầu tiên của tôi")


# df là DataFrame chứa dữ liệu về hóa đơn và tiền tip từ bộ dữ liệu "tips" của Seaborn
df = sns.load_dataset("tips")

# fig và ax là đối tượng của Matplotlib để tạo biểu đồ
# sns.scatterplot tạo biểu đồ scatter plot với dữ liệu từ DataFrame df, 
# sử dụng cột "total_bill" làm trục x và cột "tip" làm trục y
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