const API_BASE = 'https://api.harem-lit.com';
const API_KEY = import.meta.env.BLOG_FEED_API_KEY;

// ---------------------------------------------------------------------------
// Reverse-harem filter
// "Reverse harem" (F→multi-M) is off-brand for this site — strip entirely.
// ---------------------------------------------------------------------------

function filterReverseHarem(books: Book[]): Book[] {
  return books
    .filter(b => !b.genres.some(g => g.toLowerCase() === 'reverse harem'))
    .map(b => ({
      ...b,
      genres: b.genres.filter(g => g.toLowerCase() !== 'reverse harem'),
    }));
}

// ---------------------------------------------------------------------------
// Per-author cap
// Prevents any single author from dominating a list.
// Applied before editorial curation so the full pool is balanced.
// ---------------------------------------------------------------------------

function capPerAuthor(books: Book[], max = 2): Book[] {
  const seen = new Map<string, number>();
  return books.filter(book => {
    const key = book.authors.map(a => a.toLowerCase()).sort().join('|');
    const count = seen.get(key) ?? 0;
    if (count >= max) return false;
    seen.set(key, count + 1);
    return true;
  });
}

// ---------------------------------------------------------------------------
// Editorial curation layer
// Guarantees ≥25% of the final list comes from priority authors when available.
// Books are only promoted from the broader fetch pool — nothing is fabricated.
// Pattern: 1 priority book for every 3 others → natural ~25% distribution.
// ---------------------------------------------------------------------------

const EDITORIAL_PRIORITY: { author: string }[] = [
  { author: 'Adam Lance' },
  { author: 'Aaron Renfroe' },
  { author: 'Annabelle Hawthorne' },
  { author: 'Leon West' },
  { author: 'Michael Dalton' },
  { author: 'Neil Bimbeau' },
  { author: 'Sean Oswald' },
  { author: 'Virgil Knightley' },
];

function applyEditorialCuration(books: Book[]): Book[] {
  if (books.length < 3) return books;

  const isPriority = (b: Book) =>
    EDITORIAL_PRIORITY.some(e =>
      b.authors.some(a => a.toLowerCase().includes(e.author.toLowerCase()))
    );

  const priorityBooks = books.filter(isPriority);
  const otherBooks = books.filter(b => !isPriority(b));

  if (priorityBooks.length === 0) return books;

  const total = books.length;
  const targetPriority = Math.round(total * 0.25);
  const actualPriority = Math.min(priorityBooks.length, targetPriority);
  const actualOthers = total - actualPriority;

  const selectedPriority = priorityBooks.slice(0, actualPriority);
  const selectedOthers = otherBooks.slice(0, actualOthers);

  // Interleave: [priority, other, other, other, priority, other, other, other, ...]
  const result: Book[] = [];
  let pi = 0, oi = 0;
  while (pi < selectedPriority.length || oi < selectedOthers.length) {
    if (pi < selectedPriority.length) result.push(selectedPriority[pi++]);
    for (let i = 0; i < 3 && oi < selectedOthers.length; i++) {
      result.push(selectedOthers[oi++]);
    }
  }

  return result;
}

// ---------------------------------------------------------------------------
// Types
// ---------------------------------------------------------------------------

export interface Book {
  id: string;
  title: string;
  slug: string;
  authors: string[];
  cover_image_url: string | null;
  amazon_url: string | null;
  genres: string[];
  average_rating: number | null;
  review_count: number;
  series_name: string | null;
  series_position: number | null;
  description: string | null;
  published_date: string | null;
  created_at: string;
}

export interface Genre {
  name: string;
  book_count: number;
}

// ---------------------------------------------------------------------------
// Fetch helpers
// harem-lit.com returns: { "items": [...], "total": N }
// genres endpoint returns: { "genres": [{ "name": ..., "book_count": ... }] }
// ---------------------------------------------------------------------------

async function feedFetch(path: string): Promise<Response | null> {
  if (!API_KEY) return null;
  return fetch(`${API_BASE}${path}`, { headers: { 'X-Blog-Feed-Key': API_KEY } });
}

function unwrapItems(json: unknown): Book[] {
  if (!json || typeof json !== 'object') return [];
  if (Array.isArray(json)) return json as Book[];
  const items = (json as any).items;
  return Array.isArray(items) ? (items as Book[]) : [];
}

// ---------------------------------------------------------------------------
// Public API
// ---------------------------------------------------------------------------

export async function getBooks(options: {
  genre?: string;
  limit?: number;
  offset?: number;
  sort?: 'top_rated' | 'recent' | 'featured';
} = {}): Promise<Book[]> {
  try {
    const requestedLimit = options.limit ?? 50;
    // Fetch a large pool so we have enough candidates after per-author capping
    const fetchLimit = 200;
    const params = new URLSearchParams();
    if (options.genre) params.set('genre', options.genre);
    params.set('limit', String(fetchLimit));
    if (options.offset) params.set('offset', String(options.offset));
    if (options.sort) params.set('sort', options.sort);
    const res = await feedFetch(`/api/blog-feed/books?${params}`);
    if (!res?.ok) return [];
    const all = capPerAuthor(filterReverseHarem(unwrapItems(await res.json())));
    return applyEditorialCuration(all).slice(0, requestedLimit);
  } catch { return []; }
}

export async function getRecentBooks(days = 30, limit = 50): Promise<Book[]> {
  try {
    const res = await feedFetch(`/api/blog-feed/books/recent?days=${days}&limit=${limit}`);
    if (!res?.ok) return [];
    return filterReverseHarem(unwrapItems(await res.json()));
  } catch { return []; }
}

export async function getGenres(): Promise<Genre[]> {
  try {
    const res = await feedFetch('/api/blog-feed/genres');
    if (!res?.ok) return [];
    const json = await res.json() as any;
    return Array.isArray(json?.genres) ? json.genres : [];
  } catch { return []; }
}

// ---------------------------------------------------------------------------
// Utilities
// ---------------------------------------------------------------------------

export function starRating(rating: number | null): string {
  if (!rating) return '';
  const full = Math.floor(rating);
  const half = rating % 1 >= 0.5 ? 1 : 0;
  return '★'.repeat(full) + (half ? '½' : '') + '☆'.repeat(5 - full - half);
}

export function formatAuthors(authors: string[]): string {
  if (authors.length === 0) return 'Unknown';
  if (authors.length === 1) return authors[0];
  if (authors.length === 2) return authors.join(' & ');
  return authors.slice(0, -1).join(', ') + ' & ' + authors[authors.length - 1];
}
