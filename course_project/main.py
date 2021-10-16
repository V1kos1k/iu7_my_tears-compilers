from os import strerror
from antlr4 import *
import tinybasicLexer
import tinybasicParser
from tree import Tree
from scopeTree import scopeTree


def main():
  input = FileStream("example/prog1.txt")
  lexer = tinybasicLexer.tinybasicLexer(input)
  stream = CommonTokenStream(lexer)
  parser = tinybasicParser.tinybasicParser(stream)
  tree = parser.program()
  renderTree = Tree(tree).to_graph('./test-output/tree.gv')
  renderTree.render('./test-output/tree.gv')
  walker = ParseTreeWalker()

  stream.reset()
  scope_tree = scopeTree()
  walker.walk(scope_tree, tree)
  g = scope_tree.to_graph()
  g.render()

  stream.fill()
  print("\n\n\n")
  print("\n".join([str({token.text: parser.symbolicNames[token.type] if parser.symbolicNames[token.type] != "<INVALID>" else token.type}) for token in stream.tokens]))

  pass


if __name__ == '__main__':
    main()