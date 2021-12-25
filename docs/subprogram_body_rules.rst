.. include:: icons.rst

Subprogram Body Rules
---------------------

subprogram_body_400
###################

|phase_5| |error| |alignment|

This rule checks the alignment of the **<=** and **:=** operators over consecutive sequential assignments in subprogram bodies.

Following extra configurations are supported:

* :code:`if_control_statements_ends_group`,
* :code:`case_control_statements_ends_group`.
* :code:`case_keyword_statements_ends_group`.
* :code:`loop_control_statements_ends_group`,

Refer to the section `Configuring Keyword Alignment Rules <configuring.html#configuring-keyword-alignment-rules>`_ for information on changing the configurations.

**Violation**

.. code-block:: vhdl

   wr_en <= '1';
   rd_en   <= '0';
   v_variable := 10;

**Fix**

.. code-block:: vhdl

   wr_en      <= '1';
   rd_en      <= '0';
   v_variable := 10;

