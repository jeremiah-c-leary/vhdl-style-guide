
from vsg import utilities


class line():
    '''
    This class holds line contents and attributes associated with the content.
    '''

    def __init__(self, line):
        self.line = line
        self.lineLower = line.lower()
        self.lineNoComment = utilities.remove_comment(line)

        self.indentLevel = None
        # Misc attributes
        self.isBlank = False
        # Comment attributes
        self.isComment = False
        self.hasComment = False
        self.hasInlineComment = False
        self.commentColumn = None
        # Library attributes
        self.isLibrary = False
        self.isLibraryUse = False
        # Entity attributes
        self.insideEntity = False
        self.isEntityDeclaration = False
        self.isEndEntityDeclaration = False
        # Port attributes
        self.insidePortMap = False
        self.isPortDeclaration = False
        self.isPortKeyword = False
        self.isEndPortMap = False
        # Generic attributes
        self.insideGenericMap = False
        self.isGenericDeclaration = False
        self.isGenericKeyword = False
        self.isEndGenericMap = False
        # Architecture attributes
        self.insideArchitecture = False
        self.isArchitectureBegin = False
        self.isArchitectureKeyword = False
        self.isEndArchitecture = False
        # Signal attributes
        self.isSignal = False
        # Constant attributes
        self.insideConstant = False
        self.isConstant = False
        self.isConstantEnd = False
        # Variable attributes
        self.isVariable = False
        # Process attributes
        self.insideProcess = False
        self.isProcessBegin = False
        self.isProcessKeyword = False
        self.isProcessLabel = False
        self.isProcessDeclarative = False
        self.isEndProcess = False
        self.insideSensitivityList = False
        self.isSensitivityListBegin = False
        self.isSensitivityListEnd = False
        # Concurrent attributes
        self.insideConcurrent = False
        self.isConcurrentBegin = False
        self.isEndConcurrent = False
        # If attributes
        self.insideIf = False
        self.isElseKeyword = False
        self.isElseIfKeyword = False
        self.isEndIfKeyword = False
        self.isIfEnd = False
        self.isIfKeyword = False
        self.isThenKeyword = False
        # Case attributes
        self.insideCase = False
        self.insideCaseWhen = False
        self.isCaseIsKeyword = False
        self.isCaseKeyword = False
        self.isCaseWhenEnd = False
        self.isCaseWhenKeyword = False
        self.isEndCaseKeyword = False
        self.isCaseNull = False
        # Sequential attributes
        self.insideSequential = False
        self.isSequentialEnd = False
        self.isSequential = False
        self.sequentialAlignmentColumn = None
        # Component attributes
        self.insideComponent = False
        self.isComponentDeclaration = False
        self.isComponentEnd = False
        # Instantiation attributes
        self.insideInstantiation = False
        self.isInstantiationDeclaration = False
        self.isDirectInstantiationDeclaration = False
        self.insideInstantiationPortMap = False
        self.isInstantiationPortKeyword = False
        self.isInstantiationPortEnd = False
        self.isInstantiationPortAssignment = False
        self.insideInstantiationGenericMap = False
        self.isInstantiationGenericKeyword = False
        self.isInstantiationGenericEnd = False
        self.isInstantiationGenericAssignment = False
        # Package attributes
        self.insidePackage = False
        self.isPackageKeyword = False
        self.isPackageEnd = False
        # Package Body attributes
        self.insidePackageBody = False
        self.isPackageBodyKeyword = False
        self.isPackageBodyEnd = False
        # Generate attributes
        self.insideGenerate = False
        self.isGenerateBegin = False
        self.isGenerateKeyword = False
        self.isGenerateEnd = False
        # Function attributes
        self.insideFunction = False
        self.insideFunctionDeclarative = False
        self.isFunctionParameter = False
        self.isFunctionParameterEnd = False
        self.isFunctionBegin = False
        self.isFunctionKeyword = False
        self.isFunctionEnd = False
        self.isFunctionReturn = False
        self.isFunctionReturnKeyword = False
        self.isFunctionIs = False
        # For Loop attributes
        self.insideForLoop = False
        self.isForLoopKeyword = False
        self.isForLoopEnd = False
        # While Loop attributes
        self.insideWhileLoop = False
        self.isWhileLoopKeyword = False
        self.isWhileLoopEnd = False
        # Type attributes
        self.isTypeKeyword = False
        self.isTypeEnd = False
        # Subtype attributes
        self.insideSubtype = False
        self.isSubtypeKeyword = False
        self.isSubtypeEnd = False
        # Enumerated Type attributes
        self.insideTypeEnumerated = False
        self.isTypeEnumeratedKeyword = False
        self.isTypeEnumeratedEnd = False
        # Type Array attributes
        self.insideTypeArray = False
        self.isTypeArrayKeyword = False
        self.isTypeArrayEnd = False
        # Type Record attributes
        self.insideTypeRecord = False
        self.isTypeRecordKeyword = False
        self.isTypeRecordEnd = False
        # Variable Assignment attributes
        self.insideVariableAssignment = False
        self.isVariableAssignmentEnd = False
        self.isVariableAssignment = False
        self.variableAssignmentAlignmentColumn = None
        # Assert attributes
        self.isAssertKeyword = False
        self.isAssertEnd = False
        self.insideAssert = False
        # With attributes
        self.isWithKeyword = False
        # Attribute attributes
        self.isAttributeKeyword = False
        self.isAttributeEnd = False
        self.insideAttribute = False
        # File attributes
        self.isFileKeyword = False
        self.isFileEnd = False
        self.insideFile = False
        # Procedure attributes
        self.insideProcedure = False
        self.insideProcedureDeclarative = False
        self.isProcedureParameter = False
        self.isProcedureParameterEnd = False
        self.isProcedureBegin = False
        self.isProcedureKeyword = False
        self.isProcedureEnd = False
        self.isProcedureReturn = False
        self.isProcedureIs = False

    def update_line(self, sLine):
        '''
        This method updates the line, lineLower and lineNoComment attributes.
        '''
        self.line = sLine
        self.lineLower = sLine.lower()
        self.lineNoComment = utilities.remove_comment(sLine)


class blank_line(line):
    '''
    This class provides a blank line version of the line class.
    '''
    def __init__(self):
        line.__init__(self, '')
        self.isBlank = True
