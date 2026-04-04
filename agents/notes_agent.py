from database import insert_note, get_notes, delete_note

def handle_notes(query):
    q = query.lower()

    # ❌ DELETE FIRST (highest priority)
    if "delete" in q or "remove" in q:
        note = q.replace("delete", "").replace("remove", "").replace("note", "").strip()

        delete_note(note)
        return f"❌ Note deleted: {note}"

    # ✅ SHOW
    if "show" in q or "list" in q or "retrieve" in q:
        notes = get_notes()
        return f"📖 Notes: {[n[0] for n in notes]}"

    # ✅ SAVE
    if "save" in q or "note" in q:
        note = q.replace("save", "").replace("note", "").strip()

        if note:
            insert_note(note)
            return f"📝 Note saved: {note}"
        else:
            return "📝 Please provide note content."

    return "📝 Try: save / show / delete note"

        # DELETE ALL
    if "delete all" in q or "clear" in q:
        cursor.execute("DELETE FROM notes")
        conn.commit()
        return "🗑️ All notes deleted."
