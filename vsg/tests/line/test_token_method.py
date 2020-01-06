
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

    def test_colon_equal_without_spaces_with_one_at_beginning_of_line(self):
        sString = ':=this:=will:=test:=colons:='
        oLine = line.line(sString)
        self.assertTrue(oLine)
        self.assertEqual(sString, oLine.line)

        lTokens = []
        lTokens.append(':=')
        lTokens.append('this')
        lTokens.append(':=')
        lTokens.append('will')
        lTokens.append(':=')
        lTokens.append('test')
        lTokens.append(':=')
        lTokens.append('colons')
        lTokens.append(':=')

        self.assertEqual(lTokens, oLine.tokens)

    def test_star_star_without_spaces_with_one_at_beginning_of_line(self):
        sString = '**this**will**test**colons**'
        oLine = line.line(sString)
        self.assertTrue(oLine)
        self.assertEqual(sString, oLine.line)

        lTokens = []
        lTokens.append('**')
        lTokens.append('this')
        lTokens.append('**')
        lTokens.append('will')
        lTokens.append('**')
        lTokens.append('test')
        lTokens.append('**')
        lTokens.append('colons')
        lTokens.append('**')

        self.assertEqual(lTokens, oLine.tokens)

    def test_not_equal_without_spaces_with_one_at_beginning_of_line(self):
        sString = '\=this\=will\=test\=colons\='
        oLine = line.line(sString)
        self.assertTrue(oLine)
        self.assertEqual(sString, oLine.line)

        lTokens = []
        lTokens.append('\=')
        lTokens.append('this')
        lTokens.append('\=')
        lTokens.append('will')
        lTokens.append('\=')
        lTokens.append('test')
        lTokens.append('\=')
        lTokens.append('colons')
        lTokens.append('\=')

        self.assertEqual(lTokens, oLine.tokens)

    def test_lessthan_equal_without_spaces_with_one_at_beginning_of_line(self):
        sString = '<=this<=will<=test<=colons<='
        oLine = line.line(sString)
        self.assertTrue(oLine)
        self.assertEqual(sString, oLine.line)

        lTokens = []
        lTokens.append('<=')
        lTokens.append('this')
        lTokens.append('<=')
        lTokens.append('will')
        lTokens.append('<=')
        lTokens.append('test')
        lTokens.append('<=')
        lTokens.append('colons')
        lTokens.append('<=')

        self.assertEqual(lTokens, oLine.tokens)

    def test_equal_greaterthan_without_spaces_with_one_at_beginning_of_line(self):
        sString = '=>this=>will=>test=>colons=>'
        oLine = line.line(sString)
        self.assertTrue(oLine)
        self.assertEqual(sString, oLine.line)

        lTokens = []
        lTokens.append('=>')
        lTokens.append('this')
        lTokens.append('=>')
        lTokens.append('will')
        lTokens.append('=>')
        lTokens.append('test')
        lTokens.append('=>')
        lTokens.append('colons')
        lTokens.append('=>')

        self.assertEqual(lTokens, oLine.tokens)

    def test_greaterthan_equal_without_spaces_with_one_at_beginning_of_line(self):
        sString = '>=this>=will>=test>=colons>='
        oLine = line.line(sString)
        self.assertTrue(oLine)
        self.assertEqual(sString, oLine.line)

        lTokens = []
        lTokens.append('>=')
        lTokens.append('this')
        lTokens.append('>=')
        lTokens.append('will')
        lTokens.append('>=')
        lTokens.append('test')
        lTokens.append('>=')
        lTokens.append('colons')
        lTokens.append('>=')

        self.assertEqual(lTokens, oLine.tokens)

    def test_multiple_symbols_on_single_line_1(self):
        sString = 'variable We1, We2, We3, Wy : BIT := \'1\';'
        oLine = line.line(sString)
        self.assertTrue(oLine)
        self.assertEqual(sString, oLine.line)

        lTokens = []
        lTokens.append('variable')
        lTokens.append(' ')
        lTokens.append('We1')
        lTokens.append(',')
        lTokens.append(' ')
        lTokens.append('We2')
        lTokens.append(',')
        lTokens.append(' ')
        lTokens.append('We3')
        lTokens.append(',')
        lTokens.append(' ')
        lTokens.append('Wy')
        lTokens.append(' ')
        lTokens.append(':')
        lTokens.append(' ')
        lTokens.append('BIT')
        lTokens.append(' ')
        lTokens.append(':=')
        lTokens.append(' ')
        lTokens.append('\'')
        lTokens.append('1')
        lTokens.append('\'')
        lTokens.append(';')

        self.assertEqual(lTokens, oLine.tokens)

    def test_multiple_symbols_on_single_line_2(self):
        sString = '    DI_I          : in    std_logic_vector(N - 1 downto 0) := (others => \'X\');    -- parallel data in'
        oLine = line.line(sString)
        self.assertTrue(oLine)
        self.assertEqual(sString, oLine.line)

        lTokens = []
        lTokens.append('    ')
        lTokens.append('DI_I')
        lTokens.append('          ')
        lTokens.append(':')
        lTokens.append(' ')
        lTokens.append('in')
        lTokens.append('    ')
        lTokens.append('std_logic_vector')
        lTokens.append('(')
        lTokens.append('N')
        lTokens.append(' ')
        lTokens.append('-')
        lTokens.append(' ')
        lTokens.append('1')
        lTokens.append(' ')
        lTokens.append('downto')
        lTokens.append(' ')
        lTokens.append('0')
        lTokens.append(')')
        lTokens.append(' ')
        lTokens.append(':=')
        lTokens.append(' ')
        lTokens.append('(')
        lTokens.append('others')
        lTokens.append(' ')
        lTokens.append('=>')
        lTokens.append(' ')
        lTokens.append('\'')
        lTokens.append('X')
        lTokens.append('\'')
        lTokens.append(')')
        lTokens.append(';')
        lTokens.append('    ')
        lTokens.append('-- parallel data in')

        self.assertEqual(lTokens, oLine.tokens)
