from database import insert_task, get_tasks, delete_task, cursor, conn

def handle_task(query):
    q = query.lower()

    # 🔥 DELETE ALL (FIRST PRIORITY)
    if "delete all" in q or "clear all" in q or "clear tasks" in q:
        cursor.execute("DELETE FROM tasks")
        conn.commit()
        return "🗑️ All tasks deleted."

    # ❌ DELETE SINGLE
    if "delete" in q or "remove" in q:
        task = q.replace("delete", "").replace("remove", "").replace("task", "").strip()
        delete_task(task)
        return f"❌ Task deleted: {task}"

    # ✅ SHOW
    if "show" in q or "list" in q:
        tasks = get_tasks()
        return f"📋 Tasks: {[t[0] for t in tasks]}"

    # ✅ ADD
    if "add" in q or "task" in q:
        task = q.replace("add", "").replace("task", "").strip()
        insert_task(task)
        return f"✅ Task added: {task}"

    return "📋 Try: add / show / delete task"