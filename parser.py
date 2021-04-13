import sys
import lexer
from token import STRING

class Parser:

    TYPE = ['INT','BOOL', 'FLOAT', 'CHAR', 'LIST']
    STATEMENT= ['SEMICOLON', 'LBRACE', 'IDENTIFIER', 'IF', 'WHILE']
    REL_OP = ['LT', 'LTE', 'GT', 'GTE']
    ADD_OP = ['ADD', 'SUB']
    MUL_OP = ['MUL', 'DIV', 'MODULO']
    EQU_OP = ['EQ', 'NEQ']
    LITERAL = ['INTEGER_LIT', 'FLOAT_LIT', 'CHAR_LIT', 'BOOL_LIT']
    UNA_OP = ['SUB', 'EXCL']


    def __init__(self):  
        self.tokens = []
        self.errors = 0
        self.indent = []
        

    def show_next(self, n=1):
        try:
            return self.tokens[n - 1]
        except IndexError:
            print('ERROR: no more tokens left!')
            sys.exit(1)

    def expect(self, kind):
        actualToken = self.show_next()
        actualKind = actualToken.kind
        actualPosition = actualToken.position
        if isinstance(kind, STRING) : 
            if actualKind == kind:
                return self.accept_it()
            else:
                print('Error at {}: expected {}, got {} instead'.format(str(actualPosition), kind, actualKind))
                sys.exit(1)
        else : 
            if actualKind in kind : 
                 return self.accept_it()
            else:
                print('Error at {}: expected {}, got {} instead'.format(str(actualPosition), kind, actualKind))
                sys.exit(1)

    def accept_it(self):
        token = self.show_next()
        output = str(token.kind) + ' ' + token.value
        self.indentator.say(output)
        return self.tokens.pop(0)

    def parse(self, tokens):
        self.tokens = tokens
        self.parse_program()

    def parse_program(self):
        for token in self.tokens :
            if token.type == 'TAB' :
                self.indent[token.ligne()-1] += 1
                self.expect('TAB') #pop out of tokens 
                continue
            if token.type == 'IDENTIFIER' : 
                self.expect("IDENTIFIER")
                if self.show_next().type == 'EOL' : 

                self.parse_declarations()
            self.parse_statements()
            self.parse_assignment()

        self.expect('RBRACE')
        if (self.errors == 1):
            print('WARNING: 1 error found!')
        elif (self.errors > 1):
            print('WARNING: ' + str(self.errors) + ' errors found!')
        else:
            print('parser: syntax analysis successful!')

    def parse_declaration(self):
        for l
        self.expect('IDENTIFIER')
        self.expect('EQ')
        self.parse_expression()

    def parse_statements(self):
        self.indentator.indent('Parsing Statements')
        # TODO
        self.indentator.dedent()

    def parse_expression(self) : 
    

    def parse_assignment(self) : 
        self.expect('IDENTIFIER')
        self.expect('ASSIGN')
        self.parse_expression()
        self.expect('SEMICOLON')

    def parse_expression(self) : 
        self.parse('IDENTIFIER')
        self.parse(self.ADD_OP)
        self.parse('IDENTIFIER')
        