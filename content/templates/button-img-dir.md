<%*
const title = tp.frontmatter?.title ?? "";
if (title.toLowerCase().includes("image stream")) {
  tR += `\`\`\`button
name Open counter.ink
type command
action shell:open ~/github/counter.ink/content/img
\`\`\``;
}
%>