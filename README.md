# OpenAI Text Summarizer

This project is a Python-based text summarization tool that uses the OpenAI GPT-3.5 model to generate concise summaries of long text inputs. The tool stores the original text and summaries in an SQLite database for easy retrieval and management.

## Features
- **Text Summarization**: Generate concise summaries of text inputs using OpenAI's GPT-3.5-turbo model.
- **Database Storage**: Save the original text and its corresponding summary in an SQLite database.
- **CLI Input Options**: Provide text directly or via a file for summarization.

## Prerequisites

Before running the project, ensure you have the following installed:
- Python 3.7 or higher
- SQLite3 (comes pre-installed with Python)

Install the required Python libraries using pip:

```bash
pip install openai python-dotenv
```

## Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Anushka1912/Content_Summarizer.git
   cd Content_Summarizer
   ```

2. **Create a `.env` File**:
   Add your OpenAI API key to a `.env` file in the project directory:

   ```plaintext
   OPENAI_API_KEY=your_openai_api_key_here
   ```

   Replace `your_openai_api_key_here` with your actual OpenAI API key.

3. **Run the Script**:
   Execute the Python script to start summarizing text:

   ```bash
   python main.py
   ```

## How to Use

1. **Provide Input**:
   - Option 1: Enter text directly via the command line.
   - Option 2: Provide a file path to read text from a file.

2. **View the Summary**:
   - The script will display the summary on the screen.
   - The original text and summary will be saved to the SQLite database (`summarizer.db`).

## Project Structure

```
.
├── main.py     # Main script
├── .env              # Environment variables (contains API key)
├── summarizer.db     # SQLite database file (auto-created)
├── README.md         # Project documentation
└── requirements.txt  # List of dependencies
```


## Troubleshooting

1. **Missing API Key**:
   Ensure the `.env` file exists and contains your OpenAI API key.

2. **File Not Found**:
   Verify the file path provided is correct when selecting the file input option.

3. **Database Errors**:
   Ensure SQLite is properly installed and the `summarizer.db` file has the correct permissions.

