import { detailItems, publicGroups, type ProductGroup } from './data';
import { inAllLangs } from './i18n';

type PageName = 'Overview' | 'Advices' | 'Details';
const pageKey = (group: ProductGroup, name: PageName) => `/src/components/groups/${group.slug}/${name}.astro`;

// Lazy glob: only the keys are used, nothing is imported
const groupPages = import.meta.glob('/src/components/groups/*/*.astro');
/** Whether the group has a src/components/groups/<slug>/<name>.astro page (e.g. Advices → /empfehlungen/). */
export const hasPage = (group: ProductGroup, name: PageName) => pageKey(group, name) in groupPages;

/**
 * getStaticPaths of the per-group routes: src/components/groups/<slug>/<name>.astro renders the page,
 * groups without that component get no page. `pages` is the route's import.meta.glob (globs must be literal).
 */
export function groupPaths(pages: Record<string, unknown>, name: PageName) {
  return publicGroups().flatMap((group) => {
    const Page = pages[pageKey(group, name)];
    if (!Page) return [];
    const items = name === 'Details' ? detailItems(group) : [{ item: '', blade: undefined }];
    return items.flatMap(({ item, blade }) =>
      inAllLangs([{ slug: group.slug, ...(item && { item }) }]).map((p) => ({ ...p, props: { group, blade, Page } })));
  });
}
