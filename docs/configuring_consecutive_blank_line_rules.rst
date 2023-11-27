
.. _configuring-consecutive-blank-line-rules:

Configuring Consecutive Blank Line Rules
----------------------------------------

There are rules which will check for excessive number of consecutive blank lines.

There is one option to these rules:

.. |blank_lines_allowed| replace::
   :code:`blank_lines_allowed`

.. |blank_lines_allowed_description| replace::
   The maximum number of consecutive blank lines allowed.

.. |values| replace::
   integer >= 1

.. |default| replace::
   1

+-----------------------+----------+-----------+-----------------------------------+
| Option                | Values   | Default   | Description                       |
+=======================+==========+===========+===================================+
| |blank_lines_allowed| | |values| | |default| | |blank_lines_allowed_description| |
+-----------------------+----------+-----------+-----------------------------------+

This is an example of how to configure the option.

.. code-block:: yaml

   rule :
     whitespace_200:
        blank_lines_allowed: 1

All examples use the following code snippet:

.. code-block:: vhdl

   signal wr_en : std_logic;  -- Two blank lines below


   signal rd_en : std_logic;  -- Three blank lines below



   signal overflow : std_logic;

Example: |blank_lines_allowed| set to :code:`1`
###############################################

.. code-block:: vhdl

   signal wr_en : std_logic;  -- Two blank lines below

   signal rd_en : std_logic;  -- Three blank lines below

   signal overflow : std_logic;

Example: |blank_lines_allowed| set to :code:`2`
###############################################

.. code-block:: vhdl

   signal wr_en : std_logic;  -- Two blank lines below


   signal rd_en : std_logic;  -- Three blank lines below


   signal overflow : std_logic;

Rules Enforcing Consecutive Blank Lines
#######################################

* `whitespace_200 <whitespace_rules..html#whitespace-200>`_
