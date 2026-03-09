import requests
from bs4 import BeautifulSoup


class JobScraper:

    def scrape(self, url):

        try:

            job_id = url.split("/")[-1]

            api_url = f"https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/{job_id}"

            headers = {
                "User-Agent": "Mozilla/5.0"
            }

            response = requests.get(api_url, headers=headers)

            soup = BeautifulSoup(response.text, "html.parser")

            desc = soup.find("div", class_="show-more-less-html__markup")

            if desc:
                return desc.get_text("\n")

            return None

        except Exception as e:
            print(e)
            return None