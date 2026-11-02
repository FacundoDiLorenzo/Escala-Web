# Escala Web

Sitio web de **Escala Web**, el servicio de diseño web de Facundo Di Lorenzo en Málaga.

Es una página de una sola pieza (`index.html`), trilingüe (español, inglés e italiano), sin dependencias ni proceso de compilación. Solo carga las fuentes Inter e Inter Tight desde Google Fonts.

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

| Archivo       | Descripción                                   |
|---------------|-----------------------------------------------|
| `index.html`  | La web completa: HTML, estilos y textos ES/EN/IT |
| `.nojekyll`   | Desactiva Jekyll en GitHub Pages              |
| `README.md`   | Este archivo                                  |

## Contacto

WhatsApp: [+34 663 625 836](https://wa.me/34663625836)
