
#from .context import vsg
import unittest

from vsg import line

class testLineMethods(unittest.TestCase):

    def test_line_class_exists(self):
        oLine = line.line('contents of line')
        self.assertTrue(oLine)
        self.assertEqual(oLine.line, 'contents of line')

    def test_blank_line_attribute(self):
        oLine = line.line('contents of line')
        self.assertFalse(oLine.isBlank)
        oLine.isBlank = True
        self.assertTrue(oLine.isBlank)

    def test_library_attribute(self):
        oLine = line.line('contents of line')
        self.assertFalse(oLine.isLibrary)
        oLine.isLibrary = True
        self.assertTrue(oLine.isLibrary)
    
    def test_library_use_attribute(self):
        oLine = line.line('contents of line')
        self.assertFalse(oLine.isLibraryUse)
        oLine.isLibraryUse = True
        self.assertTrue(oLine.isLibraryUse)

    def test_isComment_attribute(self):
        oLine = line.line('contents of line')
        self.assertFalse(oLine.isComment)
        oLine.isComment = True
        self.assertTrue(oLine.isComment)

    def test_hasComment_attribute(self):
        oLine = line.line('contents of line')
        self.assertFalse(oLine.hasComment)
        oLine.hasComment = True
        self.assertTrue(oLine.hasComment)

    def test_commentColumn_attribute(self):
        oLine = line.line('contents of line')
        self.assertEqual(oLine.commentColumn, None)
        oLine.commentColumn = 20
        self.assertEqual(oLine.commentColumn, 20)

    def test_line_lowering_attribute(self):
        oLine = line.line('ContenTs oF Line')
        self.assertEqual(oLine.lineLower, 'contents of line')

    def test_indentLevel_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.indentLevel, None)
        oLine.indentLevel = 10
        self.assertEqual(oLine.indentLevel, 10)

    def test_entity_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.insideEntity, False)
        oLine.insideEntity = True
        self.assertEqual(oLine.insideEntity, True)

    def test_inside_entity_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.insideEntity, False)
        oLine.insideEntity = True
        self.assertEqual(oLine.insideEntity, True)

    def test_entity_declaration_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isEntityDeclaration, False)
        oLine.isEntityDeclaration = True
        self.assertEqual(oLine.isEntityDeclaration, True)

    def test_end_entity_declaration_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isEndEntityDeclaration, False)
        oLine.isEndEntityDeclaration = True
        self.assertEqual(oLine.isEndEntityDeclaration, True)

    def test_inside_port_map_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.insidePortMap, False)
        oLine.insidePortMap = True
        self.assertEqual(oLine.insidePortMap, True)

    def test_isPortDeclaration_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isPortDeclaration, False)
        oLine.isPortDeclaration = True
        self.assertEqual(oLine.isPortDeclaration, True)

    def test_isPortKeyword_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isPortKeyword, False)
        oLine.isPortKeyword = True
        self.assertEqual(oLine.isPortKeyword, True)

    def test_isEndPortMap_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isEndPortMap, False)
        oLine.isEndPortMap = True
        self.assertEqual(oLine.isEndPortMap, True)

    def test_inside_generic_map_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.insideGenericMap, False)
        oLine.insideGenericMap = True
        self.assertEqual(oLine.insideGenericMap, True)

    def test_generic_declaration_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isGenericDeclaration, False)
        oLine.isGenericDeclaration = True
        self.assertEqual(oLine.isGenericDeclaration, True)

    def test_isGenericKeyword_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isGenericKeyword, False)
        oLine.isGenericKeyword = True
        self.assertEqual(oLine.isGenericKeyword, True)

    def test_isEndGenericMap_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isEndGenericMap, False)
        oLine.isEndGenericMap = True
        self.assertEqual(oLine.isEndGenericMap, True)

    def test_inside_architecture_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.insideArchitecture, False)
        oLine.insideArchitecture = True
        self.assertEqual(oLine.insideArchitecture, True)

    def test_isArchitectureBegin_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isArchitectureBegin, False)
        oLine.isArchitectureBegin = True
        self.assertEqual(oLine.isArchitectureBegin, True)

    def test_isArchitectureKeyword_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isArchitectureKeyword, False)
        oLine.isArchitectureKeyword = True
        self.assertEqual(oLine.isArchitectureKeyword, True)

    def test_isEndArchitecture_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isEndArchitecture, False)
        oLine.isEndArchitecture = True
        self.assertEqual(oLine.isEndArchitecture, True)

    def test_isSignal_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isSignal, False)
        oLine.isSignal = True
        self.assertEqual(oLine.isSignal, True)

    def test_isConstant_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isConstant, False)
        oLine.isConstant = True
        self.assertEqual(oLine.isConstant, True)

    def test_insideProcess_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.insideProcess, False)
        oLine.insideProcess = True
        self.assertEqual(oLine.insideProcess, True)

    def test_isProcessBegin_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isProcessBegin, False)
        oLine.isProcessBegin = True
        self.assertEqual(oLine.isProcessBegin, True)

    def test_isProcessKeyword_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isProcessKeyword, False)
        oLine.isProcessKeyword = True
        self.assertEqual(oLine.isProcessKeyword, True)

    def test_isEndProcess_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isEndProcess, False)
        oLine.isEndProcess = True
        self.assertEqual(oLine.isEndProcess, True)

    def test_isProcessDeclarative_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isProcessDeclarative, False)
        oLine.isProcessDeclarative = True
        self.assertEqual(oLine.isProcessDeclarative, True)

    def test_insideSensitivityList_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.insideSensitivityList, False)
        oLine.insideSensitivityList = True
        self.assertEqual(oLine.insideSensitivityList, True)

    def test_isSensitivityListBegin_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isSensitivityListBegin, False)
        oLine.isSensitivityListBegin = True
        self.assertEqual(oLine.isSensitivityListBegin, True)

    def test_isSensitivityListEnd_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isSensitivityListEnd, False)
        oLine.isSensitivityListEnd = True
        self.assertEqual(oLine.isSensitivityListEnd, True)

    def test_insideConcurrent_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.insideConcurrent, False)
        oLine.insideConcurrent = True
        self.assertEqual(oLine.insideConcurrent, True)

    def test_isConcurrentBegin_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isConcurrentBegin, False)
        oLine.isConcurrentBegin = True
        self.assertEqual(oLine.isConcurrentBegin, True)

    def test_isEndConcurrent_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isEndConcurrent, False)
        oLine.isEndConcurrent = True
        self.assertEqual(oLine.isEndConcurrent, True)

    def test_insideIf_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.insideIf, False)
        oLine.insideIf= True
        self.assertEqual(oLine.insideIf, True)

    def test_isIfKeyword_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isIfKeyword, False)
        oLine.isIfKeyword = True
        self.assertEqual(oLine.isIfKeyword, True)

    def test_isThenKeyword_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isThenKeyword, False)
        oLine.isThenKeyword = True
        self.assertEqual(oLine.isThenKeyword, True)

    def test_isElseIfKeyword_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isElseIfKeyword, False)
        oLine.isElseIfKeyword = True
        self.assertEqual(oLine.isElseIfKeyword, True)

    def test_isEndIfKeyword_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isEndIfKeyword, False)
        oLine.isEndIfKeyword = True
        self.assertEqual(oLine.isEndIfKeyword, True)

    def test_isIfEnd_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isIfEnd, False)
        oLine.isIfEnd = True
        self.assertEqual(oLine.isIfEnd, True)

    def test_isElseKeyword_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isElseKeyword, False)
        oLine.isElseKeyword = True
        self.assertEqual(oLine.isElseKeyword, True)

    def test_isCaseKeyword_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isCaseKeyword, False)
        oLine.isCaseKeyword = True
        self.assertEqual(oLine.isCaseKeyword, True)

    def test_isCaseWhenKeyword_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isCaseWhenKeyword, False)
        oLine.isCaseWhenKeyword = True
        self.assertEqual(oLine.isCaseWhenKeyword, True)

    def test_isCaseWhenEnd_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isCaseWhenEnd, False)
        oLine.isCaseWhenEnd = True
        self.assertEqual(oLine.isCaseWhenEnd, True)

    def test_insideCaseWhen_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.insideCaseWhen, False)
        oLine.insideCaseWhen = True
        self.assertEqual(oLine.insideCaseWhen, True)

    def test_isEndCaseKeyword_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isEndCaseKeyword, False)
        oLine.isEndCaseKeyword = True
        self.assertEqual(oLine.isEndCaseKeyword, True)

    def test_isCaseIsKeyword_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isCaseIsKeyword, False)
        oLine.isCaseIsKeyword = True
        self.assertEqual(oLine.isCaseIsKeyword, True)

    def test_insideSequential_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.insideSequential, False)
        oLine.insideSequential = True
        self.assertEqual(oLine.insideSequential, True)

    def test_isSequential_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isSequential, False)
        oLine.isSequential = True
        self.assertEqual(oLine.isSequential, True)

    def test_isSequentialEnd_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isSequentialEnd, False)
        oLine.isSequentialEnd = True
        self.assertEqual(oLine.isSequentialEnd, True)

    def test_sequentialAlignmentColumn_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.sequentialAlignmentColumn, None)
        oLine.sequentialAlignmentColumn = 32
        self.assertEqual(oLine.sequentialAlignmentColumn, 32)

    def test_inside_component_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.insideComponent, False)
        oLine.insideComponent = True
        self.assertEqual(oLine.insideComponent, True)

    def test_component_declaration_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isComponentDeclaration, False)
        oLine.isComponentDeclaration = True
        self.assertEqual(oLine.isComponentDeclaration, True)

    def test_end_component_declaration_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isComponentEnd, False)
        oLine.isComponentEnd = True
        self.assertEqual(oLine.isComponentEnd, True)

    def test_inside_instantiation_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.insideInstantiation, False)
        oLine.insideInstantiation = True
        self.assertEqual(oLine.insideInstantiation, True)

    def test_instantiation_declaration_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isInstantiationDeclaration, False)
        oLine.isInstantiationDeclaration = True
        self.assertEqual(oLine.isInstantiationDeclaration, True)

    def test_instantiation_port_keyword_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isInstantiationPortKeyword, False)
        oLine.isInstantiationPortKeyword = True
        self.assertEqual(oLine.isInstantiationPortKeyword, True)

    def test_instantiation_port_end_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isInstantiationPortEnd, False)
        oLine.isInstantiationPortEnd= True
        self.assertEqual(oLine.isInstantiationPortEnd, True)

    def test_instantiation_port_assignment_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isInstantiationPortAssignment, False)
        oLine.isInstantiationPortAssignment= True
        self.assertEqual(oLine.isInstantiationPortAssignment, True)

    def test_instantiation_generic_keyword_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isInstantiationGenericKeyword, False)
        oLine.isInstantiationGenericKeyword = True
        self.assertEqual(oLine.isInstantiationGenericKeyword, True)

    def test_instantiation_generic_end_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isInstantiationGenericEnd, False)
        oLine.isInstantiationGenericEnd= True
        self.assertEqual(oLine.isInstantiationGenericEnd, True)

    def test_instantiation_generic_assignment_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isInstantiationGenericAssignment, False)
        oLine.isInstantiationGenericAssignment= True
        self.assertEqual(oLine.isInstantiationGenericAssignment, True)

    def test_inside_package_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.insidePackage, False)
        oLine.insidePackage = True
        self.assertEqual(oLine.insidePackage, True)

    def test_isPackageKeyword_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isPackageKeyword, False)
        oLine.isPackageKeyword = True
        self.assertEqual(oLine.isPackageKeyword, True)

    def test_isPackageEnd_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isPackageEnd, False)
        oLine.isPackageEnd = True
        self.assertEqual(oLine.isPackageEnd, True)

    def test_inside_packageBody_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.insidePackageBody, False)
        oLine.insidePackageBody = True
        self.assertEqual(oLine.insidePackageBody, True)

    def test_isPackageBodyKeyword_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isPackageBodyKeyword, False)
        oLine.isPackageBodyKeyword = True
        self.assertEqual(oLine.isPackageBodyKeyword, True)

    def test_isPackageBodyEnd_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isPackageBodyEnd, False)
        oLine.isPackageBodyEnd = True
        self.assertEqual(oLine.isPackageBodyEnd, True)

    def test_insideGenerate_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.insideGenerate, False)
        oLine.insideGenerate = True
        self.assertEqual(oLine.insideGenerate, True)

    def test_isGenerateBegin_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isGenerateBegin, False)
        oLine.isGenerateBegin = True
        self.assertEqual(oLine.isGenerateBegin, True)

    def test_isGenerateKeyword_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isGenerateKeyword, False)
        oLine.isGenerateKeyword = True
        self.assertEqual(oLine.isGenerateKeyword, True)

    def test_isGenerateEnd_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isGenerateEnd, False)
        oLine.isGenerateEnd = True
        self.assertEqual(oLine.isGenerateEnd, True)

    def test_insideFunction_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.insideFunction, False)
        oLine.insideFunction = True
        self.assertEqual(oLine.insideFunction, True)

    def test_isFunctionBegin_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isFunctionBegin, False)
        oLine.isFunctionBegin = True
        self.assertEqual(oLine.isFunctionBegin, True)

    def test_isFunctionKeyword_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isFunctionKeyword, False)
        oLine.isFunctionKeyword = True
        self.assertEqual(oLine.isFunctionKeyword, True)

    def test_isFunctionEnd_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isFunctionEnd, False)
        oLine.isFunctionEnd = True
        self.assertEqual(oLine.isFunctionEnd, True)

    def test_isFunctionReturn_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isFunctionReturn, False)
        oLine.isFunctionReturn = True
        self.assertEqual(oLine.isFunctionReturn, True)

    def test_isForLoopKeyword_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isForLoopKeyword, False)
        oLine.isForLoopKeyword = True
        self.assertEqual(oLine.isForLoopKeyword, True)

    def test_isForLoopEnd_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isForLoopEnd, False)
        oLine.isForLoopEnd = True
        self.assertEqual(oLine.isForLoopEnd, True)

    def test_isTypeEnd_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isTypeEnd, False)
        oLine.isTypeEnd = True
        self.assertEqual(oLine.isTypeEnd, True)

    def test_isTypeKeyword_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isTypeKeyword, False)
        oLine.isTypeKeyword = True
        self.assertEqual(oLine.isTypeKeyword, True)

    def test_insideType_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.insideType, False)
        oLine.insideType= True
        self.assertEqual(oLine.insideType, True)

    def test_isVariable_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isVariable, False)
        oLine.isVariable = True
        self.assertEqual(oLine.isVariable, True)

    def test_insideVariableAssignment_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.insideVariableAssignment, False)
        oLine.insideVariableAssignment = True
        self.assertEqual(oLine.insideVariableAssignment, True)

    def test_isVariableAssignment_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isVariableAssignment, False)
        oLine.isVariableAssignment = True
        self.assertEqual(oLine.isVariableAssignment, True)

    def test_isVariableAssignmentEnd_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isVariableAssignmentEnd, False)
        oLine.isVariableAssignmentEnd = True
        self.assertEqual(oLine.isVariableAssignmentEnd, True)

    def test_variableAssignmentAlignmentColumn_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.variableAssignmentAlignmentColumn, None)
        oLine.variableAssignmentAlignmentColumn = 32
        self.assertEqual(oLine.variableAssignmentAlignmentColumn, 32)
