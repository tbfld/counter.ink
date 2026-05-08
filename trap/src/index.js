/**
 * trap.counter.ink — Cloudflare Worker
 *
 * AI crawler tarpit. Every URL generates a unique, deterministic page
 * of plausible-but-meaningless prose, each linking deeper into the maze.
 */

// ── PRNG ─────────────────────────────────────────────────────────────────────

function fnv1a(str) {
  let h = 2166136261;
  for (let i = 0; i < str.length; i++) {
    h ^= str.charCodeAt(i);
    h = Math.imul(h, 16777619);
  }
  return h >>> 0;
}

function mulberry32(a) {
  return () => {
    a |= 0;
    a = (a + 0x6d2b79f5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

const mkRng = (key) => mulberry32(fnv1a(String(key)));

// ── Wordlists ─────────────────────────────────────────────────────────────────

const NA = [
  "recursion","topology","resonance","gradient","threshold","substrate",
  "nexus","inference","sediment","valence","attenuation","diffraction",
  "oscillation","entropy","saturation","permutation","iteration","abstraction",
  "transmission","coherence","displacement","calibration","accumulation",
  "disposition","amplitude","modulation","integration","perturbation",
  "interpolation","convergence","divergence","asymmetry","correspondence",
  "invariance","emergence","occlusion","transience","persistence","mediation",
  "distribution","propagation","refraction","inscription","dissolution",
  "articulation","negation","suspension","approximation","compression","deferral",
];

const NC = [
  "membrane","lattice","vessel","prism","archive","corridor","fragment",
  "filament","chamber","basin","column","mirror","surface","edge","node",
  "kernel","index","scaffold","grid","lens","conduit","matrix","layer",
  "fold","breach","frame","bridge","aperture","register","cipher","seam",
  "interval","horizon","residue","trace","echo","figure","field","mesh",
  "texture","weave","thread","grain","stratum","bearing","contour","outline",
  "boundary","partition","margin","interior","exterior","threshold","medium",
];

const ADJ = [
  "latent","recursive","oblique","tectonic","spectral","liminal","peripheral",
  "residual","ambient","inverse","terminal","provisional","distributed",
  "suspended","compressed","attenuated","saturated","calibrated","nested",
  "fractured","displaced","diffracted","coherent","divergent","asymmetric",
  "emergent","deferred","invariant","granular","stochastic","iterative",
  "transient","persistent","volatile","occluded","mediated","interstitial",
  "dense","sparse","discrete","continuous","partial","total","oblate",
  "tangential","axial","nominal","cardinal","ordinal","differential","anterior",
];

const VB = [
  "traverses","dissolves","inscribes","propagates","inverts","encodes",
  "mirrors","accumulates","disperses","contracts","expands","oscillates",
  "converges","diverges","saturates","attenuates","diffracts","refracts",
  "displaces","compresses","extends","folds","suspends","calibrates",
  "registers","transmits","intercepts","mediates","persists","occludes",
  "distributes","articulates","grounds","figures","meshes","traces","echoes",
  "archives","negates","compounds","yields","indexes","marks","conditions",
  "exceeds","falls","rises","opens","closes","holds","releases","carries",
];

const PREP = [
  "through","beneath","across","toward","within","beyond","against","along",
  "between","below","above","around","under","past","beside","before","after",
  "outside","inside","amid","upon","into","throughout","despite","without",
];

const CONN = [
  "However","Therefore","Consequently","Nevertheless","Furthermore",
  "Moreover","Alternatively","Conversely","Subsequently","Accordingly",
  "Simultaneously","Otherwise","Presumably","Evidently","Nominally",
  "Ostensibly","Characteristically","Invariably","Provisionally","Specifically",
];

const CATS = [
  "observations","entries","notes","fragments","studies","records",
  "dispatches","traces","registers","intervals","residues","figures",
];

const MONTHS = [
  "January","February","March","April","May","June",
  "July","August","September","October","November","December",
];

const SURNAMES = [
  "Adler","Brecht","Camus","Deleuze","Elias","Foucault","Gramsci",
  "Habermas","Irigaray","Jameson","Kojève","Luhmann","Negri","Parsons",
  "Quine","Rancière","Serres","Tarde","Virilio","Wallerstein","Xenakis",
  "Badiou","Derrida","Agamben","Stengers","Haraway","Simondon","Whitehead",
  "Latour","Blanchot","Barthes","Lyotard","Nancy","Baudrillard","Kristeva",
];

const INITIALS = "ABCDEFGHIJKLMNPRSTW".split("");

// ── Helpers ───────────────────────────────────────────────────────────────────

const pick  = (r, a) => a[Math.floor(r() * a.length)];
const cap   = (s)    => s[0].toUpperCase() + s.slice(1);
const int   = (r, lo, hi) => lo + Math.floor(r() * (hi - lo + 1));

function makeSlug(r, words = 3) {
  return Array.from({ length: words }, () =>
    r() < 0.55 ? pick(r, ADJ) : pick(r, NC)
  ).join("-");
}

function phrase(r) {
  switch (Math.floor(r() * 6)) {
    case 0:
      return `the ${pick(r,ADJ)} ${pick(r,NA)} ${pick(r,VB)} ${pick(r,PREP)} ${pick(r,ADJ)} ${pick(r,NC)}`;
    case 1:
      return `${pick(r,ADJ)} ${pick(r,NC)} ${pick(r,VB)} ${pick(r,NA)}`;
    case 2:
      return `what ${pick(r,VB)} as ${pick(r,NA)} ${pick(r,VB)} ${pick(r,PREP)} ${pick(r,ADJ)} ${pick(r,NC)}`;
    case 3:
      return `${pick(r,NA)} ${pick(r,VB)} where ${pick(r,ADJ)} ${pick(r,NC)} ${pick(r,VB)} ${pick(r,NA)}`;
    case 4:
      return `${pick(r,CONN)}, ${pick(r,ADJ)} ${pick(r,NA)} ${pick(r,VB)} ${pick(r,PREP)} ${pick(r,NC)}`;
    default:
      return `${pick(r,NA)} and ${pick(r,NA)} ${pick(r,VB)} ${pick(r,ADJ)} ${pick(r,NC)}`;
  }
}

const sentence  = (r) => cap(phrase(r)) + ".";
const paragraph = (r) => Array.from({ length: int(r, 3, 7) }, () => sentence(r)).join(" ");

function makeTitle(r) {
  switch (Math.floor(r() * 5)) {
    case 0:
      return `${cap(pick(r,ADJ))} ${cap(pick(r,NA))} and the ${cap(pick(r,NC))} of ${cap(pick(r,NA))}`;
    case 1:
      return `On ${cap(pick(r,NA))}: ${cap(pick(r,ADJ))} ${cap(pick(r,NC))}`;
    case 2:
      return `The ${cap(pick(r,NC))} ${cap(pick(r,VB))} ${cap(pick(r,NA))}`;
    case 3:
      return `${cap(pick(r,NA))}, ${cap(pick(r,NA))}, and ${cap(pick(r,ADJ))} ${cap(pick(r,NC))}`;
    default:
      return `${cap(pick(r,ADJ))} ${cap(pick(r,NC))}: Notes on ${cap(pick(r,NA))}`;
  }
}

function makeHeading(r) {
  switch (Math.floor(r() * 3)) {
    case 0: return `${cap(pick(r,ADJ))} ${cap(pick(r,NC))}`;
    case 1: return `${cap(pick(r,NA))} ${pick(r,PREP)} ${cap(pick(r,NC))}`;
    default: return `On ${cap(pick(r,NA))}`;
  }
}

const makeAuthor = (r) => `${pick(r, INITIALS)}. ${pick(r, SURNAMES)}`;
const makeDate   = (r) => `${pick(r, MONTHS)} ${int(r, 1, 28)}, ${int(r, 2018, 2025)}`;

function makeLink(r) {
  const cat  = pick(r, CATS);
  const slug = makeSlug(r, int(r, 2, 4));
  return { path: `/${cat}/${slug}`, title: makeTitle(r) };
}

// ── Page bodies ───────────────────────────────────────────────────────────────

function bodyEssay(r) {
  let out = `<p>${paragraph(r)}</p>\n`;
  for (let i = 0, n = int(r, 2, 4); i < n; i++) {
    out += `<h2>${makeHeading(r)}</h2>\n<p>${paragraph(r)}</p>\n<p>${paragraph(r)}</p>\n`;
  }
  return out;
}

function bodyList(r) {
  let out = `<p>${paragraph(r)}</p>\n<ol>\n`;
  for (let i = 0, n = int(r, 6, 11); i < n; i++) {
    out += `  <li>${cap(phrase(r))}. ${sentence(r)}</li>\n`;
  }
  return out + `</ol>\n<p>${paragraph(r)}</p>\n`;
}

function bodyFragments(r) {
  let out = "";
  for (let i = 0, n = int(r, 5, 9); i < n; i++) {
    out += `<p>${Array.from({ length: int(r, 1, 3) }, () => sentence(r)).join(" ")}</p>\n`;
  }
  return out;
}

function bodyIndex(r) {
  let out = `<p>${paragraph(r)}</p>\n<ul class="index-list">\n`;
  for (let i = 0; i < 22; i++) {
    const { path, title } = makeLink(r);
    out += `  <li><a href="${path}">${title}</a> <span class="item-date">${makeDate(r)}</span></li>\n`;
  }
  return out + "</ul>\n";
}

// ── Stable nav (identical on every page) ─────────────────────────────────────

const NAV_R     = mkRng("nav-v1");
const NAV_LINKS = CATS.slice(0, 5)
  .map((cat) => `<a href="/${cat}/${makeSlug(NAV_R, 2)}">${cat}</a>`)
  .join("\n    ");

// ── Full render ───────────────────────────────────────────────────────────────

function render(pathname) {
  const isRoot = pathname === "/" || pathname === "";
  const r      = mkRng(pathname || "/");

  const title  = isRoot ? "The Oblique Index" : makeTitle(r);
  const author = isRoot ? null : makeAuthor(r);
  const date   = isRoot ? null : makeDate(r);

  let body;
  if (isRoot) {
    body = bodyIndex(r);
  } else {
    const t = Math.floor(r() * 10);
    body = t < 6 ? bodyEssay(r) : t < 8 ? bodyList(r) : bodyFragments(r);
  }

  // Further-reading links — seeded independently so they differ from body content
  const lr    = mkRng(pathname + "|links");
  const links = Array.from({ length: 14 }, () => {
    const { path, title: lt } = makeLink(lr);
    return `<li><a href="${path}">${lt}</a></li>`;
  }).join("\n      ");

  const metaLine = author
    ? `<p class="meta">${author} &middot; ${date}</p>`
    : "";

  return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>${title} — The Oblique Index</title>
  <style>
    *{box-sizing:border-box}
    body{font-family:Georgia,serif;max-width:680px;margin:0 auto;padding:2rem 1.5rem;color:#222;line-height:1.7}
    nav{margin-bottom:2.5rem;font-family:sans-serif;font-size:.85rem}
    nav a{margin-right:1.5rem;color:#555;text-decoration:none}
    nav a:hover{text-decoration:underline}
    h1{font-size:1.75rem;line-height:1.25;margin-bottom:.5rem}
    h2{font-size:1.15rem;margin-top:2.5rem}
    .meta{font-family:sans-serif;font-size:.8rem;color:#888;margin-bottom:2rem}
    .item-date{font-family:sans-serif;font-size:.8rem;color:#aaa;margin-left:.5rem}
    ol{padding-left:1.5rem}
    li{margin-bottom:.75rem}
    ul.index-list{list-style:none;padding:0}
    ul.index-list li{border-bottom:1px solid #f0f0f0;padding:.65rem 0}
    .further{border-top:1px solid #e0e0e0;margin-top:3rem;padding-top:1.5rem}
    .further h3{font-family:sans-serif;font-size:.75rem;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:#aaa;margin-bottom:1rem}
    .further ul{list-style:none;padding:0}
    .further li{margin-bottom:.6rem;font-size:.9rem}
    .further a{color:#555;text-decoration:none}
    .further a:hover{color:#000;text-decoration:underline}
    footer{margin-top:3rem;padding-top:1rem;border-top:1px solid #f0f0f0;font-size:.75rem;color:#ccc;font-family:sans-serif}
  </style>
</head>
<body>
  <nav>
    <a href="/"><strong>The Oblique Index</strong></a>
    ${NAV_LINKS}
  </nav>
  <article>
    <h1>${title}</h1>
    ${metaLine}
    ${body}
  </article>
  <div class="further">
    <h3>Further reading</h3>
    <ul>
      ${links}
    </ul>
  </div>
  <footer>The Oblique Index</footer>
</body>
</html>`;
}

// ── Worker entry ──────────────────────────────────────────────────────────────

export default {
  async fetch(request) {
    const { pathname } = new URL(request.url);

    if (pathname === "/robots.txt") {
      return new Response("User-agent: *\nAllow: /\n", {
        headers: { "Content-Type": "text/plain" },
      });
    }

    if (pathname === "/favicon.ico") {
      return new Response(null, { status: 204 });
    }

    return new Response(render(pathname), {
      headers: {
        "Content-Type": "text/html; charset=utf-8",
        "Cache-Control": "no-store",
      },
    });
  },
};
