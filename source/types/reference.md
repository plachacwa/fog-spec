# x.2 Reference types
*Reference types* are used to access an object indirectly. In Fog, there are two types of references: *strong* (with prefix `&`) and *weak* (with prefix `@`). 

```{note}
This section does not describe the memory model and the actual relationships between objects as values ​​in real memory.
```

## Common features
Syntactically, direct access and access by reference are identical. In other words, references are automatically dereferenced. 

To obtain the address stored in a reference (the reference itself, not the referenced object), use the reference's own prefix (`&` or `@`). The value of a reference itself can be freely read and written, copied, moved, passed as an argument, and returned, unless otherwise stated.

A reference may be nullable; a nullability mark (`?`) is placed after the prefix. A reference may also be non-modifying. The `const` modifier, if present, follows the reference prefix and any nullability mark.

Dereferencing an invalid reference results in a compile‑time error. A reference is invalid if it is `null` or if the object it refers to no longer exists.

## `&` Strong reference
A *strong reference* refers to an object, allowing its state to be modified.

If a reference refers to an owned object, it is valid as long as the owner exists; if it refers to an unowned object, the reference is always valid. In either case, a non‑null strong reference is guaranteed to be valid at compile time.

## `@` Weak reference
A *weak reference* is a reference to an owned object or to an object that is strongly referenced; this type of reference does not allow the internal state of the object to be modified.

The validity of a weak reference cannot always be known at compile time; in such cases, dynamic checking of the reference's validity is required.
