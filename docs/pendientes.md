# Pendientes — MelvTech Web (v2 / techlo-lite-astro)

Última actualización: 2026-11-04

## Bloqueadores de lanzamiento (auditoría SEO 2026-11-03)

Resueltos: dominio `melvtech.com` (canonical/sitemap/robots/OG), títulos cortos
(`X | MelvTech`), metadatos del theme reemplazados, footer con navegación, redes falsas
desactivadas, tag/category fuera del sitemap, formularios enviando a
`atencion@melvtech.com`, suscripción Mailchimp del theme desactivada.

Abiertos:

- ~~**Inglés**~~ Resuelto (2026-11-04): el sitio se queda bilingüe. Contenido en inglés
  traducido (home, servicios, páginas, blog, landing) y las 77 páginas demo del theme
  eliminadas. La landing tiene URL propia: `/en/smart-home-monterrey/` (par hreflang de
  `/domotica-casas-inteligentes/`, ver `PATH_ALIASES` en `i18nUtils.ts`).
  Pendiente opcional: slugs en inglés para el resto (`/en/contacto/`, `/en/precios/`,
  `/en/services/alarmas/`...) con el mismo mecanismo de alias.
- ~~**Testimonios y equipo demo**~~ Testimonios ocultos en ambos idiomas
  (`enable: false`); `/team/` fuera del sitemap. Siguen existiendo las páginas `/team/` y el
  contenido demo en `src/content/team/`: borrarlas o marcarlas `noindex` antes de publicar.
- **Aviso de Privacidad (ES y EN)** (LFPDPPP; el formulario recolecta datos personales).
  Privacidad y Términos siguen en francés. Requiere razón social y domicilio fiscal;
  revisión legal recomendada.
- **FormSubmit**: tras publicar, enviar un mensaje de prueba por `/contacto/` y activar
  el enlace que llegará a `atencion@melvtech.com`; sin eso los leads no llegan.
- **Hosting: Dokploy.** `Dockerfile`, `deploy/` y guía en `docs/despliegue-dokploy.md`. Imagen probada en
  local el 2026-11-04 (build, healthcheck, redirecciones, gzip, caché, 404). Falta crear la
  aplicación en Dokploy y conectar el dominio.

## Landing "Domótica y casas inteligentes" (2026-11-03)

Página pilar en `/domotica-casas-inteligentes/` (contenido y FAQ en
`src/data/landing-domotica.ts`; el FAQ visible y el JSON-LD salen de los mismos datos).
`/services/domotica/` quedó con canonical hacia la landing y fuera del sitemap.
Incluye `public/llms.txt`.

Para mejorar posicionamiento y citas de IA faltan estos datos reales (no se inventaron):

- **Proyectos reales** en Monterrey con fotos propias (tipo de vivienda y zona aproximada).
- **Testimonios o reseñas** reales de clientes.
- **Años de experiencia**, marcas con las que trabajan y certificaciones.
- **Municipios** del área metropolitana donde sí dan servicio (hoy solo dice
  "Monterrey y su área metropolitana").
- **Dirección y teléfono** para añadir `LocalBusiness` al schema (hoy es `Organization` +
  `Service`) y crear/optimizar el Perfil de Negocio de Google.
- **Fecha**: actualizar `UPDATED_ISO`/`UPDATED_LABEL` en `landing-domotica.ts` cuando se
  edite la página (la fecha visible es una señal de frescura).

Cuando el dominio esté publicado: dar de alta Search Console y Bing Webmaster, enviar
`sitemap-index.xml`, y medir mensualmente 10 a 20 consultas (ej. "domótica Monterrey",
"casas inteligentes Monterrey", "qué es la domótica", "Alexa casa inteligente Monterrey")
en Google, ChatGPT y Perplexity, repitiendo cada una varias veces.

El selector de idioma de esta página enlaza a `/en/domotica-casas-inteligentes/`, que no
existe. Se resuelve al apagar el inglés (bloqueador #1 de arriba).

## Datos de contacto

- Email: `atencion@melvtech.com` (listo).
- Teléfono, dirección y horario: **pendientes de confirmar**. En `config.toml`
  (`settings.contactInfo`) están vacíos y el sitio los omite automáticamente; al
  llenarlos reaparecen en topbar, footer y menú lateral. El horario del theme era
  inventado y se eliminó.

## Imágenes pendientes

### Servicios para empresas (10 placeholders, 2 por servicio)

Cada uno de estos 5 servicios tiene una imagen principal (frontmatter `image:`) y una
secundaria (`<ImageList>` en el cuerpo) sin resolver — ver specs de tamaño/formato ya
acordadas (WebP, 4:5, ~920×1150px mínimo) en la carpeta `src/content/services/spanish/`:

- `control-accesos.mdx`
- `cableado-estructurado.mdx`
- `infraestructura-redes.mdx`
- `administrador-servidores.mdx`
- `polizas-soporte-tecnico.mdx`

### Servicios residenciales

Las imágenes principales ya están cargadas (`domotica.webp`, `redes-wifi.webp`,
`alarmas.webp`, `videovigilancia.webp`, `monitoreo.webp` en
`src/assets/images/services/`). **Falta la imagen secundaria** (`<ImageList>`) en cada
uno de esos 5 archivos `.mdx` — sigue como `{{DATO_FALTANTE: imagen_secundaria_...}}`.

### Blog (5 placeholders, uno por artículo)

Cada uno de los 5 artículos reales (ver sección "Blog" abajo) tiene su `image:` de
portada sin resolver, con el placeholder `{{DATO_FALTANTE: imagen_articulo_...}}` en
`src/content/blog/spanish/`.

## Blog

Se publicaron 5 artículos reales, todos basados en la ENVIPE 2025 (INEGI) edición
Nuevo León — cada cifra fue verificada contra el PDF oficial (no generada por IA sin
fuente) y lleva su atribución "Fuente: INEGI, ENVIPE 2025, Nuevo León" en el texto:

- `inseguridad-nuevo-leon-envipe-2025.mdx` — percepción de inseguridad (Alarmas, Videovigilancia)
- `costo-inseguridad-hogares-nuevo-leon.mdx` — costo económico del delito (Alarmas)
- `victimizacion-hogares-nuevo-leon.mdx` — 1 de cada 4 hogares víctima (Videovigilancia, Monitoreo)
- `cifra-oculta-delitos-nuevo-leon.mdx` — 92.7% de delitos sin castigo (Videovigilancia, Monitoreo)
- `miedo-al-delito-rutina-nuevo-leon.mdx` — miedo y cambios de rutina (Domótica, Monitoreo)

Se borraron los 16 posts de demo en francés que traía el theme. Falta: imágenes de
portada (ver arriba) y, si se quiere ampliar el blog, definir de dónde saldrán las
próximas fuentes de datos verificables (no hay más PDFs oficiales cargados por ahora).

## Contenido sin traducir (queda como demo, decisión consciente)

Estas secciones se dejaron intencionalmente con el texto de demo del theme (francés /
genérico) hasta tener contenido real de MelvTech:

- **Testimonios** (`src/content/sections/spanish/testimonial.md`) — citas y nombres
  falsos del theme.
- **Equipo** (`src/content/team/spanish/`) — perfiles de demo (Daniyel Karlos, etc.).

## Contenido de empresas — falta profundizar

Al construir las páginas de servicios para empresas se dejaron fuera (a propósito, para
no inventar datos) las secciones que sí tiene la referencia (cas.mx):

- Certificaciones del personal / marca
- Testimonios de clientes reales
- Casos de éxito / proyectos realizados

Agregarlas cuando haya información real que mostrar.

## Idioma inglés

La carpeta `src/content/*/english/` sigue con el contenido de demo original del theme
(sin tocar). El sitio funciona hoy en la práctica solo en español (`es` es el idioma por
default). Definir si se traduce a inglés más adelante o se deshabilita el selector de
idioma mientras tanto.

## Deuda técnica menor

- **Breadcrumb en `/services/*` y `/blog/*`**: muestra el slug de la URL humanizado en
  vez del `title` real del contenido (ej. "Polizas soporte tecnico" en vez de "Pólizas
  de Soporte Técnico", o "Blog" > "Inseguridad nuevo leon envipe 2025"), porque
  `PageHeader.astro` arma el breadcrumb a partir de la URL, no del contenido. Afecta a
  todas las páginas de servicio y de blog por igual. Requiere tocar un componente
  compartido (`src/layouts/components/widgets/PageHeader.astro`).
- **`config.generated.json` puede quedar desactualizado**: se genera desde
  `src/config/config.toml` vía `node scripts/toml-watcher.mjs` (o el watcher de
  `npm run dev`). Si se edita `config.toml` a mano y el sitio no refleja el cambio,
  correr ese script y reiniciar el dev server.

## Pendiente operativo

- **Hosting / deploy**: el proyecto trae configuración para Cloudflare Pages
  (`wrangler.toml`), Vercel (`vercel.json`) y Netlify (`netlify.toml`) de fábrica —
  falta decidir dónde se va a alojar el sitio real.
- **Dominio**: falta definir y conectar el dominio real de MelvTech
  (`baseUrl` en `config.toml` sigue apuntando al dominio de demo del theme).
- **`npm run astro-check` / `npm run build`**: verificado limpio (0 errores) al agregar
  los servicios de empresa y el blog — volver a correrlo antes de cada deploy.

## Traducción al inglés: cómo se hizo y qué revisar

`scripts/translate_es_en.py` traduce con el modelo local (qwen) con validación de cifras,
enlaces y restos de español; `scripts/fix_en_review.py` aplica las correcciones manuales.
Los 5 artículos del blog se reescribieron a mano porque el modelo inventó un título y
tradujo "Nuevo León" como "New Mexico". Si cambia el texto en español hay que actualizar
también el inglés. La carpeta `design/` (artes sociales, portadas, orquestador de modelos)
vive en la raíz, fuera de este repo.
