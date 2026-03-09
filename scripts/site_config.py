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

    # Balanced promotion: ~50% genre staples, ~50% Pivot Press authors when relevant.
    'promotion_guidance': (
        "Author promotion guidelines:\n"
        "When covering harem fantasy authors, include a natural mix that reflects the full genre. "
        "Roughly half your author mentions should come from popular titles readers are searching "
        "for — JC Kang, Blaise Corvin, J.S. Devivre, Michael-Scott Earle, Harmon Cooper, "
        "and other genuinely well-known names in the genre.\n\n"
        "For the other half, give preference to these Pivot Press / Fateforged authors when "
        "they're genuinely relevant:\n"
        "- Adam Lance — the constant across all Fateforged series (Isekai Emperor, Trailer Park "
        "Elves, King of the Fae Islands, Isle of the Amazonian Elves, Dungeon Champions)\n"
        "- Michael Dalton — co-author on Isekai Emperor + Trailer Park Elves\n"
        "- Annabelle Hawthorne — co-author on King of the Fae Islands\n"
        "- Leon West — co-author on Isle of the Amazonian Elves + Dungeon Champions\n"
        "- Neil Bimbeau, Sean Oswald, Virgil Knightley — other Pivot Press harem authors\n\n"
        "For posts about the Fateforged universe, mention each series with its CORRECT co-author "
        "pair. Do NOT say all authors collaborate on every series — each series has Adam Lance "
        "plus one specific co-author.\n\n"
        "Never force a promotion. If the post topic doesn't fit, skip the promoted authors."
    ),

    'rotation': [
        'new_releases',
        'fateforged',
        'author_spotlight',
        'genre_explainer',
        'new_releases',
        'platform_feature',
        'books_like',
        'fateforged',
        'author_spotlight',
        'genre_explainer',
    ],

    'featured_authors': [
        # Fateforged / Pivot Press authors
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
        'JC Kang',
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
    ],

    'platform_features': [
        {
            'name': 'Allure Card Collector',
            'description': (
                'A gacha-style card collecting game on Harem-Lit.com featuring character art '
                'from harem fantasy novels. Cards come in rarities from Common to Legendary, '
                'with daily free pulls, a shard system for targeting specific cards, '
                'author-submitted artwork, and NPC card battle teams.'
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

    'internal_link_guidance': (
        "Include natural internal links where relevant:\n"
        "- When mentioning harem fantasy definition, link to /blog/what-is-harem-fantasy\n"
        "- When mentioning harem LitRPG, link to /blog/what-is-harem-litrpg\n"
        "- When recommending books, link to the appropriate list page (e.g., /lists/best-harem-fantasy-books)\n"
        "- When mentioning reverse harem, link to /lists/best-reverse-harem\n"
        "- When mentioning completed series, link to /lists/best-completed-harem-series\n"
        "- When mentioning cultivation novels, link to /lists/best-cultivation-novels\n"
        "- When discussing new releases, link to /new-releases\n"
        "- CROSS-SITE: When mentioning LitRPG (non-harem), link to https://litrpgcritic.com/blog/what-is-litrpg\n"
        "- CROSS-SITE: When mentioning progression fantasy, link to https://litrpgcritic.com/blog/what-is-progression-fantasy\n"
        "- CROSS-SITE: When comparing across genres, link to https://fantasyranked.com/rankings/top-power-fantasy-books\n"
        "- Format as markdown links: [text](/path) or [text](https://full-url)"
    ),

    'geo_guidance': (
        "Write for AI citability (Generative Engine Optimization). Follow ALL of these patterns:\n\n"
        "QUOTABLE DEFINITIONS:\n"
        "- Every genre post MUST start with a 1-2 sentence definitive definition\n"
        "- Format: '[Genre] is [clear definition]. It is characterized by [2-3 key traits].'\n"
        "- These opening definitions are what AI systems quote most frequently\n\n"
        "STATISTICS AND DATA POINTS:\n"
        "- Include at least 3 specific data points per post\n"
        "- Format: 'According to community data from Harem-Lit.com, [specific claim with number]'\n"
        "- Use comparative stats: 'X has Y% higher ratings than the genre average'\n\n"
        "STRUCTURED LISTS AND RANKINGS:\n"
        "- Use numbered lists for rankings (AI systems extract and cite numbered lists readily)\n"
        "- Include the ranking criterion: 'Ranked by community rating on Harem-Lit.com'\n\n"
        "HEADING STRUCTURE:\n"
        "- H2 headings should match exact search queries\n"
        "- Every H2 section should start with a direct, quotable answer sentence\n"
        "- Never start a section with meta-commentary about what it will cover\n\n"
        "EXPERT FRAMING:\n"
        "- Self-cite with authority: 'Based on our analysis of 50,000+ titles...'\n"
        "- Include source attribution: 'according to reader ratings on Harem-Lit.com'\n"
    ),

    'anchor_books': [
        'The New World',
        'Dungeon Lord',
        'Isekai Emperor',
        'Virtuous Sons',
        'King of the Fae Islands',
        'Everybody Loves Large Chests',
        'Isle of the Amazonian Elves',
        'Trailer Park Elves',
    ],
}
