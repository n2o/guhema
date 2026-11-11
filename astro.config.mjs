import sitemap from '@astrojs/sitemap';
import { defineConfig } from 'astro/config';

// Canonical host: the other domains redirect here (keep the host redirect in public/.htaccess in sync)
const SITE = 'https://guhema.com';

export default defineConfig({
  site: SITE,
  trailingSlash: 'always',
  integrations: [
    sitemap({ i18n: { defaultLocale: 'de', locales: { de: 'de', en: 'en', ru: 'ru' } } }),
  ],
});
