document.addEventListener("nav", () => {
  const explorer = document.querySelector(".custom-explorer")
  if (!explorer) return

  // Initialize all folders as collapsed first
  const folderContainers = explorer.querySelectorAll(".folder-container")
  folderContainers.forEach((container) => {
    const folderLi = container.closest("li")
    if (folderLi) {
      folderLi.classList.add("collapsed")
      const icon = folderLi.querySelector(".folder-icon")
      if (icon) {
        icon.classList.add("collapsed")
      }
    }
  })

  // Handle folder toggle buttons
  const folderButtons = explorer.querySelectorAll(".folder-button")
  folderButtons.forEach((button) => {
    button.addEventListener("click", (e) => {
      e.preventDefault()
      e.stopPropagation()
      
      const folderLi = (button as HTMLElement).closest("li")
      if (!folderLi) return

      const folderIcon = folderLi.querySelector(".folder-icon")
      
      // Toggle collapsed state
      if (folderLi.classList.contains("collapsed")) {
        folderLi.classList.remove("collapsed")
        if (folderIcon) folderIcon.classList.remove("collapsed")
      } else {
        folderLi.classList.add("collapsed")
        if (folderIcon) folderIcon.classList.add("collapsed")
      }
    })
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
