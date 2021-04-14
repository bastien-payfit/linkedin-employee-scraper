# Purpose
Given a csv file with companies' linkedin urls to scrape, credentials to a linkedin account and a set of locations, this selenium scraper returns the number of employees of the companies in this set of locations.

# I. Clone the repo 👬
1. Open *VS Code* and Open a new terminal.
2. Move to the folder where you want the code to be. In my case, it's in bastienvelitchkine/Documents/Code. 

    > If you don't know how to navigate within a terminal, check this [Cheet Sheet on Bash Commands](https://www.educative.io/blog/bash-shell-command-cheat-sheet), especially the paragraphs on *cd* and *ls* commands.

2. Switch back to github and click on *Code* (the green flashy button) 👉 *HTTPS* and copy the url. You can also copy it from here: https://github.com/bastien-payfit/linkedin-employee-scraper.git
3. Switch back to you VS Code terminal and type "git clone https://github.com/bastien-payfit/linkedin-employee-scraper.git". The folder "linkedin-employee-scraper" has successfully been created in your Code directory 🍾 The code is now on your machine.
4. Type "cd linkedin-employee-scraper" in the Terminal to move inside your newly created directory.
5. **Don't close VS Code nor the Terminal**. You'll need them later!

# II. Requirements ⚠️
Before anything, there are a few dependencies that you need to install on you're computer to run the code. Those are the following, given that you already have **Python** and **Git** installed on your computer.
## A. Chrome Driver
First you need to install Chrome Driver. Chrome Driver is a light weight web browser. It's the Chrome Driver that will navigate your webpages to extract data.

- **Check your chrome version**: You probably already have Google Chrome installed on your computer. Check it's version by:   

1. Opening Google Chrome,
2. Going to *Parameters* 👉 *About Google Chrome*,
3. Checking the browser version (it should be around 89 or 90).

- **Install Chrome Driver**:

1. Go to [Chrome Driver Downloads](https://chromedriver.chromium.org/downloads).
2. In the list of current releases, *choose the driver version that matches your Google Chrome version*.
3. Download the *chromedriver_mac64.zip* if you're working on mac.
4. Unzip the folder right where it was downloaded.
5. Move the unzipped "chromedriver" to a location of your liking. ⚠️ Don't let it stay in your downloads! It's messy, you won't remember its location and you risk deleting the file in a few months when you'll have forgotten all about selenium.
6. **Write down the location of the driver**. We'll need it later!


## B. Selenium
If chromedriver is a puppet, selenium is the puppeteer. You need selenium to tell chromedriver what to do: what pages to navigate, which data to extract, you name it!

1. Switch back to VS Code and your terminal. ⚠️ Beware! You should be in the "linkedin-employee-scraper" directory.
2. Type "pip install selenium". That's it, you installed selenium on your computer.
## C. Parsel
**Parsel** is a package that helps parse content like an html web page to find nested pieces of info. Similarly to selenium, do the following:

1. Switch back to VS Code and your terminal. ⚠️ Beware! You should still be in the "linkedin-employee-scraper" directory.
2. Type "pip install parsel" 🎉

# III. File preparation 📑
There are a few things you need to do before the code can indeed help you find the number of employees of multiple companies in different locations, on linkedin.
- Telling selenium where to find chromedriver,
- Putting your linkedin credentials somewhere safe (you need to connect to linkedin in order to see company info),
- Putting your input data (basically, the linkedin urls of the companies you want to enrich).
## A. Hard code chromedriver's location
1. Still in VS Code, click on *File* 👉 *Open* and open the *linkedin-employee-scraper* directory.
2. Open *crawling.py* and go the *openDriver* function.
3. Change the *driverPath* parameter to the location of chromedriver on your computer (you should've written that down somewhere before).
## B. Linkedin Credentials
As stated above, you need a linkedin account to surf multiple linkedin companies.
1. Create a folder *credentials* in *linkedin-employee-scraper* (you can do that from VS Code),
2. Create a csv file inside with your credentials in it. Just like that:
    > your@email.com, you_password
3. **Write down the name of this newly created file**, you'll need it later.
## C. Input Data
Finally, you need a list of linkedin urls to scrape.
1. Create a folder *data* in *linkedin-employee-scraper* (you can do that from VS Code).
2. Put your csv with all urls to scrape in it. 
    > **WARNING**! It's of the utmost importance that your urls have the following format: linkedin.com/company/company-slug`/people`.
3. This is what your csv could look like:

    > companyName,linkedIn</br>
    TAM Trainer-Akademie,https://zw.linkedin.com/company/tam-akademie/people</br>
    conversionmedia GmbH & Co KG,https://zw.linkedin.com/company/conversionmedia-gmbh-&-co.-kg/people</br>
    launchlabs GmbH,https://za.linkedin.com/company/launchlabs-berlin/people</br>
    Company Coaching,https://www.linkedin.com/showcase/all-company-coaching/people</br>
    ZentralWeb GmbH,https://www.linkedin.com/company/zentralweb-gmbh/people</br>
    Zenjob GmbH,https://www.linkedin.com/company/zenjob/people



# IV. Scrape it! 🚀
## A. Final setup
This is the part of the setup that changes before every new scrape.
1. Open *main.py* and navigate to the "PARAMETERS BELOW" section of the file.
2. Modify the parameters in the *workFiles* json:
    - **source**: the name of the csv file with urls to scrape
    - **linkedinUrlColumnIndex**: the index of the column with urls in your csv. Beware, *indexes start from 0 in Python*. With the previous csv example, for instance, the index would be 1.
    - **credentials**: the name of the csv file with your linkedin credentials.
3. Modify the **batchSize**. The batch size is the number of urls scraped in one shot. This parameter was designed to not raise Linkedin's awereness of our ongoing little scraping. 10 is a good number to start with but you can go as high as 20 accounts in one shot with some linkedin accounts.
4. Put a set of **locations** from which you want to know the number of employees. For instance `["France", "Allemagne"]`. Beware, the name of the countries should be their names in the language of the  linkedin account you're using.
## B. Scrape!
To scrape a whole batch, switch back to the terminal and type "python3 main.py".
If you have a total of 200 companies to scrape, you'll have to run this command 20 times for instance (one of the downsides of this scraper 🤷🏻‍♂️)
> **WARNING!** Wait a bit before you rerun the command, otherwise it's useless.

