from fastapi import FastAPI, Request, Query
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.translations import textos

app = FastAPI(title="Portafolio Backend")

# Le indicamos a FastAPI dónde vivirán nuestros archivos HTML
templates = Jinja2Templates(directory="app/templates")

# Montamos la carpeta de archivos estáticos
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request, lang: str = Query("es")):

    if lang not in ["es", "en"]:
        lang = "es"  # Por defecto, español
    t = textos[lang]  

# Habilidades (Traducimos dinámicamente "Admin. Servidores" a "Server Admin")
    mis_habilidades = [
        {"nombre": "Python", "icono": "devicon-python-plain", "es_imagen": False},
        {"nombre": "FastAPI", "icono": "devicon-fastapi-plain", "es_imagen": False},
        {"nombre": "Java", "icono": "devicon-java-plain", "es_imagen": False},
        {"nombre": "Android", "icono": "devicon-android-plain", "es_imagen": False},
        {"nombre": "C", "icono": "devicon-c-plain", "es_imagen": False},
        {"nombre": "Linux", "icono": "devicon-linux-plain", "es_imagen": False},
        {"nombre": "Admin. Servidores" if lang == "es" else "Server Admin", "icono": "devicon-bash-plain", "es_imagen": False},
        {"nombre": "Docker", "icono": "devicon-docker-plain", "es_imagen": False},
        {"nombre": "PostgreSQL", "icono": "devicon-postgresql-plain", "es_imagen": False},
        {"nombre": "Oracle", "icono": "devicon-oracle-original", "es_imagen": False},
        {"nombre": "Couchbase", "icono": "devicon-couchbase-plain", "es_imagen": False},
        {"nombre": "Git", "icono": "devicon-git-plain", "es_imagen": False},
        {"nombre": "MikroTik", "icono": "mikrotik.png", "es_imagen": True}, 
        {"nombre": "Ubiquiti", "icono": "ubiquiti.png", "es_imagen": True}
    ]

    # Proyectos traducidos
    mis_proyectos = [
        {
            "nombre": "Diseño UI/UX - App Biblioteca" if lang == "es" else "UI/UX Design - Library App",
            "descripcion": {
                "es": "Diseño de interfaz y experiencia de usuario para una aplicación móvil de gestión de biblioteca, enfocada en la facilidad de uso y accesibilidad.",
                "en": "User interface and user experience design for a mobile library management application, focused on ease of use and accessibility."
            },
            "stack": ["Figma", "IHC"],
            "enlace": "https://www.figma.com/proto/LLDZiS1k3xLy1t4P80nipY/Main?node-id=0-1&t=nSOfas3ooz7mYR6Q-1"
        },
        {
            "nombre": "WISP La Soledad - Core",
            "descripcion": {
                "es": "Backend de gestión automatizada con generación de recibos en PDF y notificaciones por WhatsApp.",
                "en": "Automated management backend with PDF receipt generation and WhatsApp notifications."
            },
            "stack": ["Python", "FastAPI", "MikroTik"],
            "enlace": "https://github.com/JLopezore/WISP-Manager.git"
        },
        {
            "nombre": "WISP La Soledad - Portal del Cliente" if lang == "es" else "WISP La Soledad - Client Portal",
            "descripcion": {
                "es": "Portal web para clientes con autenticación, visualización de facturas y soporte técnico.",
                "en": "Web portal for clients featuring authentication, invoice viewing, and technical support."
            },
            "stack": ["Python", "FastAPI", "React"],
            "enlace": "https://github.com/JLopezore/WISP-Manager.git"
        },
        {
            "nombre": "Wisp La Soledad - Portal Android" if lang == "es" else "Wisp La Soledad - Android App",
            "descripcion": {
                "es": "Aplicación móvil para clientes con funcionalidades similares al portal web, optimizada para Android.",
                "en": "Mobile application for clients offering similar features to the web portal, fully optimized for Android."
            },
            "stack": ["Kotlin", "Android", "Firebase"],
            "enlace": "https://github.com/JLopezore/WispHub-Mobile.git"    
        },
        {
            "nombre": "Siplex - Backend",
            "descripcion": {
                "es": "Backend para aplicación de gestión de planificación de examenes, con autenticación y API REST.",
                "en": "Backend for an exam scheduling management application, including secure authentication and a REST API."
            },
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
            "t": t,
            "lang": lang,
            "habilidades": mis_habilidades,
            "proyectos": mis_proyectos
        }
    )

