import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"

const config: QuartzConfig = {
  configuration: {
    pageTitle: "ted byfield",
    pageTitleSuffix: " | counter.ink",
    enableSPA: true,
    enablePopovers: true,
    analytics: {
      provider: "plausible",
    },
    locale: "en-US",
    baseUrl: "counter.ink",
    ignorePatterns: ["private", "templates", ".obsidian"],
    defaultDateType: "created",
    theme: {
      fontOrigin: "googleFonts",
      cdnCaching: true,
      typography: {
        header: "Atkinson+Hyperlegible",
        body: "Atkinson+Hyperlegible",
        code: "Inconsolata",
      },
      colors: {
        lightMode: {
          light: "#fafafa",
          lightgray: "#e5e5e5",
          gray: "#b8b8b8",
          darkgray: "#4e4e4e",
          dark: "#2b2b2b",
          secondary: "#434343",
          tertiary: "#9a9a9a",
          highlight: "rgba(155, 155, 155, 0.15)",
          textHighlight: "#e0e0e088",
        },
        darkMode: {
          light: "#161616",
          lightgray: "#393939",
          gray: "#646464",
          darkgray: "#d4d4d4",
          dark: "#ebebeb",
          secondary: "#919191",
          tertiary: "#9a9a9a",
          highlight: "rgba(155, 155, 155, 0.15)",
          textHighlight: "#9a9a9a88",
        },
        ftMode: {
          light: "#f2dfce",
          lightgray: "#e0cab5",
          gray: "#a89079",
          darkgray: "#5c4d3e",
          dark: "#2e2419",
          secondary: "#6b5644",
          tertiary: "#8c7256",
          highlight: "rgba(140, 114, 86, 0.15)",
          textHighlight: "#d4b89688",
        },
        slateMode: {
          light: "#c8dae8",
          lightgray: "#b0c8db",
          gray: "#7a9db8",
          darkgray: "#3d5a72",
          dark: "#1a2d3e",
          secondary: "#4a7a9e",
          tertiary: "#5a8aae",
          highlight: "rgba(74, 122, 158, 0.15)",
          textHighlight: "#8aafcc88",
        },
        sageMode: {
          light: "#d4e0d0",
          lightgray: "#bfcfba",
          gray: "#90ab8b",
          darkgray: "#4a5d47",
          dark: "#252f24",
          secondary: "#6b8566",
          tertiary: "#7d9878",
          highlight: "rgba(107, 133, 102, 0.15)",
          textHighlight: "#a5bd9f88",
        },
        amberMode: {
          light: "#ffe8c0",
          lightgray: "#ffd89a",
          gray: "#ffbc4c",
          darkgray: "#8a6020",
          dark: "#3d2b0f",
          secondary: "#cc9533",
          tertiary: "#e6a845",
          highlight: "rgba(204, 149, 51, 0.15)",
          textHighlight: "#f5ce7888",
        },
      },
    },
  },
  plugins: {
    transformers: [
      Plugin.FrontMatter(),
      Plugin.CreatedModifiedDate({
        priority: ["frontmatter", "git", "filesystem"],
      }),
      Plugin.SyntaxHighlighting({
        theme: {
          light: "github-light",
          dark: "github-dark",
        },
        keepBackground: false,
      }),
      Plugin.ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false }),
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.TableOfContents(),
      Plugin.CrawlLinks({ markdownLinkResolution: "shortest" }),
      Plugin.Description(),
      Plugin.Latex({ renderEngine: "katex" }),
    ],
    filters: [Plugin.RemoveDrafts()],
    emitters: [
      Plugin.AliasRedirects(),
      Plugin.ComponentResources(),
      Plugin.ContentPage(),
      Plugin.FolderPage(),
      Plugin.TagPage(),
      Plugin.ContentIndex({
        enableSiteMap: true,
        enableRSS: true,
        rssLimit: 50,
        rssFullHtml: true,
      }),
      Plugin.Assets(),
      Plugin.Static(),
      Plugin.Favicon(),
      Plugin.NotFoundPage(),
      // Comment out CustomOgImages to speed up build time
      // Plugin.CustomOgImages(), // Disabled due to memory issues in GitHub Actions
    ],
  },
}

export default config
