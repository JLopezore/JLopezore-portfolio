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
            "nombre": "Diseño UI/UX para una app de biblioteca",
            "descripcion": "Diseño de interfaz y experiencia de usuario para una aplicación móvil de gestión de biblioteca, enfocada en la facilidad de uso y accesibilidad.",
            "stack": ["Figma", "IHC"],
            "enlace": "https://www.figma.com/proto/LLDZiS1k3xLy1t4P80nipY/Main?node-id=0-1&t=nSOfas3ooz7mYR6Q-1"
        },
        {
            "nombre": "WISP La Soledad - Core",
            "descripcion": "Backend de gestión automatizada con generación de recibos en PDF y notificaciones por WhatsApp.",
            "stack": ["Python", "FastAPI", "MikroTik"],
            "enlace": "https://github.com/JLopezore/WISP-Manager.git"
        },
        {
            "nombre": "WISP La Soledad - Portal del Cliente",
            "descripcion": "Portal web para clientes con autenticación, visualización de facturas y soporte técnico.",
            "stack": ["Python", "FastAPI", "React"],
            "enlace": "https://github.com/JLopezore/WISP-Manager.git"
        },
        {
            "nombre": "Wisp La Soledad - Portal Android",
            "descripcion": "Aplicación móvil para clientes con funcionalidades similares al portal web, optimizada para Android.",
            "stack": ["Kotlin", "Android", "Firebase"],
            "enlace": "https://github.com/JLopezore/WispHub-Mobile.git"    
        },
        {
            "nombre": "Siplex - backend",
            "descripcion": "Backend para aplicación de gestión de planificación de examenes, con autenticación y API REST.",
            "stack": ["Python", "FastAPI", "PostgreSQL"],
            "enlace": "https://github.com/LosRatones-404T/HORARIOS-BACKEND.git"
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

