import { i18n } from "../../i18n"
import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "../types"

const NotFound: QuartzComponent = ({ cfg }: QuartzComponentProps) => {
  // If baseUrl contains a pathname after the domain, use this as the home link
  const url = new URL(`https://${cfg.baseUrl ?? "example.com"}`)
  const baseDir = url.pathname
  const recentUrl = `${baseDir}recent`

  return (
    <article class="popover-hint">
      <h1>404</h1>
      <p>{i18n(cfg.locale).pages.error.notFound}</p>
      <p>
        Redirecting to <a href={recentUrl}>recent entries</a>…
      </p>
      <script dangerouslySetInnerHTML={{ __html: `setTimeout(()=>location.href="${recentUrl}",3000)` }} />
    </article>
  )
}

export default (() => NotFound) satisfies QuartzComponentConstructor
