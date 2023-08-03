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

## Endpoints Examples
### Search by keywords

`http://<guardian-scraper-api-url>/articles/search?query=trump`

```
[
    {
        "_id": "11d71982-4133-5cd2-8689-0f61254433f2",
        "author": [
            "Editorial"
        ],
        "headline": "The Guardian view on Donald Trump’s new indictment: America needs this trial",
        "content": "The indictment served on Donald Trump on Monday marks the beginning of a legal reckoning that is desperately required, if American democracy...",
        "published_at": "2023-08-02T18:11:55.000Z",
        "url": "https://www.theguardian.com/commentisfree/2023/aug/02/the-guardian-view-on-donald-trumps-new-indictment-america-needs-this-trial"
    },
    {
        "_id": "a0eb28db-3847-5ec9-a8d5-cd57671894b7",
        "author": [
            "Elliot Ross"
        ],
        "headline": "Don’t obsess about football selling its soul to Saudi Arabia. It sold itself to big money long ago",
        "content": "... Does the “sportswashing” work by distraction, making Saudi synonymous with football, or simply by establishing the kingdom as an unavoidable presence in public life?If sustained, the scale of the finance behind the Saudi Pro League means that, even if Mbappé follows Lionel Messi in choosing to play elsewhere, the flow of talent towards the highest pay on offer is now inevitable. If you want to watch the best players, consume the premium product, the Saudi league may soon be a fixture in your content mix. But will anything truly change in the relationship between the fans and a sport that could plausibly be under new ownership soon? Or is this merely a further debasement of an already utterly corrupted product that we’ll nevertheless keep on consuming?As the centre of power shifts, plenty of people who love football will simply borrow a phrase from Donald Trump (himself reputedly a fan of both soccer and the kingdom) and say: “I’ll still keep ...",
        "published_at": "2023-08-02T07:00:01.000Z",
        "url": "https://www.theguardian.com/commentisfree/2023/aug/02/football-saudi-arabia-big-money-cristiano-ronaldo"
    }
]
```
### Reterive All "Limited by 100"

`http://<guardian-scraper-api-url>/articles`

```
[
    {
        "_id": "0987018e-3911-5806-8f30-f49ed8c36ad9",
        "author": [],
        "headline": null,
        "content": "",
        "published_at": "2023-08-02T18:03:00.000Z",
        "url": "https://www.theguardian.com/world/video/2023/aug/02/japan-typhoon-khanun-makes-landfall-in-south-western-islands-of-okinawa-video"
    },
    {
        "_id": "11d71982-4133-5cd2-8689-0f61254433f2",
        "author": [
            "Editorial"
        ],
        "headline": "The Guardian view on Donald Trump’s new indictment: America needs this trial",
        "content": "The indictment served on Donald Trump on Monday marks the beginning of a legal reckoning that is desperately required, if American democracy is to properly free itself from his malign, insidious influence. Mr Trump already faces multiple criminal charges relating to the retention of classified national security documents and the payment of hush money to a porn star. But the gravity of the four counts outlined by the special counsel, Jack Smith, is of a different order of magnitude.Mr Trump stands accused of conspiring, in office, to overturn the result of the 2020 presidential election. Following Joe Biden’s victory, the indictment states, Mr Trump “knowingly” used false claims of electoral fraud in an attempt “to subvert the legitimate election results”. A bipartisan congressional committee report last year came to similar conclusions and provides much of the basis for the charges. But this represents the first major legal attempt to hold Mr Trump accountable for events leading up to and including the storming of the Capitol by a violent mob on 6 January 2021.The stakes could hardly be set higher. Democratic elections and the peaceful transfer of power are the cornerstones of the American republic. The testimony given to Congress indicates that Mr Trump used his authority to try to bully federal and state officials into supporting his claims that the election had been “stolen” from him. Repeatedly told that his assertions were baseless, he then mobilised a hostile crowd on 6 January to intimidate lawmakers charged with ratifying Mr Biden’s victory.It is inconceivable that Mr Trump should not be made to answer for actions that imperilled the constitutional and democratic functioning of the United States. The prosecutors’ case will hinge on their ability to prove that he knew his claims of a stolen election were bogus. But beyond the trial itself, it would be foolish to underestimate Mr Trump’s ability to turn even this situation to his own political advantage.The legal fronts on which Mr Trump is now engaged will drain his financial resources. But a narrative of victimhood and persecution has become, and will remain, the galvanising theme of his campaign. Two previous criminal indictments saw his poll ratings lift, helping him to establish a huge lead in the race for the Republican presidential nomination for 2024. Whatever the evidence to the contrary, a sizable proportion of American voters will continue to back Mr Trump’s self-serving version of reality.One of the most dangerously polarising elections in US history thus looms as, over the next 15 months, Mr Trump uses political cunning to evade the legal net that is closing around him. Through his lawyers, he will do all he can to delay matters, hoping eventually to dictate the course of events from the White House. For his part, Mr Smith said on Monday that the justice department will seek “a speedy trial”.It is in the interests of American democracy, to which Mr Trump represents a clear and present danger, that the justice department gets its wish. A healthy body politic cannot allow its founding values and core principles to be trashed with apparent impunity. Prosecutors will need to proceed with care and be alert to the complex political dynamics. But this climactic reckoning in court needs to take place before Mr Trump gets the chance to besmirch the country’s highest office all over again.",
        "published_at": "2023-08-02T18:11:55.000Z",
        "url": "https://www.theguardian.com/commentisfree/2023/aug/02/the-guardian-view-on-donald-trumps-new-indictment-america-needs-this-trial"
    }
]
```
