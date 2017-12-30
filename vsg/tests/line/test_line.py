
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

    def test_hasInlineComment_attribute(self):
        oLine = line.line('contents of line')
        self.assertFalse(oLine.hasInlineComment)
        oLine.hasInlineComment = True
        self.assertTrue(oLine.hasInlineComment)

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

    def test_insideConstant_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.insideConstant, False)
        oLine.insideConstant = True
        self.assertEqual(oLine.insideConstant, True)

    def test_isConstantEnd_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isConstantEnd, False)
        oLine.isConstantEnd = True
        self.assertEqual(oLine.isConstantEnd, True)

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

    def test_isProcessLabel_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isProcessLabel, False)
        oLine.isProcessLabel = True
        self.assertEqual(oLine.isProcessLabel, True)

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

    def test_insideCase_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.insideCase, False)
        oLine.insideCase = True
        self.assertEqual(oLine.insideCase, True)

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

    def test_isCaseNull_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isCaseNull, False)
        oLine.isCaseNull = True
        self.assertEqual(oLine.isCaseNull, True)

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

    def test_Directinstantiation_declaration_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isDirectInstantiationDeclaration, False)
        oLine.isDirectInstantiationDeclaration = True
        self.assertEqual(oLine.isDirectInstantiationDeclaration, True)

    def test_inside_instantiation_port_map_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.insideInstantiationPortMap, False)
        oLine.insideInstantiationPortMap = True
        self.assertEqual(oLine.insideInstantiationPortMap, True)

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

    def test_inside_instantiation_generic_map_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.insideInstantiationGenericMap, False)
        oLine.insideInstantiationGenericMap = True
        self.assertEqual(oLine.insideInstantiationGenericMap, True)

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

    def test_insideFunctionDeclarative_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.insideFunctionDeclarative, False)
        oLine.insideFunctionDeclarative = True
        self.assertEqual(oLine.insideFunctionDeclarative, True)

    def test_isFunctionParameter_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isFunctionParameter, False)
        oLine.isFunctionParameter = True
        self.assertEqual(oLine.isFunctionParameter, True)

    def test_isFunctionParameterEnd_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isFunctionParameterEnd, False)
        oLine.isFunctionParameterEnd = True
        self.assertEqual(oLine.isFunctionParameterEnd, True)

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

    def test_isFunctionReturnKeyword_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isFunctionReturnKeyword, False)
        oLine.isFunctionReturnKeyword = True
        self.assertEqual(oLine.isFunctionReturnKeyword, True)

    def test_isFunctionReturn_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isFunctionReturn, False)
        oLine.isFunctionReturn = True
        self.assertEqual(oLine.isFunctionReturn, True)

    def test_isFunctionIs_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isFunctionIs, False)
        oLine.isFunctionIs= True
        self.assertEqual(oLine.isFunctionIs, True)

    def test_insideForLoop_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.insideForLoop, False)
        oLine.insideForLoop = True
        self.assertEqual(oLine.insideForLoop, True)

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

    def test_insideWhileLoop_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.insideWhileLoop, False)
        oLine.insideWhileLoop = True
        self.assertEqual(oLine.insideWhileLoop, True)

    def test_isWhileLoopKeyword_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isWhileLoopKeyword, False)
        oLine.isWhileLoopKeyword = True
        self.assertEqual(oLine.isWhileLoopKeyword, True)

    def test_isWhileLoopEnd_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isWhileLoopEnd, False)
        oLine.isWhileLoopEnd = True
        self.assertEqual(oLine.isWhileLoopEnd, True)

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

    def test_isTypeEnumeratedEnd_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isTypeEnumeratedEnd, False)
        oLine.isTypeEnumeratedEnd = True
        self.assertEqual(oLine.isTypeEnumeratedEnd, True)

    def test_isTypeEnumeratedKeyword_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isTypeEnumeratedKeyword, False)
        oLine.isTypeEnumeratedKeyword = True
        self.assertEqual(oLine.isTypeEnumeratedKeyword, True)

    def test_insideTypeEnumerated_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.insideTypeEnumerated, False)
        oLine.insideTypeEnumerated = True
        self.assertEqual(oLine.insideTypeEnumerated, True)

    def test_isSubtypeEnd_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isSubtypeEnd, False)
        oLine.isSubtypeEnd = True
        self.assertEqual(oLine.isSubtypeEnd, True)

    def test_isSubtypeKeyword_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isSubtypeKeyword, False)
        oLine.isSubtypeKeyword = True
        self.assertEqual(oLine.isSubtypeKeyword, True)

    def test_insideSubtype_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.insideSubtype, False)
        oLine.insideSubtype= True
        self.assertEqual(oLine.insideSubtype, True)

    def test_isTypeArrayEnd_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isTypeArrayEnd, False)
        oLine.isTypeArrayEnd = True
        self.assertEqual(oLine.isTypeArrayEnd, True)

    def test_isTypeArrayKeyword_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isTypeArrayKeyword, False)
        oLine.isTypeArrayKeyword = True
        self.assertEqual(oLine.isTypeArrayKeyword, True)

    def test_insideTypeArray_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.insideTypeArray, False)
        oLine.insideTypeArray= True
        self.assertEqual(oLine.insideTypeArray, True)

    def test_isTypeRecordEnd_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isTypeRecordEnd, False)
        oLine.isTypeRecordEnd = True
        self.assertEqual(oLine.isTypeRecordEnd, True)

    def test_isTypeRecordKeyword_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isTypeRecordKeyword, False)
        oLine.isTypeRecordKeyword = True
        self.assertEqual(oLine.isTypeRecordKeyword, True)

    def test_insideTypeRecord_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.insideTypeRecord, False)
        oLine.insideTypeRecord= True
        self.assertEqual(oLine.insideTypeRecord, True)

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

    def test_isAssertKeyword_attribute(self):
        oLine = line.line('contents of Line')
        self.assertFalse(oLine.isAssertKeyword)
        oLine.isAssertKeyword = True
        self.assertTrue(oLine.isAssertKeyword)

    def test_isAssertEnd_attribute(self):
        oLine = line.line('contents of Line')
        self.assertFalse(oLine.isAssertEnd)
        oLine.isAssertEnd = True
        self.assertTrue(oLine.isAssertEnd)

    def test_insideAssert_attribute(self):
        oLine = line.line('contents of Line')
        self.assertFalse(oLine.insideAssert)
        oLine.insideAssert = True
        self.assertTrue(oLine.insideAssert)

    def test_isWithKeyword_attribute(self):
        oLine = line.line('contents of Line')
        self.assertFalse(oLine.isWithKeyword)
        oLine.isWithKeyword = True
        self.assertTrue(oLine.isWithKeyword)

    def test_isAttributeKeyword_attribute(self):
        oLine = line.line('contents of Line')
        self.assertFalse(oLine.isAttributeKeyword)
        oLine.isAttributeKeyword = True
        self.assertTrue(oLine.isAttributeKeyword)

    def test_isAttributeEnd_attribute(self):
        oLine = line.line('contents of Line')
        self.assertFalse(oLine.isAttributeEnd)
        oLine.isAttributeEnd = True
        self.assertTrue(oLine.isAttributeEnd)

    def test_insideAttribute_attribute(self):
        oLine = line.line('contents of Line')
        self.assertFalse(oLine.insideAttribute)
        oLine.insideAttribute = True
        self.assertTrue(oLine.insideAttribute)

    def test_isFileKeyword_attribute(self):
        oLine = line.line('contents of Line')
        self.assertFalse(oLine.isFileKeyword)
        oLine.isFileKeyword = True
        self.assertTrue(oLine.isFileKeyword)

    def test_isFileEnd_attribute(self):
        oLine = line.line('contents of Line')
        self.assertFalse(oLine.isFileEnd)
        oLine.isFileEnd = True
        self.assertTrue(oLine.isFileEnd)

    def test_insideFile_attribute(self):
        oLine = line.line('contents of Line')
        self.assertFalse(oLine.insideFile)
        oLine.insideFile = True
        self.assertTrue(oLine.insideFile)

    def test_insideProcedure_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.insideProcedure, False)
        oLine.insideProcedure = True
        self.assertEqual(oLine.insideProcedure, True)

    def test_insideProcedureDeclarative_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.insideProcedureDeclarative, False)
        oLine.insideProcedureDeclarative = True
        self.assertEqual(oLine.insideProcedureDeclarative, True)

    def test_isProcedureParameter_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isProcedureParameter, False)
        oLine.isProcedureParameter = True
        self.assertEqual(oLine.isProcedureParameter, True)

    def test_isProcedureParameterEnd_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isProcedureParameterEnd, False)
        oLine.isProcedureParameterEnd = True
        self.assertEqual(oLine.isProcedureParameterEnd, True)

    def test_isProcedureBegin_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isProcedureBegin, False)
        oLine.isProcedureBegin = True
        self.assertEqual(oLine.isProcedureBegin, True)

    def test_isProcedureKeyword_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isProcedureKeyword, False)
        oLine.isProcedureKeyword = True
        self.assertEqual(oLine.isProcedureKeyword, True)

    def test_isProcedureEnd_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isProcedureEnd, False)
        oLine.isProcedureEnd = True
        self.assertEqual(oLine.isProcedureEnd, True)

    def test_isProcedureReturn_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isProcedureReturn, False)
        oLine.isProcedureReturn = True
        self.assertEqual(oLine.isProcedureReturn, True)

    def test_isProcedureIs_attribute(self):
        oLine = line.line('contents of Line')
        self.assertEqual(oLine.isProcedureIs, False)
        oLine.isProcedureIs = True
        self.assertEqual(oLine.isProcedureIs, True)
