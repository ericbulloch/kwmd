# Google Dorking

I have heard this called many things over the years. Some of them include Google fu, Google hacking and Consulting the oracle. The idea is that Google has already indexed website and if you know how to search with Google, you can find information that is publicly available. The trick isn't just knowing what keywords to type, it also involves knowing what keywords to remove from results.

## How Google Got The Information?

Websites are incentivized to have Google index their site. Performing a Google search has become synonymous with browsing the web. If a website can reach a high position in a search result, it will be easy for users to find the site. There are many reasons people want others to find their site, but if I am being honest, those reasons mostly involve money.

### How does Google index a site?

The process I am describing is very simplistic, it is meant to give a very small idea of what is going on under the hood.

Google has software called a spider. A spider is a program that will go to the different pages of a website and put those pages into data storage. Another program will parse the content of the site so that it can be indexed. It will then use some in house system to determine that my website would be a good result if someone typed in a specific keyword. Now when a user types that keyword, the website shows up in the results.

Here is a simple real world example: Google sends a spider out to https://espn.com, it saves the content of the different pages in data storage. The next program looks at the pages that the spider collected for https://espn.com and determines that the site writes articles that are summaries of sports events. So a few hours when a user wants to know what the score was of the Celtics game, Google makes sure to show the latest Celtics game summary as a result on the page.

### Does Google index everything?

Yes and no. By default it will index everything that it can. You can tell it not to index things with a robots.txt file.

Usually, a website will provide a robots.txt file that tells Google what folders it can and cannot index. Most sites who do have a robots.txt file include the parts of the site that are sensitive in the disallowed section.  In other words the disallow section is a black list of pages and links that the owner of a website doesn't want Google to show to the whole world. This is why I like to check the robots.txt file of a website, it lists all the pages that they don't want the public to know about.

## Searching

There must be very few people on the planet that regularly browse the internet and have not used search. The concept is so simple (which means it was very complex to build). Search for what you are looking for. In the example above, a user could have searched any of the following and got the score:

- Boston Celtics
- Celtics score
- Celtics basketball
- Boston Celtics score

This is the most common search that people do. It is called a keyword search and as shown in the list above, there are multiple keywords that can be used to get the same thing. Keyword searching can only get you so far. Operators can be used to expand or reduce search results. Operators over a way to get fine grain granularity over what is trying to be found.

## Operators

Google provides many operators to make searching more precise. There are operators that can remove results based on words or phrases. Search results can pertain to just a single or group of sites. Learning operators can make searching more enjoyable and help get answers faster. Here are a list of operators, an explaination of what they do and an example.

| Operator | Explaination | Example |
| --- | --- | --- |
| " " | Double quotes are used to tell Google that I am looking for an exact phase. This can be used to find out what the name of a movie that said the quote. It can be used when Google sees that what I searched for doesn't have a lot of results and so it shows something else instead. | Putting names in quotes can be useful. Sometimes if the result count is low Google will show results for the first name or the last name. This is not good when you were looking for the combination. |
