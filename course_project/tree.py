from typing import Any
from uuid import uuid4

from antlr4.tree.Tree import TerminalNodeImpl
from graphviz import Digraph


class Tree:
    def __init__(self, ctx: Any):
        self.id = uuid4()
        self.children: list[Tree] = []

        if isinstance(ctx, TerminalNodeImpl):
            self.name = ctx.getText()
            return

        node_type = type(ctx).__name__.removesuffix("Context")
        if len(node_type) == 0:
            self.name = "__unknown_node__"
            return

        self.name = node_type[0].lower() + node_type[1:]

        for child in ctx.getChildren():
            child_node = Tree(child)
            self.children.append(child_node)

    def to_graph(self, filename: str):
        dot = Digraph(filename=filename, format='png')
        self.add_to_graph(dot)

        return dot

    def add_to_graph(self, dot: Digraph):
        dot.node(str(self.id), label=f'{self.name}')

        for child in self.children:
            child.add_to_graph(dot)
            dot.edge(str(self.id), str(child.id))
