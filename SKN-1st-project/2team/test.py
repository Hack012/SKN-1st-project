import mysql.connector
import streamlit as st
import pandas as pd

def fetch_data_from_mysql():
    # MySQL 연결
    conn = mysql.connector.connect(
        host="localhost",
        user="team2",
        password="team2",
        database="teamtestdb"
    )

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM record_table")

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows


# Streamlit UI
st.title("MySQL 데이터 가져오기")

data = fetch_data_from_mysql()

df = pd.DataFrame(data, columns=["ind", "name", "record"])

st.write("사용자 데이터:")
st.dataframe(df)