import { PageLayout, SharedLayout } from "./quartz/cfg";
import * as Component from "./quartz/components";
// import { Tagline } from "./quartz/components";
import { customSortFn } from "./sidebar-explorer-customSort-TB"; // Import sorting function

// Components shared across all pages
export const sharedPageComponents: SharedLayout = {
  head: Component.Head(),
  header: [],
  afterBody: [],
  footer: Component.Footer({
    links: {},
  }),
};

// Components for pages that display a single page (e.g., a single note)
export const defaultContentPageLayout: PageLayout = {
  beforeBody: [
    Component.ConditionalRender({
      component: Component.Breadcrumbs(),
      condition: (page) => page.fileData.slug !== "index",
    }),
    Component.ConditionalRender({
      component: Component.ArticleTitle(),
      condition: (page) => page.fileData.slug !== "recent",
    }),
    Component.ConditionalRender({
      component: Component.ContentMeta(),
      condition: (page) => page.fileData.slug !== "recent",
    }),
    Component.ConditionalRender({
      component: Component.TagList(),
      condition: (page) => page.fileData.slug !== "recent",
    }),
  ],
  left: [
    Component.Flex({
      direction: "row",
      components: [
        { Component: Component.Darkmode() },
        { Component: Component.PageTitle(), grow: true },
      ],
    }),
//  Tagline(), // Add tagline below title
    Component.MobileOnly(Component.Spacer()),
    Component.Search(),
    Component.DesktopOnly(Component.Graph()),
    Component.Explorer({ sortFn: customSortFn }), // Use external sorting function
  ],
  right: [
    Component.DesktopOnly(Component.TableOfContents()),
    Component.AllTags(),
  ],
};

// Components for pages that display lists of pages (e.g., tags or folders)
export const defaultListPageLayout: PageLayout = {
  beforeBody: [Component.Breadcrumbs(), Component.ArticleTitle(), Component.ContentMeta()],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Search(),
    Component.DesktopOnly(Component.Graph()),
    Component.Explorer({ sortFn: customSortFn }), // Use external sorting function
  ],
  right: [],
};
