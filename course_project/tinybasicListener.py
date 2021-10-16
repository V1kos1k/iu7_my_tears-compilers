# Generated from tinybasic.g4 by ANTLR 4.9
from antlr4 import *

if __name__ is not None and "." in __name__:
    from .tinybasicParser import tinybasicParser
else:
    from tinybasicParser import tinybasicParser

# This class defines a complete listener for a parse tree produced by tinybasicParser.
class tinybasicListener(ParseTreeListener):
    # Enter a parse tree produced by tinybasicParser#program.
    def enterProgram(self, ctx:tinybasicParser.ProgramContext):
        pass

    # Exit a parse tree produced by tinybasicParser#program.
    def exitProgram(self, ctx:tinybasicParser.ProgramContext):
        pass


    # Enter a parse tree produced by tinybasicParser#line.
    def enterLine(self, ctx:tinybasicParser.LineContext):
        print('line', ctx.getText())
        pass

    # Exit a parse tree produced by tinybasicParser#line.
    def exitLine(self, ctx:tinybasicParser.LineContext):
        pass


    # Enter a parse tree produced by tinybasicParser#statement.
    def enterStatement(self, ctx:tinybasicParser.StatementContext):
        print('statement', ctx.getText())
        pass

    # Exit a parse tree produced by tinybasicParser#statement.
    def exitStatement(self, ctx:tinybasicParser.StatementContext):
        pass


    # Enter a parse tree produced by tinybasicParser#exprlist.
    def enterExprlist(self, ctx:tinybasicParser.ExprlistContext):
        print('exprlist', ctx.getText())
        pass

    # Exit a parse tree produced by tinybasicParser#exprlist.
    def exitExprlist(self, ctx:tinybasicParser.ExprlistContext):
        pass


    # Enter a parse tree produced by tinybasicParser#varlist.
    def enterVarlist(self, ctx:tinybasicParser.VarlistContext):
        print('varlist', ctx.getText())
        pass

    # Exit a parse tree produced by tinybasicParser#varlist.
    def exitVarlist(self, ctx:tinybasicParser.VarlistContext):
        pass


    # Enter a parse tree produced by tinybasicParser#expression.
    def enterExpression(self, ctx:tinybasicParser.ExpressionContext):
        print('expression', ctx.getText())
        pass

    # Exit a parse tree produced by tinybasicParser#expression.
    def exitExpression(self, ctx:tinybasicParser.ExpressionContext):
        
        pass


    # Enter a parse tree produced by tinybasicParser#term.
    def enterTerm(self, ctx:tinybasicParser.TermContext):
        print('term', ctx.getText())
        pass

    # Exit a parse tree produced by tinybasicParser#term.
    def exitTerm(self, ctx:tinybasicParser.TermContext):
        pass


    # Enter a parse tree produced by tinybasicParser#factor.
    def enterFactor(self, ctx:tinybasicParser.FactorContext):
        print('factor', ctx.getText())
        pass

    # Exit a parse tree produced by tinybasicParser#factor.
    def exitFactor(self, ctx:tinybasicParser.FactorContext):
        pass


    # Enter a parse tree produced by tinybasicParser#vara.
    def enterVara(self, ctx:tinybasicParser.VaraContext):
        print('vara', ctx.getText())
        pass

    # Exit a parse tree produced by tinybasicParser#vara.
    def exitVara(self, ctx:tinybasicParser.VaraContext):
        pass


    # Enter a parse tree produced by tinybasicParser#number.
    def enterNumber(self, ctx:tinybasicParser.NumberContext):
        print('number', ctx.getText())
        pass

    # Exit a parse tree produced by tinybasicParser#number.
    def exitNumber(self, ctx:tinybasicParser.NumberContext):
        pass


    # Enter a parse tree produced by tinybasicParser#relop.
    def enterRelop(self, ctx:tinybasicParser.RelopContext):
        print('relop', ctx.getText())
        pass

    # Exit a parse tree produced by tinybasicParser#relop.
    def exitRelop(self, ctx:tinybasicParser.RelopContext):
        pass



del tinybasicParser