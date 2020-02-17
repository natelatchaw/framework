import datetime

class Output:
    def __init__(self, source, development_instance):
        self.source = source
        self.development = development_instance

        self.source_width = 15
        self.status_width = 15
        self.error_width = 15

        self.status_label = 'STATUS'
        self.error_label = 'ERROR'

        # if length of source string is greater than the source_width value
        if len(self.source) > self.source_width:
            # trim source string
            self.source = source[:source_width]

    def toggle_output(self, boolean):
        """Toggle the state of development mode."""
        
        self.development.is_enabled = boolean

    def status(self, message, timestamp=None):
        """Prints a status message to console if development mode is enabled."""

        if timestamp is None:
            datetimestamp = datetime.datetime.now()
            timestamp = datetimestamp.time()

        if self.development.is_enabled:
            print(f'[{self.status_label:^{self.status_width}}][{timestamp}][{self.source:^{self.source_width}}] {message}')

    def error(self, message, timestamp=None):
        """Prints an error message to console if development mode is enabled."""

        if timestamp is None:
            datetimestamp = datetime.datetime.now()
            timestamp = datetimestamp.time()

        if self.development.is_enabled:
            print(f'[{self.error_label:^{self.error_width}}][{timestamp}][{self.source:^{self.source_width}}] {message}')
