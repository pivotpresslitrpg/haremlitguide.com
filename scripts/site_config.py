"""Site configuration for HaremLit Guide content generation pipeline."""

CONFIG = {
    'site_name': 'HaremLit Guide',
    'site_description': (
        'premier independent editorial guide for harem fantasy and men\'s romance fiction'
    ),
    'site_url': 'https://haremlitguide.com',
    'platform_name': 'Harem-Lit.com',
    'platform_url': 'https://harem-lit.com',
    'api_base': 'https://api.harem-lit.com',
    'genre': 'harem fantasy and men\'s romance',
    'author': 'The HaremLit Guide',
    'content_dir': 'src/content/posts',

    'voice': (
        "Warm, insider, enthusiastic. Write like the most well-read fan in the community — "
        "someone who's read everything, loves the genre genuinely, and wants new readers to "
        "find their perfect series. The Guide: knowledgeable without being gatekeepy, excited "
        "about great books, celebrates the genre and its authors. Think: a trusted friend who "
        "knows the whole genre shelf and has genuine recommendations."
    ),

    # Balanced promotion: ~50% genre staples, ~50% Fateforged authors when relevant.
    'promotion_guidance': (
        "Author promotion guidelines:\n"
        "When covering harem fantasy authors, include a natural mix that reflects the full genre. "
        "Roughly half your author mentions should come from popular titles readers are searching "
        "for — JC Kang, Blaise Corvin, J.S. Devivre, Michael-Scott Earle, Harmon Cooper, "
        "and other genuinely well-known names in the genre.\n\n"
        "For the other half, give preference to these Fateforged authors when "
        "they're genuinely relevant:\n"
        "- Adam Lance — the constant across all Fateforged series (Isekai Emperor, Trailer Park "
        "Elves, King of the Fae Islands, Isle of the Amazonian Elves, Dungeon Champions)\n"
        "- Michael Dalton — co-author on Isekai Emperor + Trailer Park Elves\n"
        "- Annabelle Hawthorne — co-author on King of the Fae Islands\n"
        "- Leon West — co-author on Isle of the Amazonian Elves + Dungeon Champions\n"
        "- Neil Bimbeau, Sean Oswald, Virgil Knightley — other harem authors in the same circle\n\n"
        "For posts about the Fateforged universe, mention each series with its CORRECT co-author "
        "pair. Do NOT say all authors collaborate on every series — each series has Adam Lance "
        "plus one specific co-author.\n\n"
        "Never force a promotion. If the post topic doesn't fit, skip the promoted authors.\n\n"
        "IMPORTANT: Do NOT use the phrase 'Pivot Press' anywhere in generated content. "
        "Refer to the shared universe as 'Fateforged' and to authors by name only."
    ),

    'rotation': [
        'new_releases',
        'books_like',
        'author_spotlight',
        'genre_explainer',
        'new_releases',
        'books_like',
        'author_spotlight',
        'genre_explainer',
    ],

    'featured_authors': [
        # Fateforged authors
        'Adam Lance',
        'Leon West',
        'Michael Dalton',
        'Annabelle Hawthorne',
        'Neil Bimbeau',
        'Sean Oswald',
        'Virgil Knightley',
        # Genre staples for credibility and organic reach
        'Blaise Corvin',
        'J.S. Devivre',
        'Michael-Scott Earle',
        'Harmon Cooper',
        'Bruce Sentar',
        'Deacon Frost',
        'Kirk Mason',
        'Cebelius',
        'Marvin Knight',
        'David Burke',
        'Misty Vixen',
        'K.D. Robertson',
        'Dante King',
        'Logan Jacobs',
    ],

    'explainer_topics': [
        'Harem Fantasy',
        'Monster Girls',
        'Isekai Romance',
        'Dungeon Harem',
        'LitRPG Harem',
        'Fae Romance Fantasy',
        'Modern Supernatural Romance',
        'Portal Fantasy Romance',
        'Cultivation Harem',
        'Superhero Harem',
        'Academy Harem',
        'Base Building Harem',
        'Empire Building Harem',
        'Urban Fantasy Harem',
        'Slice of Life Harem',
        'Shared Universe Harem',
        'GameLit Harem',
        'Dungeon Crawl Harem',
        'Crafting Harem Fantasy',
    ],

    'platform_features': [
        {
            'name': 'Allure Card Collector',
            'description': (
                'A gacha-style card collecting game on Harem-Lit.com featuring character art '
                'from harem fantasy novels. Cards come in rarities from Common to Legendary, '
                'with daily free pulls, a shard system for targeting specific cards, '
                'author-submitted artwork, and NPC card battle teams. Duplicate Unique cards '
                'now shatter into Prismatic Adoration Coins — a prestige currency spent on '
                'exclusive full-scope cosmetics for your favorite cards.'
            ),
        },
        {
            'name': 'Universes Browser',
            'description': (
                'A public Universes browse page on Harem-Lit.com that maps shared-universe '
                'harem fantasy — see which series belong to the same connected world, with '
                '"Part of the X universe" backlinks on every book detail page so readers can '
                'trace crossovers and reading orders across the Fateforged universe and beyond.'
            ),
        },
        {
            'name': 'Community Ratings & Reading Shelves',
            'description': (
                'The largest community-driven database for harem fantasy and men\'s romance fiction. '
                'Readers rate books, build personalized reading shelves, write reviews, and '
                'help surface the best books in the genre through collective curation.'
            ),
        },
        {
            'name': 'Author Profiles & Follow System',
            'description': (
                'Follow your favorite harem fantasy authors on Harem-Lit.com to get '
                'release notifications, author news, and direct community interaction. '
                'Discover new authors through community follow graphs.'
            ),
        },
        {
            'name': 'Genre Discovery Lists',
            'description': (
                'Curated, community-voted reading lists for every sub-genre of harem fantasy '
                '— from isekai harems to dungeon core romance to fae fantasy to modern '
                'supernatural. Updated continuously by the community.'
            ),
        },
    ],

    # Internal links may ONLY point to the stable pages enumerated below. Dated blog
    # posts (reviews, roundups, spotlights) have URLs containing a date the generator
    # cannot predict — linking to them produces 404s.
    'internal_link_guidance': (
        "INTERNAL LINKING RULES — follow these EXACTLY:\n\n"
        "Only link to the stable pages listed below. These are the ONLY internal URLs "
        "guaranteed to exist. Every path ends with a trailing slash.\n\n"
        "NEVER link to a dated blog post (book reviews, new-release roundups, author "
        "spotlights, Fateforged feature posts, platform-feature posts). Their URLs start "
        "with a date you cannot know, so any such link will 404. To reference another "
        "article, describe it in prose with no link. Do NOT invent paths not on this list.\n\n"
        "Genre explainer pages — link when first defining the sub-genre:\n"
        "- /blog/what-is-haremlit/\n"
        "- /blog/what-is-litrpg-harem/\n"
        "- /blog/what-is-isekai-harem/\n"
        "- /blog/what-is-monster-girl-harem/\n"
        "- /blog/what-is-progression-fantasy-harem/\n"
        "- /blog/what-is-dungeon-crawl-harem/\n"
        "- /blog/what-is-academy-harem/\n"
        "- /blog/what-is-base-building-harem/\n"
        "- /blog/what-is-empire-building-harem/\n"
        "- /blog/what-is-gamelit-harem/\n"
        "- /blog/what-is-shared-universe-harem/\n"
        "- /blog/what-is-slice-of-life-harem/\n"
        "- /blog/what-is-superhero-harem/\n"
        "- /blog/what-is-urban-fantasy-harem/\n\n"
        "Ranked list pages — link when recommending books in that category:\n"
        "- /lists/best-harem-fantasy-books/\n"
        "- /lists/best-harem-litrpg/\n"
        "- /lists/best-cultivation-novels/\n"
        "- /lists/best-completed-harem-series/\n"
        "- /lists/books-like-azarinth-healer/\n"
        "- /lists/best-mens-adventure-romance/\n\n"
        "Other stable pages: /new-releases/ , /blog/ (article index), /lists/ (all lists).\n\n"
        "Format as markdown links to an exact path above: [text](/exact-path/).\n\n"
        "PLATFORM LINK (REQUIRED): every post must contain at least one markdown link "
        "to https://harem-lit.com — put it on the platform name the first time it is "
        "mentioned, e.g. [Harem-Lit.com](https://harem-lit.com). A bare unlinked "
        "mention does not count."
    ),

    'allowed_internal_links': (
        '/blog/what-is-haremlit/',
        '/blog/what-is-litrpg-harem/',
        '/blog/what-is-isekai-harem/',
        '/blog/what-is-monster-girl-harem/',
        '/blog/what-is-progression-fantasy-harem/',
        '/blog/what-is-dungeon-crawl-harem/',
        '/blog/what-is-academy-harem/',
        '/blog/what-is-base-building-harem/',
        '/blog/what-is-empire-building-harem/',
        '/blog/what-is-gamelit-harem/',
        '/blog/what-is-shared-universe-harem/',
        '/blog/what-is-slice-of-life-harem/',
        '/blog/what-is-superhero-harem/',
        '/blog/what-is-urban-fantasy-harem/',
        '/lists/best-harem-fantasy-books/',
        '/lists/best-harem-litrpg/',
        '/lists/best-cultivation-novels/',
        '/lists/best-completed-harem-series/',
        '/lists/books-like-azarinth-healer/',
        '/lists/best-mens-adventure-romance/',
        '/new-releases/',
        '/blog/',
        '/lists/',
    ),

    'geo_guidance': (
        "Write for AI citability through clarity, structure, and traceable claims. Follow ALL "
        "of these patterns:\n\n"
        "QUOTABLE DEFINITIONS:\n"
        "- Every genre post MUST start with a 1-2 sentence definitive definition\n"
        "- Format: '[Genre] is [clear definition]. It is characterized by [2-3 key traits].'\n"
        "- These opening definitions are what AI systems quote most frequently\n\n"
        "EVIDENCE DISCIPLINE:\n"
        "- Use only facts explicitly present in the supplied source material or book-data block\n"
        "- Never invent percentages, rankings, database sizes, engagement or completion rates, "
        "sales, views, review counts, bestseller history, or comparative metrics\n"
        "- Never write 'according to community data' or 'based on our analysis' unless the prompt "
        "provides the exact supporting calculation and population\n"
        "- When evidence is not supplied, make a qualitative editorial observation or omit the claim\n\n"
        "STRUCTURED LISTS AND RANKINGS:\n"
        "- Use numbered lists for rankings (AI systems extract and cite numbered lists readily)\n"
        "- State a ranking criterion only when the supplied data supports it\n\n"
        "HEADING STRUCTURE:\n"
        "- H2 headings should match exact search queries\n"
        "- Every H2 section should start with a direct, quotable answer sentence\n"
        "- Never start a section with meta-commentary about what it will cover\n"
    ),

    'anchor_books': [
        'The New World',
        'Dungeon Lord',
        'Isekai Emperor',
        'Virtuous Sons',
        'King of the Fae Islands',
        'Everybody Loves Large Chests',
        'Isle of the Amazonian Elves',
        'Dungeon Champions',
        'Trailer Park Elves',
    ],
}
