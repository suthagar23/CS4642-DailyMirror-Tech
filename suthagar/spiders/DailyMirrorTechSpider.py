// Index No : 140611L
// ***********************************************

import scrapy
import json

class DailyMirrorTechSpider(scrapy.Spider):
    name = "DailyMirrorTech"

    TOTAL_PAGINATIONS_NUMBER_FOR_CRAWL = 20
    CONTENTS_PER_PAGINATIONS = 30

    start_urls = ['http://www.dailymirror.lk/tech']
    
    for i in range (CONTENTS_PER_PAGINATIONS, TOTAL_PAGINATIONS_NUMBER_FOR_CRAWL * CONTENTS_PER_PAGINATIONS, CONTENTS_PER_PAGINATIONS):
        domain_url = 'http://www.dailymirror.lk/tech/' + str(i)
        start_urls.append(domain_url)
    print(start_urls)

    def parse(self, response):
        links = response.css('h2.media-heading.cat-header a ::attr(href)')
        for ref in links:
            yield response.follow(ref, self.parse_page)

    def parse_page(self, response):
        pageName = response.url.split("/")[-1]
        filename = 'outputs/page-%s.txt' % pageName

        pageFile = {}
        pageFile["fileName"] =  pageName.strip()
        pageFile["title"] =  response.xpath('/html/body/div[2]/div[1]/div[5]/div[1]/h1/text()').extract_first().strip()
        pageFile["date_posted"] =  response.xpath('/html/body/div[2]/div[1]/div[5]/div[1]/div[1]/text()').extract_first().strip()
        pageFile["total_views"] =  response.xpath('/html/body/div[2]/div[1]/div[5]/div[1]/div[1]/div[2]/text()').extract_first().strip()
        pageFile["total_comments"] =  response.xpath('/html/body/div[2]/div[1]/div[5]/div[1]/div[1]/div[1]/text()').extract_first().strip()
        pageFile["image_urls"] =  response.xpath('/html/body/div[2]/div[1]/div[5]/div[1]/div[3]/div[1]/img/@src').extract()
        
        pageFile["content"] =  ""
        contents = response.xpath('/html/body/div[2]/div[1]/div[5]/div[1]/div[3]/node()/text()')
        for content in contents:
            content = content.extract().strip()
            if(content != "") :
                pageFile["content"] += content + "\n"

        idIncrement = 0
        pageFileComment = []
        while(True):
            idIncrement+=1
            commentterName = response.xpath("/html/body/div[2]/div[1]/div[5]/div[1]/div[5]/ul/li/div/div[" + str(idIncrement) + "]/div/p[1]/text()")
            commentterTime = response.xpath("/html/body/div[2]/div[1]/div[5]/div[1]/div[5]/ul/li/div/div[" + str(idIncrement) + "]/div/p[1]/small[1]/text()")
            comment = response.xpath("/html/body/div[2]/div[1]/div[5]/div[1]/div[5]/ul/li/div/div[" + str(idIncrement) + "]/div/p[2]/text()")
            thumpDown = response.xpath("/html/body/div[2]/div[1]/div[5]/div[1]/div[5]/ul/li/div/div[" + str(idIncrement) + "]/div/p[3]/span[2]/text()")
            thumpUp = response.xpath("/html/body/div[2]/div[1]/div[5]/div[1]/div[5]/ul/li/div/div[" + str(idIncrement) + "]/div/p[3]/span[4]/text()")
            if(len(commentterName.extract())>0):
                commentterName = commentterName.extract()[0]
                commentterTime = commentterTime.extract()[0]
                comment = comment.extract()[0]
                thumpDown = thumpDown.extract()[0]
                thumpUp = thumpUp.extract()[0] 
            
                commentJSON = {}
                commentJSON["commentterName"] = commentterName
                commentJSON["commentterTime"] = commentterTime
                commentJSON["comment"] = comment
                commentJSON["thumpDown"] = thumpDown
                commentJSON["thumpUp"] = thumpUp
                pageFileComment.append(commentJSON)
            else:
                break
        pageFile["comments"] = pageFileComment

        with open(filename, 'w+') as f:
            json_data = json.dumps(pageFile)
            f.write((json_data))
        self.log('Saved file %s' % filename)
