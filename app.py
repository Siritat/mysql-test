import streamlit as st
import mysql.connector
from mysql.connector import Error

st.title("🔌 ทดสอบเชื่อมต่อ MySQL พร้อมระบุพอร์ต")

# ส่วนนี้สามารถใช้กับ Streamlit Cloud ที่มี secrets หรือกรอกตรงก็ได้
try:
    # หากคุณใช้ secrets.toml
    config = st.secrets["mysql"]

    conn = mysql.connector.connect(
        host=config["host"],
        user=config["user"],
        password=config["password"],
        database=config["database"],
        port=config.get("port", 25060)  # หากไม่ระบุ port จะใช้ 3306 เป็นค่า default
    )

    st.success("✅ เชื่อมต่อฐานข้อมูล MySQL สำเร็จ!")
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()
    st.write("📋 ตารางทั้งหมดในฐานข้อมูล:")
    for t in tables:
        st.write(f"- {t[0]}")
    conn.close()

except Error as e:
    st.error(f"❌ เชื่อมต่อไม่สำเร็จ: {e}")
