# 1.4. Ignored characters
Comments and whitespace are ignored during lexical parsing unless otherwise noted.

*Comments* can be single-line or multi-line. A single-line comment is any sequence of characters after a pair of `-` characters, before a line break, or before the end of file. A multi-line comment is any sequence of characters between the `--[[` and `]]` character pairs. Multi-line comments can be nested.

```lua
-- By adding square brackets, a single-line comment...
--[[ ...becomes
	a multi-line one.
]]
```

*Whitespace* characters are Unicode characters with the [{scmp}`pattern white space`](https://www.unicodesymbol.com/en/applicable-pattern-white-space-unicodes/meta-58) property, except for the {scmp}`line break`. In some cases, {scmp}`line break` can be interpreted as a statement terminator ({scmp}`semicolon`); in other cases, it is considered whitespace.

Each comment, except for nested comments, is equivalent to one whitespace character.