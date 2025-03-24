import streamlit as st
import mysql.connector
from mysql.connector import Error

st.title("🔌 ทดสอบเชื่อมต่อ MySQL แบบใส่ข้อมูลตรง")

try:
    conn = mysql.connector.connect(
        host="203.154.140.154",
        user="saoiechat",
        password="4au164T&z",
        database="oiechatbot",
        port=25060  # สำคัญ! ระบุพอร์ตให้ตรง
    )

    st.success("✅ เชื่อมต่อ MySQL สำเร็จแล้ว!")
    
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()
    
    st.write("📋 ตารางทั้งหมดในฐานข้อมูล:")
    for table in tables:
        st.write(f"- {table[0]}")
    
    conn.close()

except Error as e:
    st.error(f"❌ เชื่อมต่อไม่สำเร็จ: {e}")
