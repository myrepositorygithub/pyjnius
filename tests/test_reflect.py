from jnius.reflect import autoclass

Stack = autoclass('java.util.Stack')
stack = Stack()
stack.push('hello')
stack.push(Stack())
print stack.pop()
print stack.pop()