.. include:: icons.rst

Subtype Rules
-------------

subtype_001
###########

|phase_4| |error| |indent|

This rule checks for indentation of the **subtype** keyword.

**Violation**

.. code-block:: vhdl

   architecture rtl of fifo is

        subtype read_size is range 0 to 9;
   subtype write_size is range 0 to 9;

   begin

**Fix**

.. code-block:: vhdl

   architecture rtl of fifo is

     subtype read_size is range 0 to 9;
     subtype write_size is range 0 to 9;

   begin


subtype_002
###########

|phase_6| |error|

This rule checks for consistent capitalization of subtype names.

**Violation**

.. code-block:: vhdl

   subtype read_size is range 0 to 9;
   subtype write_size is range 0 to 9;

   signal read  : READ_SIZE;
   signal write : write_size;

   constant read_sz  : read_size := 8;
   constant write_sz : WRITE_size := 1;


**Fix**

.. code-block:: vhdl

   subtype read_size is range 0 to 9;
   subtype write_size is range 0 to 9;

   signal read  : read_size;
   signal write : write_size;

   constant read_sz  : read_size := 8;
   constant write_sz : write_size := 1;

subtype_003
###########

This rule was depricated and replaced with rules:

* `function_015 <function_rules.html#function-015>`_
* `package_019 <package_rules.html#package-019>`_
* `procedure_010 <procedure_rules.html#procedure-010>`_
* `architecture_029 <architecture_rules.html#architecture-029>`_

subtype_004
###########

|phase_7| |disabled| |error|

This rule checks for valid prefixes in subtype identifiers.
The default new subtype prefix is *st\_*.

Refer to the section `Configuring Prefix and Suffix Rules <configuring.html#configuring-prefix-and-suffix-rules>`_ for information on changing the allowed prefixes.

**Violation**

.. code-block:: vhdl

   subtype my_subtype is range 0 to 9;

**Fix**

.. code-block:: vhdl

   subtype st_my_subtype is range 0 to 9;

subtype_600
###########

|phase_7| |disabled| |error|

This rule checks for valid suffixes in subtype identifiers.
The default new subtype suffix is *\_st*.

Refer to the section `Configuring Prefix and Suffix Rules <configuring.html#configuring-prefix-and-suffix-rules>`_ for information on changing the allowed suffixes.

**Violation**

.. code-block:: vhdl

   subtype my_subtype is range 0 to 9;

**Fix**

.. code-block:: vhdl

   subtype my_subtype_st is range 0 to 9;

