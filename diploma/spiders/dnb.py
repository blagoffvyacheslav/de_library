import scrapy, os
from scrapy.http import HtmlResponse

class DnbSpider(scrapy.Spider):
    name = 'dnb'
    allowed_domains = ['dnb.de']
    start_urls = ['https://portal.dnb.de/opac/simpleSearch?query=Fischer+von+Waldheim+Gotthelf']
    # start_urls = ['http://dnb.de/']

    def parse(self, response: HtmlResponse):
        # links = response.css('')
        url = 'https://portal.dnb.de'
        links = response.xpath("""//a[starts-with(@id, 'recordLink_')]/@href""").extract()
        print('Total', len(links))
        for link in links:
            yield response.follow(url+link, callback=self.item_parse)

    def item_parse(self, response: HtmlResponse):
        # cols = response.xpath("""//table[@id='fullRecordTable']//td[1]/text()[1]""").re('[^\t\n\r]+')
        vals = response.xpath("""//table[@id='fullRecordTable']//td[2]/text()[1]""").re('[^\t\n\r]+')
        new_vals = []
        for idx, item in enumerate(vals, 1):
            for el in item:
                if el != ' ':
                    new_vals.append(item)
                    break
        name = f'{new_vals[0].replace("/","").replace(":","_")}'
        if os.path.exists(name):
            name= name + '_'
        name = name+'.txt'
        f = open(name, 'a+')
        f.write('___________________________________________\n')
        for val in new_vals:
            f.write(val+'\n')
        f.close()