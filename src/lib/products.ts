// Table helpers for product pages. They return HTML: use set:html.
import { t, type Lang } from './i18n';

export const DOT_ICON = "<i class='fa fa-circle' aria-hidden='true'></i>";

/** Visible dot for sighted users, a word for screen readers. */
export const dotfield = (lang: Lang) => `${DOT_ICON}<span class='sr-only'>${t(lang, 'lieferbar')}</span>`;
const dotcell = (lang: Lang) => `<td>${dotfield(lang)}</td>`;
const EMPTYCELL = '<td></td>';

/** Dot when the tooth count is available. */
export const checkZpz = (lang: Lang, val: unknown) => (val ? dotfield(lang) : '');

/** Band saw cell: "1" is a dot, anything else is shown bold. */
export const bandsawIndicatorCheck = (lang: Lang, val: string) =>
  val === '1' ? `<span class='indicator-dot'>${dotfield(lang)}</span>` : `<strong>${val}</strong>`;

/** Three cells for the hole saws available at one diameter. */
export function showDiameters(lang: Lang, blades: { ordernr: string }[]): string {
  if (blades.length === 3) return dotcell(lang).repeat(3);
  if (blades.length > 1) {
    return blades[1].ordernr === 'J' ? dotcell(lang) + dotcell(lang) + EMPTYCELL : dotcell(lang) + EMPTYCELL + dotcell(lang);
  }
  return dotcell(lang) + EMPTYCELL + EMPTYCELL;
}

// Tooth-count columns in the order they are preferred for the example article number
const ZPZ_FIELDS = 'L C E G H I J M N O T U V W UE'.split(' ');
const BANDSAW_FIELDS = 'L W T Z VP TP F E'.split(' ');

/** Code of the first tooth count this indicator really offers, L as fallback. */
function articleCode(ind: Record<string, unknown> | undefined, fields: string[]): string {
  if (!ind) return '';
  const field = fields.find((f) => ind[f]) ?? 'L';
  return field === 'UE' ? 'Ü' : field;
}

/** Tooth-count code for the example article number; `without`: tooth-count columns the page's table does not show. */
export const zpzCode = (ind: Record<string, unknown> | undefined, without = '') =>
  articleCode(ind, ZPZ_FIELDS.filter((f) => !without.split(' ').includes(f)));

/** Tooth-count code for the band saw example article number. */
export const validBandsawIndicator = (ind: Record<string, unknown> | undefined) => articleCode(ind, BANDSAW_FIELDS);
