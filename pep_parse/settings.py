BOT_NAME = 'pep_parse'

PEP_SPIDER = 'pep_parse.spiders'

NEWSPIDER_MODULE = PEP_SPIDER
SPIDER_MODULES = [PEP_SPIDER]

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}

FEEDS = {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    }
}
