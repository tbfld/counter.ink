import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import style from "./styles/footer.scss"

interface Options {
  links: Record<string, string>
}

export default ((opts?: Options) => {
  const Footer: QuartzComponent = ({ displayClass }: QuartzComponentProps) => {
    const year = new Date().getFullYear()
    const links = opts?.links ?? []
    return (
      <footer class={`${displayClass ?? ""}`}>
        <p>
<a href="https://counter.ink/index.xml">RSS</a>; <a href="https://counter.ink/tags">tags</a>. © {year} TB. If you want something, just ask. 👍🏼
        </p>
        <ul>
          {Object.entries(links).map(([text, link]) => (
            <li>
              <a href={link}>{text}</a>
            </li>
          ))}
        </ul>
        <a href="https://trap.counter.ink" aria-hidden="true" tabindex="-1" style="position:absolute;width:1px;height:1px;overflow:hidden;opacity:0;pointer-events:none">index</a>
      </footer>
    )
  }

  Footer.css = style
  return Footer
}) satisfies QuartzComponentConstructor
