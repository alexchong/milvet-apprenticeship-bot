# Military Veteran Software Apprenticeship Bot 🎓
A Python script to web crawl listed military-veteran apprenticeship pages for specific keywords that signal open apprenticeship positions, and sends an notification via email if positions are open.

## Installation
1. Install dependencies throughp Python binary that will be used for this script
```bash
$ pip install -r requirements.txt
```
2. Write sender and recever email crendentials to `smtp.py`
```py
receiver = 'receiver@email.com'
sender = 'sender@gmail.com' # Gmail account must have Less Secured App access enabled
sender_password = 'hunter2'
```
3. Open crontab editor
```bash
$ crontab -e
```
3. Write cron job to automate scheduled task to run script
```
# m h dom mon dow command
* 8 * * * /absolute/path/to/python absolute/path/to/milvet-apprentice.py
#
```

## Usage
#### To add an apprenticeship page to pages dictionary
Reference the following template to append an apprenticeship page to `pages_dict.py`
```py
pages_dict = {
  'Title': {
    'url': '', # URL to specific apprentice page
    'crawl': '', # BeautifulSoup.soup.find() command
    'condition': '' # text string used as signal for unavailable apprentice positions e.g. 'no jobs available at this time' 
  }
}
```