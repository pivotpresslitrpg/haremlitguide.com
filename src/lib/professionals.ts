// ---------------------------------------------------------------------------
// Industry-professional program — facts and calls to action.
//
// Every factual claim here is sourced from the live application flow on the
// platform. Do not add numbers that the platform does not publish itself.
//
// Voice note: this site is the HaremLit Guide — warm, first-person-plural, a
// community insider talking to people who already belong here. The CTA copy is
// written in that register and is deliberately NOT shared with the sister
// sites, which cover the same program in their own voices.
//
// Routing note: harem-lit.com/join is the referral signup page and has no role
// cards on it. The application entry point is /apply/industry-professional.
// ---------------------------------------------------------------------------

import { PLATFORM_BASE, PLATFORM_NAME, withUtm } from './api';

export { PLATFORM_NAME };

const PATHS = {
  directory: '/industry-professionals',
  apply: '/apply/industry-professional',
  guide: '/guides/industry-professionals',
} as const;

export type ProfessionalPath = keyof typeof PATHS;

/** Attributed deep link into the platform's professional surfaces. */
export function professionalUrl(path: ProfessionalPath, content: string): string {
  return withUtm(`${PLATFORM_BASE}${PATHS[path]}`, content);
}

// --- Roles -----------------------------------------------------------------

export interface ProfessionalRole {
  name: string;
  work: string;
  requirement: string | null;
  applyContent: string;
}

export const ROLES: ProfessionalRole[] = [
  {
    name: 'Editor',
    work: 'Developmental, line, copy, proof, and sensitivity passes — on books where the romance arc and the plot arc have to land together.',
    requirement: null,
    applyContent: 'role-editor',
  },
  {
    name: 'Narrator',
    work: 'Audiobook work quoted per finished hour, with demo reels, accent range, and the production capability to carry a large recurring cast.',
    requirement: null,
    applyContent: 'role-narrator',
  },
  {
    name: 'Cover artist',
    work: 'Covers, character art, and series branding, priced per tier — with every listed price including a commercial publishing license.',
    requirement: 'A hosted gallery of 5–10 images, an AI-use disclosure on every image, and a recorded rights attestation.',
    applyContent: 'role-artist',
  },
  {
    name: 'Beta reader',
    work: 'Feedback per 50,000 words on your own terms: turnaround, delivery format, heat-level comfort, and hard limits all declared up front. Alpha reading is an opt-in extra.',
    requirement: 'Confirmation that you have read at least 25 books in the HaremLit, monster-girl, reverse-harem, or isekai-harem space.',
    applyContent: 'role-reader',
  },
];

export const BETA_RATE_NOTE =
  'Beta readers set their own rates. The platform’s applicant guidance cites an industry norm of roughly $250–500 USD per 50,000 words for a full pass, with rush turnaround typically 1.5–2× standard.';

export const REVIEW_NOTE =
  'Applying is free. Plan 20–30 minutes the first time — everything auto-saves — and a human reviews your application within about 7 days. Your profile is public only after approval.';

// --- Homepage band -----------------------------------------------------------
// Separate copy from CTA.community on purpose: the homepage speaks to a mixed
// audience arriving cold, not to a reader who just finished a related article.
export const BAND = {
  eyebrow: 'Our professional wing',
  heading: 'The people behind your favorite series',
  body:
    'HaremLit runs on the people who love it — and the ones who work on these books now have somewhere to be found. Editors, narrators, cover artists, and beta readers, each listing their rates, availability, and boundaries openly.',
  roleLabel: 'Apply as',
};

// --- Calls to action -------------------------------------------------------

export type CtaMode = 'hire' | 'earn' | 'create' | 'community';

export interface CtaAction {
  label: string;
  path: ProfessionalPath;
  content: string;
}

export interface CtaVariant {
  eyebrow: string;
  heading: string;
  body: string;
  primary: CtaAction;
  secondary: CtaAction;
}

export const CTA: Record<CtaMode, CtaVariant> = {
  hire: {
    eyebrow: 'For authors',
    heading: 'You should not have to explain the genre to your own editor',
    body:
      'Finding someone who understands heat levels, harem pacing, and why the third love interest cannot vanish for fifteen chapters has always meant asking around and hoping. There is a directory for that now — editors, narrators, cover artists, and beta readers who work in HaremLit and men’s romance, filterable by availability and comfort zone.',
    primary: { label: 'Browse the directory', path: 'directory', content: 'cta-hire-directory' },
    secondary: { label: 'How the vetting works', path: 'guide', content: 'cta-hire-guide' },
  },

  earn: {
    eyebrow: 'For readers',
    heading: 'Twenty-five books in is not a hobby any more',
    body:
      'You already spot the pacing collapse, the arc that goes missing, the continuity slip nobody caught. Authors pay for that read before a book ships — and the application asks for your heat-level comfort and hard limits up front, so you only ever get matched with books you can honestly evaluate.',
    primary: { label: 'Apply as a beta reader', path: 'apply', content: 'cta-earn-apply' },
    secondary: { label: 'See the professionals already listed', path: 'directory', content: 'cta-earn-directory' },
  },

  create: {
    eyebrow: 'For cover artists',
    heading: 'This community can name its favorite cover artists',
    body:
      'Readers here follow artists across series and notice exactly who painted what. The directory keeps that visible: a hosted gallery, an honest AI-use disclosure on every image, a recorded rights attestation, and pricing that always includes the commercial license. Your originals stay private — only moderated display copies go public.',
    primary: { label: 'Apply as a cover artist', path: 'apply', content: 'cta-create-apply' },
    secondary: { label: 'See the current roster', path: 'directory', content: 'cta-create-directory' },
  },

  community: {
    eyebrow: 'Our professional wing',
    heading: 'The people who make these books, in one place',
    body:
      'HaremLit has always run on the people who love it. The professional directory gives the ones who work on these books — editors, narrators, cover artists, beta readers — a real listing with rates, availability, and boundaries stated openly. Authors search it free; professionals apply free.',
    primary: { label: 'Browse the directory', path: 'directory', content: 'cta-community-directory' },
    secondary: { label: 'Apply to join it', path: 'apply', content: 'cta-community-apply' },
  },
};

const ARTIST_HINTS = ['cover artist', 'visual artist', 'book cover', 'cover commission', 'artist opportunities', 'romance covers'];
const READER_HINTS = ['get paid to read', 'reader opportunities', 'alpha reader', 'paid reading'];
const AUTHOR_HINTS = ['beta reader', 'industry professional', 'writing advice', 'author resources', 'editors', 'narrators'];

function matches(haystack: string, hints: string[]): boolean {
  return hints.some((h) => haystack.includes(h));
}

/**
 * Pick the CTA register that fits a post. Artist and reader intents are checked
 * before the broader author intent because those posts also carry the generic
 * publishing tags.
 */
export function ctaModeFor(tags: string[] = [], title = ''): CtaMode {
  const hay = [...tags, title].join(' ').toLowerCase();
  if (matches(hay, ARTIST_HINTS)) return 'create';
  if (matches(hay, READER_HINTS)) return 'earn';
  if (matches(hay, AUTHOR_HINTS)) return 'hire';
  return 'community';
}
