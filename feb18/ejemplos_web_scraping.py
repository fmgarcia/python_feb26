"""
Ejemplos de uso de BeautifulSoup4
==================================
Librería para parsear y extraer datos de HTML y XML.
Instalación: pip install beautifulsoup4 requests
"""

from bs4 import BeautifulSoup
import requests

# ─────────────────────────────────────────────
# HTML de ejemplo para usar sin conexión
# ─────────────────────────────────────────────
HTML_EJEMPLO = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Página de ejemplo BeautifulSoup</title>
    <meta name="description" content="Ejemplo para practicar web scraping">
</head>
<body>
    <header>
        <h1 id="titulo-principal">Bienvenido a mi web</h1>
        <nav>
            <ul class="menu">
                <li><a href="/inicio">Inicio</a></li>
                <li><a href="/sobre-mi">Sobre mí</a></li>
                <li><a href="/contacto">Contacto</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section class="articulos">
            <article class="post" id="post-1" data-categoria="python">
                <h2 class="titulo-post">Aprendiendo Python</h2>
                <p class="resumen">Python es un lenguaje de programación versátil y fácil de aprender.</p>
                <p>Puedes usarlo para <strong>web scraping</strong>, <em>ciencia de datos</em> y mucho más.</p>
                <a href="/post/python" class="enlace-post">Leer más</a>
                <span class="fecha">2026-02-01</span>
            </article>

            <article class="post" id="post-2" data-categoria="web">
                <h2 class="titulo-post">HTML y CSS básico</h2>
                <p class="resumen">Aprende a construir páginas web desde cero.</p>
                <p>El <strong>HTML</strong> define la estructura y el <em>CSS</em> el estilo.</p>
                <a href="/post/html-css" class="enlace-post">Leer más</a>
                <span class="fecha">2026-02-10</span>
            </article>

            <article class="post" id="post-3" data-categoria="datos">
                <h2 class="titulo-post">Análisis de datos con Pandas</h2>
                <p class="resumen">Pandas es la librería estrella para manipular datos en Python.</p>
                <p>Combínala con <strong>NumPy</strong> y <em>Matplotlib</em> para análisis completos.</p>
                <a href="/post/pandas" class="enlace-post">Leer más</a>
                <span class="fecha">2026-02-18</span>
            </article>
        </section>

        <section class="precios">
            <h2>Tabla de precios</h2>
            <table id="tabla-precios" border="1">
                <thead>
                    <tr>
                        <th>Producto</th>
                        <th>Precio</th>
                        <th>Stock</th>
                    </tr>
                </thead>
                <tbody>
                    <tr class="fila-producto">
                        <td class="nombre">Teclado mecánico</td>
                        <td class="precio">89.99€</td>
                        <td class="stock">15</td>
                    </tr>
                    <tr class="fila-producto">
                        <td class="nombre">Ratón inalámbrico</td>
                        <td class="precio">45.50€</td>
                        <td class="stock">30</td>
                    </tr>
                    <tr class="fila-producto">
                        <td class="nombre">Monitor 24"</td>
                        <td class="precio">299.00€</td>
                        <td class="stock">8</td>
                    </tr>
                    <tr class="fila-producto">
                        <td class="nombre">Auriculares BT</td>
                        <td class="precio">120.00€</td>
                        <td class="stock">22</td>
                    </tr>
                </tbody>
            </table>
        </section>

        <section class="lista-tecnologias">
            <h2>Tecnologías que usamos</h2>
            <ul id="lista-tech">
                <li class="tech backend">Python</li>
                <li class="tech backend">Django</li>
                <li class="tech frontend">React</li>
                <li class="tech frontend">Vue.js</li>
                <li class="tech datos">SQL</li>
                <li class="tech datos">MongoDB</li>
            </ul>
        </section>

        <div class="comentarios">
            <h2>Comentarios</h2>
            <div class="comentario" id="com-1">
                <span class="autor">Ana García</span>
                <span class="texto">¡Muy buen artículo! Me ha ayudado mucho.</span>
                <span class="valoracion" data-puntos="5">★★★★★</span>
            </div>
            <div class="comentario" id="com-2">
                <span class="autor">Luis Martínez</span>
                <span class="texto">Interesante, pero falta profundidad.</span>
                <span class="valoracion" data-puntos="3">★★★☆☆</span>
            </div>
            <div class="comentario" id="com-3">
                <span class="autor">María López</span>
                <span class="texto">Perfecto para principiantes. Gracias.</span>
                <span class="valoracion" data-puntos="4">★★★★☆</span>
            </div>
        </div>
    </main>

    <footer>
        <p class="copyright">© 2026 Mi Web. Todos los derechos reservados.</p>
        <a href="mailto:info@miweb.com">info@miweb.com</a>
    </footer>
</body>
</html>
"""

HTML_ANIDADO = """
<div class="empresa">
    <div class="departamento" id="dev">
        <h3>Desarrollo</h3>
        <ul>
            <li class="empleado senior">Carlos Ruiz <span class="salario">3500€</span></li>
            <li class="empleado junior">Paula Sanz <span class="salario">2100€</span></li>
            <li class="empleado senior">David Mora <span class="salario">3800€</span></li>
        </ul>
    </div>
    <div class="departamento" id="marketing">
        <h3>Marketing</h3>
        <ul>
            <li class="empleado senior">Laura Vega <span class="salario">3200€</span></li>
            <li class="empleado junior">Tomás Gil <span class="salario">1900€</span></li>
        </ul>
    </div>
</div>
"""


# ─────────────────────────────────────────────
# EJEMPLO 1: Parsear HTML y obtener el título
# ─────────────────────────────────────────────
def ejemplo_titulo():
    print("\n--- EJEMPLO 1: Parsear HTML y obtener título ---")
    soup = BeautifulSoup(HTML_EJEMPLO, "html.parser")

    titulo = soup.title
    print(f"Etiqueta <title> completa : {titulo}")
    print(f"Texto del título          : {titulo.string}")
    print(f"Nombre de la etiqueta     : {titulo.name}")

    h1 = soup.h1
    print(f"\nPrimer <h1>  : {h1}")
    print(f"Texto del h1 : {h1.get_text()}")
    print(f"ID del h1    : {h1.get('id')}")


# ─────────────────────────────────────────────
# EJEMPLO 2: find() — buscar la primera coincidencia
# ─────────────────────────────────────────────
def ejemplo_find():
    print("\n--- EJEMPLO 2: find() — primera coincidencia ---")
    soup = BeautifulSoup(HTML_EJEMPLO, "html.parser")

    # Por etiqueta
    primer_p = soup.find("p")
    print(f"Primer <p>            : {primer_p.get_text()}")

    # Por clase CSS
    resumen = soup.find("p", class_="resumen")
    print(f"<p class='resumen'>   : {resumen.get_text()}")

    # Por id
    post1 = soup.find("article", id="post-1")
    print(f"<article id='post-1'> : {post1.find('h2').get_text()}")

    # Por atributo personalizado
    cat_python = soup.find("article", attrs={"data-categoria": "python"})
    print(f"Artículo categoría python: {cat_python.find('h2').get_text()}")

    # find en un subelemento
    footer = soup.find("footer")
    email = footer.find("a")
    print(f"Email en footer       : {email.get_text()}")


# ─────────────────────────────────────────────
# EJEMPLO 3: find_all() — buscar todas las coincidencias
# ─────────────────────────────────────────────
def ejemplo_find_all():
    print("\n--- EJEMPLO 3: find_all() — todas las coincidencias ---")
    soup = BeautifulSoup(HTML_EJEMPLO, "html.parser")

    # Todos los párrafos
    parrafos = soup.find_all("p")
    print(f"Total de <p> encontrados: {len(parrafos)}")

    # Todos los artículos
    articulos = soup.find_all("article", class_="post")
    print(f"\nArtículos encontrados: {len(articulos)}")
    for art in articulos:
        titulo = art.find("h2").get_text()
        fecha = art.find("span", class_="fecha").get_text()
        print(f"  - [{fecha}] {titulo}")

    # Limitar resultados con limit=
    dos_primeros_p = soup.find_all("p", limit=2)
    print(f"\nSolo 2 primeros <p>:")
    for p in dos_primeros_p:
        print(f"  {p.get_text()}")

    # Buscar múltiples etiquetas a la vez
    cabeceras = soup.find_all(["h1", "h2", "h3"])
    print(f"\nTodas las cabeceras (h1, h2, h3):")
    for h in cabeceras:
        print(f"  <{h.name}> → {h.get_text()}")


# ─────────────────────────────────────────────
# EJEMPLO 4: Selectores CSS con select() y select_one()
# ─────────────────────────────────────────────
def ejemplo_selectores_css():
    print("\n--- EJEMPLO 4: Selectores CSS ---")
    soup = BeautifulSoup(HTML_EJEMPLO, "html.parser")

    # select_one → equivale a find()
    titulo = soup.select_one("h1#titulo-principal")
    print(f"h1#titulo-principal : {titulo.get_text()}")

    # Clase CSS
    enlaces_post = soup.select("a.enlace-post")
    print(f"\nEnlaces con clase 'enlace-post':")
    for enlace in enlaces_post:
        print(f"  {enlace.get_text()} → {enlace['href']}")

    # Descendiente directo (>)
    items_menu = soup.select("ul.menu > li > a")
    print(f"\nItems del menú de navegación:")
    for item in items_menu:
        print(f"  {item.get_text()} → {item['href']}")

    # Atributo con selector CSS
    categorias = soup.select("article[data-categoria]")
    print(f"\nArticulos con data-categoria:")
    for art in categorias:
        print(f"  {art['data-categoria']}: {art.find('h2').get_text()}")

    # Selector de nth-child equivalente via find_all + índice
    filas_tabla = soup.select("tbody tr.fila-producto")
    print(f"\nFilas de la tabla ({len(filas_tabla)} filas):")
    for fila in filas_tabla:
        celdas = fila.find_all("td")
        print(f"  {celdas[0].get_text()} | {celdas[1].get_text()} | Stock: {celdas[2].get_text()}")


# ─────────────────────────────────────────────
# EJEMPLO 5: Extraer atributos de etiquetas
# ─────────────────────────────────────────────
def ejemplo_atributos():
    print("\n--- EJEMPLO 5: Extraer atributos ---")
    soup = BeautifulSoup(HTML_EJEMPLO, "html.parser")

    # Acceder a atributo como diccionario
    enlace = soup.find("a")
    print(f"href del primer enlace : {enlace['href']}")
    print(f"Texto del enlace       : {enlace.get_text()}")

    # get() — no lanza error si el atributo no existe
    meta_desc = soup.find("meta", attrs={"name": "description"})
    print(f"\nMeta description       : {meta_desc.get('content')}")
    print(f"Atributo inexistente   : {meta_desc.get('noexiste', 'N/A')}")

    # Atributo con guion (data-*)
    articulos = soup.find_all("article")
    print(f"\nData-attributes de artículos:")
    for art in articulos:
        print(f"  id={art.get('id')}, data-categoria={art.get('data-categoria')}")

    # Obtener TODOS los atributos de una etiqueta
    primer_art = soup.find("article")
    print(f"\nTodos los atributos del primer article: {primer_art.attrs}")

    # Obtener todos los href de la página
    todos_href = [a.get("href") for a in soup.find_all("a") if a.get("href")]
    print(f"\nTodos los href de la página:")
    for href in todos_href:
        print(f"  {href}")


# ─────────────────────────────────────────────
# EJEMPLO 6: Navegar el árbol (padres, hijos, hermanos)
# ─────────────────────────────────────────────
def ejemplo_navegacion_arbol():
    print("\n--- EJEMPLO 6: Navegar el árbol DOM ---")
    soup = BeautifulSoup(HTML_EJEMPLO, "html.parser")

    post1 = soup.find("article", id="post-1")

    # Hijos directos (.children)
    print("Hijos directos del article#post-1:")
    hijos = [h for h in post1.children if h.name is not None]
    for hijo in hijos:
        print(f"  <{hijo.name}> → {hijo.get_text(strip=True)[:50]}")

    # Todos los descendientes (.descendants)
    print(f"\nNúmero total de descendientes: {len(list(post1.descendants))}")

    # Padre (.parent)
    h2 = post1.find("h2")
    print(f"\nPadre del <h2>     : <{h2.parent.name}> id='{h2.parent.get('id')}'")
    print(f"Abuelo del <h2>    : <{h2.parent.parent.name}> class='{h2.parent.parent.get('class')}'")

    # Hermano siguiente (.next_sibling / find_next_sibling)
    primer_post = soup.find("article", id="post-1")
    siguiente = primer_post.find_next_sibling("article")
    print(f"\nHermano siguiente del post-1: {siguiente.find('h2').get_text()}")

    # Hermano anterior (.find_previous_sibling)
    tercer_post = soup.find("article", id="post-3")
    anterior = tercer_post.find_previous_sibling("article")
    print(f"Hermano anterior del post-3 : {anterior.find('h2').get_text()}")

    # Todos los hermanos siguientes
    print("\nTodos los artículos desde el post-1:")
    for hermano in primer_post.find_next_siblings("article"):
        print(f"  {hermano.find('h2').get_text()}")


# ─────────────────────────────────────────────
# EJEMPLO 7: Extraer texto con get_text()
# ─────────────────────────────────────────────
def ejemplo_get_text():
    print("\n--- EJEMPLO 7: Extraer texto con get_text() ---")
    soup = BeautifulSoup(HTML_EJEMPLO, "html.parser")

    # Texto simple
    h1 = soup.find("h1")
    print(f"Texto del H1             : '{h1.get_text()}'")

    # Con strip=True elimina espacios extra
    post = soup.find("article", id="post-1")
    print(f"\nTexto con strip=True:\n{post.get_text(strip=True)}")

    # Con separator para separar bloques
    print(f"\nTexto con separator='|':\n{post.get_text(separator=' | ', strip=True)}")

    # Texto completo de la página (resumido)
    texto_completo = soup.get_text(separator="\n", strip=True)
    lineas = [l for l in texto_completo.splitlines() if l.strip()]
    print(f"\nPrimeras 10 líneas de texto de la página:")
    for linea in lineas[:10]:
        print(f"  {linea}")
    print(f"  ... ({len(lineas)} líneas en total)")


# ─────────────────────────────────────────────
# EJEMPLO 8: Buscar con funciones lambda
# ─────────────────────────────────────────────
def ejemplo_busqueda_con_funciones():
    print("\n--- EJEMPLO 8: Buscar con funciones y expresiones ---")
    soup = BeautifulSoup(HTML_EJEMPLO, "html.parser")

    # Etiquetas con un atributo específico
    con_data_puntos = soup.find_all(lambda tag: tag.get("data-puntos"))
    print("Etiquetas con atributo 'data-puntos':")
    for tag in con_data_puntos:
        print(f"  {tag.name} → puntos={tag['data-puntos']}, texto={tag.get_text()}")

    # Etiquetas con más de un atributo
    con_id_y_clase = soup.find_all(lambda tag: tag.get("id") and tag.get("class"))
    print(f"\nEtiquetas con id Y clase:")
    for tag in con_id_y_clase:
        print(f"  <{tag.name}> id='{tag['id']}' class='{tag['class']}'")

    # Buscar por contenido de texto
    import re
    with_precio = soup.find_all(string=re.compile(r"\d+\.\d+€"))
    print(f"\nTextos que contienen precios (€):")
    for texto in with_precio:
        print(f"  '{texto.strip()}'")

    # Etiquetas que tienen exactamente 2 clases
    dos_clases = soup.find_all(lambda tag: len(tag.get("class", [])) == 2)
    print(f"\nEtiquetas con exactamente 2 clases:")
    for tag in dos_clases[:5]:
        print(f"  <{tag.name}> class={tag['class']} → '{tag.get_text(strip=True)[:40]}'")


# ─────────────────────────────────────────────
# EJEMPLO 9: Trabajar con tablas HTML
# ─────────────────────────────────────────────
def ejemplo_tablas():
    print("\n--- EJEMPLO 9: Extraer datos de tablas HTML ---")
    soup = BeautifulSoup(HTML_EJEMPLO, "html.parser")

    tabla = soup.find("table", id="tabla-precios")

    # Cabeceras
    cabeceras = [th.get_text() for th in tabla.find_all("th")]
    print(f"Cabeceras: {cabeceras}")

    # Filas del cuerpo
    print("\nDatos de la tabla:")
    filas = tabla.find("tbody").find_all("tr")
    for fila in filas:
        celdas = [td.get_text() for td in fila.find_all("td")]
        print(f"  {dict(zip(cabeceras, celdas))}")

    # Calcular total de stock
    stocks = [int(td.get_text()) for td in tabla.find_all("td", class_="stock")]
    print(f"\nTotal de artículos en stock: {sum(stocks)}")

    # Producto más caro
    precios = tabla.find_all("td", class_="precio")
    nombres = tabla.find_all("td", class_="nombre")
    precios_float = [float(p.get_text().replace("€", "")) for p in precios]
    idx_max = precios_float.index(max(precios_float))
    print(f"Producto más caro: {nombres[idx_max].get_text()} — {precios[idx_max].get_text()}")


# ─────────────────────────────────────────────
# EJEMPLO 10: Trabajar con listas HTML
# ─────────────────────────────────────────────
def ejemplo_listas():
    print("\n--- EJEMPLO 10: Extraer listas HTML ---")
    soup = BeautifulSoup(HTML_EJEMPLO, "html.parser")

    lista_tech = soup.find("ul", id="lista-tech")
    items = lista_tech.find_all("li")

    print("Todas las tecnologías:")
    for item in items:
        clases = item.get("class", [])
        print(f"  {item.get_text()} — clases: {clases}")

    # Filtrar por tipo
    backend = [li.get_text() for li in items if "backend" in li.get("class", [])]
    frontend = [li.get_text() for li in items if "frontend" in li.get("class", [])]
    datos = [li.get_text() for li in items if "datos" in li.get("class", [])]

    print(f"\nBackend  : {backend}")
    print(f"Frontend : {frontend}")
    print(f"Datos    : {datos}")

    # Menú de navegación
    menu = soup.find("ul", class_="menu")
    print("\nLinks del menú:")
    for li in menu.find_all("li"):
        a = li.find("a")
        print(f"  Texto='{a.get_text()}' | URL='{a['href']}'")


# ─────────────────────────────────────────────
# EJEMPLO 11: HTML anidado y estructuras complejas
# ─────────────────────────────────────────────
def ejemplo_html_anidado():
    print("\n--- EJEMPLO 11: Estructuras HTML anidadas ---")
    soup = BeautifulSoup(HTML_ANIDADO, "html.parser")

    departamentos = soup.find_all("div", class_="departamento")
    print(f"Departamentos encontrados: {len(departamentos)}")

    for depto in departamentos:
        nombre_depto = depto.find("h3").get_text()
        empleados = depto.find_all("li")
        print(f"\n  Departamento: {nombre_depto} ({len(empleados)} empleados)")

        salarios = []
        for emp in empleados:
            texto = emp.get_text(separator=" ").strip()
            salario_tag = emp.find("span", class_="salario")
            salario = float(salario_tag.get_text().replace("€", ""))
            salarios.append(salario)
            nivel = "senior" if "senior" in emp.get("class", []) else "junior"
            nombre = emp.get_text().replace(salario_tag.get_text(), "").strip()
            print(f"    [{nivel}] {nombre} — {salario_tag.get_text()}")

        print(f"    Salario medio: {sum(salarios)/len(salarios):.2f}€")

    # Buscar todos los seniors de toda la empresa
    seniors = soup.find_all("li", class_="senior")
    print(f"\nTotal seniors en la empresa: {len(seniors)}")
    for s in seniors:
        depto_id = s.find_parent("div", class_="departamento").get("id")
        nombre = s.get_text().replace(s.find("span").get_text(), "").strip()
        print(f"  {nombre} (dept: {depto_id})")


# ─────────────────────────────────────────────
# EJEMPLO 12: Modificar el DOM (solo en memoria)
# ─────────────────────────────────────────────
def ejemplo_modificar_dom():
    print("\n--- EJEMPLO 12: Modificar el DOM en memoria ---")
    soup = BeautifulSoup(HTML_EJEMPLO, "html.parser")

    # Cambiar texto de un elemento
    h1 = soup.find("h1")
    print(f"Antes : {h1.get_text()}")
    h1.string = "Título modificado por BeautifulSoup"
    print(f"Después: {h1.get_text()}")

    # Añadir un atributo
    primer_art = soup.find("article")
    print(f"\nClases antes: {primer_art.get('class')}")
    primer_art["class"].append("destacado")
    primer_art["data-nuevo"] = "valor-añadido"
    print(f"Clases después: {primer_art.get('class')}")
    print(f"Nuevo atributo: {primer_art.get('data-nuevo')}")

    # Eliminar un atributo
    del primer_art["data-nuevo"]
    print(f"Tras eliminar data-nuevo: {primer_art.get('data-nuevo', 'No existe')}")

    # Crear una nueva etiqueta e insertarla
    nueva_etiqueta = soup.new_tag("p", attrs={"class": "aviso"})
    nueva_etiqueta.string = "Este contenido fue añadido dinámicamente."
    primer_art.append(nueva_etiqueta)
    print(f"\nÚltimo elemento del article tras insertar:")
    print(f"  {list(primer_art.children)[-1]}")

    # decompose() — eliminar una etiqueta del árbol
    aviso = soup.find("p", class_="aviso")
    aviso.decompose()
    print(f"\nTras decompose(), buscando el aviso: {soup.find('p', class_='aviso')}")


# ─────────────────────────────────────────────
# EJEMPLO 13: Diferentes parsers de BeautifulSoup
# ─────────────────────────────────────────────
def ejemplo_parsers():
    print("\n--- EJEMPLO 13: Diferentes parsers ---")

    html_roto = "<html><head><title>Test<body><p>Párrafo sin cerrar<p>Otro párrafo"

    # html.parser — incluido en Python, no requiere instalación extra
    soup1 = BeautifulSoup(html_roto, "html.parser")
    print("html.parser (built-in):")
    print(f"  Párrafos: {[p.get_text() for p in soup1.find_all('p')]}")

    # lxml — más rápido, requiere: pip install lxml
    try:
        soup2 = BeautifulSoup(html_roto, "lxml")
        print("\nlxml parser:")
        print(f"  Párrafos: {[p.get_text() for p in soup2.find_all('p')]}")
    except Exception:
        print("\nlxml no instalado (pip install lxml)")

    # html5lib — más permisivo, requiere: pip install html5lib
    try:
        soup3 = BeautifulSoup(html_roto, "html5lib")
        print("\nhtml5lib parser:")
        print(f"  Párrafos: {[p.get_text() for p in soup3.find_all('p')]}")
    except Exception:
        print("\nhtml5lib no instalado (pip install html5lib)")

    # Parsear XML en lugar de HTML
    xml_ejemplo = """<?xml version="1.0"?>
<catalogo>
    <producto id="1"><nombre>Laptop</nombre><precio>999.99</precio></producto>
    <producto id="2"><nombre>Tablet</nombre><precio>399.50</precio></producto>
</catalogo>"""

    soup_xml = BeautifulSoup(xml_ejemplo, "xml" if _lxml_disponible() else "html.parser")
    print(f"\nParseo XML:")
    try:
        productos = soup_xml.find_all("producto")
        for p in productos:
            print(f"  id={p.get('id')}: {p.find('nombre').get_text()} — {p.find('precio').get_text()}€")
    except Exception as e:
        print(f"  Error al parsear XML: {e}")


def _lxml_disponible():
    try:
        import lxml
        return True
    except ImportError:
        return False


# ─────────────────────────────────────────────
# EJEMPLO 14: Web scraping real con requests
# ─────────────────────────────────────────────
def ejemplo_scraping_real():
    print("\n--- EJEMPLO 14: Web scraping real con requests ---")
    url = "https://quotes.toscrape.com/"
    print(f"Descargando: {url}")

    try:
        headers = {"User-Agent": "Mozilla/5.0 (BeautifulSoup Demo)"}
        respuesta = requests.get(url, headers=headers, timeout=10)
        respuesta.raise_for_status()

        soup = BeautifulSoup(respuesta.text, "html.parser")

        # Título de la página
        print(f"\nTítulo: {soup.title.get_text()}")

        # Extraer citas
        citas = soup.find_all("div", class_="quote")
        print(f"Citas encontradas: {len(citas)}\n")

        for i, cita in enumerate(citas[:5], 1):
            texto = cita.find("span", class_="text").get_text()
            autor = cita.find("small", class_="author").get_text()
            tags = [t.get_text() for t in cita.find_all("a", class_="tag")]
            print(f"  {i}. {texto[:70]}...")
            print(f"     — {autor}")
            print(f"     Tags: {', '.join(tags)}")
            print()

        # Enlace a la siguiente página
        siguiente = soup.find("li", class_="next")
        if siguiente:
            href = siguiente.find("a")["href"]
            print(f"Siguiente página: https://quotes.toscrape.com{href}")

    except requests.exceptions.ConnectionError:
        print("Sin conexión a internet. Ejecutar este ejemplo con conexión disponible.")
    except requests.exceptions.Timeout:
        print("Tiempo de espera agotado.")
    except requests.exceptions.HTTPError as e:
        print(f"Error HTTP: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")


# ─────────────────────────────────────────────
# EJEMPLO 15: Scraping de una Wikipedia (solo encabezados)
# ─────────────────────────────────────────────
def ejemplo_scraping_wikipedia():
    print("\n--- EJEMPLO 15: Scraping de Wikipedia (Python) ---")
    url = "https://es.wikipedia.org/wiki/Python"
    print(f"Descargando: {url}")

    try:
        headers = {"User-Agent": "Mozilla/5.0 (BeautifulSoup Demo)"}
        respuesta = requests.get(url, headers=headers, timeout=10)
        respuesta.raise_for_status()

        soup = BeautifulSoup(respuesta.text, "html.parser")

        # Título del artículo
        titulo = soup.find("h1", id="firstHeading")
        print(f"\nArtículo: {titulo.get_text()}")

        # Extraer el primer párrafo del contenido
        contenido = soup.find("div", id="mw-content-text")
        primer_parrafo = contenido.find("p")
        if primer_parrafo:
            print(f"\nPrimer párrafo:\n{primer_parrafo.get_text()[:300]}...")

        # Extraer índice de secciones (h2)
        secciones = soup.find_all("h2")
        print(f"\nSecciones del artículo:")
        for sec in secciones[:8]:
            texto = sec.get_text(strip=True)
            if texto and texto != "Menú de navegación":
                print(f"  · {texto}")

        # Contar enlaces internos de Wikipedia
        enlaces_wiki = [a for a in soup.find_all("a", href=True)
                        if a["href"].startswith("/wiki/") and ":" not in a["href"]]
        print(f"\nEnlaces internos de Wikipedia encontrados: {len(enlaces_wiki)}")
        print("Primeros 5:")
        for a in enlaces_wiki[:5]:
            print(f"  {a.get_text()} → https://es.wikipedia.org{a['href']}")

    except requests.exceptions.ConnectionError:
        print("Sin conexión a internet.")
    except Exception as e:
        print(f"Error: {e}")


# ─────────────────────────────────────────────
# MENÚ PRINCIPAL
# ─────────────────────────────────────────────
EJEMPLOS = {
    "1": ("Parsear HTML y obtener título/h1", ejemplo_titulo),
    "2": ("find() — buscar primera coincidencia", ejemplo_find),
    "3": ("find_all() — buscar todas las coincidencias", ejemplo_find_all),
    "4": ("Selectores CSS con select() y select_one()", ejemplo_selectores_css),
    "5": ("Extraer atributos de etiquetas", ejemplo_atributos),
    "6": ("Navegar el árbol DOM (padres, hijos, hermanos)", ejemplo_navegacion_arbol),
    "7": ("Extraer texto con get_text()", ejemplo_get_text),
    "8": ("Buscar con funciones lambda y regex", ejemplo_busqueda_con_funciones),
    "9": ("Extraer datos de tablas HTML", ejemplo_tablas),
    "10": ("Extraer listas HTML", ejemplo_listas),
    "11": ("Estructuras HTML anidadas y find_parent()", ejemplo_html_anidado),
    "12": ("Modificar el DOM en memoria", ejemplo_modificar_dom),
    "13": ("Diferentes parsers (html.parser, lxml, html5lib, xml)", ejemplo_parsers),
    "14": ("Web scraping REAL — quotes.toscrape.com [requiere internet]", ejemplo_scraping_real),
    "15": ("Web scraping REAL — Wikipedia [requiere internet]", ejemplo_scraping_wikipedia),
}


def mostrar_menu():
    print("\n" + "═" * 60)
    print("       EJEMPLOS DE BeautifulSoup4 — Menú Principal")
    print("═" * 60)
    for clave, (descripcion, _) in EJEMPLOS.items():
        print(f"  {clave:>2}. {descripcion}")
    print("  " + "-" * 56)
    print("   0. Ejecutar TODOS los ejemplos")
    print("   q. Salir")
    print("═" * 60)


def main():
    while True:
        mostrar_menu()
        opcion = input("\nElige una opción: ").strip().lower()

        if opcion == "q":
            print("\n¡Hasta luego!\n")
            break
        elif opcion == "0":
            print("\n>>> Ejecutando todos los ejemplos...\n")
            for _, (_, funcion) in EJEMPLOS.items():
                try:
                    funcion()
                except Exception as e:
                    print(f"  [ERROR] {e}")
            input("\nPresiona ENTER para continuar...")
        elif opcion in EJEMPLOS:
            descripcion, funcion = EJEMPLOS[opcion]
            try:
                funcion()
            except Exception as e:
                print(f"\n[ERROR en el ejemplo]: {e}")
            input("\nPresiona ENTER para volver al menú...")
        else:
            print("\n  Opción no válida. Elige un número del 1 al 15, 0 o 'q'.")


if __name__ == "__main__":
    main()
