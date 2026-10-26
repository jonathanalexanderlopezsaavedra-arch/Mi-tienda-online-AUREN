from flask import Flask
from markupsafe import escape
import json

app = Flask(__name__)

productos = [
    {
        "nombre": "Polo urbano",
        "precio": 35.00,
        "emoji": "👕",
        "imagen": "polo.jpeg",
        "categoria": "Ropa"
    },
    {
        "nombre": "Gorra",
        "precio": 25.00,
        "emoji": "🧢",
        "imagen": "gorra.jpeg",
        "categoria": "Accesorios"
    },
    {
        "nombre": "Mochila",
        "precio": 60.00,
        "emoji": "🎒",
        "imagen": "mochila.jpeg",
        "categoria": "Accesorios"
    }
]


@app.route("/")
def inicio():
    html = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="google-site-verification" content="_nflRzVJg-8Be9vrd76cF4XgiQyeoAG71vheiwRZ8HY">
        <title>AUREN | Tienda Online</title>

        <style>
            * {
                box-sizing: border-box;
            }

            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background-color: #F5F3ED;
                color: #172820;
            }

            header {
                background: linear-gradient(135deg, #172820, #243D30);
                text-align: center;
                padding: 55px 15px 50px;
            }

            header h1 {
                color: #E8D4A2;
                font-family: "Palatino Linotype", "Book Antiqua", Georgia, serif;
                font-size: 48px;
                font-style: italic;
                font-weight: normal;
                letter-spacing: 5px;
                text-shadow: 0 2px 12px rgba(232, 212, 162, 0.18);
                margin: 0 0 15px;
            }

            header p {
                color: #F5F3ED;
                font-size: 14px;
                letter-spacing: 2px;
                line-height: 1.8;
                margin: 0;
                opacity: 0.92;
            }

            .linea-elegante {
                width: 75px;
                height: 2px;
                background-color: #E8D4A2;
                margin: 20px auto 0;
            }

            .introduccion {
                text-align: center;
                padding: 35px 15px 5px;
            }

            .introduccion h2 {
                font-family: Georgia, "Times New Roman", serif;
                font-size: 27px;
                font-weight: normal;
                margin: 0 0 10px;
                color: #172820;
            }

            .introduccion p {
                color: #686B63;
                font-size: 14px;
            }

            .contenedor {
                max-width: 1100px;
                margin: 25px auto 40px;
                padding: 0 20px;
            }

            .seccion-categoria {
                margin: 35px 0 45px;
            }

            .titulo-categoria {
                color: #172820;
                font-family: "Palatino Linotype", "Book Antiqua", Georgia, serif;
                font-size: 30px;
                font-weight: normal;
                letter-spacing: 6px;
                text-align: center;
                margin: 0 0 14px;
                text-transform: uppercase;
            }

            .linea-categoria {
                width: 55px;
                height: 2px;
                background-color: #B08D57;
                margin: 0 auto 25px;
            }

            .productos-categoria {
                display: grid;
                grid-template-columns: repeat(
                    auto-fit, minmax(230px, 1fr)
                );
                gap: 25px;
            }

            .producto {
                position: relative;
                background: linear-gradient(
                    180deg, #FFFFFF 0%, #FCFAF5 100%
                );
                border: 1px solid #E5D9C2;
                border-radius: 18px;
                padding: 22px;
                text-align: center;
                box-shadow: 0 5px 18px rgba(23, 40, 32, 0.07);
                transition:
                    transform 0.3s ease,
                    box-shadow 0.3s ease,
                    border-color 0.3s ease;
                overflow: hidden;
            }

            .producto:hover {
                transform: translateY(-6px);
                border-color: #B08D57;
                box-shadow: 0 14px 30px rgba(23, 40, 32, 0.13);
            }

            .imagen {
                width: 100%;
                height: 250px;
                display: flex;
                align-items: center;
                justify-content: center;
                overflow: hidden;
            }

            .producto img {
                display: block;
                width: 100%;
                height: 100%;
                object-fit: contain;
                object-position: center;
                transition: transform 0.3s ease;
            }

            .producto:hover img {
                transform: scale(1.04);
            }

            .nombre-producto {
                font-family: "Palatino Linotype", "Book Antiqua", Georgia, serif;
                font-size: 22px;
                font-weight: normal;
                color: #172820;
                letter-spacing: 0.3px;
                line-height: 1.4;
                margin: 24px 0 8px;
            }

            .precio {
                font-family: "Palatino Linotype", "Book Antiqua", Georgia, serif;
                font-size: 20px;
                font-weight: normal;
                color: #B08D57;
                letter-spacing: 0.5px;
                margin: 12px 0 18px;
            }

            button {
                background-color: #172820;
                color: #E8D4A2;
                border: 1px solid #E8D4A2;
                padding: 12px 18px;
                border-radius: 8px;
                cursor: pointer;
                font-size: 14px;
                transition:
                    background-color 0.3s ease,
                    color 0.3s ease,
                    transform 0.3s ease,
                    box-shadow 0.3s ease;
            }

            button:hover {
                background-color: #E8D4A2;
                color: #172820;
                transform: translateY(-2px);
                box-shadow: 0 5px 12px rgba(23, 40, 32, 0.12);
            }

            .carrito {
                max-width: 1000px;
                margin: 35px auto;
                padding: 25px;
                background-color: #FFFFFF;
                border: 1px solid #E8E4DA;
                border-radius: 14px;
                box-shadow: 0 4px 14px rgba(23, 40, 32, 0.08);
            }

            .carrito h2 {
                font-family: Georgia, "Times New Roman", serif;
                font-weight: normal;
                color: #172820;
                margin-top: 0;
            }

            .carrito li {
                margin: 12px 0;
            }

            .vaciar {
                margin-top: 10px;
            }

            .whatsapp {
                display: block;
                width: 100%;
                margin-top: 20px;
                padding: 15px 18px;
                background-color: #172820;
                color: #E8D4A2;
                border: 1px solid #B08D57;
                border-radius: 8px;
                font-size: 15px;
                font-weight: bold;
                letter-spacing: 0.3px;
            }

            .whatsapp:hover {
                background-color: #B08D57;
                color: #172820;
            }

            footer {
                background-color: #172820;
                color: #E8D4A2;
                text-align: center;
                padding: 22px 15px;
                font-size: 13px;
                letter-spacing: 1px;
            }

            @media (max-width: 600px) {
                header h1 {
                    font-size: 34px;
                }

                .contenedor {
                    padding: 0 15px;
                }

                .productos-categoria {
                    grid-template-columns: 1fr;
                    gap: 20px;
                }

                .imagen {
                    height: 260px;
                }

                .carrito {
                    margin: 20px 15px;
                }
            }
        </style>
    </head>

    <body>
        <header>
            <h1>AUREN</h1>
            <p>Elegancia en cada detalle</p>
            <div class="linea-elegante"></div>
        </header>

        <section class="introduccion">
            <h2>Descubre tu estilo</h2>
            <p>Encuentra tus favoritos en nuestra colección.</p>
        </section>

        <main class="contenedor">
    """

    for categoria in ["Ropa", "Accesorios"]:
        html += f"""
            <section class="seccion-categoria">
                <h2 class="titulo-categoria">{categoria.upper()}</h2>
                <div class="linea-categoria"></div>
                <div class="productos-categoria">
        """

        for producto in productos:
            if producto["categoria"] == categoria:
                nombre_seguro = json.dumps(
                    producto["nombre"], ensure_ascii=False
                )

                html += f"""
                    <div class="producto">
                        <div class="imagen">
                            <img
                                src="/static/{escape(producto['imagen'])}"
                                alt="{escape(producto['nombre'])}"
                            >
                        </div>

                        <h3 class="nombre-producto">
                            {escape(producto['nombre'])}
                        </h3>

                        <p class="precio">
                            S/ {producto['precio']:.2f}
                        </p>

                        <button onclick='agregar({nombre_seguro})'>
                            Agregar al carrito
                        </button>
                    </div>
                """

        html += """
                </div>
            </section>
        """

    html += """
        </main>

        <section class="carrito">
            <h2>Mi carrito</h2>

            <p>
                Productos:
                <span id="cantidad">0</span>
            </p>

            <p>
                Total: S/
                <span id="total">0.00</span>
            </p>

            <ul id="lista-carrito"></ul>

            <button class="vaciar" onclick="vaciarCarrito()">
                Vaciar carrito
            </button>

            <button class="whatsapp" onclick="finalizarPorWhatsApp()">
                Finalizar pedido por WhatsApp
            </button>
        </section>

        <footer>
            AUREN · ELEGANCIA EN CADA DETALLE
        </footer>

        <script>
            let carrito = [];

            const precios = {
                "Polo urbano": 35.00,
                "Gorra": 25.00,
                "Mochila": 60.00
            };

            function agregar(nombre) {
                carrito.push(nombre);
                actualizarCarrito();
            }

            function actualizarCarrito() {
                let total = 0;
                const lista = document.getElementById("lista-carrito");

                lista.innerHTML = "";

                carrito.forEach(function(nombre) {
                    total += precios[nombre];

                    const elemento = document.createElement("li");
                    elemento.textContent =
                        nombre + " - S/ " + precios[nombre].toFixed(2);

                    lista.appendChild(elemento);
                });

                document.getElementById("cantidad").textContent =
                    carrito.length;

                document.getElementById("total").textContent =
                    total.toFixed(2);
            }

            function vaciarCarrito() {
                carrito = [];
                actualizarCarrito();
            }

            function finalizarPorWhatsApp() {
                if (carrito.length === 0) {
                    alert(
                        "Tu carrito está vacío. Agrega algún producto primero."
                    );
                    return;
                }

                let mensaje =
                    "¡Hola! Quiero hacer un pedido en AUREN:\\n\\n";

                let cantidades = {};

                carrito.forEach(function(nombre) {
                    cantidades[nombre] =
                        (cantidades[nombre] || 0) + 1;
                });

                for (let nombre in cantidades) {
                    mensaje += nombre + " x" + cantidades[nombre] +
                        " - S/ " +
                        (
                            precios[nombre] * cantidades[nombre]
                        ).toFixed(2) +
                        "\\n";
                }

                let total = 0;

                carrito.forEach(function(nombre) {
                    total += precios[nombre];
                });

                mensaje += "\\nTotal: S/ " + total.toFixed(2);

                let telefono = "51987827776";

                let enlace = "https://wa.me/" + telefono +
                    "?text=" + encodeURIComponent(mensaje);

                window.open(enlace, "_blank");
            }
        </script>
    </body>
    </html>
    """

    return html


@app.route("/sitemap.xml")
def sitemap():
    contenido = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>https://auren-e79p.onrender.com/</loc>
    </url>
</urlset>"""

    return app.response_class(
        contenido,
        mimetype="application/xml"
    )


@app.route("/robots.txt")
def robots():
    contenido = """User-agent: *
Allow: /

Sitemap: https://auren-e79p.onrender.com/sitemap.xml"""

    return app.response_class(
        contenido,
        mimetype="text/plain"
    )


if __name__ == "__main__":
    app.run(debug=True)