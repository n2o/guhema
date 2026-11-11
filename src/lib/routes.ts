import { detailItems, publicGroups } from './data';
import { inAllLangs } from './i18n';

/**
 * getStaticPaths of the per-group routes: src/components/groups/<slug>/<name>.astro renders the page,
 * groups without that component get no page. `pages` is the route's import.meta.glob (globs must be literal).
 */
export function groupPaths(pages: Record<string, unknown>, name: 'Overview' | 'Advices' | 'Details') {
  return publicGroups().flatMap((group) => {
    const Page = pages[`/src/components/groups/${group.slug}/${name}.astro`];
    if (!Page) return [];
    const items = name === 'Details' ? detailItems(group) : [{ item: '', blade: undefined }];
    return items.flatMap(({ item, blade }) =>
      inAllLangs([{ slug: group.slug, ...(item && { item }) }]).map((p) => ({ ...p, props: { group, blade, Page } })));
  });
}
