# -*- coding: utf-8 -*-

import unittest

from vsg import tokens


class testTokenMethod(unittest.TestCase):
    def test_single_spaces(self):
        sLine = "contents of line"

        lTokens = []

        lTokens.append("contents")
        lTokens.append(" ")
        lTokens.append("of")
        lTokens.append(" ")
        lTokens.append("line")

        lActual = tokens.create(sLine)

        self.assertEqual(lTokens, lActual)

    def test_multiple_spaces(self):
        sLine = "   contents   of     line"

        lTokens = []

        lTokens.append("   ")
        lTokens.append("contents")
        lTokens.append("   ")
        lTokens.append("of")
        lTokens.append("     ")
        lTokens.append("line")

        lActual = tokens.create(sLine)

        self.assertEqual(lTokens, lActual)

    def test_comment_at_end_of_line_without_spaces_around_dashes(self):
        sLine = "contents of line--This is a comment"

        lTokens = []

        lTokens.append("contents")
        lTokens.append(" ")
        lTokens.append("of")
        lTokens.append(" ")
        lTokens.append("line")
        lTokens.append("--")
        lTokens.append("This")
        lTokens.append(" ")
        lTokens.append("is")
        lTokens.append(" ")
        lTokens.append("a")
        lTokens.append(" ")
        lTokens.append("comment")

        lActual = tokens.create(sLine)

        self.assertEqual(lTokens, lActual)

    def test_comment_at_end_of_line_with_spaces_around_dashes(self):
        sLine = "contents of line --  This is a comment"

        lTokens = []

        lTokens.append("contents")
        lTokens.append(" ")
        lTokens.append("of")
        lTokens.append(" ")
        lTokens.append("line")
        lTokens.append(" ")
        lTokens.append("--")
        lTokens.append("  ")
        lTokens.append("This")
        lTokens.append(" ")
        lTokens.append("is")
        lTokens.append(" ")
        lTokens.append("a")
        lTokens.append(" ")
        lTokens.append("comment")

        lActual = tokens.create(sLine)

        self.assertEqual(lTokens, lActual)

    def test_comment_at_end_of_line_with_spaces_at_the_end_of_line(self):
        sLine = "contents of line --  This is a comment  "

        lTokens = []

        lTokens.append("contents")
        lTokens.append(" ")
        lTokens.append("of")
        lTokens.append(" ")
        lTokens.append("line")
        lTokens.append(" ")
        lTokens.append("--")
        lTokens.append("  ")
        lTokens.append("This")
        lTokens.append(" ")
        lTokens.append("is")
        lTokens.append(" ")
        lTokens.append("a")
        lTokens.append(" ")
        lTokens.append("comment")
        lTokens.append("  ")

        lActual = tokens.create(sLine)

        self.assertEqual(lTokens, lActual)

    def test_comment_only_line_with_spaces_before_the_comment(self):
        sLine = " -- This is a comment  "

        lTokens = []

        lTokens.append(" ")
        lTokens.append("--")
        lTokens.append(" ")
        lTokens.append("This")
        lTokens.append(" ")
        lTokens.append("is")
        lTokens.append(" ")
        lTokens.append("a")
        lTokens.append(" ")
        lTokens.append("comment")
        lTokens.append("  ")

        lActual = tokens.create(sLine)

        self.assertEqual(lTokens, lActual)

    def test_comment_only_line_without_spaces_before_the_comment(self):
        sLine = "-- This is a comment  "

        lTokens = []

        lTokens.append("--")
        lTokens.append(" ")
        lTokens.append("This")
        lTokens.append(" ")
        lTokens.append("is")
        lTokens.append(" ")
        lTokens.append("a")
        lTokens.append(" ")
        lTokens.append("comment")
        lTokens.append("  ")

        lActual = tokens.create(sLine)

        self.assertEqual(lTokens, lActual)

    def test_commas_without_spaces(self):
        sLine = "this,will,test,commas,"

        lTokens = []

        lTokens.append("this")
        lTokens.append(",")
        lTokens.append("will")
        lTokens.append(",")
        lTokens.append("test")
        lTokens.append(",")
        lTokens.append("commas")
        lTokens.append(",")

        lActual = tokens.create(sLine)

        self.assertEqual(lTokens, lActual)

    def test_commas_without_spaces_with_comma_at_beginning_of_line(self):
        sLine = ",this,will,test,commas,"

        lTokens = []

        lTokens.append(",")
        lTokens.append("this")
        lTokens.append(",")
        lTokens.append("will")
        lTokens.append(",")
        lTokens.append("test")
        lTokens.append(",")
        lTokens.append("commas")
        lTokens.append(",")

        lActual = tokens.create(sLine)

        self.assertEqual(lTokens, lActual)

    def test_commas_with_spaces_with_comma_at_beginning_of_line(self):
        sLine = "  ,  this  ,  will , test  , commas ,  "

        lTokens = []

        lTokens.append("  ")
        lTokens.append(",")
        lTokens.append("  ")
        lTokens.append("this")
        lTokens.append("  ")
        lTokens.append(",")
        lTokens.append("  ")
        lTokens.append("will")
        lTokens.append(" ")
        lTokens.append(",")
        lTokens.append(" ")
        lTokens.append("test")
        lTokens.append("  ")
        lTokens.append(",")
        lTokens.append(" ")
        lTokens.append("commas")
        lTokens.append(" ")
        lTokens.append(",")
        lTokens.append("  ")

        lActual = tokens.create(sLine)

        self.assertEqual(lTokens, lActual)

    def test_colons_without_spaces_with_colon_at_beginning_of_line(self):
        sLine = ":this:will:test:colons:"

        lTokens = []

        lTokens.append(":")
        lTokens.append("this")
        lTokens.append(":")
        lTokens.append("will")
        lTokens.append(":")
        lTokens.append("test")
        lTokens.append(":")
        lTokens.append("colons")
        lTokens.append(":")

        lActual = tokens.create(sLine)

        self.assertEqual(lTokens, lActual)

    def test_colons_with_spaces_with_colon_at_beginning_of_line(self):
        sLine = "  :  this  :  will : test  : commas :  "

        lTokens = []

        lTokens.append("  ")
        lTokens.append(":")
        lTokens.append("  ")
        lTokens.append("this")
        lTokens.append("  ")
        lTokens.append(":")
        lTokens.append("  ")
        lTokens.append("will")
        lTokens.append(" ")
        lTokens.append(":")
        lTokens.append(" ")
        lTokens.append("test")
        lTokens.append("  ")
        lTokens.append(":")
        lTokens.append(" ")
        lTokens.append("commas")
        lTokens.append(" ")
        lTokens.append(":")
        lTokens.append("  ")

        lActual = tokens.create(sLine)

        self.assertEqual(lTokens, lActual)

    def test_open_parenthesis_without_spaces_with_parenthesis_at_beginning_of_line(self):
        sLine = "(this(will(test(colons("

        lTokens = []

        lTokens.append("(")
        lTokens.append("this")
        lTokens.append("(")
        lTokens.append("will")
        lTokens.append("(")
        lTokens.append("test")
        lTokens.append("(")
        lTokens.append("colons")
        lTokens.append("(")

        lActual = tokens.create(sLine)

        self.assertEqual(lTokens, lActual)

    def test_open_parenthesis_with_spaces_with_parenthesis_at_beginning_of_line(self):
        sLine = "  (  this  (  will ( test  ( commas (  "

        lTokens = []

        lTokens.append("  ")
        lTokens.append("(")
        lTokens.append("  ")
        lTokens.append("this")
        lTokens.append("  ")
        lTokens.append("(")
        lTokens.append("  ")
        lTokens.append("will")
        lTokens.append(" ")
        lTokens.append("(")
        lTokens.append(" ")
        lTokens.append("test")
        lTokens.append("  ")
        lTokens.append("(")
        lTokens.append(" ")
        lTokens.append("commas")
        lTokens.append(" ")
        lTokens.append("(")
        lTokens.append("  ")

        lActual = tokens.create(sLine)

        self.assertEqual(lTokens, lActual)

    def test_close_parenthesis_without_spaces_with_parenthesis_at_beginning_of_line(self):
        sLine = ")this)will)test)colons)"

        lTokens = []

        lTokens.append(")")
        lTokens.append("this")
        lTokens.append(")")
        lTokens.append("will")
        lTokens.append(")")
        lTokens.append("test")
        lTokens.append(")")
        lTokens.append("colons")
        lTokens.append(")")

        lActual = tokens.create(sLine)

        self.assertEqual(lTokens, lActual)

    def test_close_parenthesis_with_spaces_with_parenthesis_at_beginning_of_line(self):
        sLine = "  )  this  )  will ) test  ) commas )  "

        lTokens = []

        lTokens.append("  ")
        lTokens.append(")")
        lTokens.append("  ")
        lTokens.append("this")
        lTokens.append("  ")
        lTokens.append(")")
        lTokens.append("  ")
        lTokens.append("will")
        lTokens.append(" ")
        lTokens.append(")")
        lTokens.append(" ")
        lTokens.append("test")
        lTokens.append("  ")
        lTokens.append(")")
        lTokens.append(" ")
        lTokens.append("commas")
        lTokens.append(" ")
        lTokens.append(")")
        lTokens.append("  ")

        lActual = tokens.create(sLine)

        self.assertEqual(lTokens, lActual)

    def test_single_quote_without_spaces_with_quote_at_beginning_of_line(self):
        sLine = "'this'will'test'colons'"

        lTokens = []

        lTokens.append("'")
        lTokens.append("this")
        lTokens.append("'")
        lTokens.append("will")
        lTokens.append("'")
        lTokens.append("test")
        lTokens.append("'")
        lTokens.append("colons")
        lTokens.append("'")

        lActual = tokens.create(sLine)

        self.assertEqual(lTokens, lActual)

    def test_string_literals(self):
        sLine = '"this" "will" "test" "colons with multiple things in the quotes"'

        lTokens = []

        lTokens.append('"this"')
        lTokens.append(" ")
        lTokens.append('"will"')
        lTokens.append(" ")
        lTokens.append('"test"')
        lTokens.append(" ")
        lTokens.append('"colons with multiple things in the quotes"')

        lActual = tokens.create(sLine)

        self.assertEqual(lTokens, lActual)

    def test_plus_without_spaces_with_plus_at_beginning_of_line(self):
        sLine = "+this+will+test+colons+"

        lTokens = []

        lTokens.append("+")
        lTokens.append("this")
        lTokens.append("+")
        lTokens.append("will")
        lTokens.append("+")
        lTokens.append("test")
        lTokens.append("+")
        lTokens.append("colons")
        lTokens.append("+")

        lActual = tokens.create(sLine)

        self.assertEqual(lTokens, lActual)

    def test_colon_equal_without_spaces_with_one_at_beginning_of_line(self):
        sLine = ":=this:=will:=test:=colons:="

        lTokens = []

        lTokens.append(":=")
        lTokens.append("this")
        lTokens.append(":=")
        lTokens.append("will")
        lTokens.append(":=")
        lTokens.append("test")
        lTokens.append(":=")
        lTokens.append("colons")
        lTokens.append(":=")

        lActual = tokens.create(sLine)

        self.assertEqual(lTokens, lActual)

    def test_star_star_without_spaces_with_one_at_beginning_of_line(self):
        sLine = "**this**will**test**colons**"

        lTokens = []

        lTokens.append("**")
        lTokens.append("this")
        lTokens.append("**")
        lTokens.append("will")
        lTokens.append("**")
        lTokens.append("test")
        lTokens.append("**")
        lTokens.append("colons")
        lTokens.append("**")

        lActual = tokens.create(sLine)

        self.assertEqual(lTokens, lActual)

    def test_not_equal_without_spaces_with_one_at_beginning_of_line(self):
        sLine = "/=this/=will/=test/=colons/="

        lTokens = []

        lTokens.append("/=")
        lTokens.append("this")
        lTokens.append("/=")
        lTokens.append("will")
        lTokens.append("/=")
        lTokens.append("test")
        lTokens.append("/=")
        lTokens.append("colons")
        lTokens.append("/=")

        lActual = tokens.create(sLine)

        self.assertEqual(lTokens, lActual)

    def test_lessthan_equal_without_spaces_with_one_at_beginning_of_line(self):
        sLine = "<=this<=will<=test<=colons<="

        lTokens = []

        lTokens.append("<=")
        lTokens.append("this")
        lTokens.append("<=")
        lTokens.append("will")
        lTokens.append("<=")
        lTokens.append("test")
        lTokens.append("<=")
        lTokens.append("colons")
        lTokens.append("<=")

        lActual = tokens.create(sLine)

        self.assertEqual(lTokens, lActual)

    def test_equal_greaterthan_without_spaces_with_one_at_beginning_of_line(self):
        sLine = "=>this=>will=>test=>colons=>"

        lTokens = []

        lTokens.append("=>")
        lTokens.append("this")
        lTokens.append("=>")
        lTokens.append("will")
        lTokens.append("=>")
        lTokens.append("test")
        lTokens.append("=>")
        lTokens.append("colons")
        lTokens.append("=>")

        lActual = tokens.create(sLine)

        self.assertEqual(lTokens, lActual)

    def test_greaterthan_equal_without_spaces_with_one_at_beginning_of_line(self):
        sLine = ">=this>=will>=test>=colons>="

        lTokens = []

        lTokens.append(">=")
        lTokens.append("this")
        lTokens.append(">=")
        lTokens.append("will")
        lTokens.append(">=")
        lTokens.append("test")
        lTokens.append(">=")
        lTokens.append("colons")
        lTokens.append(">=")

        lActual = tokens.create(sLine)

        self.assertEqual(lTokens, lActual)

    def test_multiple_symbols_on_single_line_1(self):
        sLine = "variable We1, We2, We3, Wy : BIT := '1';"

        lTokens = []

        lTokens.append("variable")
        lTokens.append(" ")
        lTokens.append("We1")
        lTokens.append(",")
        lTokens.append(" ")
        lTokens.append("We2")
        lTokens.append(",")
        lTokens.append(" ")
        lTokens.append("We3")
        lTokens.append(",")
        lTokens.append(" ")
        lTokens.append("Wy")
        lTokens.append(" ")
        lTokens.append(":")
        lTokens.append(" ")
        lTokens.append("BIT")
        lTokens.append(" ")
        lTokens.append(":=")
        lTokens.append(" ")
        lTokens.append("'1'")
        lTokens.append(";")

        lActual = tokens.create(sLine)

        self.assertEqual(lTokens, lActual)

    def test_multiple_symbols_on_single_line_2(self):
        sLine = "    DI_I          : in    std_logic_vector(N - 1 downto 0) := (others => 'X');    -- parallel data in"

        lTokens = []

        lTokens.append("    ")
        lTokens.append("DI_I")
        lTokens.append("          ")
        lTokens.append(":")
        lTokens.append(" ")
        lTokens.append("in")
        lTokens.append("    ")
        lTokens.append("std_logic_vector")
        lTokens.append("(")
        lTokens.append("N")
        lTokens.append(" ")
        lTokens.append("-")
        lTokens.append(" ")
        lTokens.append("1")
        lTokens.append(" ")
        lTokens.append("downto")
        lTokens.append(" ")
        lTokens.append("0")
        lTokens.append(")")
        lTokens.append(" ")
        lTokens.append(":=")
        lTokens.append(" ")
        lTokens.append("(")
        lTokens.append("others")
        lTokens.append(" ")
        lTokens.append("=>")
        lTokens.append(" ")
        lTokens.append("'X'")
        lTokens.append(")")
        lTokens.append(";")
        lTokens.append("    ")
        lTokens.append("--")
        lTokens.append(" ")
        lTokens.append("parallel")
        lTokens.append(" ")
        lTokens.append("data")
        lTokens.append(" ")
        lTokens.append("in")

        lActual = tokens.create(sLine)

        self.assertEqual(lTokens, lActual)

    def test_multiple_character_tokens_near_end_of_line(self):
        sLine = "  a <= b **c"

        lTokens = []

        lTokens.append("  ")
        lTokens.append("a")
        lTokens.append(" ")
        lTokens.append("<=")
        lTokens.append(" ")
        lTokens.append("b")
        lTokens.append(" ")
        lTokens.append("**")
        lTokens.append("c")

        lActual = tokens.create(sLine)

        self.assertEqual(lTokens, lActual)

    def test_qualified_expression(self):
        sLine = "  a => std_logic'('1'),"

        lTokens = []

        lTokens.append("  ")
        lTokens.append("a")
        lTokens.append(" ")
        lTokens.append("=>")
        lTokens.append(" ")
        lTokens.append("std_logic")
        lTokens.append("'")
        lTokens.append("(")
        lTokens.append("'1'")
        lTokens.append(")")
        lTokens.append(",")

        lActual = tokens.create(sLine)

        self.assertEqual(lTokens, lActual)

    def test_parenthesis_character_literal(self):
        sLine = "  my_char <= '(';"

        lTokens = []

        lTokens.append("  ")
        lTokens.append("my_char")
        lTokens.append(" ")
        lTokens.append("<=")
        lTokens.append(" ")
        lTokens.append("'('")
        lTokens.append(";")

        lActual = tokens.create(sLine)

        self.assertEqual(lTokens, lActual)

    def test_quotes_in_comments(self):
        sLine = '--! some text "other text'

        lTokens = []

        lTokens.append("--")
        lTokens.append("!")
        lTokens.append(" ")
        lTokens.append("some")
        lTokens.append(" ")
        lTokens.append("text")
        lTokens.append(" ")
        lTokens.append('"')
        lTokens.append("other")
        lTokens.append(" ")
        lTokens.append("text")

        lActual = tokens.create(sLine)

        self.assertEqual(lTokens, lActual)

    def test_double_dash_in_string_literal(self):
        sLine = ' x"--";'
        lTokens = []
        lTokens.append(" ")
        lTokens.append("x")
        lTokens.append('"--"')
        lTokens.append(";")

        lActual = tokens.create(sLine)

        self.assertEqual(lTokens, lActual)

    def test_single_quotes_around_spaces(self):
        sLine = "before = ' ' & after"
        lTokens = []
        lTokens.append("before")
        lTokens.append(" ")
        lTokens.append("=")
        lTokens.append(" ")
        lTokens.append("' '")
        lTokens.append(" ")
        lTokens.append("&")
        lTokens.append(" ")
        lTokens.append("after")

        lActual = tokens.create(sLine)

        self.assertEqual(lTokens, lActual)

    def test_double_quotes_in_comment(self):
        sLine = '--| "yet another string"'
        lTokens = []
        lTokens.append("--")
        lTokens.append("|")
        lTokens.append(" ")
        lTokens.append('"yet another string"')

        lActual = tokens.create(sLine)

        self.assertEqual(lTokens, lActual)

    def test_single_quotes_in_comment(self):
        sLine = "--| 'a'"
        lTokens = []
        lTokens.append("--")
        lTokens.append("|")
        lTokens.append(" ")
        lTokens.append("'a'")

        lActual = tokens.create(sLine)

        self.assertEqual(lTokens, lActual)

    def test_backward_slashes(self):
        sLine = "  function \\?=\\ (L, R : ufixed) return STD_ULOGIC;"
        lTokens = []
        lTokens.append("  ")
        lTokens.append("function")
        lTokens.append(" ")
        lTokens.append("\\" + "?=" + "\\")
        lTokens.append(" ")
        lTokens.append("(")
        lTokens.append("L")
        lTokens.append(",")
        lTokens.append(" ")
        lTokens.append("R")
        lTokens.append(" ")
        lTokens.append(":")
        lTokens.append(" ")
        lTokens.append("ufixed")
        lTokens.append(")")
        lTokens.append(" ")
        lTokens.append("return")
        lTokens.append(" ")
        lTokens.append("STD_ULOGIC")
        lTokens.append(";")

        lActual = tokens.create(sLine)

        self.assertEqual(lTokens, lActual)

    def test_combine_backslash_characters_into_symbols(self):
        sLine = " function \\?=\\ hello"

        lActual = tokens.create(sLine)

        lExpected = []
        lExpected.append(" ")
        lExpected.append("function")
        lExpected.append(" ")
        lExpected.append("\\?=\\")
        lExpected.append(" ")
        lExpected.append("hello")

        self.assertEqual(lExpected, lActual)

        sLine = " function \\?=\\"

        lActual = tokens.create(sLine)

        lExpected = []
        lExpected.append(" ")
        lExpected.append("function")
        lExpected.append(" ")
        lExpected.append("\\?=\\")

        self.assertEqual(lExpected, lActual)

        sLine = " function \\?=\\("

        lActual = tokens.create(sLine)

        lExpected = []
        lExpected.append(" ")
        lExpected.append("function")
        lExpected.append(" ")
        lExpected.append("\\?=\\")
        lExpected.append("(")

        self.assertEqual(lExpected, lActual)

        sLine = " function \\?=\\ "

        lActual = tokens.create(sLine)

        lExpected = []
        lExpected.append(" ")
        lExpected.append("function")
        lExpected.append(" ")
        lExpected.append("\\?=\\")
        lExpected.append(" ")

        self.assertEqual(lExpected, lActual)

        sLine = " function \\?=\\;"

        lActual = tokens.create(sLine)

        lExpected = []
        lExpected.append(" ")
        lExpected.append("function")
        lExpected.append(" ")
        lExpected.append("\\?=\\")
        lExpected.append(";")

        self.assertEqual(lExpected, lActual)

        sLine = " function \\?>\\  ("

        lActual = tokens.create(sLine)

        lExpected = []
        lExpected.append(" ")
        lExpected.append("function")
        lExpected.append(" ")
        lExpected.append("\\?>\\")
        lExpected.append("  ")
        lExpected.append("(")

        self.assertEqual(lExpected, lActual)

    def test_parenthesis_in_procedure_call(self):
        sLine = "  write(('a'))"
        lTokens = []
        lTokens.append("  ")
        lTokens.append("write")
        lTokens.append("(")
        lTokens.append("(")
        lTokens.append("'a'")
        lTokens.append(")")
        lTokens.append(")")

        lActual = tokens.create(sLine)

        self.assertEqual(lTokens, lActual)

    def test_multiple_character_literals(self):
        sLine = "'a' or 'b' or 'c'|'d'"
        lTokens = []
        lTokens.append("'a'")
        lTokens.append(" ")
        lTokens.append("or")
        lTokens.append(" ")
        lTokens.append("'b'")
        lTokens.append(" ")
        lTokens.append("or")
        lTokens.append(" ")
        lTokens.append("'c'")
        lTokens.append("|")
        lTokens.append("'d'")

        lActual = tokens.create(sLine)

        self.assertEqual(lTokens, lActual)

    def test_multiple_character_literals_with_qualified_expression(self):
        sLine = "std_logic'('1')|'1'|'0'"
        lTokens = []
        lTokens.append("std_logic")
        lTokens.append("'")
        lTokens.append("(")
        lTokens.append("'1'")
        lTokens.append(")")
        lTokens.append("|")
        lTokens.append("'1'")
        lTokens.append("|")
        lTokens.append("'0'")

        lActual = tokens.create(sLine)

        self.assertEqual(lTokens, lActual)

    def test_backslash(self):
        sLine = 'a "/\\" b'
        lTokens = []
        lTokens.append("a")
        lTokens.append(" ")
        lTokens.append('"/\\"')
        lTokens.append(" ")
        lTokens.append("b")

        lActual = tokens.create(sLine)

        self.assertEqual(lTokens, lActual)

    def test_real_number(self):
        sLine = "23.45e-100 6e-8 70e+8 71.6e+8 50e90 50.23e91"
        lTokens = []
        lTokens.append("23.45")
        lTokens.append("e")
        lTokens.append("-")
        lTokens.append("100")
        lTokens.append(" ")
        lTokens.append("6")
        lTokens.append("e")
        lTokens.append("-")
        lTokens.append("8")
        lTokens.append(" ")
        lTokens.append("70")
        lTokens.append("e")
        lTokens.append("+")
        lTokens.append("8")
        lTokens.append(" ")
        lTokens.append("71.6")
        lTokens.append("e")
        lTokens.append("+")
        lTokens.append("8")
        lTokens.append(" ")
        lTokens.append("50")
        lTokens.append("e")
        lTokens.append("90")
        lTokens.append(" ")
        lTokens.append("50.23")
        lTokens.append("e")
        lTokens.append("91")

        lActual = tokens.create(sLine)

        self.assertEqual(lTokens, lActual)

    def test_tabs(self):
        sLine = "a\tb \t c\t \td \t"
        lTokens = []
        lTokens.append("a")
        lTokens.append("\t")
        lTokens.append("b")
        lTokens.append(" \t ")
        lTokens.append("c")
        lTokens.append("\t \t")
        lTokens.append("d")
        lTokens.append(" \t")

        lActual = tokens.create(sLine)

        self.assertEqual(lTokens, lActual)

    def test_delimited_comment(self):
        sLine = "/* --- */"
        lTokens = []
        lTokens.append("/*")
        lTokens.append(" ")
        lTokens.append("--")
        lTokens.append("-")
        lTokens.append(" ")
        lTokens.append("*/")

        lActual = tokens.create(sLine)

        self.assertEqual(lTokens, lActual)

    def test_delimited_comment_after_comment(self):
        sLine = "-- Comment /* --- */"
        lTokens = []
        lTokens.append("--")
        lTokens.append(" ")
        lTokens.append("Comment")
        lTokens.append(" ")
        lTokens.append("/*")
        lTokens.append(" ")
        lTokens.append("--")
        lTokens.append("-")
        lTokens.append(" ")
        lTokens.append("*/")

        lActual = tokens.create(sLine)

        self.assertEqual(lTokens, lActual)

    def test_beginning_delimited_comment_before_comment(self):
        sLine = "/* --- "
        lTokens = []
        lTokens.append("/*")
        lTokens.append(" ")
        lTokens.append("--")
        lTokens.append("-")
        lTokens.append(" ")

        lActual = tokens.create(sLine)

        self.assertEqual(lTokens, lActual)

    def test_ending_delimited_comment_after_comment(self):
        sLine = "-- */"
        lTokens = []
        lTokens.append("--")
        lTokens.append(" ")
        lTokens.append("*/")

        lActual = tokens.create(sLine)

        self.assertEqual(lTokens, lActual)

    def test_ending_delimited_comment_after_comment_and_text(self):
        sLine = "-- */D]"
        lTokens = []
        lTokens.append("--")
        lTokens.append(" ")
        lTokens.append("*/")
        lTokens.append("D")
        lTokens.append("]")

        lActual = tokens.create(sLine)

        self.assertEqual(lTokens, lActual)

    def test_ending_delimited_comment_after_comment_and_text_and_trailing_whitespace(self):
        sLine = "-- */D]   "
        lTokens = []
        lTokens.append("--")
        lTokens.append(" ")
        lTokens.append("*/")
        lTokens.append("D")
        lTokens.append("]")
        lTokens.append("   ")

        lActual = tokens.create(sLine)

        self.assertEqual(lTokens, lActual)
