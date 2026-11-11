// Titles, descriptions and breadcrumbs for product pages, derived from the German path.
import { bladeName, detailItems, groupBySlug } from './data';
import { t, tr, type Lang } from './i18n';

export interface Seo {
  title?: string;
  description?: string;
  /** [name, German path] from the home page down to the current page */
  crumbs: [string, string][];
}

/** Markdown/HTML to one plain-text line of at most `max` characters, cut at a word boundary. */
export function snippet(text: string | null | undefined, max = 155): string | undefined {
  const plain = (text ?? '').trim()
    // a line before a list item or blank line ends a sentence (trailing ** etc. ignored)
    .replace(/(?<![.!?:,;\s][*_]*)[ \t]*\r?\n(?=[ \t]*(?:[*+-]|\d+\.)[ \t]|[ \t]*\r?\n)/g, '.\n')
    .replace(/^[ \t]*(?:[+-]|\d+\.)[ \t]+/gm, '') // list markers (* is stripped below)
    .replace(/<[^>]+>|[*_#>`\[\]]|\(https?:[^)]*\)|­/g, '').replace(/\s+/g, ' ').trim();
  if (!plain) return undefined;
  if (plain.length <= max) return plain;
  const cut = plain.lastIndexOf(' ', max - 1);
  return plain.slice(0, cut > 0 ? cut : max - 1) + ' …';
}

export function seoFor(path: string, lang: Lang): Seo {
  const home: [string, string] = [t(lang, 'Home'), '/'];
  const [section, slug, item] = path.split('/').filter(Boolean);
  if (section !== 'produkte') return { crumbs: [home] };

  const crumbs: [string, string][] = [home, [t(lang, 'Produkte'), '/produkte/']];
  const group = slug ? groupBySlug(slug) : undefined;
  if (!group) return { title: t(lang, 'Produkte'), crumbs };

  const name = tr(group.name, lang)!;
  const groupPath = `/produkte/${slug}/`;
  crumbs.push([name, groupPath]);
  const description = snippet(tr(group.description, lang));
  if (!item) return { title: name, description, crumbs };

  if (item === 'empfehlungen') {
    const title = `${t(lang, 'Empfehlungen')}: ${name}`;
    crumbs.push([t(lang, 'Empfehlungen'), `${groupPath}empfehlungen/`]);
    return { title, description, crumbs };
  }
  const blade = detailItems(group).find((d) => d.item === item)?.blade;
  if (!blade) return { title: name, description, crumbs };
  const product = bladeName(blade);
  crumbs.push([product, `${groupPath}${item}/`]);
  return {
    title: `${product} – ${name}`,
    description: snippet([product, tr(blade.description, lang), name].filter(Boolean).join(' · ')),
    crumbs,
  };
}
