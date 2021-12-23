.. include:: icons.rst

File Rules
----------

file_001
########

|phase_4| |error| |indent|

This rule checks the indent of **file** declarations.

**Violation**

.. code-block:: vhdl

   architecture rtl of fifo is

   file defaultImage : load_file_type open read_mode is load_file_name;

   file defaultImage : load_file_type open read_mode
   is load_file_name;

   begin

**Fix**

.. code-block:: vhdl

   architecture rtl of fifo is

     file defaultImage : load_file_type open read_mode is load_file_name;

     file defaultImage : load_file_type open read_mode
       is load_file_name;

   begin

file_002
########

|phase_6| |error| |case| |case_keyword|

This rule checks the **file** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   architecture rtl of fifo is

     FILE defaultImage : load_file_type open read_mode is load_file_name;

   begin

**Fix**

.. code-block:: vhdl

   architecture rtl of fifo is

     file defaultImage : load_file_type open read_mode is load_file_name;

   begin

file_003
########

This rule was depricated and replaced with rules:

* `function_015 <function_rules.html#function-015>`_
* `package_019 <package_rules.html#package-019>`_
* `procedure_010 <procedure_rules.html#procedure-010>`_
* `architecture_029 <architecture_rules.html#architecture-029>`_

