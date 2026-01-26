document.addEventListener("nav", () => {
  const explorer = document.querySelector(".custom-explorer")
  if (!explorer) return

  // Handle folder toggle buttons - toggle the "open" class on .folder-outer
  const folderButtons = explorer.querySelectorAll(".folder-button")
  folderButtons.forEach((button) => {
    button.addEventListener("click", (e) => {
      e.preventDefault()
      e.stopPropagation()
      
      const folderLi = (button as HTMLElement).closest("li")
      if (!folderLi) return

      const folderOuter = folderLi.querySelector(".folder-outer")
      
      if (folderOuter) {
        // Toggle the "open" class which CSS uses to expand/collapse
        folderOuter.classList.toggle("open")
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
