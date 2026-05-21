import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st


st.title("Tiêu đề")
st.write("Đây là ứng dụng Streamlit đầu tiên của tôi")


# df là DataFrame chứa dữ liệu về hóa đơn và tiền tip từ bộ dữ liệu "tips" của Seaborn
df = sns.load_dataset("tips")

# fig và ax là đối tượng của Matplotlib để tạo biểu đồ
# sns.scatterplot tạo biểu đồ scatter plot với dữ liệu từ DataFrame df, sử dụng cột "total_bill" làm trục x và cột "tip" làm trục y
fig, ax = plt.subplots()
sns.scatterplot(data=df, x="total_bill", y="tip", ax=ax)
# st.pyplot(fig) hiển thị biểu đồ đã tạo trên ứng dụng Streamlit
st.pyplot(fig)

