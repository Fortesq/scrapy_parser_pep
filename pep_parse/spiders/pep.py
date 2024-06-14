import scrapy

from pep_parse.items import PepParseItem


ALLOWED_DOMAINS = 'peps.python.org'


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = [ALLOWED_DOMAINS]
    start_urls = [f'https://{domain}/' for domain in allowed_domains]

    def parse(self, response):
        all_peps_links = response.css(
            '#numerical-index  tbody > tr > td > a::attr(href)').getall()
        for pep_link in all_peps_links:
            pep_link = pep_link + '/'
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        pep_info = response.css("section[id='pep-content']")
        number, name = (
            pep_info.css(
                'h1.page-title::text'
            ).get().split(' – ', 1)
        )
        pep_status = pep_info.css('abbr::text').get()
        pep_data = {
            'number': number.split()[1],
            'name': name,
            'status': pep_status
        }
        yield PepParseItem(pep_data)
