#!/bin/bash
_now=$(date +"%m_%d_%Y")
_file="janes_$_now.json"
echo "Writing scraped data to $_file..."
/Users/nethikasuraweera/test_scrapy/venv3s/bin/scrapy crawl janes -o $_file
