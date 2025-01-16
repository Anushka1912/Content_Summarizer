import sqlite3
import openai
from datetime import datetime
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Database setup
db_path = "summarizer.db"

def initialize_database():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS summaries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            original_text TEXT NOT NULL,
            summary TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        );
    ''')
    conn.commit()
    conn.close()

def summarize_text(long_text):
    if len(long_text.split()) < 150:  
        return "Text is too short to summarize."
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a summarization assistant."},
                {"role": "user", "content": f"Summarize the following text in under 100 words: {long_text}"}
            ]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"Error: {e}")
        return None

def save_to_database(original_text, summary):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO summaries (original_text, summary)
        VALUES (?, ?);
    ''', (original_text, summary))
    conn.commit()
    conn.close()

def main():
    initialize_database()
    # Input: Read from CLI or file
    choice = input("Enter text (1) or provide a file path (2): ")
    if choice == "1":
        long_text = input("Enter the long text: ")
    elif choice == "2":
        file_path = input("Enter the file path: ")
        try:
            with open(file_path, 'r') as file:
                long_text = file.read()
        except FileNotFoundError:
            print("File not found. Exiting.")
            return
    else:
        print("Invalid choice. Exiting.")
        return

    # Generate summary
    print("Summarizing text...")
    summary = summarize_text(long_text)
    if summary:
        # Save and display summary
        save_to_database(long_text, summary)
        print("\nSummary:\n", summary)
    else:
        print("Failed to generate summary.")

if __name__ == "__main__":
    main()
