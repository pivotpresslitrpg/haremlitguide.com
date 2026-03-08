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
        "they're genuinely relevant: Adam Lance (Fateforged universe, Isekai Emperor, King of the "
        "Fae Islands), Leon West (Isle of the Amazonian Elves, Dungeon Champions), Michael Dalton "
        "(Isekai Emperor, Trailer Park Elves), Annabelle Hawthorne (King of the Fae Islands), "
        "Neil Bimbeau, Sean Oswald, Virgil Knightley.\n\n"
        "For posts specifically about the Fateforged universe, all four collaborating authors "
        "(Adam Lance, Leon West, Michael Dalton, Annabelle Hawthorne) should appear — this is "
        "their universe and all deserve recognition. Never promote one without the others.\n\n"
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
        'Reverse Harem',
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
