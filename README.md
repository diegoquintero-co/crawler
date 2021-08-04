# crawler

Small spider script using Scrapy to crawl data from websites and export it in JSON or CSV format.

# Instructions

In the code, replace the URL to crawl:

```start_urls = ['https://help.uscreen.tv/en/']```

# 

Use the Chrome Developer Console to get the website's element tree.

For example the location `div.collection_meta` will return all of the `div` elements matched, which includes the parent `div` of all categories in the help chenter page with the `collection_meta` CSS class.

To get the first title element of every category you can write this code: `h2.t__h3.c__primary`

You add CSS extractor `::text` to get the text content of the element.

#

CSS selector for the parent element

```for e in response.css('div.collection_meta'):```

CSS selectors for the child elements

`'title': ''.join(e.css('h2.t__h3.c__primary::text').extract()).strip(),`

`'short_description': ''.join(e.css('p.paper__preview::text').extract()).strip(),`

# Run the script

1. Set the folder where you installed the script as your current directory and activate the virtual environment with the following command via Terminal:

```. venv/bin/activate```

2. Run the script with the following command on the Terminal. You can use `export.json` or `export.csv` depending which format you want to use on your site.

```scrapy runspider spider.py -o export.json```
