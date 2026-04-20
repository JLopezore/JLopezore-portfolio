from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Portafolio Backend")

# Le indicamos a FastAPI dónde vivirán nuestros archivos HTML
templates = Jinja2Templates(directory="app/templates")

# Montamos la carpeta de archivos estáticos
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    biografia = (
        "Soy estudiante de octavo semestre de la Licenciatura en Informática, enfocado en el "
        "desarrollo backend y la administración de infraestructura. Me apasiona construir soluciones "
        "eficientes, desde el código hasta el despliegue en servidores Linux. Además de crear APIs "
        "con Python y FastAPI, tengo experiencia práctica gestionando redes y equipos de "
        "telecomunicaciones para proveedores de internet (WISP), lo que me da una visión integral "
        "del ciclo de vida del software y la conectividad."
    )

    mis_habilidades = [
        {"nombre": "Python", "icono": "devicon-python-plain", "es_imagen": False},
        {"nombre": "FastAPI", "icono": "devicon-fastapi-plain", "es_imagen": False},
        {"nombre": "Java", "icono": "devicon-java-plain", "es_imagen": False},
        {"nombre": "Android", "icono": "devicon-android-plain", "es_imagen": False},
        {"nombre": "C", "icono": "devicon-c-plain", "es_imagen": False},
        {"nombre": "Linux", "icono": "devicon-linux-plain", "es_imagen": False},
        {"nombre": "Admin. Servidores", "icono": "devicon-bash-plain", "es_imagen": False}, # Agregado
        {"nombre": "Docker", "icono": "devicon-docker-plain", "es_imagen": False},
        {"nombre": "PostgreSQL", "icono": "devicon-postgresql-plain", "es_imagen": False},
        {"nombre": "Oracle", "icono": "devicon-oracle-original", "es_imagen": False},
        {"nombre": "Couchbase", "icono": "devicon-couchbase-plain", "es_imagen": False},
        {"nombre": "Git", "icono": "devicon-git-plain", "es_imagen": False},
        # Estos dos buscarán una imagen en la carpeta static
        {"nombre": "MikroTik", "icono": "mikrotik.png", "es_imagen": True}, 
        {"nombre": "Ubiquiti", "icono": "ubiquiti.png", "es_imagen": True}
    ]

    mis_proyectos = [
        {
            "nombre": "WISP La Soledad - Core",
            "descripcion": "Backend de gestión automatizada con generación de recibos en PDF y notificaciones por WhatsApp.",
            "stack": ["Python", "FastAPI", "MikroTik"]
        },
        {
            "nombre": "Clúster Distribuido",
            "descripcion": "Arquitectura de base de datos de 4 nodos configurada para pruebas de alta disponibilidad y fragmentación de rangos.",
            "stack": ["CockroachDB", "Linux", "Docker"]
        }
    ]
    
    # Renderizamos la plantilla pasándole los datos
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "desarrollador": "Jorge López López",
            "rol": "Backend & Infrastructure Developer",
            "bio": biografia,
            "habilidades": mis_habilidades,
            "proyectos": mis_proyectos
        }
    )

