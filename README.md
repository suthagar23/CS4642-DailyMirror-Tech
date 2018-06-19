# CS4642 DailyMirror-Tech

This repository contains the script to crawl the code from the DialyMirror new website to create the dump contents. 
Please find the dumbed files from the outputs folder in this repository. 

Source URL : http://www.dailymirror.lk/tech

## Requirements 

You should install these following dependencies before trying this code, 
1. Python 3+
2. Scrapy
3. JSON Module

## How to run this Script 

* First clone this repository into your local machine
* Go inside the main repository folder
* type `scrapy crawl DailyMirrorTech`

## Output Files 

This repository contains 599 dumped files from the DailyMirror - Tech content News section. Each file is dumbed according to this following JSON structure, 

```
{
	"fileName": "page-15668.txt",
	"title": "Sri Lanka's Biggest Story Based Role Playing Game",
	"date_posted": "2016-12-15 09:19:59",
	"total_views": "45241",
	"total_comments": "3",
	"image_urls": [],
	"content": "Sri Lankan tech company that is being the genesis of interactive digital media",
  "comments": [{
		"commentterName": "cvs ",
		"commentterTime": "Friday, 16 December 2016 03:05 ",
		"comment": "Amazing piece of work...",
		"thumpDown": "0",
		"thumpUp": "16"
	}, {
		"commentterName": "perera ",
		"commentterTime": "Friday, 16 December 2016 20:29 ",
		"comment": "asdfgh",
		"thumpDown": "0",
		"thumpUp": "3"
	}, {
		"commentterName": "Vibhu  ",
		"commentterTime": "Sunday, 18 December 2016 07:57 ",
		"comment": "This game seems to be good. An amazing job guys..........",
		"thumpDown": "0",
		"thumpUp": "4"
	}]
}
```

 
