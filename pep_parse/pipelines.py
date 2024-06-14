import csv
from collections import defaultdict
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
TIME = datetime.now().strftime('%Y-%m-%dT%H-%M-%S')
RESULTS = 'results'
RESULTS_DIR = BASE_DIR / RESULTS
STATUS_SUMMARY = f'RESULTS/status_summary_{TIME}.csv'


class PepParsePipeline:
    def __init__(self):
        RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    def open_spider(self, spider):
        self.status_count = defaultdict(int)

    def process_item(self, item, spider):
        self.status_count[item['status']] += 1
        return item

    def close_spider(self, spider):
        path = BASE_DIR / STATUS_SUMMARY
        total = sum(self.status_count.values())
        data = (
            ('Статус', 'Количество'),
            *self.status_count.items(),
            ('Total', total)
        )
        with open(path, mode='w', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(data)
