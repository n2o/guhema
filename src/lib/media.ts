import type { ImageMetadata } from 'astro';
import { getImage } from 'astro:assets';

const FILES = import.meta.glob<ImageMetadata>('/src/media/**/*.{png,jpg,jpeg,gif,webp,PNG,JPG,JPEG}', {
  eager: true,
  import: 'default',
});

/** Thumbnail sizes: box [w, h]; the image covers the box, one side may overflow, never upscaled. */
const ALIASES = {
  products_clamping: [250, 80],
  products_teaserimage: [262, 174],
  blade_image: [458, 80],
  blade_image_250h: [600, 250],
} as const;
export type Alias = keyof typeof ALIASES;

/** Image by its path under src/media (e.g. "blades/x.png"); null if missing. */
export function media(path: string | null | undefined): ImageMetadata | null {
  return (path && FILES[`/src/media/${path}`]) || null;
}

export async function thumbnail(path: string | null | undefined, alias: Alias) {
  const src = media(path);
  if (!src) return null;
  const [w, h] = ALIASES[alias];
  const factor = Math.min(1, Math.max(w / src.width, h / src.height));
  const width = Math.round(src.width * factor);
  const height = Math.round(src.height * factor);
  // 2x for sharp images on high-density screens (Astro skips it when the original is too small)
  const img = await getImage({ src, width, height, densities: [2] });
  return { src: img.src, srcset: img.srcSet.attribute || undefined, width, height };
}
