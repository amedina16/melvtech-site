"""
Genera las 4 páginas de servicio restantes en formato .mdx, usando
domotica.mdx (dentro de src/content/services/spanish/) como molde,
con Qwen2.5-Coder-7B corriendo localmente en LM Studio.

Uso:
    python generate_services_mdx.py

Requisitos:
    - LM Studio corriendo con el modelo cargado, servidor activo en el puerto 1234
    - pip install requests
    - Debes correr este script desde la raíz del proyecto Astro
"""

import json
import requests
from pathlib import Path

LM_STUDIO_URL = "http://localhost:1234/v1/chat/completions"
MODEL_NAME = "qwen2.5-coder-7b-instruct"

SYSTEM_PROMPT = """Eres un generador de contenido MDX para el sitio web de MelvTech, una empresa de domótica, redes, alarmas, videovigilancia y monitoreo de cámaras en Monterrey y su área metropolitana.

REGLAS ESTRICTAS:
1. Sigues EXACTAMENTE la estructura del archivo .mdx molde que se te entrega: mismo frontmatter (mismas claves), mismos componentes MDX (ImageList, ImageItem, CardWrapper, Card), mismo número aproximado de secciones.
2. Solo reemplazas el contenido de texto y los valores de frontmatter según los datos del nuevo servicio.
3. NUNCA inventas precios exactos, testimonios, estadísticas, nombres de clientes o rutas de imagen reales. Si no tienes una ruta de imagen real, usa el placeholder {{DATO_FALTANTE: descripcion_corta_del_campo}} tal cual, igual que en el molde.
4. El tono es cercano, confiable y sin tecnicismos — dirigido a clientes residenciales y comerciales, no a instaladores.
5. Nunca menciones precios cerrados. Si el contexto lo requiere, usa "desde $X" o invita a cotizar.
6. MelvTech nació como especialista en videovigilancia y se posiciona como una ampliación de esa identidad, no un cambio de rubro — puedes reforzar esa continuidad si aplica naturalmente, sin forzarlo.
7. No agregues comentarios ni explicaciones fuera del archivo. Tu salida es ÚNICAMENTE el contenido final del archivo .mdx, listo para guardar.

Si algún dato de entrada no viene incluido, usa el placeholder {{DATO_FALTANTE: nombre_del_campo}} en el lugar exacto donde iría — nunca lo rellenes con contenido inventado."""


def build_user_message(molde: str, servicio: dict) -> str:
    return f"""MOLDE DE REFERENCIA (respeta esta estructura exacta, incluyendo frontmatter y componentes MDX):
{molde}

DATOS DEL NUEVO SERVICIO A GENERAR:
- Nombre: {servicio['nombre']}
- Slug (usar como customSlug): {servicio['slug']}
- Ícono Lucide sugerido: {servicio['icono_lucide']}
- Descripción corta: {servicio['descripcion_corta']}
- Beneficios: {json.dumps(servicio['beneficios'], ensure_ascii=False)}
- Público: {servicio['publico']}
- Servicios complementarios (para mencionar o enlazar si el molde lo permite): {json.dumps(servicio['complementario'], ensure_ascii=False)}

Genera el archivo .mdx completo para este servicio, siguiendo el molde exactamente."""


def call_qwen(molde: str, servicio: dict) -> str:
    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": build_user_message(molde, servicio)},
        ],
        "temperature": 0.2,
    }
    response = requests.post(LM_STUDIO_URL, json=payload, timeout=120)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]


def main():
    data = json.loads(Path("servicios-data.json").read_text(encoding="utf-8"))
    molde_slug = data["molde_referencia"]

    services_dir = Path("src/content/services/spanish")
    molde_path = services_dir / f"{molde_slug}.mdx"
    molde = molde_path.read_text(encoding="utf-8")

    for servicio in data["servicios"]:
        if servicio["slug"] == molde_slug:
            continue  # el molde ya existe, no se regenera

        print(f"Generando {servicio['slug']}.mdx ...")
        contenido = call_qwen(molde, servicio)

        out_path = services_dir / f"{servicio['slug']}.mdx"
        out_path.write_text(contenido, encoding="utf-8")

        if "{{DATO_FALTANTE" in contenido:
            print(f"  ⚠️  {servicio['slug']}.mdx tiene datos pendientes (imágenes probablemente) — revisar antes de publicar")
        else:
            print(f"  ✅ {servicio['slug']}.mdx generado")

    print("\nListo. Revisa cada archivo generado antes de integrarlo al proyecto.")


if __name__ == "__main__":
    main()
