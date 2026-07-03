# 1.3. Identifiers, symbols and suffixes
An *identifier* is a Unicode character sequence that:
- {spec}```lex.identifier|starts with the {uc}`005f|_` character or another character with Unicode property [{scmp}`xid start`](https://www.unicodesymbol.com/en/applicable-xid-start-unicodes/meta-143)```;
- {spec}```lex.identifier|continues with an {scmp}`apostrophe`, the {uc}`005f|_` character and/or characters with Unicode property [{scmp}`xid continue`](https://www.unicodesymbol.com/en/applicable-xid-continue-unicodes/meta-123)```.

{spec}`lex.symbols-suffixes|*Suffixes* are identifiers not separated by whitespace characters from preceding digits, quotation marks, and brackets.` Precending character is not a part of another identifier. *Symbols* are identifiers that are not suffixes.

```lua
    This_is_Symbol'
--  ~~~~~~~~~~~~~~~    <- Symbol borders
    78_this_is_suffix'  
--    ~~~~~~~~~~~~~~~~ <- Suffix borders
```

{spec}```lex.normalization|Identifiers and suffixes are normalized according to *Normalization Form C* ({scmp}`NFC`) as defined in *Unicode Standard Annex #31*.```