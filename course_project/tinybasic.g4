grammar tinybasic;

program
    : line*
    ;

line
   : number statement CR
   | statement CR
   ;

statement
   : 'PRINT' exprlist
   | 'IF' expression relop expression 'THEN'? statement
   | 'GOTO' number
   | 'INPUT' varlist
   | 'LET'? vara '=' expression
   | 'GOSUB' expression
   | 'RETURN'
   | 'CLEAR'
   | 'LIST'
   | 'RUN'
   | 'END'
   ;

exprlist
   : (STRING | expression) (',' (STRING | expression))*
   ;

varlist
   : vara (',' vara)*
   ;
 
expression
   : ('+' | '-' )? term (('+' | '-') term)*
   ;

term
   : factor (('*' | '/') factor)*
   ;

factor
   :
   vara
   | number
   ;

vara
    : VAR
    | STRING
    ;

number
   : DIGIT +
   ;

relop
   : ('<' ('>' | '=' )?)
   | ('>' ('<' | '=' )?)
   | '='
   ;


STRING
   : '"' ~ ["\r\n]* '"'
   ;


DIGIT
   : '0' .. '9'
   ;


VAR
   : 'A' .. 'Z'
   ;


CR
   : [\r\n]+
   ;


WS
   : [ \t] -> skip
   ;