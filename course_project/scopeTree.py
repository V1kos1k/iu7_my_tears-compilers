from typing import Any
from uuid import uuid4
from graphviz import Digraph

from tinybasicListener import tinybasicListener
from tinybasicParser import tinybasicParser

FILENAME = 'test-output/scope'

class info:
  def __init__(self) -> None:
    self.uid = uuid4()
    self.global_variables = {}

  def to_graph(self):
    dot = Digraph(filename=FILENAME, format="png")
    dot.node(str(self.uid), label=f'{self.format_variables()}', shape="none")

    return dot

  def format_variables(self):
    return "\n".join([f'{variable} = {value}\l' for variable, value in self.global_variables.items()])


class scopeTree(tinybasicListener):
  def __init__(self) -> None:
    super().__init__()

    self.info = None
    self.info_stack = [info()]

  def enterStatement(self, ctx: tinybasicParser.StatementContext):
      self.get_global_variables(ctx)
      self.get_global_input_variables(ctx)

  def exitStatement(self, ctx: tinybasicParser.StatementContext):
    self.info = self.info_stack[0]

  def get_global_variables(self, ctx: tinybasicParser.StatementContext):
    vara_ctx: tinybasicParser.VaraContext = ctx.vara()
    expression_ctx: tinybasicParser.ExpressionContext = ctx.expression(0)

    if vara_ctx == None or expression_ctx == None:
      return

    name = vara_ctx.VAR()
    info = self.info_stack[0]
    info.global_variables[name] = expression_ctx.getText()

  def get_global_input_variables(self, ctx: tinybasicParser.StatementContext):
    varlist_ctx: tinybasicParser.VarlistContext = ctx.varlist()
    if varlist_ctx == None:
      return
    print('get_global_input_variables', varlist_ctx.vara())

    variables = varlist_ctx.vara()

    if len(variables) < 2 or len(variables)%2 != 0:
      print(f"error: unexpected amount of values {variables}")
      return

    info = self.info_stack[0]

    i = 0
    value = None
    while (i < len(variables)):
      if i%2 == 0:
        value = variables[i].getText()
      else:
        info.global_variables[variables[i].getText()] = value
      print('variables[i].getText()', i, variables[i].getText())
      i += 1

  def set_variables_and_values_for_scope(self, variable: Any, value: Any, global_scope):
    if variable == None:
      return

    info = self.info_stack[0]
    print(variable, value)
    print('>>>> variable, value', variable, value)
    info.global_variables[variable] = value


  def to_graph(self) -> Digraph:
    return self.info.to_graph()