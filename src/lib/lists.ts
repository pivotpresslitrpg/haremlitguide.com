export interface FAQ {
  q: string;
  a: string;
}

export interface ListConfig {
  title: string;
  description: string;
  intro: string;
  genre?: string;
  sort: 'top_rated' | 'featured';
  limit: number;
  faq?: FAQ[];
}

export const listConfig: Record<string, ListConfig> = {
  'best-harem-fantasy-books': {
    title: 'The 50 Best Harem Fantasy Books',
    description: 'The definitive ranked list of harem fantasy and men\'s romance fiction — ranked by community ratings from Harem-Lit.com.',
    intro: `Harem fantasy sits at one of the most interesting intersections in genre fiction: power progression, relationship dynamics, and the kind of found-family storytelling that makes long series genuinely hard to put down. The genre has its roots in Japanese light novels and cultivation fiction, but the English-language harem fantasy scene has developed its own distinctive voice — harder-edged, more action-focused, and deeply embedded in LitRPG and system mechanics.

The best harem fantasy uses the relationship dynamics to do real narrative work. The harem isn't set dressing — it's a community, a group of people with distinct personalities and loyalties, whose relationships with the protagonist and each other evolve meaningfully across books. When authors get that right, harem fantasy is some of the most compelling long-form genre fiction being published.

This list draws on community ratings from Harem-Lit.com — the largest tracking platform for harem fantasy readers — combined with editorial judgment about craft and staying power. These are the books that the community returns to, recommends first, and cites as the reason they found the genre.`,
    sort: 'top_rated',
    limit: 50,
    faq: [
      {
        q: 'What is harem fantasy?',
        a: 'Harem fantasy is a genre of men\'s fiction in which the protagonist develops romantic or close relationships with multiple female characters over the course of the story, typically alongside power progression, adventure, or system mechanics. It draws from Japanese harem light novel traditions and has developed a large English-language community.',
      },
      {
        q: 'What is the best harem fantasy book to start with?',
        a: 'For readers new to the genre, He Who Fights With Monsters (Jason Cheyne) offers LitRPG with romantic elements and is widely accessible. For traditional harem fantasy, Azarinth Healer and The Beginning After The End are community favorites as starting points.',
      },
      {
        q: 'Is harem fantasy the same as reverse harem?',
        a: 'No — traditional harem fantasy features a male protagonist with multiple female love interests. Reverse harem (also called "why choose" romance) features a female protagonist with multiple male love interests. Both sub-genres have active communities and are tracked on this site.',
      },
      {
        q: 'Where can I find more harem fantasy readers?',
        a: 'The community hub for harem fantasy readers is Harem-Lit.com, which hosts ratings, discussions, and tracking for thousands of titles in the genre. Reddit\'s r/HaremFantasyNovels is also active.',
      },
    ],
  },

  'best-cultivation-novels': {
    title: 'Best Cultivation Novels in English',
    description: 'The top xianxia and cultivation fantasy novels available in English — translated and original.',
    intro: `Cultivation fiction — xianxia in its Chinese-origin form — is one of the oldest and most developed traditions in the broader harem and power fantasy genre. The premise is its own sub-genre convention: a practitioner cultivates their spiritual energy, refines their soul, and ascends through realms of power over decades or centuries of in-universe time. The journey is the point.

The genre's roots are deep in Chinese web fiction, particularly platforms like Qidian and its international counterparts. The English-language cultivation scene now spans official translations of landmark Chinese novels, fan translations, and a growing body of original English cultivation fiction from authors who grew up reading the translated works.

What makes cultivation fiction distinct from other progression fantasy is the philosophical weight it often carries — the idea of cultivation as a path to genuine enlightenment, not just power. The best cultivation novels use their system as a meditation on patience, sacrifice, and the cost of ambition. The worst use it as an excuse for infinite power numbers. This list focuses on the former.`,
    genre: 'Cultivation',
    sort: 'top_rated',
    limit: 30,
    faq: [
      {
        q: 'What is a cultivation novel?',
        a: 'Cultivation novels (xianxia fiction) are a Chinese-origin fantasy genre in which practitioners cultivate spiritual energy — "qi" or similar — to advance through realms of power, gain supernatural abilities, and pursue immortality. The genre is defined by long power arcs, sect politics, realm hierarchies, and philosophical undertones.',
      },
      {
        q: 'What is the best cultivation novel to start with?',
        a: 'I Shall Seal The Heavens (ISSTH) by Er Gen is widely considered the gateway cultivation novel for English readers — well-translated, manageable in scope, and representative of the genre\'s best qualities. Cradle (Will Wight) is an English-original cultivation-influenced series that removes the translation barrier entirely.',
      },
      {
        q: 'What is the difference between xianxia and wuxia?',
        a: 'Wuxia is martial arts fiction set in a historical Chinese world — mortal warriors with exceptional physical skill. Xianxia adds supernatural cultivation: qi refinement, spiritual cultivation, immortal realms. Xianxia is the cultivation sub-genre; wuxia is its grounded, non-fantastical cousin.',
      },
    ],
  },

  'best-reverse-harem': {
    title: 'Best Reverse Harem Fantasy Series',
    description: 'The top reverse harem (why choose) fantasy series — female protagonist, multiple love interests, fantasy world.',
    intro: `Reverse harem — known in the romance community as "why choose" — flips the traditional harem dynamic: a female protagonist who develops deep relationships with multiple male love interests, without being required to choose one. The genre has exploded in the last five years, particularly in fantasy settings where the tropes of progression fantasy and epic world-building give the relationship dynamics genuine stakes and context.

Reverse harem fantasy does something the straight romance genre often struggles with: it gives the power fantasy appeal of the broader genre to a female protagonist who is both the center of relationships and the central agent of action. The best entries don't use the harem structure as wish fulfillment shorthand — they use it to explore genuinely complex dynamics across a cast of distinct, well-written characters.

This list covers the best reverse harem fantasy with meaningful genre elements — adventure, magic systems, power progression, or world-building that gives the "why choose" dynamic something to operate against.`,
    genre: 'Reverse Harem',
    sort: 'top_rated',
    limit: 25,
    faq: [
      {
        q: 'What is reverse harem fantasy?',
        a: 'Reverse harem (or "why choose") fantasy features a female protagonist who develops romantic relationships with multiple male characters, typically in a fantasy setting. Unlike traditional romance, the protagonist is not required to choose one partner — the multiple-relationship dynamic is part of the story\'s structure.',
      },
      {
        q: 'Is reverse harem romance the same as reverse harem fantasy?',
        a: 'Reverse harem romance focuses primarily on the romantic relationships, following genre conventions (happily ever after ending). Reverse harem fantasy uses the same relationship structure in an adventure or progression fantasy context, where the romance is one element alongside world-building, magic systems, and action.',
      },
      {
        q: 'What is the best reverse harem fantasy series to start with?',
        a: 'Zodiac Academy (Caroline Peckham & Susanne Valenti) is the most widely recommended entry point in reverse harem fantasy — it has a massive readership and is representative of the genre\'s appeal. For readers who want stronger LitRPG elements alongside the reverse harem dynamic, check our Harem LitRPG list.',
      },
    ],
  },

  'best-harem-litrpg': {
    title: 'Best Harem LitRPG — Where the Genres Cross',
    description: 'LitRPG with harem elements — game mechanics, power progression, and relationship dynamics in one.',
    intro: `Harem LitRPG is where two of the most popular sub-genres in online fiction collide: the explicit game mechanics and power progression of LitRPG, and the relationship-centered storytelling of harem fantasy. The combination has proven enormously popular — the system gives the harem dynamics a mechanical grounding (party composition, companion bonding, shared advancement), and the relationships give the system something personal to care about.

The best harem LitRPG doesn't treat the relationship elements as optional flavor — the characters are genuinely interesting, their dynamics with the protagonist and each other evolve meaningfully, and the power progression feels connected to the relationships rather than separate from them. These are books where you're invested in both the next level-up and the next conversation.

This list focuses on titles where both the LitRPG mechanics and the harem elements are genuinely developed — not LitRPG books with a romance footnote, and not romance books with a level-up button.`,
    genre: 'Harem LitRPG',
    sort: 'top_rated',
    limit: 25,
    faq: [
      {
        q: 'What is harem LitRPG?',
        a: 'Harem LitRPG combines explicit game mechanics (stat screens, level-ups, skill trees) with harem fantasy relationship dynamics — a protagonist who advances in power through a game-like system while building a group of close companions with romantic elements.',
      },
      {
        q: 'How does the LitRPG system work in harem LitRPG?',
        a: 'In most harem LitRPG, the game system is fully explicit — the protagonist can see their stats, skill descriptions, and level-up notifications. Companions often have their own stats and abilities that complement the protagonist\'s build. Some series tie romantic or relationship progression directly to gameplay mechanics.',
      },
      {
        q: 'Is harem LitRPG suitable for readers new to LitRPG?',
        a: 'Harem LitRPG can be a good entry point precisely because the relationship elements provide narrative hooks alongside the system mechanics. He Who Fights With Monsters and The Beginning After The End are often recommended as accessible starting points for readers discovering both genres simultaneously.',
      },
    ],
  },

  'best-completed-harem-series': {
    title: 'Best Completed Harem Fantasy Series (Finished & Bingeable)',
    description: 'Complete harem fantasy series you can read start-to-finish right now — no cliffhangers into unwritten sequels.',
    intro: `Harem fantasy is a genre that rewards long series — the relationship dynamics deepen across books, the power progression compounds, and the world-building expands in ways that shorter works can't. But all of that requires the series to actually finish.

This list is for readers who've been burned. Every series here has a genuine conclusion — a final book, a resolved main arc, a story that ended rather than just stopped. The authors finished the job.

Harem fantasy has a meaningful body of completed work, particularly in cultivation fiction where the Chinese web novel tradition has produced complete runs of extraordinary length. This list covers the best of those alongside English-original series that reached their intended conclusion.`,
    sort: 'top_rated',
    limit: 25,
    faq: [
      {
        q: 'What counts as "completed" in this list?',
        a: 'Every series here has a published final book that resolves the main narrative arc. We do not include series that have gone quiet or have had no update for several years without an explicit conclusion from the author.',
      },
      {
        q: 'What is the best completed harem series to binge first?',
        a: 'The Beginning After The End (TurtleMe) is complete and widely regarded as the best English-original harem fantasy series — it has a definitive ending, a massive readership, and holds up across its full run.',
      },
    ],
  },

  'books-like-azarinth-healer': {
    title: 'Best Books Like Azarinth Healer',
    description: 'If you loved Azarinth Healer, these books share its female protagonist, progression fantasy depth, and solo-capable healer-fighter combination.',
    intro: `Azarinth Healer — Rhaenarch's progression fantasy series following Ilea Spears, a healer who is also absolutely capable of killing everything she encounters — became one of the most beloved series in the English progression fantasy community by doing something deceptively simple: it committed. Ilea is genuinely strong, the power progression feels earned, the world keeps expanding, and the series doesn't constantly manufacture reasons to nerf the protagonist.

The combination of healer class with combat power, female protagonist who doesn't need rescuing, and the slice-of-life enjoyment of watching a character reach genuine mastery has proven hard to replicate. Most "like Azarinth Healer" recommendations fall short because they miss one of those elements.

This list focuses on books that share the specific appeal of Azarinth Healer: genuine progression, a protagonist with meaningful agency, and the satisfaction of a character who grows into something formidable.`,
    sort: 'top_rated',
    limit: 20,
    faq: [
      {
        q: 'What makes Azarinth Healer different from other progression fantasy?',
        a: 'Azarinth Healer\'s combination of female protagonist, healer-combat hybrid class, and commitment to genuine power progression without constant artificial setbacks set it apart. Ilea becomes genuinely powerful and the story doesn\'t punish her for it. The community feel of the world-building is also frequently cited.',
      },
      {
        q: 'Is Azarinth Healer a harem fantasy?',
        a: 'Azarinth Healer has some romantic elements but is primarily a solo progression fantasy — it\'s not a harem series in the traditional sense. It appears on this site because it has a significant readership overlap with the harem fantasy community and because its female protagonist is of interest to reverse harem readers.',
      },
      {
        q: 'Is Azarinth Healer complete?',
        a: 'Yes — Azarinth Healer is a complete series. You can read the full story from beginning to end without waiting for further installments.',
      },
    ],
  },

  'best-mens-adventure-romance': {
    title: 'Best Men\'s Adventure Romance Series',
    description: 'The best men\'s adventure fiction with strong romantic elements — action, progression, and relationships that matter.',
    intro: `Men's adventure romance is a useful label for a category that resists precise definition: fiction primarily targeting male readers that combines action, power progression, and relationship dynamics without fitting neatly into either pure LitRPG, pure harem fantasy, or pure romance. These are books where the adventure is genuine, the power fantasy is real, and the romance or relationship elements are developed enough to be a meaningful part of why readers keep coming back.

The category spans contemporary settings and epic fantasy, LitRPG and non-system progression, completed series and ongoing epics. What connects them is a tonal combination — the action and competence fantasy of men's adventure alongside the interpersonal stakes of well-written relationships.

This list captures the best men's adventure romance that doesn't fit more specific sub-genre categories. If you're looking for pure harem LitRPG or pure cultivation, see those dedicated lists. This is the broader category — and some of its best entries are genuinely excellent fiction.`,
    sort: 'top_rated',
    limit: 25,
    faq: [
      {
        q: 'What is men\'s adventure romance?',
        a: 'Men\'s adventure romance is a broad category label for fiction that combines action and adventure — often with power progression elements — with meaningful romantic or relationship dynamics, primarily targeting male readers. It overlaps with LitRPG, harem fantasy, and military fantasy.',
      },
      {
        q: 'How is men\'s adventure romance different from harem fantasy?',
        a: 'Harem fantasy specifically involves multiple simultaneous romantic interests. Men\'s adventure romance is a broader category that includes harem elements but also covers single-relationship romance in adventure settings, bromance-style relationships, and fiction where relationships are important but not necessarily romantic.',
      },
    ],
  },
};
