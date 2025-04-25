#  🤖 OllamaBot Chat - Streamlit Interface
A simple yet powerful chatbot built using [Streamlit](https://streamlit.io/) and [Ollama](https://ollama.com/), designed to let you interact with local LLMs like LLaMA 3, gemma3, and Qwen.

### 🎯 Features
- Chat Interface with memory.
- Model selection via sidebar.
- Customizable generation parameters (Temperature, Top-k, Top-p, Max Tokens).
- Error handling and graceful fallbacks.

### 🚀 Technologies Used
- Python
- uv
- Ollama
- Streamlit

### 🧪 Example Models
* [llama3.2](https://ollama.com/library/llama3.2)
* [llama3.1](https://ollama.com/library/llama3.1)
* [qwen2.5:3b](https://ollama.com/library/qwen2.5:3b)
* [gemma3](https://ollama.com/library/gemma3)

## 🛠️ Setup

### 1. Clone the repository
```bash
git clone https://github.com/DonLuisM/OllamaBot_ST.git
cd OllamaBot_ST
```

### 2. Download Ollama, models and uv
- Ollama - [Download](https://ollama.com/)
- uv - [terminal](https://docs.astral.sh/uv/#__tabbed_1_1)

### 3. Install dependencies
```bash
cd OllamaBot_ST
uv add
uv sync
```
### 4. Run the chatbot
```bash
uv run streamlit run app.py
```

--- 

### 📜 License
MIT License – see [LICENSE](./LICENSE) for details.

### 🤝 Contributing
If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. All contributions are welcome!

