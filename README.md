# Parser + Converter
Wrote this utility to get tests *(those ones with questions and answers, not unit- or something)* from some special site and then convert them to `.gift` format automatically.  
## Elements
There are classes  
* Block  
* Question  
* Answer  

which were added to simplify the process of parsing html.  
Unfortunately, due to JS logic on site I had to download `.html` files manually.

## Main.py
### `save_html_to_json(html_dir, json_dir)`  
Parses all `.html` files in `html_dir` and saves them to `json_dir`.  
Also downloads images to `src/img` if there are any.
### `save_json_to_gift(json_dir, gift_dir)`
Converts all `.json` files in `json_dir` into special `.gift` format and saves them to `gift_dir`.
