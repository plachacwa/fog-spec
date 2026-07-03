# x.1. Primitive types

## Boolean type
The boolean type, which the `bool` corresponds to, is a primitive type with two possible values: `false` and `true`.

When converted to numeric types, the value `false` corresponds to the zero, and the value `true` corresponds to the number `1` or, when converted from numeric types, any non-zero number.

## Numeric types
There are signed and unsigned integer and floating-point types.

*Unsigned integer* types have prefix&nbsp;`u`, *signed integer* types have prefix&nbsp;`i`. Generic Built-in integer types are listed below:
```{csv-table}
:header-rows: 1

Type,   Minimum, Maximum,      , Type,   Minimum,              Maximum
`u08`,  0,       2{sup}`8`-1,  , `i08`,  -2{sup}`7`,           2{sup}`7`-1
`u16`,  0,       2{sup}`16`-1, , `i16`,  -2{sup}`15`,          2{sup}`15`-1
`u32`,  0,       2{sup}`32`-1, , `i32`,  -2{sup}`31`,          2{sup}`31`-1
`u64`,  0,       2{sup}`64`-1, , `i64`,  -2{sup}`63`,          2{sup}`63`-1
`u128`, 0,       2{sup}`128`-1,, `i128`, -2{sup}`127`,         2{sup}`127`-1
`usize`,0,       *see below*,  , `isize`,-`isize`{sub}`max`+1, `usize`{sub}`max` / 2
```

`usize` and `isize` are implementation-defined: `usize` is an alias for the least built-in unsigned integer type that may represent every address at the target platform. `isize` is alias for corresponding signed integer type.

Built-in *floating-point types* are represented by {scmp}`ieee 754-2019` "binary32", "binary64" and "binary128" types as `f32`, `f64` and `f128`, respectively.

## Character types
There is three built-in character types; each value of any character type represents a valid Unicode code point.

The `c08` type represents characters with codes from {scmp}`u+0000` to {scmp}`u+00ff`; the `c16` type, up to {scmp}`u+ffff`; and the `c32` type, up to {scmp}`u+10ffff`. Values from {scmp}`d800`{sub}`16` to {scmp}`dfff`{sub}`16` are not valid values ​​of type `c32`.

## Void type
The `void` type has one value: nothing. The value can be written as `()` or by the name of its type; it can be used as a temporary object, but cannot be written or read.