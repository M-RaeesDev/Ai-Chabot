# AI Chatbot using Chainlit & Gemini API

This is an **AI-powered chatbot** built using **Python**, **Chainlit**, and **Google Gemini API (OpenAI-style endpoint)**.  
It responds in real-time with a natural, human-like typing flow and provides an interactive chat interface.

---

## Features

- Real-time streaming responses  
- Natural human-like typing effect  
- Built using Chainlit (modern Python-based chat UI)  
- Secure API key handling via `.env` file  
- Fully asynchronous and optimized for smooth user experience  

---

## Tech Stack

- **Python 3.9+**
- **Chainlit**
- **Gemini API (via AsyncOpenAI)**
- **dotenv** for environment variable management

---

## Installation & Setup

Follow these steps to run the project on your system:

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-chatbot-chainlit.git
cd ai-chatbot-chainlit

```
### 2. Create a virtual environment (recommended)

Windows:
python -m venv venv
venv\Scripts\activate

### 3. Add your Gemini API key

Create a file named .env in the root folder and add your API key:
GEMINI_API_KEY=your_real_gemini_api_key_here


### 4. Running the Project

Start the chatbot server using:
chainlit run app.py -w


Then open your browser and visit:
http://localhost:8000
