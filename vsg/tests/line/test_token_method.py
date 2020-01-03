
import unittest

from vsg import line

class testTokenMethod(unittest.TestCase):

    def test_single_spaces(self):
        oLine = line.line('contents of line')
        self.assertTrue(oLine)
        self.assertEqual('contents of line', oLine.line)

        lTokens = []
        lTokens.append('contents')
        lTokens.append(' ')
        lTokens.append('of')
        lTokens.append(' ')
        lTokens.append('line')

        self.assertEqual(lTokens, oLine.tokens)

    def test_multiple_spaces(self):
        oLine = line.line('   contents   of     line')
        self.assertTrue(oLine)
        self.assertEqual('   contents   of     line', oLine.line)

        lTokens = []
        lTokens.append('   ')
        lTokens.append('contents')
        lTokens.append('   ')
        lTokens.append('of')
        lTokens.append('     ')
        lTokens.append('line')

        self.assertEqual(lTokens, oLine.tokens)

    def test_comment_at_end_of_line_without_spaces_around_dashes(self):
        oLine = line.line('contents of line--This is a comment')
        self.assertTrue(oLine)
        self.assertEqual('contents of line--This is a comment', oLine.line)

        lTokens = []
        lTokens.append('contents')
        lTokens.append(' ')
        lTokens.append('of')
        lTokens.append(' ')
        lTokens.append('line')
        lTokens.append('--This is a comment')

        self.assertEqual(lTokens, oLine.tokens)

    def test_comment_at_end_of_line_with_spaces_around_dashes(self):
        oLine = line.line('contents of line --  This is a comment')
        self.assertTrue(oLine)
        self.assertEqual('contents of line --  This is a comment', oLine.line)

        lTokens = []
        lTokens.append('contents')
        lTokens.append(' ')
        lTokens.append('of')
        lTokens.append(' ')
        lTokens.append('line')
        lTokens.append(' ')
        lTokens.append('--  This is a comment')

        self.assertEqual(lTokens, oLine.tokens)

    def test_comment_at_end_of_line_with_spaces_at_the_end_of_line(self):
        oLine = line.line('contents of line --  This is a comment  ')
        self.assertTrue(oLine)
        self.assertEqual('contents of line --  This is a comment  ', oLine.line)

        lTokens = []
        lTokens.append('contents')
        lTokens.append(' ')
        lTokens.append('of')
        lTokens.append(' ')
        lTokens.append('line')
        lTokens.append(' ')
        lTokens.append('--  This is a comment  ')

        self.assertEqual(lTokens, oLine.tokens)

    def test_comment_only_line_with_spaces_before_the_comment(self):
        oLine = line.line(' -- This is a comment  ')
        self.assertTrue(oLine)
        self.assertEqual(' -- This is a comment  ', oLine.line)

        lTokens = []
        lTokens.append(' ')
        lTokens.append('-- This is a comment  ')

        self.assertEqual(lTokens, oLine.tokens)

    def test_comment_only_line_without_spaces_before_the_comment(self):
        oLine = line.line('-- This is a comment  ')
        self.assertTrue(oLine)
        self.assertEqual('-- This is a comment  ', oLine.line)

        lTokens = []
        lTokens.append('-- This is a comment  ')

        self.assertEqual(lTokens, oLine.tokens)

    def test_commas_without_spaces(self):
        oLine = line.line('this,will,test,commas,')
        self.assertTrue(oLine)
        self.assertEqual('this,will,test,commas,', oLine.line)

        lTokens = []
        lTokens.append('this')
        lTokens.append(',')
        lTokens.append('will')
        lTokens.append(',')
        lTokens.append('test')
        lTokens.append(',')
        lTokens.append('commas')
        lTokens.append(',')

        self.assertEqual(lTokens, oLine.tokens)

    def test_commas_without_spaces_with_comma_at_beginning_of_line(self):
        oLine = line.line(',this,will,test,commas,')
        self.assertTrue(oLine)
        self.assertEqual(',this,will,test,commas,', oLine.line)

        lTokens = []
        lTokens.append(',')
        lTokens.append('this')
        lTokens.append(',')
        lTokens.append('will')
        lTokens.append(',')
        lTokens.append('test')
        lTokens.append(',')
        lTokens.append('commas')
        lTokens.append(',')

        self.assertEqual(lTokens, oLine.tokens)

    def test_commas_with_spaces_with_comma_at_beginning_of_line(self):
        sString = '  ,  this  ,  will , test  , commas ,  '
        oLine = line.line(sString)
        self.assertTrue(oLine)
        self.assertEqual(sString, oLine.line)

        lTokens = []
        lTokens.append('  ')
        lTokens.append(',')
        lTokens.append('  ')
        lTokens.append('this')
        lTokens.append('  ')
        lTokens.append(',')
        lTokens.append('  ')
        lTokens.append('will')
        lTokens.append(' ')
        lTokens.append(',')
        lTokens.append(' ')
        lTokens.append('test')
        lTokens.append('  ')
        lTokens.append(',')
        lTokens.append(' ')
        lTokens.append('commas')
        lTokens.append(' ')
        lTokens.append(',')
        lTokens.append('  ')

        self.assertEqual(lTokens, oLine.tokens)

    def test_colons_without_spaces_with_colon_at_beginning_of_line(self):
        sString = ':this:will:test:colons:'
        oLine = line.line(sString)
        self.assertTrue(oLine)
        self.assertEqual(sString, oLine.line)

        lTokens = []
        lTokens.append(':')
        lTokens.append('this')
        lTokens.append(':')
        lTokens.append('will')
        lTokens.append(':')
        lTokens.append('test')
        lTokens.append(':')
        lTokens.append('colons')
        lTokens.append(':')

        self.assertEqual(lTokens, oLine.tokens)

    def test_colons_with_spaces_with_colon_at_beginning_of_line(self):
        sString = '  :  this  :  will : test  : commas :  '
        oLine = line.line(sString)
        self.assertTrue(oLine)
        self.assertEqual(sString, oLine.line)

        lTokens = []
        lTokens.append('  ')
        lTokens.append(':')
        lTokens.append('  ')
        lTokens.append('this')
        lTokens.append('  ')
        lTokens.append(':')
        lTokens.append('  ')
        lTokens.append('will')
        lTokens.append(' ')
        lTokens.append(':')
        lTokens.append(' ')
        lTokens.append('test')
        lTokens.append('  ')
        lTokens.append(':')
        lTokens.append(' ')
        lTokens.append('commas')
        lTokens.append(' ')
        lTokens.append(':')
        lTokens.append('  ')

        self.assertEqual(lTokens, oLine.tokens)

    def test_open_parenthesis_without_spaces_with_parenthesis_at_beginning_of_line(self):
        sString = '(this(will(test(colons('
        oLine = line.line(sString)
        self.assertTrue(oLine)
        self.assertEqual(sString, oLine.line)

        lTokens = []
        lTokens.append('(')
        lTokens.append('this')
        lTokens.append('(')
        lTokens.append('will')
        lTokens.append('(')
        lTokens.append('test')
        lTokens.append('(')
        lTokens.append('colons')
        lTokens.append('(')

        self.assertEqual(lTokens, oLine.tokens)

    def test_open_parenthesis_with_spaces_with_parenthesis_at_beginning_of_line(self):
        sString = '  (  this  (  will ( test  ( commas (  '
        oLine = line.line(sString)
        self.assertTrue(oLine)
        self.assertEqual(sString, oLine.line)

        lTokens = []
        lTokens.append('  ')
        lTokens.append('(')
        lTokens.append('  ')
        lTokens.append('this')
        lTokens.append('  ')
        lTokens.append('(')
        lTokens.append('  ')
        lTokens.append('will')
        lTokens.append(' ')
        lTokens.append('(')
        lTokens.append(' ')
        lTokens.append('test')
        lTokens.append('  ')
        lTokens.append('(')
        lTokens.append(' ')
        lTokens.append('commas')
        lTokens.append(' ')
        lTokens.append('(')
        lTokens.append('  ')

        self.assertEqual(lTokens, oLine.tokens)

    def test_close_parenthesis_without_spaces_with_parenthesis_at_beginning_of_line(self):
        sString = ')this)will)test)colons)'
        oLine = line.line(sString)
        self.assertTrue(oLine)
        self.assertEqual(sString, oLine.line)

        lTokens = []
        lTokens.append(')')
        lTokens.append('this')
        lTokens.append(')')
        lTokens.append('will')
        lTokens.append(')')
        lTokens.append('test')
        lTokens.append(')')
        lTokens.append('colons')
        lTokens.append(')')

        self.assertEqual(lTokens, oLine.tokens)

    def test_close_parenthesis_with_spaces_with_parenthesis_at_beginning_of_line(self):
        sString = '  )  this  )  will ) test  ) commas )  '
        oLine = line.line(sString)
        self.assertTrue(oLine)
        self.assertEqual(sString, oLine.line)

        lTokens = []
        lTokens.append('  ')
        lTokens.append(')')
        lTokens.append('  ')
        lTokens.append('this')
        lTokens.append('  ')
        lTokens.append(')')
        lTokens.append('  ')
        lTokens.append('will')
        lTokens.append(' ')
        lTokens.append(')')
        lTokens.append(' ')
        lTokens.append('test')
        lTokens.append('  ')
        lTokens.append(')')
        lTokens.append(' ')
        lTokens.append('commas')
        lTokens.append(' ')
        lTokens.append(')')
        lTokens.append('  ')

        self.assertEqual(lTokens, oLine.tokens)

    def test_single_quote_without_spaces_with_quote_at_beginning_of_line(self):
        sString = '\'this\'will\'test\'colons\''
        oLine = line.line(sString)
        self.assertTrue(oLine)
        self.assertEqual(sString, oLine.line)

        lTokens = []
        lTokens.append('\'')
        lTokens.append('this')
        lTokens.append('\'')
        lTokens.append('will')
        lTokens.append('\'')
        lTokens.append('test')
        lTokens.append('\'')
        lTokens.append('colons')
        lTokens.append('\'')

        self.assertEqual(lTokens, oLine.tokens)

    def test_double_quote_without_spaces_with_quote_at_beginning_of_line(self):
        sString = '"this"will"test"colons"'
        oLine = line.line(sString)
        self.assertTrue(oLine)
        self.assertEqual(sString, oLine.line)

        lTokens = []
        lTokens.append('"')
        lTokens.append('this')
        lTokens.append('"')
        lTokens.append('will')
        lTokens.append('"')
        lTokens.append('test')
        lTokens.append('"')
        lTokens.append('colons')
        lTokens.append('"')

        self.assertEqual(lTokens, oLine.tokens)

    def test_plus_without_spaces_with_plus_at_beginning_of_line(self):
        sString = '+this+will+test+colons+'
        oLine = line.line(sString)
        self.assertTrue(oLine)
        self.assertEqual(sString, oLine.line)

        lTokens = []
        lTokens.append('+')
        lTokens.append('this')
        lTokens.append('+')
        lTokens.append('will')
        lTokens.append('+')
        lTokens.append('test')
        lTokens.append('+')
        lTokens.append('colons')
        lTokens.append('+')

        self.assertEqual(lTokens, oLine.tokens)
