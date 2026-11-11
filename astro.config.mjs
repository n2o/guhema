import sitemap from '@astrojs/sitemap';
import { defineConfig } from 'astro/config';

// Canonical host: the other domains redirect here (public/.htaccess)
const SITE = 'https://www.guhema.com';

export default defineConfig({
  site: SITE,
  trailingSlash: 'always',
  integrations: [
    sitemap({
      i18n: { defaultLocale: 'de', locales: { de: 'de', en: 'en', ru: 'ru' } },
      // Legal pages are German only; en/ru copies are canonicalized to the German page
      filter: (page) => !/\/(en|ru)\/(impressum|datenschutz)\/$/.test(page),
    }),
  ],
});
