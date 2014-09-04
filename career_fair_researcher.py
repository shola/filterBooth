__author__ = 'Mike Situ'
__email__ = 'michael.o.situ@gmail.com'
__version__ = '0.8'
__license__ = 'GPL'
__status__ = 'Prototype'

def glassdoor_rate():
    '''
    Purpose: easily obtain GlassDoor employee ratings for tech companies.
    ===========================================================================
    System Prerequisites: Python 3.4, *nix
    ===========================================================================
    Required Modules: google, bs4 (BeautifulSoup)
    ===========================================================================
    Input: create a file named 'companyList.txt' that has one company name per
    line, and place it in this scripts directory.
    ===========================================================================
    Output: CSV file named 'glassdoorRatings.txt' of company_names
    and company_ratings.
    ===========================================================================
    Motivation: the Python glassdoor module returns 'None' for most
    companies. A more robust method of rating retrieval is to visit the first
    URL from googling 'glassdoor {companyName}', parse HTML, then use CSS
    selectors to get the decimal rating.
    '''
    import google
    from urllib.request import Request, urlopen
    from bs4 import BeautifulSoup

    companies = open('companyList.txt', 'r')
    companies_ratings = open('glassdoorRatings.txt', 'w+')
    companies_ratings.write('Company Name' + '\t' + 'Rating' + '\n')

    for co in companies:
        co = co.replace('\n', '')
        co_url = next(google.search('glassdoor review' + co))
        print('processing {0}[{1}]'.format(co, co_url))

        # i'm a human, not a robot.
        req = Request(co_url, headers={'User-Agent' : 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        soup = BeautifulSoup(webpage)

        try:
            rating = soup.find('span', 'value-title')['title']
        except TypeError:
            # the BeautifulSoup search failed, there is no rating on this page
            rating = '-1'
        finally:
            print('saved: {0} {1} {2} {3}'.format(co, '|', rating, '\n'))
            companies_ratings.write(co + '\t' + rating + '\n')

if __name__ == "__main__":
    glassdoor_rate()
