import streamlit as st
import mysql.connector
from mysql.connector import Error

st.title("🔌 ทดสอบเชื่อมต่อ MySQL")

try:
    conn = mysql.connector.connect(
        host=st.secrets["mysql"]["host"],
        user=st.secrets["mysql"]["user"],
        password=st.secrets["mysql"]["password"],
        database=st.secrets["mysql"]["database"]
    )
    st.success("✅ เชื่อมต่อฐานข้อมูล MySQL ได้แล้ว!")
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()
    st.write("📋 ตารางทั้งหมดในฐานข้อมูล:")
    for table in tables:
        st.write(f"- {table[0]}")
    conn.close()

except Error as e:
    st.error(f"❌ เชื่อมต่อไม่สำเร็จ: {e}")
