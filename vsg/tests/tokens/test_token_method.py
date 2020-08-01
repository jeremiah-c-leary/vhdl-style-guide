
import unittest

from vsg import line

class testTokenMethod(unittest.TestCase):

    def test_single_spaces(self):
        oLine = line.line('contents of line')
        self.assertTrue(oLine)
        self.assertEqual('contents of line', oLine.line)

        lTokens = []
        lSeparators = []

        lSeparators.append('')
        lTokens.append('contents')
        lSeparators.append(' ')
        lTokens.append('of')
        lSeparators.append(' ')
        lTokens.append('line')

        self.assertEqual(lTokens, oLine.tokens)
        self.assertEqual(lSeparators, oLine.separators)

    def test_multiple_spaces(self):
        oLine = line.line('   contents   of     line')
        self.assertTrue(oLine)
        self.assertEqual('   contents   of     line', oLine.line)

        lTokens = []
        lSeparators = []

        lSeparators.append('   ')
        lTokens.append('contents')
        lSeparators.append('   ')
        lTokens.append('of')
        lSeparators.append('     ')
        lTokens.append('line')

        self.assertEqual(lTokens, oLine.tokens)
        self.assertEqual(lSeparators, oLine.separators)

    def test_comment_at_end_of_line_without_spaces_around_dashes(self):
        oLine = line.line('contents of line--This is a comment')
        self.assertTrue(oLine)
        self.assertEqual('contents of line--This is a comment', oLine.line)

        lTokens = []
        lSeparators = []

        lSeparators.append('')
        lTokens.append('contents')
        lSeparators.append(' ')
        lTokens.append('of')
        lSeparators.append(' ')
        lTokens.append('line')
        lSeparators.append('')
        lTokens.append('--This is a comment')

        self.assertEqual(lTokens, oLine.tokens)
        self.assertEqual(lSeparators, oLine.separators)

    def test_comment_at_end_of_line_with_spaces_around_dashes(self):
        oLine = line.line('contents of line --  This is a comment')
        self.assertTrue(oLine)
        self.assertEqual('contents of line --  This is a comment', oLine.line)

        lTokens = []
        lSeparators = []

        lSeparators.append('')
        lTokens.append('contents')
        lSeparators.append(' ')
        lTokens.append('of')
        lSeparators.append(' ')
        lTokens.append('line')
        lSeparators.append(' ')
        lTokens.append('--  This is a comment')

        self.assertEqual(lTokens, oLine.tokens)
        self.assertEqual(lSeparators, oLine.separators)

    def test_comment_at_end_of_line_with_spaces_at_the_end_of_line(self):
        oLine = line.line('contents of line --  This is a comment  ')
        self.assertTrue(oLine)
        self.assertEqual('contents of line --  This is a comment  ', oLine.line)

        lTokens = []
        lSeparators = []

        lSeparators.append('')
        lTokens.append('contents')
        lSeparators.append(' ')
        lTokens.append('of')
        lSeparators.append(' ')
        lTokens.append('line')
        lSeparators.append(' ')
        lTokens.append('--  This is a comment  ')

        self.assertEqual(lTokens, oLine.tokens)
        self.assertEqual(lSeparators, oLine.separators)

    def test_comment_only_line_with_spaces_before_the_comment(self):
        oLine = line.line(' -- This is a comment  ')
        self.assertTrue(oLine)
        self.assertEqual(' -- This is a comment  ', oLine.line)

        lTokens = []
        lSeparators = []

        lSeparators.append(' ')
        lTokens.append('-- This is a comment  ')

        self.assertEqual(lTokens, oLine.tokens)
        self.assertEqual(lSeparators, oLine.separators)

    def test_comment_only_line_without_spaces_before_the_comment(self):
        oLine = line.line('-- This is a comment  ')
        self.assertTrue(oLine)
        self.assertEqual('-- This is a comment  ', oLine.line)

        lTokens = []
        lSeparators = []

        lSeparators.append('')
        lTokens.append('-- This is a comment  ')

        self.assertEqual(lTokens, oLine.tokens)
        self.assertEqual(lSeparators, oLine.separators)

    def test_commas_without_spaces(self):
        oLine = line.line('this,will,test,commas,')
        self.assertTrue(oLine)
        self.assertEqual('this,will,test,commas,', oLine.line)

        lTokens = []
        lSeparators = []

        lSeparators.append('')
        lTokens.append('this')
        lSeparators.append('')
        lTokens.append(',')
        lSeparators.append('')
        lTokens.append('will')
        lSeparators.append('')
        lTokens.append(',')
        lSeparators.append('')
        lTokens.append('test')
        lSeparators.append('')
        lTokens.append(',')
        lSeparators.append('')
        lTokens.append('commas')
        lSeparators.append('')
        lTokens.append(',')

        self.assertEqual(lTokens, oLine.tokens)
        self.assertEqual(lSeparators, oLine.separators)

    def test_commas_without_spaces_with_comma_at_beginning_of_line(self):
        oLine = line.line(',this,will,test,commas,')
        self.assertTrue(oLine)
        self.assertEqual(',this,will,test,commas,', oLine.line)

        lTokens = []
        lSeparators = []

        lSeparators.append('')
        lTokens.append(',')
        lSeparators.append('')
        lTokens.append('this')
        lSeparators.append('')
        lTokens.append(',')
        lSeparators.append('')
        lTokens.append('will')
        lSeparators.append('')
        lTokens.append(',')
        lSeparators.append('')
        lTokens.append('test')
        lSeparators.append('')
        lTokens.append(',')
        lSeparators.append('')
        lTokens.append('commas')
        lSeparators.append('')
        lTokens.append(',')

        self.assertEqual(lTokens, oLine.tokens)
        self.assertEqual(lSeparators, oLine.separators)

    def test_commas_with_spaces_with_comma_at_beginning_of_line(self):
        sString = '  ,  this  ,  will , test  , commas ,  '
        oLine = line.line(sString)
        self.assertTrue(oLine)
        self.assertEqual(sString, oLine.line)

        lTokens = []
        lSeparators = []

        lSeparators.append('  ')
        lTokens.append(',')
        lSeparators.append('  ')
        lTokens.append('this')
        lSeparators.append('  ')
        lTokens.append(',')
        lSeparators.append('  ')
        lTokens.append('will')
        lSeparators.append(' ')
        lTokens.append(',')
        lSeparators.append(' ')
        lTokens.append('test')
        lSeparators.append('  ')
        lTokens.append(',')
        lSeparators.append(' ')
        lTokens.append('commas')
        lSeparators.append(' ')
        lTokens.append(',')
        lSeparators.append('  ')

        self.assertEqual(lTokens, oLine.tokens)
        self.assertEqual(lSeparators, oLine.separators)

    def test_colons_without_spaces_with_colon_at_beginning_of_line(self):
        sString = ':this:will:test:colons:'
        oLine = line.line(sString)
        self.assertTrue(oLine)
        self.assertEqual(sString, oLine.line)

        lTokens = []
        lSeparators = []

        lSeparators.append('')
        lTokens.append(':')
        lSeparators.append('')
        lTokens.append('this')
        lSeparators.append('')
        lTokens.append(':')
        lSeparators.append('')
        lTokens.append('will')
        lSeparators.append('')
        lTokens.append(':')
        lSeparators.append('')
        lTokens.append('test')
        lSeparators.append('')
        lTokens.append(':')
        lSeparators.append('')
        lTokens.append('colons')
        lSeparators.append('')
        lTokens.append(':')

        self.assertEqual(lTokens, oLine.tokens)
        self.assertEqual(lSeparators, oLine.separators)

    def test_colons_with_spaces_with_colon_at_beginning_of_line(self):
        sString = '  :  this  :  will : test  : commas :  '
        oLine = line.line(sString)
        self.assertTrue(oLine)
        self.assertEqual(sString, oLine.line)

        lTokens = []
        lSeparators = []

        lSeparators.append('  ')
        lTokens.append(':')
        lSeparators.append('  ')
        lTokens.append('this')
        lSeparators.append('  ')
        lTokens.append(':')
        lSeparators.append('  ')
        lTokens.append('will')
        lSeparators.append(' ')
        lTokens.append(':')
        lSeparators.append(' ')
        lTokens.append('test')
        lSeparators.append('  ')
        lTokens.append(':')
        lSeparators.append(' ')
        lTokens.append('commas')
        lSeparators.append(' ')
        lTokens.append(':')
        lSeparators.append('  ')

        self.assertEqual(lTokens, oLine.tokens)
        self.assertEqual(lSeparators, oLine.separators)

    def test_open_parenthesis_without_spaces_with_parenthesis_at_beginning_of_line(self):
        sString = '(this(will(test(colons('
        oLine = line.line(sString)
        self.assertTrue(oLine)
        self.assertEqual(sString, oLine.line)

        lTokens = []
        lSeparators = []

        lSeparators.append('')
        lTokens.append('(')
        lSeparators.append('')
        lTokens.append('this')
        lSeparators.append('')
        lTokens.append('(')
        lSeparators.append('')
        lTokens.append('will')
        lSeparators.append('')
        lTokens.append('(')
        lSeparators.append('')
        lTokens.append('test')
        lSeparators.append('')
        lTokens.append('(')
        lSeparators.append('')
        lTokens.append('colons')
        lSeparators.append('')
        lTokens.append('(')

        self.assertEqual(lTokens, oLine.tokens)
        self.assertEqual(lSeparators, oLine.separators)

    def test_open_parenthesis_with_spaces_with_parenthesis_at_beginning_of_line(self):
        sString = '  (  this  (  will ( test  ( commas (  '
        oLine = line.line(sString)
        self.assertTrue(oLine)
        self.assertEqual(sString, oLine.line)

        lTokens = []
        lSeparators = []

        lSeparators.append('  ')
        lTokens.append('(')
        lSeparators.append('  ')
        lTokens.append('this')
        lSeparators.append('  ')
        lTokens.append('(')
        lSeparators.append('  ')
        lTokens.append('will')
        lSeparators.append(' ')
        lTokens.append('(')
        lSeparators.append(' ')
        lTokens.append('test')
        lSeparators.append('  ')
        lTokens.append('(')
        lSeparators.append(' ')
        lTokens.append('commas')
        lSeparators.append(' ')
        lTokens.append('(')
        lSeparators.append('  ')

        self.assertEqual(lTokens, oLine.tokens)
        self.assertEqual(lSeparators, oLine.separators)

    def test_close_parenthesis_without_spaces_with_parenthesis_at_beginning_of_line(self):
        sString = ')this)will)test)colons)'
        oLine = line.line(sString)
        self.assertTrue(oLine)
        self.assertEqual(sString, oLine.line)

        lTokens = []
        lSeparators = []

        lSeparators.append('')
        lTokens.append(')')
        lSeparators.append('')
        lTokens.append('this')
        lSeparators.append('')
        lTokens.append(')')
        lSeparators.append('')
        lTokens.append('will')
        lSeparators.append('')
        lTokens.append(')')
        lSeparators.append('')
        lTokens.append('test')
        lSeparators.append('')
        lTokens.append(')')
        lSeparators.append('')
        lTokens.append('colons')
        lSeparators.append('')
        lTokens.append(')')

        self.assertEqual(lTokens, oLine.tokens)
        self.assertEqual(lSeparators, oLine.separators)

    def test_close_parenthesis_with_spaces_with_parenthesis_at_beginning_of_line(self):
        sString = '  )  this  )  will ) test  ) commas )  '
        oLine = line.line(sString)
        self.assertTrue(oLine)
        self.assertEqual(sString, oLine.line)

        lTokens = []
        lSeparators = []

        lSeparators.append('  ')
        lTokens.append(')')
        lSeparators.append('  ')
        lTokens.append('this')
        lSeparators.append('  ')
        lTokens.append(')')
        lSeparators.append('  ')
        lTokens.append('will')
        lSeparators.append(' ')
        lTokens.append(')')
        lSeparators.append(' ')
        lTokens.append('test')
        lSeparators.append('  ')
        lTokens.append(')')
        lSeparators.append(' ')
        lTokens.append('commas')
        lSeparators.append(' ')
        lTokens.append(')')
        lSeparators.append('  ')

        self.assertEqual(lTokens, oLine.tokens)
        self.assertEqual(lSeparators, oLine.separators)

    def test_single_quote_without_spaces_with_quote_at_beginning_of_line(self):
        sString = '\'this\'will\'test\'colons\''
        oLine = line.line(sString)
        self.assertTrue(oLine)
        self.assertEqual(sString, oLine.line)

        lTokens = []
        lSeparators = []

        lSeparators.append('')
        lTokens.append('\'')
        lSeparators.append('')
        lTokens.append('this')
        lSeparators.append('')
        lTokens.append('\'')
        lSeparators.append('')
        lTokens.append('will')
        lSeparators.append('')
        lTokens.append('\'')
        lSeparators.append('')
        lTokens.append('test')
        lSeparators.append('')
        lTokens.append('\'')
        lSeparators.append('')
        lTokens.append('colons')
        lSeparators.append('')
        lTokens.append('\'')

        self.assertEqual(lTokens, oLine.tokens)
        self.assertEqual(lSeparators, oLine.separators)

    def test_string_literals(self):
        sString = '"this" "will" "test" "colons with multiple things in the quotes"'
        oLine = line.line(sString)
        self.assertTrue(oLine)
        self.assertEqual(sString, oLine.line)

        lTokens = []
        lSeparators = []

        lSeparators.append('')
        lTokens.append('"this"')
        lSeparators.append(' ')
        lTokens.append('"will"')
        lSeparators.append(' ')
        lTokens.append('"test"')
        lSeparators.append(' ')
        lTokens.append('"colons with multiple things in the quotes"')

        self.assertEqual(lTokens, oLine.tokens)
        self.assertEqual(lSeparators, oLine.separators)

    def test_plus_without_spaces_with_plus_at_beginning_of_line(self):
        sString = '+this+will+test+colons+'
        oLine = line.line(sString)
        self.assertTrue(oLine)
        self.assertEqual(sString, oLine.line)

        lTokens = []
        lSeparators = []

        lSeparators.append('')
        lTokens.append('+')
        lSeparators.append('')
        lTokens.append('this')
        lSeparators.append('')
        lTokens.append('+')
        lSeparators.append('')
        lTokens.append('will')
        lSeparators.append('')
        lTokens.append('+')
        lSeparators.append('')
        lTokens.append('test')
        lSeparators.append('')
        lTokens.append('+')
        lSeparators.append('')
        lTokens.append('colons')
        lSeparators.append('')
        lTokens.append('+')

        self.assertEqual(lTokens, oLine.tokens)
        self.assertEqual(lSeparators, oLine.separators)

    def test_colon_equal_without_spaces_with_one_at_beginning_of_line(self):
        sString = ':=this:=will:=test:=colons:='
        oLine = line.line(sString)
        self.assertTrue(oLine)
        self.assertEqual(sString, oLine.line)

        lTokens = []
        lSeparators = []

        lSeparators.append('')
        lTokens.append(':=')
        lSeparators.append('')
        lTokens.append('this')
        lSeparators.append('')
        lTokens.append(':=')
        lSeparators.append('')
        lTokens.append('will')
        lSeparators.append('')
        lTokens.append(':=')
        lSeparators.append('')
        lTokens.append('test')
        lSeparators.append('')
        lTokens.append(':=')
        lSeparators.append('')
        lTokens.append('colons')
        lSeparators.append('')
        lTokens.append(':=')

        self.assertEqual(lTokens, oLine.tokens)
        self.assertEqual(lSeparators, oLine.separators)

    def test_star_star_without_spaces_with_one_at_beginning_of_line(self):
        sString = '**this**will**test**colons**'
        oLine = line.line(sString)
        self.assertTrue(oLine)
        self.assertEqual(sString, oLine.line)

        lTokens = []
        lSeparators = []

        lSeparators.append('')
        lTokens.append('**')
        lSeparators.append('')
        lTokens.append('this')
        lSeparators.append('')
        lTokens.append('**')
        lSeparators.append('')
        lTokens.append('will')
        lSeparators.append('')
        lTokens.append('**')
        lSeparators.append('')
        lTokens.append('test')
        lSeparators.append('')
        lTokens.append('**')
        lSeparators.append('')
        lTokens.append('colons')
        lSeparators.append('')
        lTokens.append('**')

        self.assertEqual(lTokens, oLine.tokens)
        self.assertEqual(lSeparators, oLine.separators)

    def test_not_equal_without_spaces_with_one_at_beginning_of_line(self):
        sString = '/=this/=will/=test/=colons/='
        oLine = line.line(sString)
        self.assertTrue(oLine)
        self.assertEqual(sString, oLine.line)

        lTokens = []
        lSeparators = []

        lSeparators.append('')
        lTokens.append('/=')
        lSeparators.append('')
        lTokens.append('this')
        lSeparators.append('')
        lTokens.append('/=')
        lSeparators.append('')
        lTokens.append('will')
        lSeparators.append('')
        lTokens.append('/=')
        lSeparators.append('')
        lTokens.append('test')
        lSeparators.append('')
        lTokens.append('/=')
        lSeparators.append('')
        lTokens.append('colons')
        lSeparators.append('')
        lTokens.append('/=')

        self.assertEqual(lTokens, oLine.tokens)
        self.assertEqual(lSeparators, oLine.separators)

    def test_lessthan_equal_without_spaces_with_one_at_beginning_of_line(self):
        sString = '<=this<=will<=test<=colons<='
        oLine = line.line(sString)
        self.assertTrue(oLine)
        self.assertEqual(sString, oLine.line)

        lTokens = []
        lSeparators = []

        lSeparators.append('')
        lTokens.append('<=')
        lSeparators.append('')
        lTokens.append('this')
        lSeparators.append('')
        lTokens.append('<=')
        lSeparators.append('')
        lTokens.append('will')
        lSeparators.append('')
        lTokens.append('<=')
        lSeparators.append('')
        lTokens.append('test')
        lSeparators.append('')
        lTokens.append('<=')
        lSeparators.append('')
        lTokens.append('colons')
        lSeparators.append('')
        lTokens.append('<=')

        self.assertEqual(lTokens, oLine.tokens)
        self.assertEqual(lSeparators, oLine.separators)

    def test_equal_greaterthan_without_spaces_with_one_at_beginning_of_line(self):
        sString = '=>this=>will=>test=>colons=>'
        oLine = line.line(sString)
        self.assertTrue(oLine)
        self.assertEqual(sString, oLine.line)

        lTokens = []
        lSeparators = []

        lSeparators.append('')
        lTokens.append('=>')
        lSeparators.append('')
        lTokens.append('this')
        lSeparators.append('')
        lTokens.append('=>')
        lSeparators.append('')
        lTokens.append('will')
        lSeparators.append('')
        lTokens.append('=>')
        lSeparators.append('')
        lTokens.append('test')
        lSeparators.append('')
        lTokens.append('=>')
        lSeparators.append('')
        lTokens.append('colons')
        lSeparators.append('')
        lTokens.append('=>')

        self.assertEqual(lTokens, oLine.tokens)
        self.assertEqual(lSeparators, oLine.separators)

    def test_greaterthan_equal_without_spaces_with_one_at_beginning_of_line(self):
        sString = '>=this>=will>=test>=colons>='
        oLine = line.line(sString)
        self.assertTrue(oLine)
        self.assertEqual(sString, oLine.line)

        lTokens = []
        lSeparators = []

        lSeparators.append('')
        lTokens.append('>=')
        lSeparators.append('')
        lTokens.append('this')
        lSeparators.append('')
        lTokens.append('>=')
        lSeparators.append('')
        lTokens.append('will')
        lSeparators.append('')
        lTokens.append('>=')
        lSeparators.append('')
        lTokens.append('test')
        lSeparators.append('')
        lTokens.append('>=')
        lSeparators.append('')
        lTokens.append('colons')
        lSeparators.append('')
        lTokens.append('>=')

        self.assertEqual(lTokens, oLine.tokens)
        self.assertEqual(lSeparators, oLine.separators)

    def test_multiple_symbols_on_single_line_1(self):
        sString = "variable We1, We2, We3, Wy : BIT := '1';"
        oLine = line.line(sString)
        self.assertTrue(oLine)
        self.assertEqual(sString, oLine.line)

        lTokens = []
        lSeparators = []

        lSeparators.append('')
        lTokens.append('variable')
        lSeparators.append(' ')
        lTokens.append('We1')
        lSeparators.append('')
        lTokens.append(',')
        lSeparators.append(' ')
        lTokens.append('We2')
        lSeparators.append('')
        lTokens.append(',')
        lSeparators.append(' ')
        lTokens.append('We3')
        lSeparators.append('')
        lTokens.append(',')
        lSeparators.append(' ')
        lTokens.append('Wy')
        lSeparators.append(' ')
        lTokens.append(':')
        lSeparators.append(' ')
        lTokens.append('BIT')
        lSeparators.append(' ')
        lTokens.append(':=')
        lSeparators.append(' ')
        lTokens.append("'1'")
        lSeparators.append('')
        lTokens.append(';')

        self.assertEqual(lTokens, oLine.tokens)
        self.assertEqual(lSeparators, oLine.separators)

    def test_multiple_symbols_on_single_line_2(self):
        sString = "    DI_I          : in    std_logic_vector(N - 1 downto 0) := (others => 'X');    -- parallel data in"
        oLine = line.line(sString)
        self.assertTrue(oLine)
        self.assertEqual(sString, oLine.line)

        lTokens = []
        lSeparators = []

        lSeparators.append('    ')
        lTokens.append('DI_I')
        lSeparators.append('          ')
        lTokens.append(':')
        lSeparators.append(' ')
        lTokens.append('in')
        lSeparators.append('    ')
        lTokens.append('std_logic_vector')
        lSeparators.append('')
        lTokens.append('(')
        lSeparators.append('')
        lTokens.append('N')
        lSeparators.append(' ')
        lTokens.append('-')
        lSeparators.append(' ')
        lTokens.append('1')
        lSeparators.append(' ')
        lTokens.append('downto')
        lSeparators.append(' ')
        lTokens.append('0')
        lSeparators.append('')
        lTokens.append(')')
        lSeparators.append(' ')
        lTokens.append(':=')
        lSeparators.append(' ')
        lTokens.append('(')
        lSeparators.append('')
        lTokens.append('others')
        lSeparators.append(' ')
        lTokens.append('=>')
        lSeparators.append(' ')
        lTokens.append("'X'")
        lSeparators.append('')
        lTokens.append(')')
        lSeparators.append('')
        lTokens.append(';')
        lSeparators.append('    ')
        lTokens.append('-- parallel data in')

        self.assertEqual(lTokens, oLine.tokens)
        self.assertEqual(lSeparators, oLine.separators)

    def test_multiple_character_tokens_near_end_of_line(self):
        sString = '  a <= b **c'
        oLine = line.line(sString)
        self.assertTrue(oLine)
        self.assertEqual(sString, oLine.line)

        lTokens = []
        lSeparators = []

        lSeparators.append('  ')
        lTokens.append('a')
        lSeparators.append(' ')
        lTokens.append('<=')
        lSeparators.append(' ')
        lTokens.append('b')
        lSeparators.append(' ')
        lTokens.append('**')
        lSeparators.append('')
        lTokens.append('c')

        self.assertEqual(lTokens, oLine.tokens)
        self.assertEqual(lSeparators, oLine.separators)


