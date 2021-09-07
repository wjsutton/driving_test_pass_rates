# Download practical driving test data from GOV website
# URL: https://www.gov.uk/government/statistical-data-sets/car-driving-test-data-by-test-centre

# Process below downloads files the following files to data/
# - "dvsa0201" all practical tests pass rates
# - "dvsa1206" all automatic test pass rates 

from requests import get  # to make GET request

# function to download files from url
def download(url, file_name):
    # open in binary mode
    with open(file_name, "wb") as file:
        # get request
        response = get(url)
        # write to file
        file.write(response.content)


# File urls
all_practical_tests = 'https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/996308/dvsa0201.ods'
auto_practical_tests = 'https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/996312/dvsa1206.ods'

# Download files
download(all_practical_tests,'data/all_practical_tests.ods')
download(auto_practical_tests,'data/auto_practical_tests.ods')

print('data downloaded')

# all test centres
# http://assets.dft.gov.uk/dvsa/find-your-nearest/practical.csv