# Welcome to the Wiki Project

#### Video Demo: <[URL HERE](....)>
Hello world, Welcome to GoogleClone, Marouane BEN ABBOU's CS50w first project.

## Description
The Online Encyclopedia is a web-based platform built using Python and Django, with a sprinkle of HTML, CSS, and Bootstrap. This application is designed to mimic the functionality of a Wikipedia-like online encyclopedia, where users can explore, create, edit, and search for encyclopedia entries.

## Features
The Online Encyclopedia offers several features that make it an excellent choice for anyone looking to build their own encyclopedia-style platform:

#### Entry Page
The entry page of the Online Encyclopedia allows users to view the contents of any encyclopedia entry by visiting the URL /wiki/TITLE, where TITLE is the title of the entry. If the entry exists, the user will be presented with a page that displays its contents, along with the entry's title. If the entry does not exist, the user will receive an error message indicating that the requested page was not found.

#### Home Page
The Home page of the Online Encyclopedia has been updated to allow users to directly access an entry by clicking its title. Instead of merely listing the names of all pages in the encyclopedia, the Home page provides a convenient way for users to access the entries they're interested in.

#### Search
The Online Encyclopedia also provides a powerful search function that enables users to find entries of interest. Users can type a query into the search box in the sidebar, and the application will return a list of all encyclopedia entries that have the query as a substring. If the query matches the name of an encyclopedia entry, the user will be redirected to that entry's page.

#### New Page
The Online Encyclopedia allows users to create new entries by clicking the "Create New Page" link in the sidebar. Users can enter a title for the page and its contents in Markdown format. The application will save the new entry to disk, and the user will be taken to the new entry's page. If an encyclopedia entry already exists with the provided title, the user will receive an error message.

#### Edit Page
The Online Encyclopedia enables users to edit existing entries by clicking a link on the entry's page. The user will be taken to a page where they can edit the entry's Markdown content in a textarea, which will be pre-populated with the existing content. Once the changes are saved, the user will be redirected back to the entry's page.

#### Random Page
Finally, the Online Encyclopedia provides a "Random Page" feature that allows users to explore the platform by visiting a random encyclopedia entry. This feature is accessible from the sidebar and provides a fun and easy way for users to discover new entries and expand their knowledge.

## Usage
To run the project, first make sure you have Python and Django installed on your computer. Then follow these steps:

    1. Clone or download the repository to your local machine.
    2. Open a terminal or command prompt window in the project directory.
    3. Run the command pip install -r requirements.txt to install the necessary packages.
    4. Run the command python manage.py runserver to start the local server.
    5. Open a web browser and go to http://localhost:8000/ to access the application.
And that's it! Now you can explore the various features of the Wikipedia-like online encyclopedia, from viewing and creating entries to searching and editing existing ones. Have fun!

## Conclusion
The Online Encyclopedia is a versatile and feature-rich platform that can be used to build your own encyclopedia-style website. Whether you're a hobbyist, student, or professional, this platform offers everything you need to create a powerful and user-friendly web-based encyclopedia.
