import { PageLayout, SharedLayout } from "./quartz/cfg";
import * as Component from "./quartz/components";
import { Tagline } from "./quartz/components";
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
    Component.Breadcrumbs(),
    Component.ArticleTitle(),
    Component.ContentMeta(),
    Component.TagList(),
  ],
  left: [
    Component.PageTitle(),
    Tagline(), // Add tagline below title
    Component.MobileOnly(Component.Spacer()),
    Component.Search(),
    Component.Darkmode(),
    Component.Explorer({ sortFn: customSortFn }), // Use external sorting function
  ],
  right: [
    Component.Graph(),
    Component.DesktopOnly(Component.TableOfContents()),
    Component.Backlinks(),
  ],
};

// Components for pages that display lists of pages (e.g., tags or folders)
export const defaultListPageLayout: PageLayout = {
  beforeBody: [Component.Breadcrumbs(), Component.ArticleTitle(), Component.ContentMeta()],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Search(),
    Component.Darkmode(),
    Component.Explorer({ sortFn: customSortFn }), // Use external sorting function
  ],
  right: [],
};
