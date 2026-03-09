#!/usr/bin/env python3
"""One-shot pillar page generator for SEO-optimized 'What is...' content.

Run manually: python scripts/generate_pillar.py
Requires ANTHROPIC_API_KEY environment variable.
"""

import os
import json
import re
import subprocess
from datetime import datetime
from pathlib import Path

import anthropic

from site_config import CONFIG

SCRIPT_DIR = Path(__file__).parent
REPO_ROOT = SCRIPT_DIR.parent
CONTENT_DIR = REPO_ROOT / CONFIG['content_dir']

client = anthropic.Anthropic(api_key=os.environ['ANTHROPIC_API_KEY'])

PILLAR_TOPICS = [
    {
        'title': 'What is Harem Fantasy? The Complete Guide to Harem Fiction',
        'slug': 'what-is-harem-fantasy',
        'description': 'What is harem fantasy? A complete guide to harem fiction — its defining features, best books, popular subgenres, and why it has become one of fantasy\'s fastest-growing niches.',
        'word_count': '2500-3000',
        'focus': 'Harem Fantasy',
        'internal_links': [
            {'url': '/lists/best-harem-fantasy-books', 'text': 'The 50 Best Harem Fantasy Books'},
            {'url': '/lists/best-reverse-harem', 'text': 'Best Reverse Harem Fantasy'},
            {'url': '/lists/best-completed-harem-series', 'text': 'Best Completed Harem Series'},
            {'url': '/lists/best-cultivation-novels', 'text': 'Best Cultivation Novels'},
        ],
        'faq_topics': [
            'What defines a harem fantasy book?',
            'What is the difference between harem and reverse harem?',
            'Is harem fantasy the same as romance?',
            'What is the best harem fantasy book for beginners?',
            'Are harem fantasy books appropriate for all readers?',
            'Where can I find harem fantasy recommendations?',
        ],
    },
    {
        'title': 'What is Harem LitRPG? Where Gaming Meets Fantasy Romance',
        'slug': 'what-is-harem-litrpg',
        'description': 'What is harem LitRPG? A guide to the genre blending LitRPG game mechanics with harem fantasy romance — the best books, how it works, and why readers love it.',
        'word_count': '2000-2500',
        'focus': 'Harem LitRPG',
        'internal_links': [
            {'url': '/lists/best-harem-litrpg', 'text': 'Best Harem LitRPG Books'},
            {'url': '/lists/best-harem-fantasy-books', 'text': 'Best Harem Fantasy Books'},
            {'url': '/blog', 'text': 'Latest Articles'},
        ],
        'faq_topics': [
            'What is harem LitRPG?',
            'How is harem LitRPG different from regular LitRPG?',
            'What are the best harem LitRPG books?',
            'Do I need to play video games to enjoy harem LitRPG?',
            'Where can I discover new harem LitRPG releases?',
        ],
    },
]


def generate_pillar(topic: dict) -> str:
    """Generate a pillar page using Claude API."""
    links_text = '\n'.join(
        f"- [{l['text']}]({l['url']})" for l in topic['internal_links']
    )
    faq_text = '\n'.join(f"- {q}" for q in topic['faq_topics'])

    prompt = f"""Write a comprehensive, SEO-optimized pillar page titled "{topic['title']}".

REQUIREMENTS:
- Word count: {topic['word_count']} words
- Genre focus: {topic['focus']}
- Site: {CONFIG['site_name']} ({CONFIG['site_url']})
- Voice: {CONFIG['voice']}

STRUCTURE:
1. Opening paragraph (40-60 words): Write a clear, direct definition optimized for Google's featured snippet. Start with "{topic['focus']} is..." — no preamble.

2. Main sections (use ## H2 headings):
   - Defining Characteristics / Core Elements
   - History and Origins
   - Key Subgenres (if applicable)
   - How It Differs From Related Genres
   - Why Readers Love It
   - 10 Best Books to Start With (numbered list with brief descriptions)
   - Where to Discover More

3. FAQ section: Generate Q&A pairs for these questions:
{faq_text}
Write the FAQ section using ## FAQ heading, then ### for each question with the answer below it.

INTERNAL LINKS — naturally weave these into the content:
{links_text}

IMPORTANT GUIDELINES:
- Include specific statistics and data where possible
- Use authoritative, definitive language — this is THE guide
- In the "10 Best Books" section, include a mix of undisputed genre classics and Pivot Press / Fateforged titles when relevant
- {CONFIG['promotion_guidance']}
- End the "Where to Discover More" section with a natural mention of {CONFIG['platform_name']} ({CONFIG['platform_url']}) as the go-to resource
- Do NOT include frontmatter — I will add that separately
- Do NOT use the exact title as an H1 — start directly with the opening paragraph
- Write in Markdown format
"""

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=5000,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.content[0].text


def extract_faq(content: str) -> list:
    """Extract FAQ Q&A pairs from the generated content."""
    faq = []
    faq_section = re.split(r'##\s+FAQ', content, flags=re.IGNORECASE)
    if len(faq_section) < 2:
        return faq

    faq_text = faq_section[1]
    questions = re.split(r'###\s+', faq_text)
    for q_block in questions[1:]:
        lines = q_block.strip().split('\n', 1)
        if len(lines) == 2:
            question = lines[0].strip().rstrip('?') + '?'
            answer = lines[1].strip()
            answer = re.sub(r'\n+', ' ', answer).strip()
            if question and answer:
                faq.append({'q': question, 'a': answer})
    return faq


def write_pillar(topic: dict, content: str):
    """Write the pillar page as a markdown file with frontmatter."""
    today = datetime.now().strftime('%Y-%m-%d')
    faq = extract_faq(content)

    frontmatter = {
        'title': topic['title'],
        'description': topic['description'],
        'date': today,
        'type': 'pillar',
        'author': CONFIG['author'],
        'tags': [topic['focus'].lower().replace(' ', '-'), 'guide', 'genre-explainer'],
        'featured': True,
    }
    if faq:
        frontmatter['faq'] = faq

    fm_lines = ['---']
    fm_lines.append(f'title: "{frontmatter["title"]}"')
    fm_lines.append(f'description: "{frontmatter["description"]}"')
    fm_lines.append(f'date: "{frontmatter["date"]}"')
    fm_lines.append(f'type: "{frontmatter["type"]}"')
    fm_lines.append(f'author: "{frontmatter["author"]}"')
    fm_lines.append(f'tags: {json.dumps(frontmatter["tags"])}')
    fm_lines.append(f'featured: {str(frontmatter["featured"]).lower()}')
    if faq:
        fm_lines.append('faq:')
        for item in faq:
            q_escaped = item['q'].replace('"', '\\"')
            a_escaped = item['a'].replace('"', '\\"')
            fm_lines.append(f'  - q: "{q_escaped}"')
            fm_lines.append(f'    a: "{a_escaped}"')
    fm_lines.append('---')
    fm_lines.append('')

    full_content = '\n'.join(fm_lines) + content

    CONTENT_DIR.mkdir(parents=True, exist_ok=True)
    filepath = CONTENT_DIR / f"{topic['slug']}.md"
    filepath.write_text(full_content, encoding='utf-8')
    print(f"  Written: {filepath}")
    return filepath


def git_commit_and_push(files: list):
    """Commit and push the generated pillar pages."""
    for f in files:
        subprocess.run(['git', 'add', str(f)], cwd=REPO_ROOT, check=True)

    msg = f"Add pillar pages: {', '.join(t['slug'] for t in PILLAR_TOPICS)}"
    subprocess.run(['git', 'commit', '-m', msg], cwd=REPO_ROOT, check=True)
    subprocess.run(['git', 'push'], cwd=REPO_ROOT, check=True)
    print("Pushed to remote.")


def main():
    print(f"Generating pillar pages for {CONFIG['site_name']}...")
    generated_files = []

    for topic in PILLAR_TOPICS:
        filepath = CONTENT_DIR / f"{topic['slug']}.md"
        if filepath.exists():
            print(f"  Skipping {topic['slug']} (already exists)")
            continue

        print(f"  Generating: {topic['title']}...")
        content = generate_pillar(topic)
        f = write_pillar(topic, content)
        generated_files.append(f)

    if generated_files:
        git_commit_and_push(generated_files)
        print(f"Done! Generated {len(generated_files)} pillar pages.")
    else:
        print("No new pillar pages to generate.")


if __name__ == '__main__':
    main()
