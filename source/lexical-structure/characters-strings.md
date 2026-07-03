# 1.6. Character and string literals
A *character literal* is any Unicode character—except {scmp}`apostrophe` and {scmp}`line break`— or a valid escape sequence enclosed within a pair of {uc}`0027|\'` characters.

A *string literal* is any sequence of Unicode characters—except {uc}`0022|\"`—and valid escape sequences enclosed within a pair of {uc}`0022|\"` characters.

```lua
'a' -- one character
"many" -- characters in string
```

*Escape character sequences* are equivalent to a single Unicode character. Each escape sequence begins with the {uc}`005c|\\` character (backslash). The length and meaning of an escape sequence are determined by the character following the backslash:
- the {uc}`0078|x`, {uc}`0075|u`, or {uc}`0055|U` character following a backslash indicates that the sequence escapes a single, double, or quadruple code point, respectively. The `x` character is followed by {spec}```lex.valid-8bit-char|two hexadecimal digits, corresponding to the Unicode character representation ({scmp}`utf-32` encoding)```; the `u` character is followed by four hexadecimal digits; and the `U` character is followed by eight hexadecimal digits.
```hs
'\x78'       -- letter 'x'
'\u0434'     -- Cyrillic letter 'д'
'\U0001f601' -- 😁
```
- {uc}`006e|n` equals {scmp}`lf`, {uc}`0072|r` equals {scmp}`cr`, and {uc}`0074|t` equals {uc}`0009|Tab`.
- {uc}`0030|0` equals {scmp}`null character`.
- {uc}`0062|b` equals {uc}`0008|Backspace`.
- {uc}`0065|e` equals {uc}`001b|Escape`.
- {uc}`0022|\"`, {uc}`0027|\'`, and {uc}`005c|\\` escape themselves.
- {scmp}`line break` escape sequence equals zero characters.