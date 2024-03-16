Classifying
-----------

The Classifying process takes the output of the tokenize process along with the defined token and applies the rules in the VHDL LRM.
The process employs a recursive methodology to apply the rules.
The rules are divided into python modules under the vsg/vhdlFile/classify directory.
Each module name matches a VHDL production name.
Each module will have at least one of the following functions:

* detect
* classify
* classify_until

detect
======

The detect function is used to check if a production exists.
It will typically call the classify function if the production is detected.

classify
========

The classify function takes each token in the tokenized list and assigns a corresponding token from the token classes.

classify_until
==============

The classify_until function performs the same function as classify except it stops when it detects a particular token value.
The token value can be a special character like a close parenthesis or a colon, or a known word.

Example
=======

For example, the following production for the architecture_body:

.. code-block:: text

   architecture_body ::=
       architecture identifier of *entity*_name is
           architecture_declarative_part
       begin
           architecture_statement_part
       end [ architecture ] [ *architecture*_simple_name ] ;

...has a classifier file named vsg/vhdlFile/classify/architecture_body.py.

This file has a detect function:

.. code-block:: python

   def detect(iToken, lObjects):
       '''
       architecture identifier of *entity*_name is
           architecture_declarative_part
       begin
           architecture_statement_part
       end [ architecture ] [ *architecture*_simple_name ] ;
       '''

       if utils.is_next_token('architecture', iToken, lObjects):
           return classify(iToken, lObjects)
       return iToken

The detect function searches for the keyword 'architecture' in the tokenized list.
If this keyword is found then it calls the classify function.

The classify function:

.. code-block:: python

   def classify(iToken, lObjects):

       iCurrent = classify_opening_declaration(iToken, lObjects)

       iCurrent = architecture_declarative_part.detect(iCurrent, lObjects)

       iCurrent = utils.assign_next_token_required('begin', token.begin_keyword, iCurrent, lObjects)

       iCurrent = architecture_statement_part.classify_until(['end'], iCurrent, lObjects)

       iCurrent = classify_closing_declaration(iToken, lObjects)

       return iCurrent

...includes two helper functions classify_opening_declaration and classify_closing_declaration:

.. code-block:: python

   def classify_opening_declaration(iToken, lObjects):

       iCurrent = utils.assign_next_token_required('architecture', token.architecture_keyword, iToken, lObjects)
       iCurrent = utils.assign_next_token(token.identifier, iCurrent, lObjects)
       iCurrent = utils.assign_next_token_required('of', token.of_keyword, iCurrent, lObjects)
       iCurrent = utils.assign_next_token(token.entity_name, iCurrent, lObjects)
       iCurrent = utils.assign_next_token_required('is', token.is_keyword, iCurrent, lObjects)

       return iCurrent

.. code-block:: python

   def classify_closing_declaration(iToken, lObjects):

       iCurrent = utils.assign_next_token_required('end', token.end_keyword, iToken, lObjects)
       iCurrent = utils.assign_next_token_if('architecture', token.end_architecture_keyword, iCurrent, lObjects)
       iCurrent = utils.assign_next_token_if_not(';', token.architecture_simple_name, iCurrent, lObjects)
       iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)

       return iCurrent

The classification of the opening portion of the production, from **architecture** to **is**, is handled by the classify_opening_declaration function.

After the **is** keyword, the detect function of the architecture_declarative_part is called to check if there is anything in that production.
If there are no more items in the architecture_declarative_part, then the begin keyword is classified.
After the **begin** keyword, the detect function of the architecture_statement_part is called to check if there is anything in that production.
If there are no more items in the architecture_statement_part, then the closing portion of the production, from **end** to the semicolon, is handled by the classify_closing_declaration function.

The recursive nature is implemented by calling other productions and then those productions returning to the caller.
