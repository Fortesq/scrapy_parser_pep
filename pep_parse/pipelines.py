import csv
from collections import defaultdict
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
TIME = datetime.now().strftime('%Y-%m-%dT%H-%M-%S')


class PepParsePipeline:
    def open_spider(self, spider):
        self.status_count = defaultdict(int)

    def process_item(self, item, spider):
        self.status_count[item['status']] += 1
        return item

    def close_spider(self, spider):
        path = BASE_DIR / f'results/status_summary_{TIME}.csv'
        with open(path, mode='w', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Статус', 'Количество'])
            writer.writerows(self.status_count.items())
            total = sum(self.status_count.values())
            writer.writerow(['Total', total])