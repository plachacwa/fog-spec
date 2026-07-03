# 1.8. Operators
An *operator* is any sequence of characters belonging to the *operator character* set that is not part of other tokens:

:::borderless-list-wrapper
:::nowrap-list-wrapper
```{list-table} Operator characters
:header-rows: 0 
* - {uc}``0021|!``
  - {uc}``002d|-``
  - {uc}``003f|?``

* - {uc}``0024|$``
  - {uc}``002e|.``
  - {uc}``0040|@``

* - {uc}``0025|%``
  - {uc}``002f|/``
  - {uc}``005c|\\``
* - {uc}``0026|&``
  - {uc}``003a|:``
  - {uc}``005e|^``
* - {uc}``002a|*``
  - {uc}``003c|<``
  - {uc}``0060|&#96;``
* - {uc}``002b|+``
  - {uc}``003d|=``
  - {uc}``007c||``
* - {uc}``002c|,``
  - {uc}``003e|>``
  - {uc}``007e|~``
```
:::
:::

In addition to built-in operators, a program can define its own operators.

Any non-existent operator (not built into the language or defined by the program) may be parsed into existing operators, if any exist. Splitting algorithm:

1. The operator that is the longest substring from the beginning of the sequence of unsplit operators is selected;
2. If the current operator can act in different functions (prefix, binary, or postfix), then:
    - Before any binary or N-ary operator, or before the last operator in the sequence, a postfix operator is preferred over a prefix operator, and a binary or N-ary operator is preferred over a postfix operator.
    - If a binary or N-ary operator has already appeared in the sequence, but a prefix one has not, or the current operator is the last operator in the chain, then a postfix operator is preferred over a binary or N-ary operator, and a prefix operator is preferred over a postfix operator.
    - If a prefix operator has already appeared in the sequence, then operators other than prefix ones are prohibited.
3. If there is no suitable option, the algorithm fails. The remaining sequence of operator symbols continues to be considered non-existent and causes a compilation error.

```{note}
It is guaranteed that no single operator can simultaneously implement binary and N-ary behaviour.
```

Some operators may exist and be interpreted by the compiler, but may be prohibited from use in the program text (their use is considered a compilation error).