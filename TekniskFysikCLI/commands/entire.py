"""The download entire library command."""

import os
import sys
from requests import get
from bs4 import BeautifulSoup as bs
from .base import Base

class Entire(Base):
    """Download every pdf that is currently uploaded."""

    def run(self):
        try:
            i = input("Creates new folder called Courses, is this ok (y/n): ")
            if i != 'y':
                raise ValueError
        except ValueError:
            print('Exiting without creating folder')
            sys.exit(0)

        newpath = os.path.join(os.getcwd(), 'Courses')
        if not os.path.exists(newpath):
            os.makedirs(newpath)

        # get course information from tekniskfysik.org
        print("Collects information on available courses.")
        course_dict = self.courses()

        for course, link in course_dict.items():
            print("Preparing download of {}.".format(course))
            # create course folder
            coursepath = os.path.join(newpath, course)
            if not os.path.exists(coursepath):
                os.makedirs(coursepath)
            # get all pdf links at course page
            pdflinks = self.pdf_links(link)
            # Download all pdfs into course folder
            self.pdf_download(pdflinks, coursepath)

    def courses(self) -> dict:
        'Retrieves links and names to courses from tekniskfysik.org'
        classifier = ['ar-ett', 'ar-tva', 'ar-tre', 'ar-tre-2']
        response = get("http://tekniskfysik.org/")
        data = response.text
        soup = bs(data, "html.parser")

        name_link_dict = {}
        for link in [x.get('href') for x in soup.find_all('a')]:
            if any(x in link for x in classifier):
                course_name = os.path.basename(link[:-1])
                if not any(x in course_name for x in classifier):
                    if course_name in name_link_dict:
                        course_name += '1'
                    name_link_dict[course_name] = link

        return name_link_dict

    def pdf_links(self, url) -> list:
        'Retrieves links to pdf files from html link'
        response = get(url)
        data = response.text
        soup = bs(data, "html.parser")

        links = []
        for link in soup.find_all('a'):
            linkstring = link.get('href')
            if '.pdf' in linkstring:
                links.append(linkstring)

        return links

    def pdf_download(self, links, path):
        'Downloads pdfs from links to path'
        for link in links:
            filename = os.path.basename(link)
            filepath = os.path.join(path, filename)
            print("Downloading {}".format(filename))
            self.download(link, filepath)

    def download(self, url, filepath):
        'Downloads binaries from url to filepath'
        # open in binary mode
        with open(filepath, 'wb') as file:
            # get request
            response = get(url)
            # write to file
            file.write(response.content)
