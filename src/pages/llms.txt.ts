// llms.txt (https://llmstxt.org): a Markdown map of the site for AI assistants, generated from the product data.
import type { APIRoute } from 'astro';
import { bladeName, catalogs, detailItems, detailPath, publicGroups } from '../lib/data';
import { LANG_NAMES, tr, type Translated } from '../lib/i18n';
import { hasPage } from '../lib/routes';
import { snippet } from '../lib/seo';

const de = <T>(field: Translated<T> | null | undefined) => tr(field, 'de');

export const GET: APIRoute = ({ site }) => {
  const abs = (path: string) => new URL(path, site).href;
  const products = publicGroups().flatMap((group) => [
    `- [${de(group.name)}](${abs(`/produkte/${group.slug}/`)}): ${snippet(de(group.description), 300)}`,
    ...(hasPage(group, 'Advices') ? [`  - [Empfehlungen und Schnittdaten](${abs(`/produkte/${group.slug}/empfehlungen/`)})`] : []),
    ...(hasPage(group, 'Details') ? detailItems(group) : []).map(({ blade }) =>
      `  - [${bladeName(blade)}](${abs(detailPath(group, blade))}): ${snippet([de(blade.name), de(blade.description)].filter(Boolean).join('\n'), 200)}`),
  ]);
  const body = `# GUHEMA GmbH & Co. KG

> Hersteller von Metallsägeblättern aus Remscheid: Maschinensägeblätter, Metallsägebänder, Metallkreissägeblätter, Lochsägen sowie Stich-, Säbel- und Handsägeblätter für Metall. Made in Germany seit 1867.

- Familienunternehmen in der 5. Generation, gegründet 1867
- Unternehmensabläufe zertifiziert nach DIN EN ISO 9001 seit 1997
- Adresse: Walter-Freitag-Straße 37, 42899 Remscheid, Deutschland
- Telefon: +49 2191 8867 0, E-Mail: info@guhema.com
- Die Website gibt es auf Deutsch (${abs('/')}), Englisch (${abs('/en/')}) und Russisch (${abs('/ru/')}).

## Produkte

${products.join('\n')}

## Kataloge

${catalogs.map(([code]) => `- [Katalog, ${LANG_NAMES[code]} (PDF)](${abs(`/static/catalogs/guhema_catalog_${code}.pdf`)})`).join('\n')}

## Unternehmen

- [Unternehmen](${abs('/unternehmen/')})
- [Impressum und Kontakt](${abs('/impressum/')})
`;
  return new Response(body, { headers: { 'Content-Type': 'text/plain; charset=utf-8' } });
};
