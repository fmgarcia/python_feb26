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
        parentheses_map = {r'</html>': '<html>', 
                           r'</head>': '<head>', 
                           r'</body>': '<body>', 
                           r'</div>': '<div>', 
                           r'</span>': '<span>', 
                           r'</p>': '<p>', 
                           r'</a>': '<a>', 
                           r'</ul>': '<ul>', 
                           r'</ol>': '<ol>', 
                           r'</li>': '<li>',
                           r'</h1>': '<h1>',}
        
        palabras = expression.split()  # Divide la expresión en palabras utilizando el método split(), lo que permite analizar cada palabra individualmente para verificar si son etiquetas HTML de apertura o cierre.
        for palabra in palabras:
            if palabra in parentheses_map.values():  # Si la palabra es un paréntesis de apertura
                stack.push(palabra)  # Lo agregamos a la pila
            elif palabra in parentheses_map.keys():  # Si la palabra es un paréntesis de cierre
                if stack.is_empty() or stack.pop() != parentheses_map[palabra]:  # Verificamos si la pila está vacía o si el último paréntesis no coincide con el esperado
                    return False  # Si no coincide, la expresión no es válida
        
        return stack.is_empty()  # Al final, la pila debe estar vacía para que la expresión sea válida
    
    def __str__(self):
        return f"Stack({self.items})"
            

def ejemplo1():
    htlm = """
    <html>
    <body>
    <h1> Hello, World! </h1>
    <p> We are learning the art of coding
    with Python programming language.
    Here we are learning ... </p>
    <ul>
    <li> Data Structures, </li>
    <li> Algorithms, </li>
    <li> and Computational Thinking,
    eventually. </li>
    </ul>
    </body>
    </html>
    """
    if Stack().check_parentheses(htlm):
        print("Html es correcto")
    else:
        print("Html no es correcto")
   
if __name__ == "__main__":
    ejemplo1()
