import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';
import type { APIContext } from 'astro';

export async function GET(context: APIContext) {
  const posts = (await getCollection('posts'))
    .sort((a, b) => b.data.date.localeCompare(a.data.date));

  return rss({
    title: 'HaremLit Guide',
    description: "Harem fantasy rankings — the best harem LitRPG, cultivation novels, and men's romance fiction.",
    site: context.site!,
    xmlns: { atom: 'http://www.w3.org/2005/Atom' },
    items: posts.map(post => ({
      title: post.data.title,
      pubDate: new Date(post.data.date + 'T12:00:00'),
      description: post.data.description,
      link: `/blog/${post.id}/`,
    })),
    customData: `<language>en-us</language>
<atom:link href="https://litrpgcritic.com/rss.xml" rel="related" type="application/rss+xml" title="LitRPG Critic"/>
<atom:link href="https://fantasyranked.com/rss.xml" rel="related" type="application/rss+xml" title="Fantasy Ranked"/>`,
  });
}
