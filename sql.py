from dotenv import load_dotenv
import streamlit as st
import os
import sqlite3
import google.generativeai as genai

# Load environment variables and configure Gemini
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to call Gemini and get SQL query
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-1.5-pro')
    response = model.generate_content([prompt[0], question])
    sql = response.text.strip()

    # Remove ```sql or ``` wrappers if they exist
    if sql.startswith("```"):
        sql = sql.split("```")[1].strip()
    return sql

# Function to execute SQL on the student.db database
def read_sql_query(sql, db):
    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        conn.close()
        return rows
    except Exception as e:
        st.error(f"SQL execution failed: {e}")
        return []

# Prompt to guide Gemini
prompt = ["""
You are an expert in converting natural language to SQL. The SQLite database named 'student.db' has a table STUDENT with three columns: NAME, 
CLASS, and SECTION.

Example Query 1: What is the total number of entries that are present in the database?
SQL Query Output 1: SELECT COUNT(*) FROM STUDENT;

Example Query 2: Information of all the students who study in Data Science class?
SQL Query Output 2: SELECT * FROM STUDENT WHERE CLASS = "Data Science";

Only return valid SQLite SQL syntax with no extra words or formatting.
"""]

# Streamlit UI setup
st.set_page_config(page_title="SQL Generator with Gemini")
st.title("🔍 Gemini App to Retrieve SQL Queries from student.db")

# Input
question = st.text_input("Ask your question about the student database:")
submit = st.button("Generate SQL and Run")

# Run if user submits a query
if submit and question:
    with st.spinner("Generating SQL with Gemini..."):
        sql_query = get_gemini_response(question, prompt)
        st.subheader("🔢 Generated SQL:")
        st.code(sql_query)

    with st.spinner("Running SQL query on database..."):
        result = read_sql_query(sql_query, "student.db")

    st.subheader("📊 Query Results:")
    if result:
        for row in result:
            st.write(row)
    else:
        st.info("No results returned by the query.")
