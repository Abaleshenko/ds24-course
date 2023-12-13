import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from urllib.request import urlretrieve

def download_images(url, save_folder='images'):
    # Create a folder to save the images if it doesn't exist
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    # Send a GET request to the URL
    response = requests.get(url)
    
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all image tags
        img_tags = soup.find_all('img')

        for img_tag in img_tags:
            # Extract the source URL of the image
            img_url = img_tag.get('src')

            if img_url:
                # Create an absolute URL if it's a relative URL
                img_url = urljoin(url, img_url)

                # Extract the image file name
                img_name = os.path.basename(urlparse(img_url).path)

                # Download and save the image
                img_path = os.path.join(save_folder, img_name)
                urlretrieve(img_url, img_path)
                print(f"Downloaded: {img_name}")

    else:
        print(f"Failed to fetch the page. Status code: {response.status_code}")

if __name__ == "__main__":
    behance_url = "https://www.behance.net/gallery/182135347/Vintage-computer-rendering-test-for-warm-light-scenes?tracking_source=for_you_logged_in_feed_recommended"
    download_images(behance_url)
