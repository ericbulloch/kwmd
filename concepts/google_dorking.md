# Google Dorking

- [Introduction](#introduction)
- [How Google Got The Information?](#how-google-got-the-information)
- [Searching](#searching)
- [Operators](#operators)
- [Examples](#examples)

## Introduction

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

Google provides many operators to make searching more precise. There are operators that can remove results based on words or phrases. Search results can pertain to just a single or group of sites. Learning operators can make searching more enjoyable and help get answers faster. Here are a list of operators and an explaination of what they do.

| Operator | Explaination |
| --- | --- |
| " " | Double quotes are used to tell Google that I am looking for an exact phase. This can be used to find out what the name of a movie that said the quote. It can be used when Google sees that what I searched for doesn't have a lot of results and so it shows something else instead. |
| OR or `\|` | The or operator is used to tell Google that both results are good. Results can have just one of the keywords or both of the keywords. |
| AND | This operator is used to tell Google that both terms must be in the results. Having just one of the terms isn't enough, a result must have both. |
| `-` | The `-` operator will tell Google to remove any results that that contain the term after the `-` operator. |
| `*` | The `*` operator will tell Google to match any word or phrase at the position of the `*` operator. |
| ( ) | The ( ) operator will group multiple searches. This is often used in combination with the AND and OR operators. |
| define: | This operator is used to get the definition of a word or phrase. |
| cache: | This operator is used to get the most recent cache or a webpage. |
| filetype: | This operator is used to look for results that are of a particular file type (i.e. .pdf, .zip, .tar). |
| ext: | Same as filetype: |
| site: | This operator will filter all results to a single website. |
| related: | This operator will search sites that are related to the provided domain. |
| intitle: | This operator will find results that have a particular keyword in the title. |
| allintitle: | Same as intitle: but it searches for multiple keywords. |
| inurl: | Search for pages with a particular keyword in the url. |
| allinurl: | Same as inurl: but it searches multiple keywords. |
| intext: | This operator search for pages with a keyword in the content of the page. |
| allintext: | Same as intext: but it searches multiple keywords. |
| weather: | This operator searches the weather for a location. |
| stocks: | This operator searches a keyword for stock information. |
| map: | This operator will show Google Map results to show up. |
| movie: | This operator will show results for a particular movie. |
| in | This operator can be used to convert a value from one unit of measurement to another. |
| source: | This operator will search results from a particular source in Google News. |
| before: | This operator will search results before a particular date. |
| after: | This operator will search results after a particular date. |

## Examples

### Looking for emails with that username

If I discovered the username `firstlast` for a person name `First Last`, I could search for all emails address that use that username and are part of a .com top level domain with this search query:

```text
"firstlast*com
```

This would find things like `firstlast@yahoo.com` and `firstlast.123@aol.com`.

### Looking for pages that talk about SQL Injection

```text
intext:"sql injection"
```

### Looking for pages that talk about SQL Injection on TryHackMe

```
site:https://tryhackme.com intext:"sql injection"
```

### Looking for audit information

```
security audit -financial
```
