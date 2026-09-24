# NduTalk Language Specification
 
## Language Overview
NduTalk is a simple, Turing-incomplete toy language designed for educational purposes.
It supports variable assignment, arithmetic expressions with precedence,
string literals, print statements, and simple if-then-end conditionals.
It deliberately has no loops or functions, keeping it Turing-incomplete.
 
## Example Programs
 
### Example 1 – Basic Arithmetic
```
let a = 10
let b = 5
print a + b * 2
```
Expected output: 20
 
### Example 2 – Strings
```
let name = "Niger Delta"
print name
```
Expected output: Niger Delta
 
### Example 3 – Simple Conditional
```
let score = 85
if score > 50 then
  print "Pass"
end
```
Expected output: Pass
 
### Example 4 – Mixed
```
let x = 7
let y = 3
print x * y + 1
let msg = "Done"
print msg
```
 
## Formal Grammar (EBNF)
 
program        = { statement } ;
 
statement      = assignment
               | print_stmt
               | if_stmt
               | comment ;
 
assignment     = "let" , identifier , "=" , expression ;
 
print_stmt     = "print" , expression ;
 
if_stmt        = "if" , expression , "then" , { statement } , "end" ;
 
expression     = term , { ("+" | "-") , term } ;
 
term           = factor , { ("*" | "/") , factor } ;
 
factor         = number
               | string
               | identifier
               | "(" , expression , ")"
               | comparison ;
 
comparison     = expression , (">" | "<" | "==") , expression ;
 
identifier     = letter , { letter | digit | "_" } ;
 
number         = digit , { digit } ;
 
string         = '"' , { character } , '"' ;
 
comment        = "#" , { character } ;
 
letter         = "A" | ... | "Z" | "a" | ... | "z" ;
digit          = "0" | ... | "9" ;
 
## Token Types
- KEYWORD: let, print, if, then, end
- IDENTIFIER: variable names
- NUMBER: integer literals
- STRING: text inside double quotes
- OPERATOR: + - * / = > < ==
- PAREN: ( )
- COMMENT: lines starting with #
- EOF: end of file
 
## Design Notes
The language is intentionally small. Multiplication and division have higher
precedence than addition and subtraction. There are no loops, so the language
is Turing-incomplete as required by the assignment.
