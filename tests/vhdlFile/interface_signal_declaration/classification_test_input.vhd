

entity FIFO is
  port (
    port1 : in std_logic;
    port1 : out std_logic;
    port1 : inout std_logic bus;
    port1 : buffer std_logic bus := "asdf";
    port1 : linkage std_logic := "asdf";
    port1 : std_logic;
    port1 : view some_view;
    port1 : view some_view of rec;
    port1 : view some_view of rec(f1(5 downto 0));
    port1 : view some_view of rec(f1(5 downto 0), f2(0 to 1));
    port1 : view (some_array_view) of rec_array;
    port1 : view (some_array_view) of rec_array(0 to 7)
  );
end entity FIFO;

entity FIFO is
  port (
    signal port1 : in std_logic;
    signal port1 : out std_logic;
    signal port1 : inout std_logic;
    signal port1 : buffer std_logic;
    signal port1 : linkage std_logic;
    signal port1 : std_logic;
    signal port1 : view some_view;
    signal port1 : view some_view of rec;
    signal port1 : view some_view of rec(f1(5 downto 0));
    signal port1 : view some_view of rec(f1(5 downto 0), f2(0 to 1));
    signal port1 : view (some_array_view) of rec_array;
    signal port1 : view (some_array_view) of rec_array(0 to 7)
  );
end entity FIFO;
