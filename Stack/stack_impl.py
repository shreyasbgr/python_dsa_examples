
def create_stack():
    stack = []
    return stack

def is_empty(stack):
    return len(stack) == 0

def push(stack,item):
    stack.append(item)
    print(f"Pushed item is {item}")

def pop(stack):
    if is_empty(stack):
        return "Stack is empty"
    else:
        return stack.pop()

stack = create_stack()
push(stack,4)
push(stack,8)
push(stack,5)
push(stack,7)
pop_val = pop(stack)
print(f"Popped value is {pop_val}")
print(f"Stack: {stack}")