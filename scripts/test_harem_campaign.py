"""Frozen editorial identity and publication timing for the September campaign."""
import copy
import json
import tempfile
import unittest
from datetime import date, timedelta
from pathlib import Path
from unittest.mock import patch

import publish_scheduled_post as publisher

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    'Isekai Emperor': ('Cole', 'male', 3, '2026-09-22'),
    'Dungeon Champions': ('Rhea', 'female', 3, '2026-09-24'),
    'Fate’s Enforcer': ('Grant', 'male', 3, '2026-09-26'),
    'Isle of the Amazonian Elves': ('Tessa', 'female', 2, '2026-09-21'),
}

def campaign():
    return [p for p in publisher.load_schedule()['posts'] if p['post_type'] == 'editorial_review']

class HaremCampaignTests(unittest.TestCase):
    def test_identity_cadence_and_frozen_sources(self):
        posts = campaign()
        self.assertEqual(len(posts), 11)
        self.assertEqual(len({p['publish_date'] for p in posts}), 11)
        observed = {series: [] for series in EXPECTED}
        for post in posts:
            content, manifest, issues = publisher.validate_entry(post)
            self.assertEqual(issues, [])
            series = manifest['series']
            voice, gender, count, start = EXPECTED[series]
            self.assertEqual(manifest['voice'], voice)
            self.assertEqual(manifest['fictional_gender'], gender)
            observed[series].append(manifest['book_number'])
            self.assertEqual(post['publish_date'], (date.fromisoformat(start) + timedelta(days=7*(manifest['book_number']-1))).isoformat())
            self.assertIn(f'{voice} is a fictional {gender}', content)
            self.assertIn('not a personal reader testimonial', content)
            self.assertIn('owned by Pivot Press Publishing', content)
            self.assertIn('<small class="text-sm">', content)
            self.assertIn('selected manuscript passages', content)
            self.assertTrue(manifest['internet_sources'])
            self.assertEqual(manifest['researched_at'], '2026-09-15')
        for series, (_, _, count, _) in EXPECTED.items():
            self.assertEqual(sorted(observed[series]), list(range(1, count+1)))

    def test_publication_rehearsal_is_ordered_and_idempotent(self):
        schedule = {'version': 1, 'posts': copy.deepcopy(campaign())}
        for post in schedule['posts']:
            post['status'] = 'scheduled'
            post.pop('published_at', None)
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary)
            with patch.object(publisher, 'CONTENT_DIR', target/'posts'), patch.object(publisher, 'SCHEDULE_FILE', target/'queue.json'), patch.object(publisher, '_write_github_output'):
                self.assertIsNone(publisher.publish_due(schedule, '2026-09-20', git_push=False))
                for post in sorted(schedule['posts'], key=lambda p:p['publish_date']):
                    result = publisher.publish_due(schedule, post['publish_date'], git_push=False)
                    self.assertEqual(result['slug'], post['slug'])
                    self.assertIsNone(publisher.publish_due(schedule, post['publish_date'], git_push=False))
                    destination = target/'posts'/f"{post['publish_date']}-{post['slug']}.md"
                    self.assertEqual(destination.read_text(encoding='utf-8'), (ROOT/'scripts'/post['draft']).read_text(encoding='utf-8'))
                self.assertEqual(len(list((target/'posts').glob('*.md'))), 11)
                self.assertTrue(all(p['status']=='published' for p in json.loads((target/'queue.json').read_text())['posts']))

    def test_four_slots_and_successful_same_repo_deploy(self):
        content = (ROOT/'.github/workflows/content.yml').read_text()
        deploy = (ROOT/'.github/workflows/deploy.yml').read_text()
        for day in [1,2,4,6]:
            self.assertIn(f"cron: '0 9 * * {day}'", content)
        self.assertIn("github.event.schedule != '0 9 * * 1'", content)
        self.assertIn('workflow_run:', deploy)
        self.assertIn('workflows: ["Generate Blog Post"]', deploy)
        self.assertIn("github.event.workflow_run.conclusion == 'success'", deploy)
        self.assertIn('github.event.workflow_run.head_repository.full_name == github.repository', deploy)
        self.assertIn('branches: [main]', deploy)

if __name__ == '__main__':
    unittest.main()
