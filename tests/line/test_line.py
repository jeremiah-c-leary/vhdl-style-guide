
#from .context import modules
import unittest

from modules import line

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

    def test_comment_attribute(self):
        oLine = line.line('contents of line')
        self.assertFalse(oLine.isComment)
        oLine.isComment = True
        self.assertTrue(oLine.isComment)

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

if __name__ == '__main__':
    unittest.main()
