
architecture RTL of FIFO is

  constant StartDay : WeekDay := Sat;

  constant LogicalGND : Bit := '0';

  constant BusWidth, QueueLength : Integer := 16;

  constant CLKPeriod : Time := 15 ns;

  constant MaxSimTime : Time := 200 * CLKPeriod;

  constant EntryCode : NumericCodeType := (2,6,4,8,0,0,1,3);

  constant DataBusReset: Std_Logic_Vector(7 downto 0) := "00000000";

begin

end architecture RTL;
