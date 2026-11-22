import config from "../../../.astro/config.generated.json";
import { useTranslations } from "@/lib/utils/i18nUtils.ts";

/**
 * Enlace de WhatsApp con el mensaje inicial en el idioma de la página.
 * Devuelve `url` vacío si no hay número configurado en config.toml
 * (settings.contactInfo.whatsapp).
 */
export async function getWhatsApp(locale: string) {
  const t = await useTranslations(locale);
  const number = String(config.settings.contactInfo.whatsapp || "").replace(
    /\D/g,
    "",
  );
  return {
    label: t("whatsapp.label") as string,
    url: number
      ? `https://wa.me/${number}?text=${encodeURIComponent(t("whatsapp.message"))}`
      : "",
  };
}

/**
 * Páginas donde NO se muestra el botón flotante de WhatsApp (rutas sin el
 * prefijo de idioma):
 *  - Landings: tienen una sola llamada a la acción y el botón flotante
 *    competiría con ella. Al crear una landing nueva, agrégala aquí
 *    (en español e inglés si el slug cambia).
 *  - Contacto: ya ofrece formulario y botón a WhatsApp.
 *  - Páginas legales.
 */
const HIDE_FLOATING_WHATSAPP = [
  "/domotica-casas-inteligentes",
  "/smart-home-monterrey",
  "/contacto",
  "/privacy-policy",
  "/terms-conditions",
];

export function showFloatingWhatsApp(pathname: string) {
  const path =
    pathname.replace(/^\/en(?=\/|$)/, "").replace(/\/+$/, "") || "/";
  return !HIDE_FLOATING_WHATSAPP.includes(path);
}

export function isContactPage(pathname: string) {
  return /^(\/en)?\/contacto\/?$/.test(pathname);
}
