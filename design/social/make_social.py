"""Generador de artes de redes sociales de MelvTech.

Uso (desde la raíz del proyecto):
    python design/social/make_social.py            # todo
    python design/social/make_social.py S1-M       # un solo post
    python design/social/make_social.py brand      # avatar, portada FB y destacadas

Lee design/social/calendario.json y escribe en design/social/out/.
Requiere Pillow. Tipografía: Sora (OFL), design/social/fonts/Sora-Variable.ttf.
"""
import json
import os
import sys

from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
FONT = os.path.join(HERE, "fonts", "Sora-Variable.ttf")
LOGO = Image.open(os.path.join(HERE, "logo_bolt.png")).convert("RGBA")

K = 2  # supersampling

DARK = (4, 13, 67)       # #040D43
NAVY = (10, 22, 94)      # #0A165E
BLUE = (43, 77, 255)     # #2B4DFF
SOFT = (143, 162, 255)   # #8FA2FF
LIGHT = (206, 208, 223)  # #CED0DF
PAPER = (245, 246, 247)  # #F5F6F7
GREY = (142, 147, 181)   # #8E93B5
WHITE = (255, 255, 255)

MX = 72          # margen
W, H = 1080, 1350


def font(size, weight):
    f = ImageFont.truetype(FONT, int(size * K))
    f.set_variation_by_axes([weight])
    return f


def wrap(d, text, fnt, max_w):
    lines, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if d.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            lines.append(cur)
            cur = w
    lines.append(cur)
    return lines


def glow(base, cx, cy, r, strength):
    g = Image.new("RGB", base.size, (0, 0, 0))
    ImageDraw.Draw(g).ellipse((cx - r, cy - r, cx + r, cy + r), fill=BLUE)
    g = g.filter(ImageFilter.GaussianBlur(r * 0.42)).point(lambda v: int(v * strength))
    return ImageChops.add(base, g)


def bg_dark(w, h):
    base = Image.new("RGB", (w * K, h * K), DARK)
    grad = Image.linear_gradient("L").resize((w * K, h * K))
    base = Image.composite(Image.new("RGB", base.size, NAVY), base, grad.point(lambda v: int(v * 0.85)))
    base = glow(base, int(w * 0.85 * K), int(h * 0.18 * K), int(min(w, h) * 0.36 * K), 0.55)
    base = glow(base, int(w * 0.04 * K), int(h * 1.0 * K), int(min(w, h) * 0.30 * K), 0.30)
    return base.convert("RGBA")


def bg_light(w, h):
    return Image.new("RGBA", (w * K, h * K), PAPER)


def header(img, d, dark=True, y=64):
    lh = 52 * K
    lw = int(LOGO.width * lh / LOGO.height)
    img.alpha_composite(LOGO.resize((lw, lh), Image.LANCZOS), (MX * K, y * K))
    d.text((MX * K + lw + 16 * K, y * K + lh // 2), "MelvTech", font=font(34, 700),
           fill=WHITE if dark else NAVY, anchor="lm")


def footer_bar(d, w=W, h=H):
    d.rectangle((0, (h - 14) * K, w * K, h * K), fill=BLUE)


def counter(d, i, n, dark):
    if n > 1:
        d.text(((W - MX) * K, 90 * K), f"{i}/{n}", font=font(28, 500), fill=GREY if not dark else LIGHT, anchor="rm")


def text_block(d, text, fnt, x, y, max_w, fill, lead):
    for ln in wrap(d, text, fnt, max_w * K):
        d.text((x * K, y * K), ln, font=fnt, fill=fill, anchor="la")
        y += lead
    return y


def fit_lines(d, text, weight, max_w, max_lines, start, floor):
    """Mayor tamaño (start..floor) con el que el texto cabe en max_lines líneas."""
    size = start
    while size >= floor:
        f = font(size, weight)
        ls = wrap(d, text, f, max_w * K)
        if len(ls) <= max_lines:
            return f, size, ls
        size -= 4
    f = font(floor, weight)
    return f, floor, wrap(d, text, f, max_w * K)


# ---------------------------------------------------------------- plantillas
def s_cover(s, i, n):
    img = bg_dark(W, H)
    d = ImageDraw.Draw(img)
    header(img, d, True)
    counter(d, i, n, True)
    f, size, lines = fit_lines(d, s["text"], 800, W - 2 * MX, 5, 124, 84)
    lead = int(size * 1.14)
    y = (H - len(lines) * lead) // 2 - 40
    d.rounded_rectangle((MX * K, (y - 56) * K, (MX + 96) * K, (y - 48) * K), radius=4 * K, fill=BLUE)
    for ln in lines:
        d.text((MX * K, y * K), ln, font=f, fill=WHITE, anchor="la")
        y += lead
    d.text((MX * K, (H - 110) * K), "Desliza", font=font(40, 700), fill=SOFT, anchor="ls")
    ax = MX + d.textlength("Desliza", font=font(40, 700)) / K + 24
    ay = H - 124
    d.line((ax * K, ay * K, (ax + 56) * K, ay * K), fill=SOFT, width=6 * K)
    d.line(((ax + 36) * K, (ay - 20) * K, (ax + 56) * K, ay * K, (ax + 36) * K, (ay + 20) * K), fill=SOFT, width=6 * K, joint="curve")
    footer_bar(d)
    return img


def s_point(s, i, n):
    img = bg_light(W, H)
    d = ImageDraw.Draw(img)
    header(img, d, False)
    counter(d, i, n, False)
    f, size, lines = fit_lines(d, s["title"], 800, W - 2 * MX, 4, 104, 72)
    lead = int(size * 1.14)
    top = 360  # ancla fija: el texto no salta de una slide a otra al deslizar el carrusel
    d.text((MX * K, (top + 34) * K), s["kicker"].upper(), font=font(34, 700), fill=BLUE, anchor="ls")
    y = top + 80
    for ln in lines:
        d.text((MX * K, y * K), ln, font=f, fill=NAVY, anchor="la")
        y += lead
    d.rounded_rectangle((MX * K, (y + 18) * K, (MX + 96) * K, (y + 26) * K), radius=4 * K, fill=BLUE)
    text_block(d, s["body"], font(48, 500), MX, y + 70, W - 2 * MX, (58, 64, 110), 70)
    footer_bar(d)
    return img


def s_stat(s, i, n):
    img = bg_dark(W, H)
    d = ImageDraw.Draw(img)
    header(img, d, True)
    counter(d, i, n, True)
    max_w = (W - 2 * MX) * K
    size = 330
    while size > 120 and d.textlength(s["stat"], font=font(size, 800)) > max_w:
        size -= 6
    fs = font(size, 800)
    x = MX * K
    cap = int(size * 0.73)
    tl = wrap(d, s["text"], font(52, 500), max_w)
    sl = wrap(d, s["source"], font(28, 400), max_w)
    total = cap + 58 + 8 + 42 + len(tl) * 72 + 24 + len(sl) * 40
    top = 150 + (H - 14 - 150 - total) // 2
    base = (top + cap) * K
    ry = top + cap
    for ch in s["stat"]:
        d.text((x, base), ch, font=fs, fill=SOFT if ch in "%$" else WHITE, anchor="ls")
        x += d.textlength(ch, font=fs) + (10 * K if ch == "$" else 0)
    d.rounded_rectangle((MX * K, (ry + 58) * K, (MX + 96) * K, (ry + 66) * K), radius=4 * K, fill=BLUE)
    y = text_block(d, s["text"], font(52, 500), MX, ry + 108, W - 2 * MX, LIGHT, 72)
    src = font(28, 400)
    sy = y + 24
    for ln in wrap(d, s["source"], src, max_w):
        d.text((MX * K, sy * K), ln, font=src, fill=GREY, anchor="la")
        sy += 40
    footer_bar(d)
    return img


def s_list(s, i, n):
    img = bg_light(W, H)
    d = ImageDraw.Draw(img)
    header(img, d, False)
    counter(d, i, n, False)
    f, size, lines = fit_lines(d, s["title"], 800, W - 2 * MX, 3, 84, 60)
    lead = int(size * 1.14)
    total = len(lines) * lead + 40 + len(s["items"]) * 128
    y = 150 + (H - 14 - 150 - total) // 2
    for ln in lines:
        d.text((MX * K, y * K), ln, font=f, fill=NAVY, anchor="la")
        y += lead
    y += 40
    fi = font(46, 500)
    for k, item in enumerate(s["items"], 1):
        d.ellipse((MX * K, y * K, (MX + 72) * K, (y + 72) * K), fill=BLUE)
        d.text(((MX + 36) * K, (y + 36) * K), str(k), font=font(38, 800), fill=WHITE, anchor="mm")
        ls = wrap(d, item, fi, (W - 2 * MX - 112) * K)
        ty = y + 36 - (len(ls) * 58) // 2
        for ln in ls:
            d.text(((MX + 104) * K, ty * K), ln, font=fi, fill=(58, 64, 110), anchor="la")
            ty += 58
        y += 128
    footer_bar(d)
    return img


def pill(d, x, y, text, fnt):
    tw = d.textlength(text, font=fnt)
    pad = 40 * K
    h = 96 * K
    d.rounded_rectangle((x, y, x + tw + 2 * pad, y + h), radius=h // 2, fill=BLUE)
    d.text((x + pad, y + h // 2), text, font=fnt, fill=WHITE, anchor="lm")


def s_closing(s, i, n):
    img = bg_dark(W, H)
    d = ImageDraw.Draw(img)
    header(img, d, True)
    counter(d, i, n, True)
    f, size, lines = fit_lines(d, s["text"], 800, W - 2 * MX, 4, 96, 64)
    lead = int(size * 1.14)
    total = len(lines) * lead + 56 + 96
    y = 150 + (H - 14 - 150 - total) // 2
    for ln in lines:
        d.text((MX * K, y * K), ln, font=f, fill=WHITE, anchor="la")
        y += lead
    pill(d, MX * K, (y + 56) * K, s["cta"], font(44, 700))
    footer_bar(d)
    return img


def s_brand(s, i, n):
    img = bg_dark(W, H)
    d = ImageDraw.Draw(img)
    # rayo grande + wordmark
    lh = 170 * K
    lw = int(LOGO.width * lh / LOGO.height)
    img.alpha_composite(LOGO.resize((lw, lh), Image.LANCZOS), (MX * K, 190 * K))
    f, size, lines = fit_lines(d, s["title"], 800, W - 2 * MX, 3, 140, 88)
    lead = int(size * 1.12)
    y = 410
    for ln in lines:
        d.text((MX * K, y * K), ln, font=f, fill=WHITE, anchor="la")
        y += lead
    d.rounded_rectangle((MX * K, (y + 10) * K, (MX + 96) * K, (y + 18) * K), radius=4 * K, fill=BLUE)
    y = text_block(d, s["text"], font(52, 500), MX, y + 56, W - 2 * MX, LIGHT, 72)
    if s.get("cta"):
        pill(d, MX * K, (y + 40) * K, s["cta"], font(44, 700))
    footer_bar(d)
    return img


KINDS = {"cover": s_cover, "point": s_point, "stat": s_stat, "list": s_list,
         "closing": s_closing, "brand": s_brand}


def save(img, path, size=None):
    out = img.convert("RGB")
    out = out.resize(size or (W, H), Image.LANCZOS)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    out.save(path, "PNG", optimize=True)
    return path


def build_posts(only=None):
    data = json.load(open(os.path.join(HERE, "calendario.json"), encoding="utf8"))
    md = ["# Textos de publicación, mes 1\n",
          "Generado por `design/social/make_social.py` desde `calendario.json`. No editar a mano.\n",
          "UTM: `?utm_source=instagram|facebook&utm_medium=social&utm_campaign=mes1&utm_content=<código>`\n"]
    for p in data["posts"]:
        md.append(f"\n## {p['code']} · {p['day']} semana {p['week']} · {p['title']} ({p['pillar']})\n")
        md.append(f"Slides: {len(p['slides'])}\n")
        md.append("Texto:\n\n" + "\n".join("> " + ln if ln else ">" for ln in p["caption"].split("\n")) + "\n")
        md.append(f"\nEnlace: {p['link']}?utm_source=instagram&utm_medium=social&utm_campaign=mes1&utm_content={p['code']}\n")
        md.append(f"\nHashtags (Instagram): {p['tags']}\n")
        if only and p["code"] != only:
            continue
        n = len(p["slides"])
        for i, s in enumerate(p["slides"], 1):
            path = os.path.join(OUT, "posts", p["code"], f"{p['code']}_{i:02d}.png")
            save(KINDS[s["kind"]](s, i, n), path)
        print(f"{p['code']}: {n} slide(s)")
    open(os.path.join(OUT, "textos-mes1.md"), "w", encoding="utf8").write("".join(md))


# ---------------------------------------------------------------- marca
def avatar():
    base = Image.new("RGBA", (1080 * K, 1080 * K), (255, 255, 255, 255))
    lh = 620 * K
    lw = int(LOGO.width * lh / LOGO.height)
    base.alpha_composite(LOGO.resize((lw, lh), Image.LANCZOS), ((1080 * K - lw) // 2, (1080 * K - lh) // 2))
    return save(base, os.path.join(OUT, "marca", "perfil_1080.png"), (1080, 1080))


def fb_cover():
    w, h = 820, 360
    img = bg_dark(w, h)
    d = ImageDraw.Draw(img)
    lh = 86 * K
    lw = int(LOGO.width * lh / LOGO.height)
    # franja central segura de ~640 px: x de 90 a 730
    x0 = 90
    img.alpha_composite(LOGO.resize((lw, lh), Image.LANCZOS), (x0 * K, 98 * K))
    d.text(((x0 + 80) * K, 141 * K), "MelvTech", font=font(60, 800), fill=WHITE, anchor="lm")
    d.text((x0 * K, 232 * K), "Domótica y seguridad en Monterrey", font=font(33, 700), fill=LIGHT, anchor="ls")
    d.text((x0 * K, 276 * K), "Casas inteligentes · Alarmas · Videovigilancia · Redes", font=font(21, 500), fill=SOFT, anchor="ls")
    d.rectangle((0, (h - 8) * K, w * K, h * K), fill=BLUE)
    return save(img, os.path.join(OUT, "marca", "portada_facebook_820x360.png"), (w, h))


def highlights():
    items = [("Servicios", "Servicios"), ("Datos NL", "Datos NL"), ("Domótica", "Domótica"),
             ("Empresas", "Empresas"), ("Cotiza", "Cotiza")]
    paths = []
    for name, label in items:
        w, h = 1080, 1920
        img = bg_dark(w, h)
        d = ImageDraw.Draw(img)
        cx, cy = w // 2, h // 2
        d.ellipse(((cx - 330) * K, (cy - 330) * K, (cx + 330) * K, (cy + 330) * K), outline=BLUE, width=14 * K)
        lh = 340 * K
        lw = int(LOGO.width * lh / LOGO.height)
        img.alpha_composite(LOGO.resize((lw, lh), Image.LANCZOS), ((w * K - lw) // 2, (cy - 215) * K))
        d.text((cx * K, (cy + 470) * K), label, font=font(96, 800), fill=WHITE, anchor="mm")
        paths.append(save(img, os.path.join(OUT, "marca", f"destacada_{name.lower().replace(' ', '_')}.png"), (w, h)))
    return paths


def build_brand():
    avatar()
    fb_cover()
    highlights()
    print("marca: perfil, portada FB, 5 destacadas")


if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else None
    os.makedirs(OUT, exist_ok=True)
    if arg == "brand":
        build_brand()
    elif arg:
        build_posts(arg)
    else:
        build_brand()
        build_posts()
