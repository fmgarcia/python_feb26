import re

re_email = r'^[\w\.-]+@[\w\.-]+\.\w+$' # Expresión regular para validar un correo electrónico básico
re_email_avanzado = r"""
    (?!\.)                          # No puede empezar con punto
    (
        [a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+  # Caracteres permitidos localmente
        (?:\.[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+)* # Puntos internos (no consecutivos)
    )
    @                               # Separador
    (?:
        (?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+ # Subdominios
        [a-zA-Z]{2,63}              # TLD (Dominio de nivel superior)
        |                           # O una dirección IP (caso extremo)
        \[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}
        (?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\]
    )
"""

# Expresión regular avanzada para validar un correo electrónico con más precisión, incluyendo validación de caracteres permitidos, estructura del dominio y evitando casos comunes de errores como puntos consecutivos o dominios sin TLD válido.
# Se usaría para un cuadro de validación de emails en un formulario web, donde se requiere una validación más estricta para evitar entradas no válidas.
email_regex = re.compile(r"""
    ^                               # Inicio de cadena
    (?!\.)                          # No puede empezar con punto
    (
        [a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+  # Caracteres permitidos localmente
        (?:\.[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+)* # Puntos internos (no consecutivos)
    )
    @                               # Separador
    (?:
        (?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+ # Subdominios
        [a-zA-Z]{2,63}              # TLD (Dominio de nivel superior)
        |                           # O una dirección IP (caso extremo)
        \[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}
        (?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\]
    )
    $                               # Fin de cadena
""", re.VERBOSE)


password_regex = re.compile(r"""
    ^                           # Inicio
    (?=.*[A-Z])                 # Lookahead: Debe haber una mayúscula
    (?=.*[a-z])                 # Lookahead: Debe haber una minúscula
    (?=.*\d)                    # Lookahead: Debe haber un dígito
    (?=.*[@$!%*?&._#/-])        # Lookahead: Debe haber un especial
    [A-Za-z\d@$!%*?&._#/-]      # Permitir solo estos caracteres
    {12,}                       # Longitud mínima de 12
    $                           # Fin
""", re.VERBOSE)

# Captura protocolos, dominios, puertos, rutas y parámetros de consulta.
url_regex = re.compile(r"""
    \b                          # Límite de palabra
    (?:https?://|www\.)         # Protocolo obligatorio o www
    (?:
        [^\s()<>]+              # Caracteres que no son espacios ni paréntesis
        |                       # O
        \([^\s()<> garden]+\)    # Paréntesis equilibrados (común en Wikipedia)
    )+
    (?<=[^\s`!()\[\]{};:'".,<>?«»“”‘’]) # El último carácter no debe ser puntuación
""", re.VERBOSE | re.IGNORECASE)

# Expresión regular para teléfonos españoles con diferentes formatos, incluyendo prefijos internacionales, espacios, guiones y puntos como separadores.
regex_telefonos = r"(?P<prefijo>(?:\+|00)34)?[\s.-]?(?P<cuerpo>(?P<primer_bloque>[6789]\d{2})[\s.-]?(?P<segundo_bloque>\d{2,3})[\s.-]?(?P<tercer_bloque>\d{2,3})[\s.-]?(?P<cuarto_bloque>\d{2,4})?)"


def validar_email(email):    
    if re.match(re_email, email):
        return True
    else:
        return False
    
def validar_email_con_regex(email):    
    if email_regex.match(email):
        return True
    else:
        return False

def ejemplo1():  
    emails = [
        "usuario@dominio.com",
        "usuario@dominio",
        "usuario@dominio.",
        "@dominio.com",
        "usuario@.com",
        "usuario@dominio.c",
        "fran.garcia@ejemplo.eoi.com",
        "fran.garcia@ejemplo..com"
    ]

    print("Validación con expresión regular básica:")
    for email in emails:
        print(f"{email}: {validar_email(email)}")

    print("\nValidación con expresión regular avanzada:")    
    for email in emails:
        print(f"{email}: {validar_email_con_regex(email)}")


def ejemplo2():
    """
    Buscar un email dentro de una cadena
    """
    cadena = "Mi correo es fran@example.com y mi contraseña es P@ssw0rd1234"
    email_encontrado = re.search(re_email_avanzado, cadena, re.VERBOSE)
    if email_encontrado:
        print("Email encontrado:", email_encontrado.group())
        print("El valor delante de la arroba es: ", email_encontrado.group(0))
        print("El dominio es: ", email_encontrado.group(1))
    else:
        print("No se encontró ningún email en la cadena.")
  

def ejemplo_telefonos(texto):    
    for coincidencia in re.finditer(regex_telefonos, texto):
        print(f"Número encontrado: {coincidencia.group('cuerpo')}")
        print(f"  -> Prefijo: {coincidencia.group('prefijo')}")
        print(f"  -> Inicio:  {coincidencia.group('primer_bloque')}")      

#ejemplo1()
#ejemplo2()  
ejemplo_telefonos("Mi contacto es +34 600 123 456 y el de la oficina 912345678")