import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import datetime
from io import StringIO



if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

df = pd.DataFrame([
    {"ID": 1, "Title": "Python Basics", "Stock": 10, "Price (Rs.)": 500},
    {"ID": 2, "Title": "AI & ML", "Stock": 5, "Price (Rs.)": 450},
    {"ID": 3, "Title": "Data Science", "Stock": 8, "Price (Rs.)": 400},
    {"ID": 4, "Title": "Web Development", "Stock": 6, "Price (Rs.)": 350},
    {"ID": 5, "Title": "Cyber Security", "Stock": 4, "Price (Rs.)": 390},
])

with st.sidebar:
    selected=option_menu(
        menu_title="Book Store Navigation",
        options=["Home","Buy a Book","Login","Admin Panel"],
        icons=["house-heart-fill","stack of books","key","lock"],
        menu_icon=["stack of books"],
        default_index=0,

    )
if selected == "Home":
    st.title("📚 Available Books")
    st.dataframe(df, use_container_width=True)

if selected == "Buy a Book":    
  if not st.session_state.logged_in:
        st.warning("🔒 Please login first from the 'Login' tab.")
  else:
    st.title("🛒 Purchase a Book")

    box = st.selectbox("Choose a Book", df["Title"].tolist())
    buyer_name = st.text_input("Enter your name", placeholder="name")

    if st.button("Buy Now"):
        book_info = df[df["Title"] == box].iloc[0]  

        st.success(f"✅ Purchase successful!\n\nYou bought '{book_info['Title']}' for Rs. {book_info['Price (Rs.)']}")

        receipt = pd.DataFrame({
            "Buyer Name": [buyer_name],
            "Book Title": [book_info["Title"]],
            "Price (Rs.)": [book_info["Price (Rs.)"]],
            "Purchase Time": [datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
            "Status": ["Purchased"]
        })

        csv_buffer = StringIO()
        receipt.to_csv(csv_buffer, index=False)
        csv_data = csv_buffer.getvalue()

        st.download_button(
            label="📥 Download Receipt",
            data=csv_data,
            file_name=f"{buyer_name}_receipt.csv",
            mime="text/csv"
        )

if selected == "Login":
    st.title("🔑 User Login")
    name=st.text_input("Username", placeholder="admin")
    password=st.text_input("Password", placeholder="password", type="password")

    if st.button("Login"):
        if name == "noman" and password == "nomi1":
            st.session_state.logged_in = True
            st.success("Successfully Login")
        else:
            st.error("Invalid username or password")

if selected == "Admin Panel":
    st.title("🔐 Admin Panel")
    admin_user=st.text_input("Admin Username", placeholder="Enter Admin Username")
    admin_password=st.text_input("Admin Password", placeholder="Enter Admin Password", type="password")

    if st.button("Login as Admin"):
        if admin_user == "noman" and admin_password == "nomi":
            st.success("Successfully Login")
        else:
            st.error("Invalid username or password")