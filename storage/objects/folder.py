import os

class Folder():
    """Represents a folder on disk."""
    def __init__(self, path):
        """
        Creates a representation of a Folder.

        Arguments:
        path -- a string containing a path to the target folder. Any valid path
        representation can be provided (both relative path and absolute path).
        """

        # folder path attributes
        self.path = path
        self.abspath = os.path.abspath(self.path)
        self.directory = os.path.dirname(self.abspath)
        self.parent = os.path.basename(self.directory)

        # folder attributes
        self.name = os.path.basename(self.abspath)
        self.valid = os.path.exists(self.abspath)

        # folder content attributes
        self.contents = os.listdir(self.abspath)

        if not os.path.exists(self.abspath):
            os.mkdir(self.abspath)
