pages_dict = {
  'Microsoft Leap Apprenticeship Program': {
    'url': 'https://www.microsoft.com/en-us/leap/pathways/software-engineering/',
    'crawl': 'soup.find(class_="entry-content").text',
    'condition': 'Currently,  there are no open cohort application dates officially announced. Check back often for updates.'
  },
  'AWS Military Apprenticeships': {
    'url': 'https://www.amazon.jobs/en/landing_pages/mil-apprentice',
    'crawl': 'soup.find(class_="title-container").find(class_="subtitle").text',
    'condition': '0 open jobs'   
  }
}

def items():
  return pages_dict.items()