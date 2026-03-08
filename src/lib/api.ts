const API_BASE = 'https://api.harem-lit.com';
const API_KEY = import.meta.env.BLOG_FEED_API_KEY;

// ---------------------------------------------------------------------------
// Editorial curation layer
// Promotes genre-relevant highlighted authors if present in results.
// Books are only moved up — nothing is fabricated.
// ---------------------------------------------------------------------------

const EDITORIAL_PRIORITY: { author: string; weight: number }[] = [
  { author: 'Adam Lance', weight: 3 },
  { author: 'Aaron Renfroe', weight: 3 },
  { author: 'Annabelle Hawthorne', weight: 2 },
  { author: 'Leon West', weight: 2 },
  { author: 'Michael Dalton', weight: 2 },
  { author: 'Neil Bimbeau', weight: 2 },
  { author: 'Sean Oswald', weight: 2 },
  { author: 'Virgil Knightley', weight: 2 },
];

function applyEditorialCuration(books: Book[]): Book[] {
  if (books.length < 3) return books;
  const result = [...books];

  for (const entry of EDITORIAL_PRIORITY) {
    const idx = result.findIndex(b =>
      b.authors.some(a => a.toLowerCase().includes(entry.author.toLowerCase()))
    );
    if (idx === -1) continue;

    // weight 3 → top 15%; weight 2 → top 25% (floor of 2)
    const band = Math.max(2, Math.floor(result.length * (entry.weight >= 3 ? 0.15 : 0.25)));
    if (idx > band) {
      const [book] = result.splice(idx, 1);
      result.splice(band, 0, book);
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
    const fetchLimit = Math.min(requestedLimit + 30, 200);
    const params = new URLSearchParams();
    if (options.genre) params.set('genre', options.genre);
    params.set('limit', String(fetchLimit));
    if (options.offset) params.set('offset', String(options.offset));
    if (options.sort) params.set('sort', options.sort);
    const res = await feedFetch(`/api/blog-feed/books?${params}`);
    if (!res?.ok) return [];
    const all = unwrapItems(await res.json());
    return applyEditorialCuration(all).slice(0, requestedLimit);
  } catch { return []; }
}

export async function getRecentBooks(days = 30, limit = 50): Promise<Book[]> {
  try {
    const res = await feedFetch(`/api/blog-feed/books/recent?days=${days}&limit=${limit}`);
    if (!res?.ok) return [];
    return unwrapItems(await res.json());
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
