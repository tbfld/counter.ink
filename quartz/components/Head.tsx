import { i18n } from "../i18n"
import { joinSegments } from "../util/path"
import { CSSResourceToStyleElement, JSResourceToScriptElement } from "../util/resources"
import { googleFontHref, googleFontSubsetHref } from "../util/theme"
import { QuartzComponent, QuartzComponentProps, QuartzComponentConstructor } from "./types"
import { unescapeHTML } from "../util/escape"
import { SocialImageOptions, defaultImage, getSatoriFonts } from "../util/og"
import satori, { SatoriOptions } from "satori"
import sharp from "sharp"
import fs from "node:fs"

interface CustomImageOptions {
  cfg: any
  description: string
  fileName: string
  fontsPromise: Promise<SatoriOptions["fonts"]>
  title: string
  fileData: any
}

async function generateSocialImage(
  { cfg, description, fileName, fontsPromise, title, fileData }: CustomImageOptions,
  userOpts: SocialImageOptions,
  imageDir: string,
) {
  const fonts = await fontsPromise
  const { width, height } = userOpts

  const imageComponent = userOpts.imageStructure({
    cfg,
    userOpts,
    title,
    description,
    fonts,
    fileData,
    iconBase64: undefined,
  })

  const svg = await satori(imageComponent, { width, height, fonts })
  const compressed = await sharp(Buffer.from(svg)).webp({ quality: 40 }).toBuffer()

  const filePath = joinSegments(imageDir, `${fileName}.${extension}`)
  fs.writeFileSync(filePath, compressed)
}

const extension = "webp"

const defaultOptions: SocialImageOptions = {
  colorScheme: "lightMode",
  width: 1200,
  height: 630,
  imageStructure: defaultImage,
  excludeRoot: false,
}

export default (() => {
  let fontsPromise: Promise<SatoriOptions["fonts"]>
  let fullOptions: SocialImageOptions

  const Head: QuartzComponent = ({ cfg, fileData, externalResources, ctx }: QuartzComponentProps) => {
    if (!fullOptions) {
      fullOptions = defaultOptions
    }

    if (!fontsPromise) {
      fontsPromise = getSatoriFonts(cfg.theme.typography.header, cfg.theme.typography.body)
    }

    const slug = fileData.filePath
    const fileName = slug?.replaceAll("/", "-")
    const fdDescription = fileData.description?.trim() ?? i18n(cfg.locale).propertyDefaults.description
    const titleSuffix = cfg.pageTitleSuffix ?? ""
    const title = (fileData.frontmatter?.title ?? i18n(cfg.locale).propertyDefaults.title) + titleSuffix
    let description = fileData.frontmatter?.socialDescription || fileData.frontmatter?.description || unescapeHTML(fdDescription)

    const fileDir = joinSegments(ctx.argv.output, "static", "social-images")
    if (fileName) {
      if (!fs.existsSync(fileDir)) {
        fs.mkdirSync(fileDir, { recursive: true })
      }
      generateSocialImage({ title, description, fileName, fontsPromise, cfg, fileData }, fullOptions, fileDir)
    }

    const { css, js } = externalResources

    // Generate Schema.org structured data
    const schemaData = {
      "@context": "https://schema.org",
      "@type": "BlogPosting",
      "headline": fileData.frontmatter?.title ?? title.replace(titleSuffix, ''),
      "description": description,
      "author": {
        "@type": "Person",
        "name": fileData.frontmatter?.author || "ted byfield"
      },
      "datePublished": fileData.dates?.created,
      "dateModified": fileData.dates?.modified || fileData.dates?.created,
      "publisher": {
        "@type": "Organization",
        "name": cfg.pageTitle,
        "url": `https://${cfg.baseUrl}`
      },
      "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": `https://${cfg.baseUrl}/${slug || ''}`
      }
    }

    return (
      <head>
        <title>{title}</title>
        <meta charSet="utf-8" />
        <meta
          httpEquiv="Content-Security-Policy"
          content="default-src 'self'; script-src 'self' 'unsafe-inline' 'unsafe-eval' plausible.io cdnjs.cloudflare.com cdn.jsdelivr.net; style-src 'self' 'unsafe-inline' cdnjs.cloudflare.com cdn.jsdelivr.net; img-src 'self' data:; font-src 'self' cdn.jsdelivr.net; connect-src 'self' plausible.io; base-uri 'self'; form-action 'self';"
        />
        {slug && (
          <script type="application/ld+json">
            {JSON.stringify(schemaData)}
          </script>
        )}
        {cfg.theme.fontOrigin === "local" && (
          <link rel="stylesheet" href="/static/fonts.css" />
        )}
        {cfg.theme.cdnCaching && cfg.theme.fontOrigin === "googleFonts" && (
          <>
            <link rel="preconnect" href="https://fonts.googleapis.com" />
            <link rel="preconnect" href="https://fonts.gstatic.com" />
            <link rel="stylesheet" href={googleFontHref(cfg.theme)} />
            {cfg.theme.typography.title && (
              <link rel="stylesheet" href={googleFontSubsetHref(cfg.theme, cfg.pageTitle)} />
            )}
          </>
        )}
        <link rel="preconnect" href="https://cdnjs.cloudflare.com" crossOrigin="anonymous" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <meta name="generator" content="Quartz" />

        {/* Favicon */}
        <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png" />
        <link rel="icon" type="image/x-icon" href="/favicon.ico" />
        <link rel="shortcut icon" href="/favicon.ico" />

        {css.map((resource) => CSSResourceToStyleElement(resource, true))}
        {js.filter((resource) => resource.loadTime === "beforeDOMReady").map((res) => JSResourceToScriptElement(res, true))}

        {/* Plausible Analytics */}
        <script
          defer
          data-domain="counter.ink"
          src="https://plausible.io/js/script.file-downloads.hash.outbound-links.js"
        ></script>
        <script>
          {`window.plausible = window.plausible || function() { 
            (window.plausible.q = window.plausible.q || []).push(arguments) 
          }`}
        </script>
      </head>
    )
  }

  return Head
}) satisfies QuartzComponentConstructor
