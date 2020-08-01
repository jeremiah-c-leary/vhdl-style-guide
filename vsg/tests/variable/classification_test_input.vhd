

variable INDEX: integer range 0 to 99 := 0;

variable COUNT: POSITIVE;

variable MEMORY: BIT_MATRIX (0 to 7, 0 to 1023);

shared variable Counter: SharedCounter;

shared variable addend, augend, result: ComplexNumber;

variable bit_stack: VariableSizeBitArray := "0000";

shared
variable
addend
,
augend
,
result
:
ComplexNumber
;
