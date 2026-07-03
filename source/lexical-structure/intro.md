# 1. Lexical structure

Source code files are read as a {scmp}`utf-8` character sequence without {scmp}`bom`. 

{spec}```lex.nullchar|The {scmp}`u+0000` character must not be used in program text.``` {spec}```lex.valid-utf8|Program text must contain only valid {scmp}`utf-8` octet sequences.```

The resulting text is divided into a token sequence according to the following rules.

```{toctree}
:hidden:
glossary
keywords
identifiers
ignored
directives
characters-strings
numeric
operators
punctuation
```