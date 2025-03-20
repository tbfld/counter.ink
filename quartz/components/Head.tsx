import { i18n } from "../i18n"
import { FullSlug, joinSegments, pathToRoot } from "../util/path"
import { CSSResourceToStyleElement, JSResourceToScriptElement } from "../util/resources"
import { googleFontHref } from "../util/theme"
import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import satori, { SatoriOptions } from "satori"
import fs from "fs"
import sharp from "sharp"
import { ImageOptions, SocialImageOptions, getSatoriFont, defaultImage } from "../util/og"
import { unescapeHTML } from "../util/escape"

async function generateSocialImage(
  { cfg, description, fileName, fontsPromise, title, fileData }: ImageOptions,
  userOpts: SocialImageOptions,
  imageDir: string,
) {
  const fonts = await fontsPromise
  const { width, height } = userOpts

  const imageComponent = userOpts.imageStructure(cfg, userOpts, title, description, fonts, fileData)

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
      fullOptions = typeof cfg.generateSocialImages !== "boolean" 
        ? { ...defaultOptions, ...cfg.generateSocialImages }
        : defaultOptions
    }

    if (!fontsPromise && cfg.generateSocialImages) {
      fontsPromise = getSatoriFont(cfg.theme.typography.header, cfg.theme.typography.body)
    }

    const slug = fileData.filePath
    const fileName = slug?.replaceAll("/", "-")
    const fdDescription = fileData.description?.trim() ?? i18n(cfg.locale).propertyDefaults.description
    const titleSuffix = cfg.pageTitleSuffix ?? ""
    const title = (fileData.frontmatter?.title ?? i18n(cfg.locale).propertyDefaults.title) + titleSuffix
    let description = fileData.frontmatter?.socialDescription || fileData.frontmatter?.description || unescapeHTML(fdDescription)

    const fileDir = joinSegments(ctx.argv.output, "static", "social-images")
    if (cfg.generateSocialImages) {
      if (!fs.existsSync(fileDir)) {
        fs.mkdirSync(fileDir, { recursive: true })
      }
      if (fileName) {
        generateSocialImage({ title, description, fileName, fileDir, fileExt: extension, fontsPromise, cfg, fileData }, fullOptions, fileDir)
      }
    }

    const { css, js } = externalResources
    const url = new URL(`https://${cfg.baseUrl ?? "example.com"}`)
    const baseDir = fileData.slug === "404" ? url.pathname as FullSlug : pathToRoot(fileData.slug!)
    const iconPath = joinSegments(baseDir, "static/icon.png")

    return (
      <head>
        <title>{title}</title>
        <meta charSet="utf-8" />
        {cfg.theme.cdnCaching && cfg.theme.fontOrigin === "googleFonts" && (
          <>
            <link rel="preconnect" href="https://fonts.googleapis.com" />
            <link rel="preconnect" href="https://fonts.gstatic.com" />
            <link rel="stylesheet" href={googleFontHref(cfg.theme)} />
          </>
        )}
        <link rel="preconnect" href="https://cdnjs.cloudflare.com" crossOrigin={"anonymous"} />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <meta name="generator" content="Quartz" />
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
