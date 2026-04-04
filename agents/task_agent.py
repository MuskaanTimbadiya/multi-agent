from database import insert_task, get_tasks, delete_task

def handle_task(query):
    q = query.lower()

    # ✅ SHOW
    if "show" in q or "list" in q:
        tasks = get_tasks()
        return f"📋 Tasks: {[t[0] for t in tasks]}"

    # ❌ DELETE
    if "delete" in q or "remove" in q:
        task = q.replace("delete", "").replace("remove", "").strip()
        delete_task(task)
        return f"❌ Task deleted: {task}"

    # ✅ ADD
    if "add" in q or "task" in q:
        task = q.replace("add", "").replace("task", "").strip()
        insert_task(task)
        return f"✅ Task added: {task}"

    return "📋 Try: add task / show tasks / delete task"


    # DELETE ALL
    if "delete all" in q or "clear" in q:
        cursor.execute("DELETE FROM tasks")
        conn.commit()
    return "🗑️ All tasks deleted."
