# Despliegue en Dokploy

El sitio es estático (Astro). El `Dockerfile` lo compila con Node 22 y lo sirve con nginx.
No necesita variables de entorno ni base de datos. El formulario de contacto envía a
FormSubmit (externo).

## Archivos

| Archivo | Para qué |
|---|---|
| `Dockerfile` | Etapa 1: `npm ci` + `npm run build`. Etapa 2: nginx con `dist/` |
| `deploy/nginx.conf` | Trailing slash, redirección `/sitemap.xml` → `/sitemap-index.xml`, gzip, caché, 404 |
| `deploy/security-headers.conf` | Cabeceras de seguridad básicas |
| `.dockerignore` | Deja fuera `node_modules`, `dist`, `.astro`, `docs` |

## Pasos en Dokploy

1. **Create Project** y dentro **Create Service → Application**.
2. **Provider:** GitHub (repo `amedina16/melvtech-site`, rama `main`) o el que uses.
3. **Build Type:** `Dockerfile` (ruta `Dockerfile`, contexto `.`).
4. **Domains:** agrega `melvtech.com` y `www.melvtech.com`, **Container Port `80`**, HTTPS
   activado (Let's Encrypt).
5. **Deploy.**
6. Opcional: activa *Auto Deploy* para publicar en cada push a `main`.

## DNS

Apunta `melvtech.com` y `www` (registros A) a la IP del servidor de Dokploy. Para que no
haya contenido duplicado, configura una redirección de `www.melvtech.com` a
`melvtech.com` (o al revés) y deja **un solo dominio canónico**. El sitio declara
`https://melvtech.com/` como canónico.

## Después del primer despliegue

- Revisar `https://melvtech.com/`, `/en/`, `/sitemap-index.xml` y `/robots.txt`.
- Enviar un mensaje de prueba por `/contacto/` y **activar FormSubmit** con el correo que
  llega a `atencion@melvtech.com` (sin eso, los leads no llegan).
- Dar de alta Search Console y Bing Webmaster y enviar `sitemap-index.xml`.

## Probar la imagen en local

```bash
docker build -t melvtech-web .
docker run --rm -p 8080:80 melvtech-web
```

Abrir http://localhost:8080/.

## Notas

- La compilación necesita internet (descarga las fuentes de Google).
- Si cambias `config.toml`, el build regenera `.astro/config.generated.json` solo.
- HSTS no está en nginx: lo gestiona Traefik/Dokploy si lo activas.
- Las imágenes tienen caché de 7 días; los archivos de `/_astro/` (con hash) de un año.
