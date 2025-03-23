# Streamlit CRUD Application

## Introduction
This is a simple CRUD (Create, Read, Update, Delete) web application built using **Streamlit**. The application allows users to manage data entries with an interactive and user-friendly interface.

## Features
- **Navigation Sidebar**: Allows users to switch between different sections.
- **Create Entry**: Users can enter data such as name and age.
- **Read Entries**: Displays existing data entries.
- **Update Entry**: Modify existing records.
- **Delete Entry**: Remove unwanted records.

## Installation
To run this Streamlit application, ensure you have **Python 3.7+** installed. Then, follow these steps:

```sh
# Clone the repository (if applicable)
git clone https://github.com/your-repository.git
cd your-repository

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

## Configuration
You can modify the app theme by creating or editing the Streamlit configuration file (`.streamlit/config.toml`):

```toml
[theme]
primaryColor = "#6C63FF"
backgroundColor = "#F5F5F5"
secondaryBackgroundColor = "#C084FC"
textColor = "#333333"
font = "sans serif"
```

## Styling
For additional UI enhancements, custom CSS has been applied using `st.markdown`.

```python
def apply_custom_css():
    st.markdown(
        """
        <style>
        .stSidebar { background: linear-gradient(135deg, #4B0082, #FF6B6B); padding: 20px; }
        .stButton>button { background-color: #6C63FF; color: white; border-radius: 8px; }
        .stTextInput>div>div>input { background-color: #F0F0F0; border-radius: 5px; }
        </style>
        """,
        unsafe_allow_html=True
    )

apply_custom_css()
```

## Usage
1. **Home Page**: Displays a welcome message.
2. **Create**: Allows users to enter new records.
3. **Read**: Displays stored data.
4. **Update**: Edit existing records.
5. **Delete**: Remove records from the database.

## License
This project is licensed under the MIT License. Feel free to use and modify it for your own needs!

## Contributing
If you'd like to contribute, fork the repository and submit a pull request with your changes.

Happy coding! 🚀

