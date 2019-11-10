Configuring Number of Signals in Signal Declaration
---------------------------------------------------

VHDL allows of any number of signals to be declared within a single signal declaration.
While this may be allowed, in practice there are limits impossed by the designers.
Limiting the number of signals declared improves the readability of VHDL code.

The default number of signals allowed, 2, can be set by configuring rule **signal_015**.

Overriding Number of Signals
############################

The default setting can be changed using a configuration.
We can use the following configuration to change the number of signals allowed to 1.

.. code-block:: yaml

   ---

   rule :
     signal_015 :
        consecutive : 1

