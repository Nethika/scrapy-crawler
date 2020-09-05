# Scrapy Crawler for Newsletters                               

## From:

http://www.janes.com/

	
## Codes:

**janes.com/janes_archive.py**,   output: janes.com/janes_archive.json	

## Run the Code:
```bash
scrapy runspider janes_archive.py -o janes_archive.json
```

## Requirements: 

Scrapy 1.2

SelectorGadget

scrapy-deltafetch

crontab


## Daily update Automation

### Installation instructions:
```bash
$ brew install berkeley-db
$ export BERKELEYDB_DIR=/usr/local/opt/berkeley-db/
$ export YES_I_HAVE_THE_RIGHT_TO_USE_THIS_BERKELEY_DB_VERSION=1
$ pip install bsddb3
$ pip install scrapy-deltafetch
```


### Create a Scrapy Project: 

At '/Users/nethikasuraweera/scrapy_newsletters/'

```bash
scrapy startproject web_scrape janes_update
```

Project created: '/Users/nethikasuraweera/scrapy_newsletters/janes_update'

### Copy the spider (janes.py)

To: '/Users/nethikasuraweera/scrapy_newsletters/janes_update/web_scrape/spiders/'


### Changes to settings.py:
At '/Users/nethikasuraweera/scrapy_newsletters/janes_update/web_scrape/settings.py’

```bash
DELTAFETCH_ENABLED = True
DELTAFETCH_DIR = '/Users/nethikasuraweera/scrapy_newsletters/janes_update/web_scrape/deltafetch'
DELTAFETCH_RESET = False

SPIDER_MIDDLEWARES = {
      'scrapy_deltafetch.DeltaFetch': 100,
}
```


### Create run_spider.sh:

(At : '/Users/nethikasuraweera/scrapy_newsletters/janes_update/')

```bash
#!/bin/bash
_now=$(date +"%m_%d_%Y")
_file="janes_$_now.json"
echo "Writing scraped data to $_file..."
/Users/nethikasuraweera/test_scrapy/venv3s/bin/scrapy crawl janes -o $_file
```

### crontab:
```bash
52 18 * * * cd ~/scrapy_newsletters/janes_update/ && ~/scrapy_newsletters/janes_update/run_spider.sh
```

### Output:

**janes_10_19_2016.json**

At : '/Users/nethikasuraweera/scrapy_newsletters/janes_update/'
### More help:
https://github.com/scrapy-plugins/scrapy-deltafetch

https://blog.scrapinghub.com/2016/07/20/scrapy-tips-from-the-pros-july-2016/

http://stackoverflow.com/questions/20045751/enabling-deltafetch-in-scrapy

