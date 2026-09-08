# Pendientes — MelvTech Web (v2 / techlo-lite-astro)

Última actualización: 2026-09-08

## Datos de contacto reales

Hoy son placeholders `{{DATO_FALTANTE: ...}}` visibles en el sitio. Faltan:

- Teléfono real → `src/config/config.toml` (`settings.contactInfo.phone`)
- Email real → `src/config/config.toml` (`settings.contactInfo.email`)
- Dirección real → `src/config/config.toml` (`settings.contactInfo.address`) y
  `src/content/sections/spanish/contact-section-two.md` (bloque `info`)

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

## Contenido sin traducir (queda como demo, decisión consciente)

Estas secciones se dejaron intencionalmente con el texto de demo del theme (francés /
genérico) hasta tener contenido real de MelvTech:

- **Testimonios** (`src/content/sections/spanish/testimonial.md`) — citas y nombres
  falsos del theme.
- **Equipo** (`src/content/team/spanish/`) — perfiles de demo (Daniyel Karlos, etc.).
- **Blog** (`src/content/blog/spanish/`, `src/content/sections/spanish/blog-section.md`)
  — posts de ejemplo del theme.

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

- **Breadcrumb en `/services/*`**: muestra "Services" en vez de "Servicios" y pierde
  acentos (ej. "Polizas soporte tecnico"), porque `PageHeader.astro` arma el breadcrumb
  a partir del slug de la URL, no del `title` del contenido. Afecta a todas las páginas
  de servicio por igual. Requiere tocar un componente compartido
  (`src/layouts/components/widgets/PageHeader.astro`).
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
- **`npm run astro-check` / `npm run build`**: no se ha corrido una verificación de
  build completa desde que se agregaron los servicios de empresa — conviene correrlo
  antes de desplegar a producción.
