import os

class File():
    """Represents a file on disk."""
    def __init__(self, path):
        """
        Creates a representation of a File object.

        Arguments:
        path -- a string containing a path to the target file. Any valid path
        representation can be provided (both relative path and absolute path).
        """

        # file paths
        self.path = path
        self.abspath = os.path.abspath(path)
        self.directory = os.path.dirname(self.abspath)
        self.parent = os.path.basename(self.directory)

        # file attributes
        self.filename = os.path.basename(self.abspath)
        self.name = os.path.splitext(self.filename)[0]
        self.extension = os.path.splitext(self.filename)[-1]
        self.valid = os.path.exists(self.abspath)
