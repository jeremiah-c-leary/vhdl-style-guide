.. _configuring-use-clause-indenting:

Configuring Use Clause Indenting
--------------------------------

The indent of a use clause is set during the indent phase shortly after a file is read.

There are several options which allow configuration of use clauses.

.. |integer_value| replace::
   :code:`<integer>`

.. |current_value| replace::
   :code:`current`

.. |plus_value| replace::
   :code:`'+<integer>'`

.. |minus_value| replace::
   :code:`'-<integer>'`

.. |token_after_library_clause| replace::
   :code:`token_after_library_clause`

.. |token_if_no_matching_library_clause| replace::
   :code:`token_if_no_matching_library_clause`

.. |integer__description| replace::
   |integer_value| = Sets the indent level to the specified value.

.. |current__description| replace::
   |current_value| = Uses the existing indent level.

.. |plus_one__description| replace::
   |plus_value| = Increase the indent relative to the current indent level.

.. |minus_one__description| replace::
   |minus_value| = Decrease the indent relative to the current indent level.

+---------------------------------------+-----------------+--------------+----------------------------+
| Option                                |   Values        | Default      | Description                |
+=======================================+=================+==============+============================+
| |token_after_library_clause|          | |integer_value| | :code:`'+1'` | * |integer__description|   |
|                                       | |current_value| |              | * |current__description|   |
+---------------------------------------+ |plus_value|    |              | * |plus_one__description|  |
| |token_if_no_matching_library_clause| | |minus_value|   |              | * |minus_one__description| |
+---------------------------------------+-----------------+--------------+----------------------------+

This is an example of how to configure these options.

.. code-block:: yaml

   indent:
     tokens:
       use_clause:
         keyword:
           token_after_library_clause: '+1'
           token_if_no_matching_library_clause: '+1'

The following code snippet is used for all examples.

.. code-block:: vhdl

    library ieee;
      use ieee.std_logic_1164.all;

      use work.my_package.all;

Example: |token_if_no_matching_library_clause| set to |current_value|
#####################################################################

The |token_if_no_matching_library_clause| option controls the indent of use clauses if there is no matching library clause.

.. code-block:: vhdl

    library ieee;
      use ieee.std_logic_1164.all;

    use work.my_package.all;

Example: |token_if_no_matching_library_clause| set to :code:`'+1'`
##################################################################

.. code-block:: vhdl

    library ieee;
      use ieee.std_logic_1164.all;

      use work.my_package.all;

Example: |token_after_library_clause| set to |current_value|
############################################################

The |token_after_library_clause| option controls the indent of use clauses if there is a matching library clause.

.. code-block:: vhdl

    library ieee;
    use ieee.std_logic_1164.all;

      use work.my_package.all;

Example: |token_after_library_clause| set to :code:`'+1'`
#########################################################

.. code-block:: vhdl

    library ieee;
      use ieee.std_logic_1164.all;

      use work.my_package.all;

Rules Enforcing Use Clause Indenting
####################################

* `library_008 <library_rules.html#library-008>`_
