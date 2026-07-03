# 1.7. Numeric literals
A *numeric literal* is a valid sequence of characters beginning with a {scmp}`decimal digit`. There are non-decimal literals, decimal integer literals, floating-point literals, and scientific notation literals.
- A *non-decimal integer* literal begins with the {uc}`0030|0` character, followed by an alphabetic character indicating the number system or an {scmp}`octal digit`. These literals cannot be accompanied by suffixes.
  - A *binary* literal is denoted by the {uc}`0042|B` or {uc}`0062|b` alphabetic character, followed by {scmp}`binary digits` and {scmp}`apostrophes`.
  - An *octal* literal is denoted by the {uc}`004f|O` or {uc}`006f|o` alphabetic character, followed by {scmp}`octal digits` and {scmp}`apostrophes`. The alphabetic character is optional.
  - A *hexadecimal* literal is denoted by the {uc}`0058|X` or {uc}`0078|x` alphabetic character, followed by {scmp}`hexadecimal digits` and {scmp}`apostrophes`.
```lua
0b01, 0B10   -- binary numbers
0o1, 0O2, 07 -- octal numbers
0x01, 0XFF   -- hexadecimal numbers
```
- A *decimal integer* literal begins with any decimal digit except {uc}`0030|0` and contains only {scmp}`decimal digits` and {scmp}`apostrophes`; or contains a single {uc}`0030|0` character.
```lua
    0, 1m, 64min
--  ^  ^   ^^    -- decimal integers
```
- *Decimal floating-point* literals contain two sequences of {scmp}`decimal digits` and {scmp}`apostrophes`, separated by a single {uc}`002e|.` character (decimal point). A decimal point cannot be the initial or final character of a literal.
```lua
    0.0, 0.12f, 3.14
--  ^^^  ^^^^   ^^^^ -- decimal floating-point numbers
```
- Numeric literals *in scientific notation* consist of a mantissa—any valid decimal literal—and an exponent—a decimal integer literal—separated by an exponent character, represented by {uc}`0045|E` or {uc}`0065|e`, optionally followed by the character {uc}`002b|+` or {uc}`002d|-`. {uc}`0030|0` can be first character of an exponent.
```lua
    3e08, 6.4e-7
--  ^^^^  ^^^^^^ -- numbers in scientific notation
```