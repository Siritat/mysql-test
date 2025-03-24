import streamlit as st
import mysql.connector
from mysql.connector import Error

st.title("🔌 ทดสอบเชื่อมต่อ MySQL (ระบุพอร์ต)")

try:
    config = st.secrets["mysql"]  # โหลดจาก secrets.toml

    conn = mysql.connector.connect(
        host=config["host"],
        user=config["user"],
        password=config["password"],
        database=config["database"],
        port=config.get("port", 25060)  # ใช้ port 25060 จาก config
    )

    st.success("✅ เชื่อมต่อสำเร็จ!")
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()
    for t in tables:
        st.write(f"- {t[0]}")
    conn.close()

except Error as e:
    st.error(f"❌ เชื่อมต่อไม่สำเร็จ: {e}")
