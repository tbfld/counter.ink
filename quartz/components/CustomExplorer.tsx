import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import style from "./styles/explorer.scss"
// @ts-ignore
import explorerScript from "./scripts/explorer.inline"
// @ts-ignore
import customScript from "./scripts/customExplorer.inline"
import { classNames } from "../util/lang"

export default (() => {
  const CustomExplorer: QuartzComponent = ({ displayClass }: QuartzComponentProps) => {
    return (
      <div class={classNames(displayClass, "explorer custom-explorer")}>
        <button
          type="button"
          class="explorer-toggle mobile-explorer hide-until-loaded"
          aria-label="Toggle explorer"
          aria-expanded={false}
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="18"
            height="18"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
            class="lucide lucide-menu"
          >
            <line x1="4" x2="20" y1="12" y2="12" />
            <line x1="4" x2="20" y1="6" y2="6" />
            <line x1="4" x2="20" y1="18" y2="18" />
          </svg>
        </button>
        <button
          type="button"
          class="title-button explorer-toggle desktop-explorer"
          data-mobile={false}
          aria-expanded={true}
        >
          <h2>Contents</h2>
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="14"
            height="14"
            viewBox="5 8 14 8"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
            class="fold"
          >
            <polyline points="6 9 12 15 18 9"></polyline>
          </svg>
        </button>
        <div class="explorer-content" aria-expanded={true} role="navigation">
          <ul class="explorer-ul">
            {/* notes */}
            <li>
              <div class="folder-container">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="12"
                  height="12"
                  viewBox="5 8 14 8"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  class="folder-icon"
                >
                  <polyline points="6 9 12 15 18 9"></polyline>
                </svg>
                <div>
                  <button class="folder-button">
                    <span class="folder-title">notes</span>
                  </button>
                </div>
              </div>
              <div class="folder-outer">
                <ul class="content">
                  <li><a href="/micro">small</a></li>
                  <li><a href="/blg/new">new</a></li>
                  <li><a href="/blg/old">old</a></li>
                </ul>
              </div>
            </li>

            {/* image streams */}
            <li>
              <div class="folder-container">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="12"
                  height="12"
                  viewBox="5 8 14 8"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  class="folder-icon"
                >
                  <polyline points="6 9 12 15 18 9"></polyline>
                </svg>
                <div>
                  <button class="folder-button">
                    <span class="folder-title">image streams</span>
                  </button>
                </div>
              </div>
              <div class="folder-outer">
                <ul class="content">
                  <li><a href="/images">current</a></li>
                  <li><a href="/img/images-1-(starting-2025-03-13)">stream 1</a></li>
                  <li><a href="/img/images-2-(2025-02-25-to-2025-03-12)">stream 2</a></li>
                  <li><a href="/img/images-3-(2025-02-24)">stream 3</a></li>
                  <li><a href="/img/images-4-(2025-02-23)">stream 4</a></li>
                  <li><a href="/img/images-5-(through-2025-02-22)">stream 5</a></li>
                </ul>
              </div>
            </li>

            {/* and static things */}
            <li>
              <div class="folder-container">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="12"
                  height="12"
                  viewBox="5 8 14 8"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  class="folder-icon"
                >
                  <polyline points="6 9 12 15 18 9"></polyline>
                </svg>
                <div>
                  <button class="folder-button">
                    <span class="folder-title">and static things</span>
                  </button>
                </div>
              </div>
              <div class="folder-outer">
                <ul class="content">
                  <li><a href="/obj">objects</a></li>
                  <li><a href="/txt">texts</a></li>
                  <li><a href="/links">and links</a></li>
                </ul>
              </div>
            </li>

            {/* about */}
            <li>
              <a href="/about">about</a>
            </li>
          </ul>
        </div>
      </div>
    )
  }

  CustomExplorer.css = style
  CustomExplorer.afterDOMLoaded = `
    ${explorerScript};
    ${customScript};
  `
  return CustomExplorer
}) satisfies QuartzComponentConstructor
