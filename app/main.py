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
    # Datos dinámicos que enviaremos al frontend
    # En el futuro, esto vendrá de una consulta a base de datos
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
            "desarrollador": "Jorge López",
            "rol": "Backend & Infrastructure Developer",
            "proyectos": mis_proyectos
        }
    )