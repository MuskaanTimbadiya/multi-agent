from database import insert_event, get_events, delete_event, cursor, conn

def handle_calendar(query):
    q = query.lower()

    # ❌ DELETE ALL (VERY FIRST CHECK)
    if "delete all" in q or "clear all" in q or "clear events" in q:
        cursor.execute("DELETE FROM events")
        conn.commit()
        return "🗑️ All events deleted."

    # ❌ DELETE SINGLE
    if "delete" in q or "remove" in q:
        event = q.replace("delete", "").replace("remove", "").replace("event", "").strip()
        delete_event(event)
        return f"❌ Event deleted: {event}"

    # ✅ SHOW
    if "show" in q or "list" in q:
        events = get_events()
        return f"📆 Events: {[e[0] for e in events]}"

    # ✅ ADD
    if "add" in q or "schedule" in q or "remind" in q:
        event = q.replace("add", "").replace("schedule", "").replace("remind me to", "").strip()
        insert_event(event)
        return f"📅 Event scheduled: {event}"

    return "📅 Try: schedule / show / delete event"
