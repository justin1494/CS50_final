# NOTLY

#### Video Demo: <https://www.youtube.com/watch?v=I4PPiGlCLh0>

#### Description:

My project is a web application that lets you save all the articles that yo wish to read later.

It supports different users, and stores everything in app.db.

All you have to do is grab the URL of an article and the app will do the rest. It has web scraper build in so it fetches the H1 tag directly from the article's page.

The article card has to button one is used to open article (in another tab) and the second one is used to delete cards.

**templates FOLDER:**

-   contains every HTML template used in this project

**app.db:**

-   that is the database that my app uses. It has to tables

    -   users - that holds informations about all the users

    -   articles - that holds informations about all the articles every user has saved. Every row has foreign key that is the id of a specific user.

**app.py:**

-   this is where all the serverside happens

**helpers.py**

-   here is only one "helper" - it is a login_required dunction, that do not allow unsigned users to enter particualar links.

**scraper.py**

-   hold function find_title that, when recive a URL, while scrape the site and retrive a text in H1 tag.
