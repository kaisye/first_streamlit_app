import streamlit as st

from factorial import fact


# Cấu hình cơ bản cho trang web Streamlit.
st.set_page_config(
    page_title="Factorial App",
    page_icon="!",
)


def main():
    """Hàm chính để chạy ứng dụng tính giai thừa."""

    # st.title dùng để tạo tiêu đề lớn cho ứng dụng.
    st.title("Factorial Calculator")

    # st.write dùng để hiển thị văn bản ra màn hình.
    st.write("Ứng dụng đơn giản để tính giai thừa của một số nguyên không âm.")

    # st.number_input tạo ô nhập số.
    # min_value=0 để người dùng không nhập số âm.
    # max_value=900 để tránh kết quả quá lớn làm app khó hiển thị.
    number = st.number_input(
        "Nhập một số:",
        min_value=0,
        max_value=900,
        value=5,
        step=1,
    )

    # st.button tạo nút bấm.
    # Code bên trong if chỉ chạy khi người dùng bấm nút.
    if st.button("Tính giai thừa"):
        result = fact(number)

        # st.success hiển thị thông báo kết quả với màu nổi bật.
        st.success(f"Giai thừa của {number} là:")

        # st.code giúp hiển thị số lớn dễ copy hơn.
        st.code(result, language="text")

        # st.balloons tạo hiệu ứng bóng bay sau khi tính xong.
        st.balloons()

    # Phần ghi chú nhỏ để người học hiểu công thức giai thừa.
    st.subheader("Ghi chú")
    st.write("Giai thừa của n được ký hiệu là n!.")
    st.write("Ví dụ: 5! = 5 x 4 x 3 x 2 x 1 = 120")
    st.write("Theo quy ước: 0! = 1 và 1! = 1")


if __name__ == "__main__":
    main()
