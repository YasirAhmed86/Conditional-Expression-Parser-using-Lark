from lark import Lark, Transformer

grammar = r"""
    start: pre_assignments if_stmt

    pre_assignments: (xy_assign)*
    xy_assign: XY "=" NUMBER ";"

    XY: "x" | "y"
    
    if_stmt: "if" "(" cond ")" block (elif_stmt)* (else_stmt)?
    elif_stmt: "else" "if" "(" cond ")" block
    else_stmt: "else" block
    
    cond: operand OP operand
    operand: XY       -> var
           | NUMBER   -> number
    
    OP: ">" | "<" | "==" | "!="

    block: "{" z_assign "}"
    z_assign: "z" "=" NUMBER ";"

    %import common.NUMBER
    %import common.WS
    %ignore WS
"""

class EvalTransformer(Transformer):
    def __init__(self):
        self.env = {"x": 0, "y": 0, "z": None}
    
    def xy_assign(self, items):
        var = items[0].value 
        value = int(items[1].value)
        self.env[var] = value

    def if_stmt(self, items):
        cond = items[0]
        block = items[1]
        elifs = []
        else_block = None
        for item in items[2:]:
            if isinstance(item, tuple):
                elifs.append(item)
            else:
                else_block = item

        if self.evaluate_condition(cond):
            self.execute_block(block)
            return
        
        for cond_elif, block_elif in elifs:
            if self.evaluate_condition(cond_elif):
                self.execute_block(block_elif)
                return
        
        if else_block is not None:
            self.execute_block(else_block)
    
    def elif_stmt(self, items):
        cond = items[0]
        block = items[1]
        return (cond, block)
    
    def else_stmt(self, items):
        return items[0]
    
    def cond(self, items):
        left = items[0]
        op = items[1].value 
        right = items[2]
        return (left, op, right)
    
    def var(self, items):
        return items[0].value
    
    def number(self, items):
        return int(items[0])
    
    def block(self, items):
        return items[0]
    
    def z_assign(self, items):
        return int(items[0].value)
    
    def execute_block(self, block):
        self.env["z"] = block
    
    def evaluate_condition(self, cond):
        left, op, right = cond
        left_val = self.env[left] if isinstance(left, str) else left
        right_val = self.env[right] if isinstance(right, str) else right
        if op == ">":
            return left_val > right_val
        elif op == "<":
            return left_val < right_val
        elif op == "==":
            return left_val == right_val
        elif op == "!=":
            return left_val != right_val
        else:
            raise Exception(f"Unknown operator: {op}")
    
    def start(self, items):
        return self.env

parser = Lark(grammar, parser='earley', transformer=EvalTransformer())

example_program = """
x = 2;
y = 3;
if (x < 3) { z = 10; } else if (y == 2) { z = 20; } else { z = 30; }
"""
result = parser.parse(example_program)
print("The value of z is:", result["z"])
