session_store = {}

def save_session(session_id, state):
    session_store[session_id] = state

def get_session(session_id):
    return session_store.get(session_id, {})
