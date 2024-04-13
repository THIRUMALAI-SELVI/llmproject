# Import necessary libraries
import streamlit as st
from langchain.llms import GooglePalm
from langchain_experimental.sql import SQLDatabaseChain
from urllib.parse import quote_plus

# Define function to connect to MySQL database
def connect_to_mysql():
    # Database credentials
    username = "root"
    password = "thiru@2611"
    host = "127.0.0.1"
    port = "3306"
    database_name = "atliq_tshirts"

    # Encode the password
    encoded_password = quote_plus(password)

    # Construct the database URI
    db_uri = f"mysql+mysqlconnector://{username}:{encoded_password}@{host}:{port}/{database_name}"

    # Connect to the database
    try:
        db = SQLDatabase.from_uri(db_uri)
        st.write("Connected to MySQL server successfully")
        return db
    except Exception as e:
        st.error(f"Error connecting to MySQL server: {e}")
        return None

# Define function to query the database using GooglePalm LLM
def query_database(question, llm, db):
    try:
        # Query the database
        result = db.query(question)
        return result
    except Exception as e:
        st.error(f"Error querying the database: {e}")
        return None

# Set page title and layout
st.set_page_config(page_title="AtliQ T Shirts: Database Q&A", layout="wide", initial_sidebar_state="collapsed")

# Custom CSS for styling
st.markdown(
    """
    <style>
        /* Set page background color */
        body {
            background-color: #f9f9f9;
            font-family: Arial, sans-serif;
        }

        /* Set header styles */
        .header {
            background-color: #5f27cd;
            color: #ffffff;
            padding: 20px;
            text-align: center;
            font-size: 36px;
            margin-bottom: 30px;
            border-top-left-radius: 10px;
            border-top-right-radius: 10px;
        }

        /* Set footer styles */
        .footer {
            background-color: #5f27cd;
            color: #ffffff;
            padding: 10px;
            text-align: center;
            position: fixed;
            bottom: 0;
            width: 100%;
            border-bottom-left-radius: 10px;
            border-bottom-right-radius: 10px;
        }

        /* Style the main content */
        .main-content {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 10px;
            margin: 0 auto;
            max-width: 800px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Header
st.markdown("<div class='header'>AtliQ T Shirts: Database Q&A</div>", unsafe_allow_html=True)

# Main content area
st.markdown("<div class='main-content'>", unsafe_allow_html=True)
st.write("Welcome to AtliQ T Shirts! Feel free to explore our collection and ask any questions.", unsafe_allow_html=True)

# Image
shirt_image_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRO2pCdWyoRw5zXrV8RXEeAzQ0XXxc5WpehZw&usqp=CAU"  # Replace with your shirt image URL
st.image(shirt_image_url, width=100)

# Text input for user's question
question = st.text_input("Ask a Question:")

# Conditional block to handle question submission
if question:
    # Placeholder for query processing logic
    # You would typically have some code here to process the user's question
    # and retrieve an appropriate answer from the database or other sources
    
    # Connect to MySQL database
    db = connect_to_mysql()
    
    if db is not None:
        # Create GooglePalm LLM instance
        llm = GooglePalm(google_api_key='YOUR_API_KEY_HERE', temperature=0.2, deprecation_minor_release="X.X")
        
        # Create SQLDatabaseChain instance
        db_chain = SQLDatabaseChain(llm=llm, db=db, verbose=True)
        
        # Query the database
        result = query_database(question, llm, db_chain)
        
        # Display result
        if result is not None:
            st.info(result)

# Footer
st.markdown("<div class='footer'>© 2024 AtliQ T Shirts. All rights reserved.</div>", unsafe_allow_html=True)
