class InMemoryStorage:
    def __init__(self):
        self.users = []
        self.refresh_sessions = {}
        self.refresh_sessions_ttl = {}
