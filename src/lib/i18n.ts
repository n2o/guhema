import en from '../i18n/en.json';
import ru from '../i18n/ru.json';

export const LANGS = ['de', 'en', 'ru'] as const;
export type Lang = (typeof LANGS)[number];
export const LANG_NAMES: Record<Lang, string> = { de: 'Deutsch', en: 'English', ru: 'Русский' };

const DICTS: Record<Lang, Record<string, string>> = { de: {}, en, ru };

/**
 * Keys are the German source strings; "context|text" where the same German text needs different translations.
 * Placeholders keep the gettext form "%(name)s". Some strings contain HTML (e.g. <sup>): render those with set:html.
 */
export function t(lang: Lang, key: string, vars: Record<string, string | number> = {}): string {
  const text = DICTS[lang][key] || key.split('|').pop()!;
  return text.replace(/%\((\w+)\)s/g, (_, name) => String(vars[name])).replace(/%%/g, '%');
}

/** Decimal number as in the catalogue: always one decimal for whole numbers ("1.0", "0.65"), language's decimal separator. */
export function float(lang: Lang, value: number | null | undefined): string {
  if (value == null) return '';
  const text = Number.isInteger(value) ? value.toFixed(1) : String(value);
  return lang === 'en' ? text : text.replace('.', ',');
}

export type Translated<T = string> = Record<Lang, T | null>;

/** Translated data field with German fallback. */
export function tr<T>(field: Translated<T> | null | undefined, lang: Lang): T | null {
  return field?.[lang] ?? field?.de ?? null;
}

/** Site path for a language; `path` is the German path, e.g. "/produkte/". */
export function url(lang: Lang, path: string): string {
  return lang === 'de' ? path : `/${lang}${path}`;
}

/** German path of the current page, i.e. without the /en or /ru prefix. */
export function basePath(pathname: string): string {
  return pathname.replace(/^\/(en|ru)(?=\/)/, '');
}

/** Rest param `[...lang]`: undefined is German at the root. */
export const langParams = LANGS.map((lang) => (lang === 'de' ? undefined : lang));

export function langOf(param: string | undefined): Lang {
  return (param ?? 'de') as Lang;
}

/** getStaticPaths helper: every given param set in every language. */
export function inAllLangs<P extends Record<string, string>>(params: P[] = [{} as P]) {
  return langParams.flatMap((lang) => params.map((p) => ({ params: { lang, ...p } })));
}
