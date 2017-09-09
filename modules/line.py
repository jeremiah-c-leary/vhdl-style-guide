

class line():

    def __init__(self, line):
        self.line = line
        self.lineLower = line.lower()
        self.indentLevel = None
        ## Misc attributes
        self.isBlank = False
        self.isComment = False
        ## Library attributes
        self.isLibrary = False
        self.isLibraryUse = False
        ## Entity attributes
        self.insideEntity = False
        self.isEntityDeclaration = False
        self.isEndEntityDeclaration = False
        ## Port attributes
        self.insidePortMap = False
        self.isPortDeclaration = False
        self.isPortKeyword = False
        self.isEndPortMap = False
        ## Generic attributes
        self.insideGenericMap = False
        self.isGenericDeclaration = False
        self.isGenericKeyword = False
        self.isEndGenericMap = False
        ## Architecture attributes
        self.insideArchitecture = False
        self.isArchitectureBegin = False
        self.isArchitectureKeyword = False
        self.isEndArchitecture = False

