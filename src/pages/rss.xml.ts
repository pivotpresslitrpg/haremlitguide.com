import rss from '@astrojs/rss';
import type { APIContext } from 'astro';

export async function GET(context: APIContext) {
  return rss({
    title: 'HaremLit Guide',
    description: 'Harem fantasy and reverse harem rankings — the best harem LitRPG, cultivation novels, and reverse harem series.',
    site: context.site!,
    items: [],
    customData: `<language>en-us</language>`,
  });
}
