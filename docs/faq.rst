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
