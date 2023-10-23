import requests
from bs4 import BeautifulSoup
# לא עובד
# Step 1: Fetch the PDF URL
url = "https://www.w3schools.com/js/js_statements.asp"
response = requests.get(url)

if response.status_code == 200:
    # Step 2: Parse the HTML to get the PDF link
    soup = BeautifulSoup(response.text, 'html.parser')
    link = soup.find('a')['href']

    # Step 3: Download the PDF
    pdf_url = url + link
    pdf_response = requests.get(pdf_url)

    if pdf_response.status_code == 200:
        with open('document.pdf', 'wb') as f:
            f.write(pdf_response.content)
        print('PDF downloaded successfully.')
    else:
        print('Error:', pdf_response.status_code)
else:
    print('Error:', response.status_code)
