document.addEventListener("nav", () => {
  const explorer = document.querySelector(".custom-explorer")
  if (!explorer) return

  // Handle folder toggle buttons
  const folderButtons = explorer.querySelectorAll(".folder-button")
  folderButtons.forEach((button) => {
    button.addEventListener("click", (e) => {
      e.preventDefault()
      e.stopPropagation()
      
      const folderLi = (button as HTMLElement).closest("li")
      if (!folderLi) return

      const folderOuter = folderLi.querySelector(".folder-outer")
      const folderIcon = folderLi.querySelector(".folder-icon")
      
      if (folderOuter && folderIcon) {
        const isCollapsed = folderLi.classList.toggle("collapsed")
        folderIcon.classList.toggle("collapsed", isCollapsed)
      }
    })
  })

  // Initialize all folders as collapsed
  const folderItems = explorer.querySelectorAll("li:has(.folder-button)")
  folderItems.forEach((item) => {
    item.classList.add("collapsed")
    const icon = item.querySelector(".folder-icon")
    if (icon) {
      icon.classList.add("collapsed")
    }
  })

  // Handle main explorer toggle
  const explorerToggle = explorer.querySelector(".explorer-toggle")
  const explorerContent = explorer.querySelector(".explorer-content")
  
  if (explorerToggle && explorerContent) {
    explorerToggle.addEventListener("click", () => {
      const isExpanded = explorerContent.getAttribute("aria-expanded") === "true"
      explorerContent.setAttribute("aria-expanded", (!isExpanded).toString())
      explorerToggle.setAttribute("aria-expanded", (!isExpanded).toString())
    })
  }
})
