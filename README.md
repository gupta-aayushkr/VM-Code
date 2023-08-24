# Issues and Important Notes
## Issue - selenium Version
pip install selenium --upgrade - if the webdriver chrome does not work due to incompatible version
can also delete and retry for selenium to work for browser
if you look closely in terminal each session has a chromedriver which needs to get upgraded when the chrome version is updated - which sadely doesn't follow in selenium

## Note - Country Keyword
Every country has varied lenght to be truncated in the Keyword. If you change the target region don't forget to change Keyword truncation in b.py