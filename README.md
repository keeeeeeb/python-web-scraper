# Python Web Scraper Project

A beginner-friendly Python web scraper that collects book titles and prices from [Books to Scrape](https://books.toscrape.com/), a practice website built for learning web scraping, and saves them to a CSV file.

This project is part of my learning journey. The notes throughout this README explain the concepts as I learn them.

## What I'm Learning

**Web scraping** is using code to automatically collect data from websites instead of copying it by hand.

**Where it's used today:**

- Price tracking and comparison (e-commerce, flights, hotels)
- Market and stock research
- Collecting job listings or real estate listings
- Gathering data for research and data science projects
- Monitoring news or product availability

**The basic process:**

1. Download a page's HTML (`requests`)
2. Find the data inside the HTML (`BeautifulSoup`)
3. Save the data somewhere useful (CSV file)

## Features

- Downloads pages with `requests`
- Parses HTML with `BeautifulSoup`
- Follows "next page" links to scrape every page
- Waits between requests to avoid overloading the server
- Saves results to `books.csv`
