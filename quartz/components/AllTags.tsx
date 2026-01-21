import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import style from "./styles/allTags.scss"
import { resolveRelative } from "../util/path"
import { classNames } from "../util/lang"

const AllTags: QuartzComponent = ({
  fileData,
  allFiles,
  displayClass,
}: QuartzComponentProps) => {
  // Collect all unique tags from all files
  const allTags = new Set<string>()
  allFiles.forEach((file) => {
    if (file.frontmatter?.tags) {
      const tags = Array.isArray(file.frontmatter.tags)
        ? file.frontmatter.tags
        : [file.frontmatter.tags]
      tags.forEach((tag: string) => allTags.add(tag))
    }
  })

  // Sort tags alphabetically
  const sortedTags = Array.from(allTags).sort((a, b) => a.localeCompare(b))

  if (sortedTags.length === 0) {
    return null
  }

  return (
    <div class={classNames(displayClass, "all-tags")}>
      <h3>Tags</h3>
      <div class="tag-cloud" style="max-height: 400px; overflow-y: auto;">
        {sortedTags.map((tag, index) => (
          <>
            <a href={resolveRelative(fileData.slug!, `tags/${tag}` as any)} class="internal tag-link">
              {tag}
            </a>
            {index < sortedTags.length - 1 && <span> * </span>}
          </>
        ))}
      </div>
    </div>
  )
}

AllTags.css = style

export default (() => AllTags) satisfies QuartzComponentConstructor
