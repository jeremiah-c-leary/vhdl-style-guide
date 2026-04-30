.. _configuring-block-comments:

Configuring Block Comments
==========================

Block comments are sequential comment lines with a header and footer. Below are several examples of block comments::

    ----------------------------------
    -- Comment
    -- Comment
    ----------------------------------

    --================================
    -- Comment
    -- Comment
    --================================

    --+-------------------------------
    --| Comment
    --| Comment
    --+-------------------------------

    --+---------< header >------------
    --| Comment
    --| Comment
    --+---------< footer >------------

Block Comment Structure
-----------------------

The above examples can be generalized into the following::

    --<header_left><header_left_repeat><header_string><header_right_repeat>
    --<comment_left>
    --<footer_left><footer_left_repeat><footer_string><footer_right_repeat>

Where:

====================  ===============================  =======  ===========================================================
Attribute             Values                           Default  Description
====================  ===============================  =======  ===========================================================
header_left           String                           None     The string to place to the right of the ``--``
header_left_repeat    String                           ``-``    A character to repeat between ``header_left`` and ``header_string``
header_string         String                           None     A string to place in the header
header_right_repeat   String                           None     A character to repeat after ``header_string``
comment_left          String                           None     A string which should exist to the right of the ``--``
footer_left           String                           None     The string to place to the right of the ``--``
footer_left_repeat    String                           ``-``    A character to repeat between ``footer_left`` and ``footer_string``
footer_string         String                           None     A string to place in the footer
footer_right_repeat   String                           None     A character to repeat after ``footer_string``
====================  ===============================  =======  ===========================================================

There are additional options for configuring block comments:

====================  ===============================  =========  ===========================================================
Attribute             Values                           Default    Description
====================  ===============================  =========  ===========================================================
min_height            Integer                          3          Sets minimum number of consecutive comment lines before being considered a block comment
header_alignment      ``left`` ``center`` ``right``   ``center`` Sets horizontal position of the header string
max_header_column     Integer                          120        Sets the maximum length of the combined header
footer_alignment      ``left`` ``center`` ``right``   ``center`` Sets horizontal position of the footer string
max_footer_column     Integer                          120        Sets the maximum length of the combined footer
allow_indenting       ``yes`` ``no``                  ``yes``    Allows indented block comments. Setting this to ``no`` will only detect block comments starting at column 0
====================  ===============================  =========  ===========================================================

Multiple Block Comment Styles
-----------------------------

Each block comment attribute may be configured as either:

* a scalar value, which defines one block comment style
* a list of values, which defines multiple allowed block comment styles

When lists are used, VSG evaluates the block comment as a whole. The header, all middle comment lines, and the footer must all match the **same** style index.

Within one family:

* all scalar values are broadcast to every style index
* list-valued fields must have either 1 entry or ``N`` entries

Across the three block comment rule families:

* ``block_comment_001`` determines the header style count
* ``block_comment_002`` determines the body style count
* ``block_comment_003`` determines the footer style count

All three families must resolve to the same number of styles. If the number of entries does not match, a configuration error is raised.

It is recommended to use ``''`` for empty strings in YAML examples instead of ``null`` when an empty marker is intended.

Examples
--------

It is important to note the rules are disabled by default. They must be enabled using a configuration.

Simple Block Comment
~~~~~~~~~~~~~~~~~~~~

To configure the following example...::

    ----------------------------------
    -- Comment
    -- Comment
    ----------------------------------

...the configuration would be::

    rule:
      block_comment_001:
        disable : False
        header_left : ''
        header_left_repeat : '-'
        header_string : ''
        header_right_repeat : ''
      block_comment_002:
        disable : False
        comment_left : ''
      block_comment_003:
        disable : False
        footer_left : ''
        footer_left_repeat : '-'
        footer_string : ''
        footer_right_repeat : ''

Complex Block Comment
~~~~~~~~~~~~~~~~~~~~~

To configure the following example...::

    --+-<Header>==============================
    --| Purpose:
    --| Author:
    --+------------------------------<Footer>=

...the configuration would be::

    rule:
      block_comment_001:
        disable : False
        header_left : '+'
        header_left_repeat : '-'
        header_string : '<Header>'
        header_right_repeat : '='
        header_alignment : 'left'
      block_comment_002:
        disable : False
        comment_left : '|'
      block_comment_003:
        disable : False
        footer_left : '+'
        footer_left_repeat : '-'
        footer_string : '<Footer>'
        footer_right_repeat : '='
        footer_alignment : 'right'

Multiple Styles
~~~~~~~~~~~~~~~

To allow three different block comment separator styles...::

    --|-----------------------------------------------------------------------------
    --| Comment
    --|-----------------------------------------------------------------------------

    --|==================================================================================
    --| Comment
    --|==================================================================================

    --!-----------------------------------------------------------------------------
    --! Comment
    --!-----------------------------------------------------------------------------

...the configuration would be::

    rule:
      block_comment_001:
        disable : False
        header_left : ['|', '|', '!']
        header_left_repeat : ['-', '=', '-']
        header_string : ['', '', '']
        header_right_repeat : ['-', '=', '-']
        max_header_column : [80, 85, 80]

      block_comment_002:
        disable : False
        comment_left : ['|', '|', '!']

      block_comment_003:
        disable : False
        footer_left : ['|', '|', '!']
        footer_left_repeat : ['-', '=', '-']
        footer_string : ['', '', '']
        footer_right_repeat : ['-', '=', '-']
        max_footer_column : [80, 85, 80]

Autofix Notes
-------------

``block_comment_001`` and ``block_comment_003`` support autofix for separator-only headers and footers.

For example, if a block comment header starts with ``--|-`` and the configured style requires an 80-column ``-`` separator, autofix can rebuild the full separator line to the configured width. The same applies to separator-only footers.

Textual headers and footers continue to report violations normally when they do not match the configured style.

Rules Enforcing Block Comments
------------------------------

* ``block_comment_001``
* ``block_comment_002``
* ``block_comment_003``
