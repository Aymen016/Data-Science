# 🚀 Groq API with LangChain

Welcome to the **Groq API Integration with LangChain**! This project demonstrates how to leverage **Groq's high-speed AI models** using Python and LangChain to generate intelligent responses efficiently. 

## 🔥 Features
- Utilizes **Groq's LLMs** 
- Integrates with **LangChain** for prompt handling
- Provides **fast & accurate responses** using AI
- Demonstrates **best practices** for API key security

---

## 🛠 Installation

### Clone this repository:
```bash
 git clone https://github.com/yourusername/your-repo.git
 cd your-repo
```

### Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### Install dependencies:
```bash
pip install -r requirements.txt
```

---

## 🔑 API Key Setup
Before running the script, set up your **Groq API Key**:

### Method 1: Export API Key (Recommended)
**Windows (Command Prompt):**
```cmd
set GROQ_API_KEY=your_api_key_here
```
**Windows (PowerShell):**
```powershell
$env:GROQ_API_KEY = "your_api_key_here"
```
**macOS/Linux:**
```bash
export GROQ_API_KEY=your_api_key_here
```

### Method 2: Hardcode API Key (Not Recommended)
Edit `lang.py` and replace:
```python
GROQ_API_KEY = "your_api_key_here"
```
---

## 🚀 Usage
Run the script to interact with the Groq model:
```bash
python lang.py
```
### Example Query:
> "Write a simple code to generate Fibonacci numbers in Rust?"

### Example Output:
```rust
fn fibonacci(n: u32) -> Vec<u32> {
    let mut sequence = vec![0, 1];
    for i in 2..n {
        let next = sequence[i - 1] + sequence[i - 2];
        sequence.push(next);
    }
    sequence
}
fn main() {
    println!("{:?}", fibonacci(10));
}
```

---

## 🤝 Contributing
1. Fork the repo 🍴
2. Create a new branch 🚀 (`git checkout -b feature-branch`)
3. Commit your changes 📝 (`git commit -m 'Add new feature'`)
4. Push to the branch 📤 (`git push origin feature-branch`)
5. Create a Pull Request 🔥

---

## 📜 License
This project is **MIT Licensed**. Feel free to modify and use it! 🎉

---

💡 **Made with ❤️ by Aymen** | Happy Coding! 🚀

