# lexer.py - NduTalk Lexer (Week 1)
# Converts source code text into a list of tokens
 
class Token:
    def __init__(self, type_, value, line=1):
        self.type = type_
        self.value = value
        self.line = line
 
    def __repr__(self):
        return f"Token({self.type}, {repr(self.value)}, line={self.line})"
 
 
class Lexer:
    KEYWORDS = {"let", "print", "if", "then", "end"}
 
    def __init__(self, source):
        self.source = source
        self.pos = 0
        self.line = 1
        self.tokens = []
 
    def current_char(self):
        if self.pos >= len(self.source):
            return None
        return self.source[self.pos]
 
    def advance(self):
        if self.current_char() == "\n":
            self.line += 1
        self.pos += 1
 
    def skip_whitespace(self):
        while self.current_char() is not None and self.current_char() in " \t\r":
            self.advance()
 
    def skip_comment(self):
        # Comments start with # and go to the end of the line
        while self.current_char() is not None and self.current_char() != "\n":
            self.advance()
 
    def read_number(self):
        start = self.pos
        while self.current_char() is not None and self.current_char().isdigit():
            self.advance()
        value = self.source[start:self.pos]
        return Token("NUMBER", int(value), self.line)
 
    def read_string(self):
        self.advance()  # skip opening quote
        start = self.pos
        while self.current_char() is not None and self.current_char() != '"':
            if self.current_char() == "\n":
                raise Exception(f"Unterminated string on line {self.line}")
            self.advance()
        if self.current_char() is None:
            raise Exception(f"Unterminated string on line {self.line}")
        value = self.source[start:self.pos]
        self.advance()  # skip closing quote
        return Token("STRING", value, self.line)
 
    def read_identifier(self):
        start = self.pos
        while self.current_char() is not None and (self.current_char().isalnum() or self.current_char() == "_"):
            self.advance()
        value = self.source[start:self.pos]
        if value in self.KEYWORDS:
            return Token("KEYWORD", value, self.line)
        return Token("IDENTIFIER", value, self.line)
 
    def tokenize(self):
        while self.current_char() is not None:
            self.skip_whitespace()
 
            char = self.current_char()
            if char is None:
                break
 
            # Newline – we just skip it (statements are line-based)
            if char == "\n":
                self.advance()
                continue
 
            # Comment
            if char == "#":
                self.skip_comment()
                continue
 
            # Numbers
            if char.isdigit():
                self.tokens.append(self.read_number())
                continue
 
            # Strings
            if char == '"':
                self.tokens.append(self.read_string())
                continue
 
            # Identifiers and keywords
            if char.isalpha() or char == "_":
                self.tokens.append(self.read_identifier())
                continue
 
            # Two-character operator ==
            if char == "=" and self.pos + 1 < len(self.source) and self.source[self.pos + 1] == "=":
                self.tokens.append(Token("OPERATOR", "==", self.line))
                self.advance()
                self.advance()
                continue
 
            # Single-character operators and symbols
            if char in "+-*/=<>()":
                self.tokens.append(Token("OPERATOR" if char not in "()" else "PAREN", char, self.line))
                self.advance()
                continue
 
            # Illegal character
            raise Exception(f"Illegal character '{char}' on line {self.line}")
 
        self.tokens.append(Token("EOF", None, self.line))
        return self.tokens
 
 
# Quick test when you run this file directly
if __name__ == "__main__":
    sample = '''
let x = 10
print x + 5
# this is a comment
let name = "Hello"
'''
    lexer = Lexer(sample)
    tokens = lexer.tokenize()
    for t in tokens:
        print(t)
