# Artefact coding challenge
## News Content Collect and Store 📰

The following solution consist of two applications guardian_scraper which scrapes The Guardian News websire and a FastAPI application acting as an API Gateway for querying and reteriving scraped data.

Before you run any of these application install the depenencies by:

`pip install -r requierments.txt`

After that you must set an environment varible for MongoDB connection string:

`export MONGODB_CONNECTION=mongodb+srv://<username>:<password>@<database>.<hostname>?retryWrites=true&w=majority`

Now you can either start crawling 🕷️:

`cd guardian_scraper`

`scrapy crawl guardian_scraper`

Or expose what you collected by running FastAPI:

`python3 -m uvicorn main:app --reload`

## Summary and Ideas Worth Mentioning ✨

### Spider

the spider starts from the path `https://www.theguardian.com/world/all` and starts collecting articles from the first page till the end. It could be improved to have multiple spiders each for categorgy and section, this would benefit the solution by both enhancing its performance and enriching the metadata extracted for each article like from where which section and what are the related categories.

### API & Search 

Its a standard api the thing worth mentioning here is that how it treat user input to search the articles. it can be both senteces or keywords and there will be scoring based on how it relates to user input and it will reterive articles with the highest score. I achevied that by using an Atlas Search Index and using aggregate collection function to quickly retrieve related article. 

I had more Ideas about creating tag based search and preprocess the articles and generate tags using nltk and related tools which will make the metadata about the article very rich and it will enhance the search results, but I didn't have the time.
