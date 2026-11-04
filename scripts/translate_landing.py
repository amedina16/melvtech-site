"""Genera src/data/landing-domotica.en.ts desde design/landing-es.json con el modelo local.

Campos SEO críticos (meta, hero) y textos de interfaz se escriben a mano en OVERRIDE;
el resto lo traduce scripts/translate_es_en.py (con validación de cifras, enlaces y español).
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import translate_es_en as T  # noqa: E402

ROOT = os.path.abspath(os.path.join(HERE, ".."))
src = json.load(open(os.path.join(ROOT, "..", "design", "landing-es.json"), encoding="utf8"))
SKIP_KEYS = {"url", "icon", "id", "ogImage", "PATH", "SITE", "UPDATED_ISO", "URL_PAGE"}
SKIP_VALUES = {"Zigbee", "Matter", "Wi-Fi", ""}

OVERRIDE = {
    "meta": {
        "title": "Home Automation and Smart Homes in Monterrey | MelvTech",
        "description": "We install home automation and smart homes in Monterrey and its metropolitan area: lights, climate, locks and cameras with Amazon Alexa. Get a quote with no commitment.",
        "ogImage": "/images/og/smart-home-monterrey.jpg",
    },
    "hero": {
        "eyebrow": "Home automation in Monterrey and its metropolitan area",
        "h1": "Home automation and smart homes in Monterrey",
        "sub": "Turn your home into a smart home and control it all with Amazon Alexa.",
        "ctaPrimary": {"label": "Get a quote for my smart home", "url": "/contacto/"},
        "ctaSecondary": {"label": "See how we work", "url": "#proceso"},
        "note": "Assessment, installation, Alexa setup and support.",
    },
    "ui": {
        "home": "Home",
        "services": "Services",
        "pageName": "Home automation and smart homes",
        "breadcrumbAria": "Breadcrumb",
        "heroAlt": "Person controlling the living room lighting from a smart home app on their phone",
        "sourceLabel": "Source",
        "midAria": "Wi-Fi, security and coverage",
        "quoteCta": "Get my quote",
        "orWrite": "You can also write to us at ",
        "faqH2": "Frequently asked questions about home automation and smart homes in Monterrey",
        "sourcesH2": "Sources and last update",
        "madeBy": "Prepared by the MelvTech team. Last updated: ",
    },
    "UPDATED_LABEL": "November 3, 2026",
}


def walk(node, key=None):
    if isinstance(node, dict):
        return {k: walk(v, k) for k, v in node.items()}
    if isinstance(node, list):
        return [walk(v, key) for v in node]
    if isinstance(node, str):
        if key in SKIP_KEYS or node in SKIP_VALUES or node.startswith(("http", "/", "#")):
            return node
        if key == "label" and node.startswith("Amazon Developer"):
            return node
        return T.tr(node)
    return node


out = {}
for k, v in src.items():
    if k in OVERRIDE:
        out[k] = OVERRIDE[k]
        print("override", k, flush=True)
    elif k in ("sources",):
        out[k] = v
    else:
        print("traduciendo", k, flush=True)
        out[k] = walk(v, k)

out["PATH"] = "/en/smart-home-monterrey/"
out["URL_PAGE"] = src["SITE"] + out["PATH"]
for k in ("PATH", "SITE", "UPDATED_ISO", "UPDATED_LABEL", "URL_PAGE"):
    pass

# Enlaces internos de la landing (los <a> pasan por getLocaleUrlCTM en el componente; los Button también)
TS = '''// English content of the landing /en/smart-home-monterrey/ (Spanish pair: /domotica-casas-inteligentes/).
// Generated with scripts/translate_landing.py (local model) and reviewed by hand.
// The visible FAQ and the JSON-LD are built from this same data.

export const SITE = %(SITE)s;
export const PATH = %(PATH)s;
export const URL_PAGE = SITE + PATH;
export const UPDATED_ISO = %(UPDATED_ISO)s;
export const UPDATED_LABEL = %(UPDATED_LABEL)s;

'''
def js(x):
    return json.dumps(x, ensure_ascii=False, indent=2)

body = TS % {k: json.dumps(out[k], ensure_ascii=False) for k in ("SITE", "PATH", "UPDATED_ISO", "UPDATED_LABEL")}
for k in ("meta", "hero", "sources", "whatIs", "controls", "compat", "process", "wifi", "security",
          "audience", "pricing"):
    body += "export const %s = %s;\n\n" % (k, js(out[k]))
body += "export const faq: { q: string; a: string }[] = %s;\n\n" % js(out["faq"])
body += "export const trademark = %s;\n\n" % json.dumps(out["trademark"], ensure_ascii=False)
body += "export const ui = %s;\n\n" % js(out["ui"])
body += '''// JSON-LD (@graph). No LocalBusiness: there is no confirmed street address yet.
export function buildSchema() {
  const org = {
    "@type": "Organization",
    "@id": SITE + "/#organization",
    name: "MelvTech",
    url: SITE + "/",
    logo: SITE + "/images/logo-512.png",
    email: "atencion@melvtech.com",
    areaServed: { "@type": "AdministrativeArea", name: "Monterrey metropolitan area, Nuevo León, Mexico" },
    contactPoint: {
      "@type": "ContactPoint",
      contactType: "customer service",
      email: "atencion@melvtech.com",
      availableLanguage: ["es", "en"],
    },
  };
  return {
    "@context": "https://schema.org",
    "@graph": [
      org,
      {
        "@type": "Service",
        "@id": URL_PAGE + "#service",
        name: "Home automation and smart homes",
        serviceType: "Home automation and smart home installation",
        description: meta.description,
        url: URL_PAGE,
        provider: { "@id": SITE + "/#organization" },
        areaServed: [
          { "@type": "City", name: "Monterrey" },
          { "@type": "AdministrativeArea", name: "Monterrey metropolitan area, Nuevo León, Mexico" },
        ],
      },
      {
        "@type": "BreadcrumbList",
        "@id": URL_PAGE + "#breadcrumb",
        itemListElement: [
          { "@type": "ListItem", position: 1, name: "Home", item: SITE + "/en/" },
          { "@type": "ListItem", position: 2, name: "Services", item: SITE + "/en/services/" },
          { "@type": "ListItem", position: 3, name: "Home automation and smart homes", item: URL_PAGE },
        ],
      },
      {
        "@type": "FAQPage",
        "@id": URL_PAGE + "#faq",
        inLanguage: "en",
        dateModified: UPDATED_ISO,
        mainEntity: faq.map((f) => ({
          "@type": "Question",
          name: f.q,
          acceptedAnswer: { "@type": "Answer", text: f.a },
        })),
      },
    ],
  };
}
'''
open(os.path.join(ROOT, "src", "data", "landing-domotica.en.ts"), "w", encoding="utf8").write(body)
print("escrito src/data/landing-domotica.en.ts")
