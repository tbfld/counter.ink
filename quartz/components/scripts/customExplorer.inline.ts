document.addEventListener("nav", () => {
  const explorer = document.querySelector(".custom-explorer") as HTMLElement | null
  if (!explorer) return

  // Toggle a folder open/closed given any element inside folder-container
  function toggleFolder(target: HTMLElement) {
    const folderContainer = target.closest(".folder-container") as HTMLElement | null
    if (!folderContainer) return
    const folderOuter = folderContainer.nextElementSibling as HTMLElement | null
    if (!folderOuter) return
    folderOuter.classList.toggle("open")
  }

  // Make the entire folder-container row clickable
  const folderContainers = explorer.querySelectorAll(".folder-container")
  folderContainers.forEach((container) => {
    container.addEventListener("click", (e) => {
      e.preventDefault()
      e.stopPropagation()
      toggleFolder(e.target as HTMLElement)
    })
  })

  // Main explorer collapse/expand (desktop title button)
  const desktopToggle = explorer.querySelector(".desktop-explorer")
  if (desktopToggle) {
    desktopToggle.addEventListener("click", () => {
      explorer.classList.toggle("collapsed")
    })
  }

  // Mobile hamburger toggle
  const mobileToggle = explorer.querySelector(".mobile-explorer")
  if (mobileToggle) {
    mobileToggle.addEventListener("click", () => {
      const isCollapsed = explorer.classList.toggle("collapsed")
      if (!isCollapsed) {
        document.documentElement.classList.add("mobile-no-scroll")
      } else {
        document.documentElement.classList.remove("mobile-no-scroll")
      }
    })
  }
})
