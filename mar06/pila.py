class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None
            #raise IndexError("La pila está vacía. No se pueden eliminar elementos de una pila vacía.")

    def is_empty(self):
        return len(self.items) == 0
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None
        
    def check_parentheses(self, expression):
        stack = Stack()
        parentheses_map = {')': '(', '}': '{', ']': '['}
        
        for char in expression:
            if char in parentheses_map.values():  # Si el carácter es un paréntesis de apertura
                stack.push(char)  # Lo agregamos a la pila
            elif char in parentheses_map.keys():  # Si el carácter es un paréntesis de cierre
                if stack.is_empty() or stack.pop() != parentheses_map[char]:  # Verificamos si la pila está vacía o si el último paréntesis no coincide con el esperado
                    return False  # Si no coincide, la expresión no es válida
        
        return stack.is_empty()  # Al final, la pila debe estar vacía para que la expresión sea válida
            

def ejemplo1():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.pop())  # Output: 3
    print(stack.pop())  # Output: 2
    print(stack.is_empty())  # Output: False
    print(stack.pop())  # Output: 1
    print(stack.is_empty())  # Output: True
    stack.pop()  # Esto lanzará una excepción IndexError porque la pila está vacía y no se pueden eliminar elementos de una pila vacía. Es importante manejar esta situación adecuadamente para evitar errores en tiempo de ejecución.

def ejemplo2():
    stack = Stack()
    expression = "[(2 + 3) * (5 - 4)]"
    if stack.check_parentheses(expression):
        print("La expresión tiene paréntesis balanceados.")
    else:
        print("La expresión no tiene paréntesis balanceados.")

    
if __name__ == "__main__":
    #ejemplo1()
    ejemplo2()