import sys
from lark import Lark
from lark import Transformer
from functools import reduce

# 構文解析器の実行部
class CalcTransformer(Transformer):
    def expr(self, tree):
        return reduce(lambda x, y: x + y, tree)
    def term(self, tree):
        return reduce(lambda x, y: x * y, tree)
    def factor(self, tree):
        return tree[0]
    def number(self, tree):
        return int(tree[0])

args = sys.argv
text = args[1]
with open("./calc_grammar.lark", encoding="utf-8") as grammar:
    parser = Lark(grammar.read(),start="expr")
    tree = parser.parse(text)
    result = CalcTransformer().transform(tree)
    print(result)