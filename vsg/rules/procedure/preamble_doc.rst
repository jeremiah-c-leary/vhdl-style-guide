There are three forms a procedure:  with parameters, without parameters, and a package declaration:

**with parameters**

.. code-block:: vhdl

   procedure average_samples (
      constant a : in integer;
      signal b : in std_logic;
      variable c : in std_logic_vector(3 downto 0);
      signal d : out std_logic) is
   begin
   end procedure average_samples;

**without parameters**

.. code-block:: vhdl

   procedure average_samples is
   begin
   end procedure average_samples;

**package declaration**

.. code-block:: vhdl

   procedure average_samples;

   procedure average_samples (
      constant a : in integer;
      signal b : in std_logic;
      variable c : in std_logic_vector(3 downto 0);
      signal d : out std_logic);
