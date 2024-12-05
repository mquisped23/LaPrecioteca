
from flask import Flask, render_template, request, session, redirect, url_for,jsonify,send_file
from productos_scraping.limon_scraping import limon_precio  # Importar la función limon_precio
from productos_scraping.cebolla_scraping import cebolla_precio  # Importar la función limon_precio
from productos_scraping.zanahoria_scraping import zanahoria_precio  # Importar la función limon_precio
from productos_scraping.tomate_scraping import tomate_precio  # Importar la función limon_precio
from productos_scraping.choclo_scraping import choclo_precio  # Importar la función limon_precio
from productos_scraping.ajo_scraping import ajo_precio  # Importar la función limon_precio
from productos_scraping.kion_scraping import kion_precio  # Importar la función limon_precio
from productos_scraping.pimiento_scraping import pimiento_precio  # Importar la función limon_precio
from productos_scraping.aji_amarillo_scraping import ajiAmarillo_precio  # Importar la función limon_precio
from productos_scraping.palta_scraping import palta_precio  # Importar la función limon_precio
from productos_scraping.vainita_scraping import vainita_precio  # Importar la función limon_precio
from productos_scraping.arveja_scraping import arveja_precio  # Importar la función limon_precio
from productos_scraping.maracuya_scraping import maracuya_precio  # Importar la función limon_precio
from productos_scraping.cebolla_blanca_scraping import cebollaBlanca_precio  # Importar la función limon_precio
from productos_scraping.nabo_scraping import nabo_precio  # Importar la función limon_precio
from collections import defaultdict

import uuid


app = Flask(__name__)
app.secret_key = 'MiCaserita' 


# RUTA PRINCIPAL DE FLASK
@app.route('/')
def paginaPrincipal():
     return render_template('index.html')
  


#  datos de productos
listaProductos = [
    {
        'nombre': 'limon',
        'imagen_url': 'https://superlavioleta.com/cdn/shop/files/limon.png?v=1719498616',
        'url': '/productos/limon'
    },
    # Agrega más productos con diferentes nombres, imágenes y URLs.
    {
        'nombre': 'cebolla',
        'imagen_url': 'https://static.vecteezy.com/system/resources/previews/013/855/808/non_2x/red-onion-isolated-free-png.png',
        'url': '/productos/cebolla'
    },
    {
        'nombre': 'zanahoria',
        'imagen_url': 'https://png.pngtree.com/png-clipart/20231127/original/pngtree-a-carrot-png-image_13717899.png',
        'url': '/productos/zanahoria'
    }
    ,
    {
        'nombre': 'tomate',
        'imagen_url': 'https://static.vecteezy.com/system/resources/previews/028/882/790/original/tomato-tomato-red-tomato-with-transparent-background-ai-generated-free-png.png',
        'url': '/productos/tomate'
    },
    {
        'nombre': 'choclo',
        'imagen_url': 'https://www.veguitashop.cl/427-large_default/choclo-peruano.jpg',
        'url': '/productos/choclo'
    }
    ,
    {
        'nombre': 'ajo',
        'imagen_url': 'https://static.vecteezy.com/system/resources/previews/027/216/058/original/garlic-garlic-garlic-transparent-background-ai-generated-free-png.png',
        'url': '/productos/ajo'
    }
    ,
    {
        'nombre': 'kion',
        'imagen_url': 'https://png.pngtree.com/png-clipart/20210530/original/pngtree-ginger-food-seasoning-cooking-png-image_6343229.jpg',
        'url': '/productos/kion'
    }
    ,
    {
        'nombre': 'pimiento',
        'imagen_url': 'https://static.vecteezy.com/system/resources/previews/027/216/286/original/red-capsicum-red-capsicum-transparent-background-ai-generated-free-png.png',
        'url': '/productos/pimiento'
    }
    ,
    {
        'nombre': 'aji amarillo',
        'imagen_url': 'https://png.pngtree.com/png-vector/20240815/ourmid/pngtree-hot-pepper-aji-amarillo-png-image_13491322.png',
        'url': '/productos/ajiAmarillo'
    }
    ,
    {
        'nombre': 'palta',
        'imagen_url': 'https://i.pinimg.com/originals/59/ea/ee/59eaeedd8ebc8ddfc77caf2bb3666faf.png',
        'url': '/productos/palta'
    }
    ,
    {
        'nombre': 'vainita',
        'imagen_url': 'https://static.wixstatic.com/media/9d9d48_5f5de22887ef462a88ceea6ce8eca941~mv2.png/v1/fit/w_500,h_500,q_90/file.png',
        'url': '/productos/vainita'
    }
    ,
    {
        'nombre': 'arveja',
        'imagen_url': 'https://hortisemillas.com/assets/img/semillas/arverja-main.png',
        'url': '/productos/arveja'
    }
    ,
    {
        'nombre': 'maracuya',
        'imagen_url': 'https://static.vecteezy.com/system/resources/thumbnails/047/465/326/small_2x/delicious-passion-fruit-with-half-cut-isolated-illustration-on-a-transparent-background-png.png',
        'url': '/productos/maracuya'
    }
    ,
    {
        'nombre': 'cebolla blanca',
        'imagen_url': 'https://png.pngtree.com/png-vector/20240204/ourmid/pngtree-slice-of-white-onion-png-image_11606634.png',
        'url': '/productos/cebollaBlanca'
    }
    ,
    {
        'nombre': 'nabo',
        'imagen_url': 'https://static.vecteezy.com/system/resources/previews/028/830/117/original/fresh-turnip-vegetable-png.png',
        'url': '/productos/nabo'
    }
]

# Ruta para la página de productos
@app.route('/productos')
def listar_productos():
    search_query = request.args.get('search', '').lower()
    if search_query:
        productos_filtrados = [p for p in listaProductos if search_query in p['nombre'].lower()]
    else:
        productos_filtrados = listaProductos
    
    # Renderiza solo el contenido de los productos
    return render_template('productos.html', productos=productos_filtrados)

#lista de los 4 supermercados
@app.route('/productos/limon', methods=['GET'])
def listar_limon():
    precios = limon_precio()
    lista_precios = session.get('lista_precios', [])
    print("mi lista de precios  get es:", lista_precios)
    return render_template('limon_view.html', precios=precios)  # Asegúrate de renderizar la plantilla correctamente

#Esto hace que se guarde en la sesion los productos
@app.route('/productos/limon', methods=['POST'])
def enviar_peticion_limon():
    # Obtener los datos enviados por el formulario como listas
    supermercados = request.form.getlist('supermercado')
    precios = request.form.getlist('precio')
    
    # Verifica si la lista de precios ya existe en la sesión, si no, inicialízala
    if 'lista_precios' not in session:
        session['lista_precios'] = []

    # Agregar todos los supermercados y precios a la lista de la sesión
    for supermercado, precio in zip(supermercados, precios):
        # Agregar el ítem a la lista
        item_id = str(uuid.uuid4())  # Generar un identificador único
        session['lista_precios'].append({
            'id': item_id,
            'producto': 'limon',
            'unidad' : "Kg",
            'supermercado': supermercado,
            'precio': precio
        })
        
    # Marca la sesión como modificada
    session.modified = True
    
    # Redirigir a la lista de precios seleccionados
    return redirect(url_for('ver_lista_precios'))
       




  
#Aca se listan los productos guardados en la sesion
@app.route('/lista_precios')
def ver_lista_precios():
    # Obtiene la lista de precios de la sesión
    lista_precios = session.get('lista_precios', [])
    
    # Agrupar los precios por supermercado
    precios_por_supermercado = defaultdict(list)
    for item in lista_precios:
        precios_por_supermercado[item['supermercado']].append(item)

    # Calcular la suma total de los precios por supermercado
    suma_por_supermercado = {supermercado: sum(float(item['precio']) for item in items)
                             for supermercado, items in precios_por_supermercado.items()}

    # Calcular la suma total general
    total_precio = sum(float(item['precio']) for item in lista_precios)

    return render_template('lista_precios.html', 
                           precios_por_supermercado=precios_por_supermercado, 
                           suma_por_supermercado=suma_por_supermercado)

#Aca se elimina un producto de mi lista de sesion


@app.route('/eliminar_precio', methods=['POST'])
def eliminar_precio():
    # Obtener el ID del ítem a eliminar desde el formulario
    item_id_a_eliminar = request.form['item_id']  # No es necesario convertirlo a int

    # Obtener la lista de precios de la sesión
    lista_precios = session.get('lista_precios', [])

    # Filtrar la lista para eliminar el ítem con el ID correspondiente
    session['lista_precios'] = [item for item in lista_precios if item['id'] != item_id_a_eliminar]

    # Marca la sesión como modificada
    session.modified = True

    # Redirigir a la lista de precios seleccionados
    return redirect(url_for('ver_lista_precios'))


#Cebolla

@app.route('/productos/cebolla', methods=['GET'])
def listar_cebolla():
    precios = cebolla_precio()
    lista_precios = session.get('lista_precios', [])
    print("mi lista de precios  get es:", lista_precios)
    return render_template('cebolla_view.html', precios=precios)  # Asegúrate de renderizar la plantilla correctamente

#Esto hace que se guarde en la sesion los productos
@app.route('/productos/cebolla', methods=['POST'])
def enviar_peticion_cebolla():
    # Obtener los datos enviados por el formulario como listas
    supermercados = request.form.getlist('supermercado')
    precios = request.form.getlist('precio')
    
    # Verifica si la lista de precios ya existe en la sesión, si no, inicialízala
    if 'lista_precios' not in session:
        session['lista_precios'] = []

    # Agregar todos los supermercados y precios a la lista de la sesión
    for supermercado, precio in zip(supermercados, precios):
        # Agregar el ítem a la lista
        item_id = str(uuid.uuid4())  # Generar un identificador único
        session['lista_precios'].append({
            'id': item_id,
            'producto': 'cebolla',
            'unidad' : "Kg",
            'supermercado': supermercado,
            'precio': precio
        })
        
    # Marca la sesión como modificada
    session.modified = True
    
    # Redirigir a la lista de precios seleccionados
    return redirect(url_for('ver_lista_precios'))



#Zanahoria

@app.route('/productos/zanahoria', methods=['GET'])
def listar_zanahoria():
    precios = zanahoria_precio()
    return render_template('zanahoria_view.html', precios=precios)  # Asegúrate de renderizar la plantilla correctamente



#Esto hace que se guarde en la sesion los productos
@app.route('/productos/zanahoria', methods=['POST'])
def enviar_peticion_zanahoria():
    # Obtener los datos enviados por el formulario como listas
    supermercados = request.form.getlist('supermercado')
    precios = request.form.getlist('precio')
    
    # Verifica si la lista de precios ya existe en la sesión, si no, inicialízala
    if 'lista_precios' not in session:
        session['lista_precios'] = []

    # Agregar todos los supermercados y precios a la lista de la sesión
    for supermercado, precio in zip(supermercados, precios):
        # Agregar el ítem a la lista
        item_id = str(uuid.uuid4())  # Generar un identificador único
        session['lista_precios'].append({
            'id': item_id,
            'producto': 'zanahoria',
            'unidad' : "Kg",
            'supermercado': supermercado,
            'precio': precio
        })
        
    # Marca la sesión como modificada
    session.modified = True
    
    # Redirigir a la lista de precios seleccionados
    return redirect(url_for('ver_lista_precios'))





#tomate

@app.route('/productos/tomate', methods=['GET'])
def listar_tomate():
    precios = tomate_precio()
    return render_template('tomate_view.html', precios=precios)  # Asegúrate de renderizar la plantilla correctamente



#Esto hace que se guarde en la sesion los productos
@app.route('/productos/tomate', methods=['POST'])
def enviar_peticion_tomate():
    # Obtener los datos enviados por el formulario como listas
    supermercados = request.form.getlist('supermercado')
    precios = request.form.getlist('precio')
    
    # Verifica si la lista de precios ya existe en la sesión, si no, inicialízala
    if 'lista_precios' not in session:
        session['lista_precios'] = []

    # Agregar todos los supermercados y precios a la lista de la sesión
    for supermercado, precio in zip(supermercados, precios):
        # Agregar el ítem a la lista
        item_id = str(uuid.uuid4())  # Generar un identificador único
        session['lista_precios'].append({
            'id': item_id,
            'producto': 'tomate',
            'unidad' : "Kg",
            'supermercado': supermercado,
            'precio': precio
        })
        
    # Marca la sesión como modificada
    session.modified = True
    
    # Redirigir a la lista de precios seleccionados
    return redirect(url_for('ver_lista_precios'))




#choclo

@app.route('/productos/choclo', methods=['GET'])
def listar_choclo():
    precios = choclo_precio()
    return render_template('choclo_view.html', precios=precios)  # Asegúrate de renderizar la plantilla correctamente



#Esto hace que se guarde en la sesion los productos
@app.route('/productos/choclo', methods=['POST'])
def enviar_peticion_choclo():
    # Obtener los datos enviados por el formulario como listas
    supermercados = request.form.getlist('supermercado')
    precios = request.form.getlist('precio')
    
    # Verifica si la lista de precios ya existe en la sesión, si no, inicialízala
    if 'lista_precios' not in session:
        session['lista_precios'] = []

    # Agregar todos los supermercados y precios a la lista de la sesión
    for supermercado, precio in zip(supermercados, precios):
        # Agregar el ítem a la lista
        item_id = str(uuid.uuid4())  # Generar un identificador único
        session['lista_precios'].append({
            'id': item_id,
            'producto': 'choclo',
            'unidad' : "Unid",
            'supermercado': supermercado,
            'precio': precio
        })
        
    # Marca la sesión como modificada
    session.modified = True
    
    # Redirigir a la lista de precios seleccionados
    return redirect(url_for('ver_lista_precios'))


#Ajo

@app.route('/productos/ajo', methods=['GET'])
def listar_ajo():
    precios = ajo_precio()
    return render_template('ajo_view.html', precios=precios)  # Asegúrate de renderizar la plantilla correctamente



#Esto hace que se guarde en la sesion los productos
@app.route('/productos/ajo', methods=['POST'])
def enviar_peticion_ajo():
    # Obtener los datos enviados por el formulario como listas
    supermercados = request.form.getlist('supermercado')
    precios = request.form.getlist('precio')
    
    # Verifica si la lista de precios ya existe en la sesión, si no, inicialízala
    if 'lista_precios' not in session:
        session['lista_precios'] = []

    # Agregar todos los supermercados y precios a la lista de la sesión
    for supermercado, precio in zip(supermercados, precios):
        # Agregar el ítem a la lista
        item_id = str(uuid.uuid4())  # Generar un identificador único
        session['lista_precios'].append({
            'id': item_id,
            'producto': 'ajo',
            'unidad' : "kg",
            'supermercado': supermercado,
            'precio': precio
        })
        
    # Marca la sesión como modificada
    session.modified = True
    
    # Redirigir a la lista de precios seleccionados
    return redirect(url_for('ver_lista_precios'))

#Kion

@app.route('/productos/kion', methods=['GET'])
def listar_kion():
    precios = kion_precio()
    return render_template('kion_view.html', precios=precios)  # Asegúrate de renderizar la plantilla correctamente



#Esto hace que se guarde en la sesion los productos
@app.route('/productos/kion', methods=['POST'])
def enviar_peticion_kion():
    # Obtener los datos enviados por el formulario como listas
    supermercados = request.form.getlist('supermercado')
    precios = request.form.getlist('precio')
    
    # Verifica si la lista de precios ya existe en la sesión, si no, inicialízala
    if 'lista_precios' not in session:
        session['lista_precios'] = []

    # Agregar todos los supermercados y precios a la lista de la sesión
    for supermercado, precio in zip(supermercados, precios):
        # Agregar el ítem a la lista
        item_id = str(uuid.uuid4())  # Generar un identificador único
        session['lista_precios'].append({
            'id': item_id,
            'producto': 'kion',
            'unidad' : "kg",
            'supermercado': supermercado,
            'precio': precio
        })
        
    # Marca la sesión como modificada
    session.modified = True
    
    # Redirigir a la lista de precios seleccionados
    return redirect(url_for('ver_lista_precios'))

#Pimiento

@app.route('/productos/pimiento', methods=['GET'])
def listar_pimiento():
    precios = pimiento_precio()
    return render_template('pimiento_view.html', precios=precios)  # Asegúrate de renderizar la plantilla correctamente



#Esto hace que se guarde en la sesion los productos
@app.route('/productos/pimiento', methods=['POST'])
def enviar_peticion_pimiento():
    # Obtener los datos enviados por el formulario como listas
    supermercados = request.form.getlist('supermercado')
    precios = request.form.getlist('precio')
    
    # Verifica si la lista de precios ya existe en la sesión, si no, inicialízala
    if 'lista_precios' not in session:
        session['lista_precios'] = []

    # Agregar todos los supermercados y precios a la lista de la sesión
    for supermercado, precio in zip(supermercados, precios):
        # Agregar el ítem a la lista
        item_id = str(uuid.uuid4())  # Generar un identificador único
        session['lista_precios'].append({
            'id': item_id,
            'producto': 'pimiento',
            'unidad' : "kg",
            'supermercado': supermercado,
            'precio': precio
        })
        
    # Marca la sesión como modificada
    session.modified = True
    
    # Redirigir a la lista de precios seleccionados
    return redirect(url_for('ver_lista_precios'))


#ajiAmarillo

@app.route('/productos/ajiAmarillo', methods=['GET'])
def listar_ajiAmarillo():
    precios = ajiAmarillo_precio()
    return render_template('ajiAmarillo_view.html', precios=precios)  # Asegúrate de renderizar la plantilla correctamente



#Esto hace que se guarde en la sesion los productos
@app.route('/productos/ajiAmarillo', methods=['POST'])
def enviar_peticion_ajiAmarillo():
    # Obtener los datos enviados por el formulario como listas
    supermercados = request.form.getlist('supermercado')
    precios = request.form.getlist('precio')
    
    # Verifica si la lista de precios ya existe en la sesión, si no, inicialízala
    if 'lista_precios' not in session:
        session['lista_precios'] = []

    # Agregar todos los supermercados y precios a la lista de la sesión
    for supermercado, precio in zip(supermercados, precios):
        # Agregar el ítem a la lista
        item_id = str(uuid.uuid4())  # Generar un identificador único
        session['lista_precios'].append({
            'id': item_id,
            'producto': 'ajiAmarillo',
            'unidad' : "kg",
            'supermercado': supermercado,
            'precio': precio
        })
        
    # Marca la sesión como modificada
    session.modified = True
    
    # Redirigir a la lista de precios seleccionados
    return redirect(url_for('ver_lista_precios'))

#palta

@app.route('/productos/palta', methods=['GET'])
def listar_palta():
    precios = palta_precio()
    return render_template('palta_view.html', precios=precios)  # Asegúrate de renderizar la plantilla correctamente



#Esto hace que se guarde en la sesion los productos
@app.route('/productos/palta', methods=['POST'])
def enviar_peticion_palta():
    # Obtener los datos enviados por el formulario como listas
    supermercados = request.form.getlist('supermercado')
    precios = request.form.getlist('precio')
    
    # Verifica si la lista de precios ya existe en la sesión, si no, inicialízala
    if 'lista_precios' not in session:
        session['lista_precios'] = []

    # Agregar todos los supermercados y precios a la lista de la sesión
    for supermercado, precio in zip(supermercados, precios):
        # Agregar el ítem a la lista
        item_id = str(uuid.uuid4())  # Generar un identificador único
        session['lista_precios'].append({
            'id': item_id,
            'producto': 'palta',
            'unidad' : "kg",
            'supermercado': supermercado,
            'precio': precio
        })
        
    # Marca la sesión como modificada
    session.modified = True
    
    # Redirigir a la lista de precios seleccionados
    return redirect(url_for('ver_lista_precios'))


#vainita

@app.route('/productos/vainita', methods=['GET'])
def listar_vainita():
    precios = vainita_precio()
    return render_template('vainita_view.html', precios=precios)  # Asegúrate de renderizar la plantilla correctamente



#Esto hace que se guarde en la sesion los productos
@app.route('/productos/vainita', methods=['POST'])
def enviar_peticion_vainita():
    # Obtener los datos enviados por el formulario como listas
    supermercados = request.form.getlist('supermercado')
    precios = request.form.getlist('precio')
    
    # Verifica si la lista de precios ya existe en la sesión, si no, inicialízala
    if 'lista_precios' not in session:
        session['lista_precios'] = []

    # Agregar todos los supermercados y precios a la lista de la sesión
    for supermercado, precio in zip(supermercados, precios):
        # Agregar el ítem a la lista
        item_id = str(uuid.uuid4())  # Generar un identificador único
        session['lista_precios'].append({
            'id': item_id,
            'producto': 'vainita',
            'unidad' : "kg",
            'supermercado': supermercado,
            'precio': precio
        })
        
    # Marca la sesión como modificada
    session.modified = True
    
    # Redirigir a la lista de precios seleccionados
    return redirect(url_for('ver_lista_precios'))


#arveja

@app.route('/productos/arveja', methods=['GET'])
def listar_arveja():
    precios = arveja_precio()
    return render_template('arveja_view.html', precios=precios)  # Asegúrate de renderizar la plantilla correctamente



#Esto hace que se guarde en la sesion los productos
@app.route('/productos/arveja', methods=['POST'])
def enviar_peticion_arveja():
    # Obtener los datos enviados por el formulario como listas
    supermercados = request.form.getlist('supermercado')
    precios = request.form.getlist('precio')
    
    # Verifica si la lista de precios ya existe en la sesión, si no, inicialízala
    if 'lista_precios' not in session:
        session['lista_precios'] = []

    # Agregar todos los supermercados y precios a la lista de la sesión
    for supermercado, precio in zip(supermercados, precios):
        # Agregar el ítem a la lista
        item_id = str(uuid.uuid4())  # Generar un identificador único
        session['lista_precios'].append({
            'id': item_id,
            'producto': 'arveja',
            'unidad' : "kg",
            'supermercado': supermercado,
            'precio': precio
        })
        
    # Marca la sesión como modificada
    session.modified = True
    
    # Redirigir a la lista de precios seleccionados
    return redirect(url_for('ver_lista_precios'))

#maracuya

@app.route('/productos/maracuya', methods=['GET'])
def listar_maracuya():
    precios = maracuya_precio()
    return render_template('maracuya_view.html', precios=precios)  # Asegúrate de renderizar la plantilla correctamente



#Esto hace que se guarde en la sesion los productos
@app.route('/productos/maracuya', methods=['POST'])
def enviar_peticion_maracuya():
    # Obtener los datos enviados por el formulario como listas
    supermercados = request.form.getlist('supermercado')
    precios = request.form.getlist('precio')
    
    # Verifica si la lista de precios ya existe en la sesión, si no, inicialízala
    if 'lista_precios' not in session:
        session['lista_precios'] = []

    # Agregar todos los supermercados y precios a la lista de la sesión
    for supermercado, precio in zip(supermercados, precios):
        # Agregar el ítem a la lista
        item_id = str(uuid.uuid4())  # Generar un identificador único
        session['lista_precios'].append({
            'id': item_id,
            'producto': 'maracuya',
            'unidad' : "kg",
            'supermercado': supermercado,
            'precio': precio
        })
        
    # Marca la sesión como modificada
    session.modified = True
    
    # Redirigir a la lista de precios seleccionados
    return redirect(url_for('ver_lista_precios'))


#cebollaBlanca

@app.route('/productos/cebollaBlanca', methods=['GET'])
def listar_cebollaBlanca():
    precios = cebollaBlanca_precio()
    return render_template('cebollaBlanca_view.html', precios=precios)  # Asegúrate de renderizar la plantilla correctamente



#Esto hace que se guarde en la sesion los productos
@app.route('/productos/cebollaBlanca', methods=['POST'])
def enviar_peticion_cebollaBlanca():
    # Obtener los datos enviados por el formulario como listas
    supermercados = request.form.getlist('supermercado')
    precios = request.form.getlist('precio')
    
    # Verifica si la lista de precios ya existe en la sesión, si no, inicialízala
    if 'lista_precios' not in session:
        session['lista_precios'] = []

    # Agregar todos los supermercados y precios a la lista de la sesión
    for supermercado, precio in zip(supermercados, precios):
        # Agregar el ítem a la lista
        item_id = str(uuid.uuid4())  # Generar un identificador único
        session['lista_precios'].append({
            'id': item_id,
            'producto': 'cebollaBlanca',
            'unidad' : "kg",
            'supermercado': supermercado,
            'precio': precio
        })
        
    # Marca la sesión como modificada
    session.modified = True
    
    # Redirigir a la lista de precios seleccionados
    return redirect(url_for('ver_lista_precios'))


#nabo

@app.route('/productos/nabo', methods=['GET'])
def listar_nabo():
    precios = nabo_precio()
    return render_template('nabo_view.html', precios=precios)  # Asegúrate de renderizar la plantilla correctamente



#Esto hace que se guarde en la sesion los productos
@app.route('/productos/nabo', methods=['POST'])
def enviar_peticion_nabo():
    # Obtener los datos enviados por el formulario como listas
    supermercados = request.form.getlist('supermercado')
    precios = request.form.getlist('precio')
    
    # Verifica si la lista de precios ya existe en la sesión, si no, inicialízala
    if 'lista_precios' not in session:
        session['lista_precios'] = []

    # Agregar todos los supermercados y precios a la lista de la sesión
    for supermercado, precio in zip(supermercados, precios):
        # Agregar el ítem a la lista
        item_id = str(uuid.uuid4())  # Generar un identificador único
        session['lista_precios'].append({
            'id': item_id,
            'producto': 'nabo',
            'unidad' : "kg",
            'supermercado': supermercado,
            'precio': precio
        })
        
    # Marca la sesión como modificada
    session.modified = True
    
    # Redirigir a la lista de precios seleccionados
    return redirect(url_for('ver_lista_precios'))

if __name__ == '__main__':
    app.run(debug=True)
