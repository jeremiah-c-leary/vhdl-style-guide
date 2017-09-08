

class line():

    def __init__(self, line):
        self.line = line
        self.lineLower = line.lower()
        self.indentLevel = None
        self.isBlank = False
        ## Library attributes
        self.isLibrary = False
        self.isLibraryUse = False
        self.isComment = False


