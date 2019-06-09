Frequency Asked Questions
-------------------------

How do I allow my user defined type definitions to not be lower cased?
######################################################################

Rules *type_004* and *signal_011* enforce a lower case consistency for user defined types.
Rule *signal_010* enforces lower case signal types for VHDL base types.
If you want to allow for any case in user defined types, then we need to:

* Disable type_004
* Disable signal_011
* Enable signal_010

Use the following configuration and pass it to VSG when you analyze your code:

.. code-block:: json

   {
       "rule":{
           "type_004":{
               "disable":true
           },
           "signal_011":{
               "disable":true
           },
           "signal_010":{
               "disable":false
           }
       }
   }

How do I align *signal_003*, *constant_003*, *file_003*, *type_003*, *subtype_003*, and *file_003*?
###################################################################################################

The default behavior of VSG is to minimize horizontal spacing whenever possible.
This would result in the following code formatting:

.. code-block:: vhdl

   signal wr_en : std_logic;
   constant size : integer := 1;
   type state_machine is (IDLE, WRITE, READ, DONE);
   subtype read_size is range 0 to 9;
   file defaultImage : load_file_type open read_mode is load_file_name;

If you would rather the code formatting as follows:

.. code-block:: vhdl

   signal   wr_en : std_logic;
   constant size : integer := 1;
   type     state_machine is (IDLE, WRITE, READ, DONE);
   subtype  read_size is range 0 to 9;
   file     defaultImage : load_file_type open read_mode is load_file_name;

Then use the following YAML code in a configuration file:

.. code-block:: yaml

   rule:
     signal_003:
       spaces: 3
     type_003:
       spaces: 5
     subtype_003:
       spaces: 2
     file_003:
       spaces: 5 

