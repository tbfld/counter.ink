import { FullSlug, resolveRelative } from "../../util/path"
import { QuartzEmitterPlugin } from "../types"
import { write } from "./helpers"

// TB ADDED 2026-11-16: redirect stubs for old tag URLs that Google still
// requests (Search Console "Not found (404)"). Tags were reorganised into
// hierarchies (e.g. /tags/fashion -> /tags/culture/fashion) and an older
// scheme used /tag_law-style paths. Same mechanism as AliasRedirects: a tiny
// HTML page with a canonical link and a meta refresh. Add pairs here as needed.
const REDIRECTS: Record<string, string> = {
  "tag/tag_media": "tags/media",
  "tag_design": "tags/design",
  "tag_education": "tags/education",
  "tag_law": "tags/governance/law",
  "tags/academia": "tags/education/academia",
  "tags/advertising": "tags/design/advertising",
  "tags/africa": "tags/international/africa",
  "tags/anthropology": "tags/culture/anthropology",
  "tags/antifascism": "tags/politics/antifascism",
  "tags/capitalism": "tags/economics/capitalism",
  "tags/cartoons": "tags/art/cartoons",
  "tags/corporation": "tags/governance/corporation",
  "tags/corruption": "tags/governance/corruption",
  "tags/covid": "tags/health/covid",
  "tags/data": "tags/information/data",
  "tags/democracy": "tags/politics/democracy",
  "tags/democrats": "tags/politics/democrats",
  "tags/disinformation": "tags/politics/disinformation",
  "tags/elections": "tags/politics/elections",
  "tags/email": "tags/media/email",
  "tags/fashion": "tags/culture/fashion",
  "tags/film": "tags/art/film",
  "tags/genre": "tags/language/genre",
  "tags/labor": "tags/economics/labor",
  "tags/magazines": "tags/media/publishing",
  "tags/medicine": "tags/health/medicine",
  "tags/ml": "tags/technology/ai",
  "tags/policy": "tags/governance/policy",
  "tags/protocol": "tags",
  "tags/race": "tags/culture/race",
  "tags/satire": "tags/language/satire",
  "tags/social-commentary": "tags",
  "tags/social-media": "tags/media/social",
  "tags/theater": "tags/art/theater",
  "tags/uk": "tags/international/uk",
  "tags/visual-culture": "tags/art/visual-culture",
}

export const TagRedirects: QuartzEmitterPlugin = () => ({
  name: "TagRedirects",
  async *emit(ctx) {
    for (const [from, to] of Object.entries(REDIRECTS)) {
      const redirUrl = resolveRelative(from as FullSlug, to as FullSlug)
      yield write({
        ctx,
        content: `<!DOCTYPE html>
<html lang="en-us">
<head>
<title>${from}</title>
<link rel="canonical" href="${redirUrl}">
<meta name="robots" content="noindex">
<meta charset="utf-8">
<meta http-equiv="refresh" content="0; url=${redirUrl}">
</head>
</html>
`,
        slug: from as FullSlug,
        ext: ".html",
      })
    }
  },
  async *partialEmit() {},
})
