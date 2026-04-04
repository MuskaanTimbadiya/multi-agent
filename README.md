# 🚀 Multi-Agent AI Assistant

A production-ready AI system that manages tasks, events, and notes using:

- 🤖 Multi-agent architecture
- 🧠 LLM-based routing (Gemini)
- 🔗 MCP-style tool integration
- 💬 Chat UI + Dashboard
- 🗄 SQLite database

🧩 Architecture

User (Chat UI)

↓

Main Agent (LLM Router)

↓

┌──────────────┐

│ Task Agent   │

│ Calendar Agent│

│ Notes Agent │

└─────────────┘

↓

Database (SQLite)

↓

Response → UI
---

## 🤖 Features

### ✅ Multi-Agent System
- Main agent coordinates multiple sub-agents  
- Modular and scalable design  

### 🔗 MCP Tool Integration
- Task Manager  
- Calendar / Reminder system  
- Notes Manager  

### 🧠 LLM-Powered Routing
- Gemini selects the appropriate agent dynamically  

### 🔁 Multi-Step Workflows
add task study and remind me to call mom


### 🗄 CRUD + Bulk Operations
- Add / View / Delete  
- Example:delete all events


### 💬 Chat Interface
- ChatGPT-style UI  
- Typing animation  
- Conversation history  

### 📊 Dashboard
- View tasks, events, and notes in one place  

---

## 🧪 Example Commands

### 📋 Tasks
- add task study  
- show tasks  
- delete task study  

### 📅 Events
- remind me to call mom  
- schedule meeting tomorrow  
- delete all events  

### 📝 Notes
- save note startup idea  
- show notes  
- delete note startup  

---

## 🛠 Tech Stack

- **Backend:** FastAPI  
- **LLM:** Google Gemini API  
- **Database:** SQLite  
- **Frontend:** HTML, CSS, Jinja2  
- **Deployment:** Docker + Cloud Run  

---

## 🚀 Getting Started

### 1. Clone repository
git clone https://github.com/MuskaanTimbadiya/multi-agent.git


### 2. Install dependencies
pip install -r requirements.txt


### 3. Set API key
export GOOGLE_API_KEY="your-api-key"


### 4. Run locally
uvicorn main:app --reload


### 5. Open
http://127.0.0.1:8000/


---

## 📸 Screenshots

assets/chat.png

assets/dashboard.png



---

## 🎯 Key Highlights

- Multi-agent orchestration  
- MCP-style architecture  
- LLM-based intelligent routing  
- Multi-step workflow execution  
- Chat UI + Dashboard  

---

## 📌 Future Improvements

- Real-time chat (AJAX)  
- Google Calendar API integration  
- User authentication  
- Memory-aware conversations  

---

## 🙌 Author

**Muskaan Timbadiya**

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
