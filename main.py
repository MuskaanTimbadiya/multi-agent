from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from database import get_tasks, get_events, get_notes

# 🔥 Jinja fix (Python 3.14 safe)
from jinja2 import Environment, FileSystemLoader

# Agents
from agents.task_agent import handle_task
from agents.calendar_agent import handle_calendar
from agents.notes_agent import handle_notes

# LLM Router
from llm_router import route_query

app = FastAPI()

# Templates setup
templates = Jinja2Templates(directory="templates")

# 🔥 Fix Jinja bug
templates.env = Environment(
    loader=FileSystemLoader("templates"),
    cache_size=0
)

# 💬 Chat memory
chat_history = []

# 🤖 MAIN AGENT (LLM-powered)
def main_agent(query: str):
    q = query.lower()

    # 🔥 FORCE HANDLE DELETE ALL
    if "delete all" in q:
        if "event" in q:
            return handle_calendar(q)
        elif "task" in q:
            return handle_task(q)
        elif "note" in q:
            return handle_notes(q)

    try:
        responses = []

        # 🔥 STEP 1: split properly
        if " and " in q:
            parts = [p.strip() for p in q.split(" and ")]

        else:
            parts = [q]

        # 🔥 STEP 2: process each part independently
        for part in parts:
            agent = route_query(part)
            print("🧠 LLM selected:", agent, "| for:", part)

            if "task" in agent:
                responses.append(handle_task(part))

            elif "calendar" in agent:
                responses.append(handle_calendar(part))

            elif "note" in agent:
                responses.append(handle_notes(part))

            else:
                responses.append("🤖 Couldn't process: " + part)

        # 🔥 STEP 3: combine responses
        return " | ".join(responses)

    except Exception as e:
        print("LLM Error:", e)

        # fallback (still multi-step safe)
        responses = []

        if " and " in q:
            parts = [p.strip() for p in q.split(" and ")]
        else:
            parts = [q]

        for part in parts:
            if "task" in part:
                responses.append(handle_task(part))
            elif "remind" in part or "meeting" in part:
                responses.append(handle_calendar(part))
            elif "note" in part:
                responses.append(handle_notes(part))

        return " | ".join(responses)

# 🖥️ HOME (UI)
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
       request=request,
        name="index.html",
        context={"chat_history": chat_history}
    )

# 📝 HANDLE CHAT
@app.post("/ask", response_class=HTMLResponse)
async def ask(request: Request, query: str = Form(...)):
    result = main_agent(query)

    # Store conversation
    chat_history.append(("user", query))
    chat_history.append(("bot", result))

    return templates.TemplateResponse(
             request=request,
            name="index.html",
            context={"chat_history": chat_history}
    )

# 🔗 API (for Cloud Run / testing)
@app.get("/api")
def api(query: str):
    return {"response": main_agent(query)}

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    tasks = get_tasks()
    events = get_events()
    notes = get_notes()

    task_list = [t[0] for t in tasks]
    event_list = [e[0] for e in events]
    note_list = [n[0] for n in notes]

    # 📊 Stats
    stats = {
        "tasks": len(task_list),
        "events": len(event_list),
        "notes": len(note_list)
    }

    # 🧠 Simple AI Insight
    insight = "You're all caught up! 🚀"

    if stats["tasks"] > 3:
        insight = "You have multiple tasks pending. Stay focused 💪"
    elif stats["events"] > 2:
        insight = "Busy schedule ahead! Plan wisely 📅"
    elif stats["notes"] > 3:
        insight = "You're capturing great ideas 🧠✨"

    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={
            "tasks": task_list,
            "events": event_list,
            "notes": note_list,
            "stats": stats,
            "insight": insight
        }
    )