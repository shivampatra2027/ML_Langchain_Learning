from langchain.tools import tool

@tool
def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    print("Multiplication tool has been called!!")
    return a * b

@tool 
def add(a:int,b:int)->int:
    """Add two number"""
    print("Addition tool has been called!!")
    return a+b;