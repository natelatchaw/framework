class Development:
    def __init__(self, is_enabled=False):
        self.is_enabled = is_enabled

    def enable_development_mode(self, is_enabled=True):
        """Set the development mode. Defaults to True."""
        self.is_enabled = is_enabled
