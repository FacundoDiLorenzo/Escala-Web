# Escala Web

Sitio web de **Escala Web**, el servicio de diseño web de Facundo Di Lorenzo en Málaga.

Es una web estática con portada y subpáginas, trilingüe (español, inglés e italiano), sin dependencias externas: las tipografías (Archivo y Newsreader) y la foto se sirven desde la propia web.

## Ver la web en local

Abre `index.html` directamente en el navegador, o sirve la carpeta con cualquier servidor estático:

```bash
python3 -m http.server 8000
# y entra en http://localhost:8000
```

## Publicar con GitHub Pages

1. En el repositorio, ve a **Settings → Pages**.
2. En **Build and deployment**, elige **Deploy from a branch**.
3. Selecciona la rama `main` y la carpeta `/ (root)`, y guarda.
4. En un par de minutos la web estará en `https://dilorenzofacundo19-rgb.github.io/Escala-Web/`.

El archivo `.nojekyll` indica a GitHub Pages que sirva los archivos tal cual, sin procesarlos con Jekyll.

## Estructura

| Archivo | Descripción |
|---|---|
| `index.html` | Portada |
| `servicios.html` | Los cuatro servicios en detalle y el proceso de trabajo |
| `sobre-mi.html` | Sobre Facundo, con la tarjeta de la foto |
| `preguntas-frecuentes.html` | Preguntas frecuentes |
| `contacto.html` | Qué contar del proyecto y datos de contacto |
| `aviso-legal.html`, `privacidad.html` | Páginas legales |
| `404.html` | Página para enlaces rotos |
| `assets/styles.css` | Estilos compartidos |
| `assets/main.js` | Idioma, menú, animaciones y botones de copiar |
| `assets/i18n.js` | Textos en ES, EN e IT |
| `assets/fonts/`, `assets/facundo.webp` | Tipografías y foto |
| `scripts/build.py` | Genera las páginas HTML (cabecera y pie compartidos) |
| `.nojekyll` | Desactiva Jekyll en GitHub Pages |

## Editar textos

- Traducciones: `assets/i18n.js` (cada texto tiene su clave en `es`, `en` e `it`).
- Estructura de las páginas y textos legales: `scripts/build.py`. Después de cambiarlo, regenera las páginas con `python3 scripts/build.py .` desde la raíz del repositorio.

## Contacto

WhatsApp: [+34 663 625 836](https://wa.me/34663625836)
