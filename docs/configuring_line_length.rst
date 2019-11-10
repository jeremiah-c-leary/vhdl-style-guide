Configuring the Maximum Line Length
-----------------------------------

Limiting the line length of the VHDL code can improve readability.
Code that exceeds the editor window is more difficult to read.

The default line length is 120, and can be set by configuring rule **length_001**.

Overriding Line Length
######################

The default setting can be changed using a configuration.
We can use the following configuration to change the line length to 180. 

.. code-block:: yaml

   ---

   rule :
     length_001 :
        length : 180

