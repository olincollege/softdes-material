---
title: Web Data Formats
nav_order: 12
layout: default
---

# Web Data Formats

In this reading, we describe some common types of data you can get from the Web, along with libraries for working with them.

### Pillow: Image Processing

To read media files, such as images, GIFs, and videos, you can read the HTTP response content as binary data (a sequence of bytes) instead. You can see the [“Binary Response Content”](https://requests.readthedocs.io/en/master/user/quickstart/#binary-response-content) section of the `requests` Quickstart guide for how to do this. If you want to work with images, we recommend the [Pillow library](https://python-pillow.org/), which is designed to process image files in Python.

### `requests` and `json`: Data from Web APIs

Many sites also have APIs (application programming interfaces, which allow you to send specifically formatted requests to certain URLs to receive text data for processing. For example, you may use an API to get upcoming weather and temperature data or stock prices. This data is often returned in a format called JSON (JavaScript Object Notation). The way that JSON is structured corresponds nicely to Python data types, and `requests` provides a function that allows you to parse the text of the JSON response into the appropriate Python data types. You can read about this in the [“JSON Response Content”](https://requests.readthedocs.io/en/master/user/quickstart/#json-response-content) section of the Quickstart guide. The [`json` module](https://docs.python.org/3/library/json.html) in the Python standard library also provides some useful functions for working with JSON data, including writing and reading with both strings and files.

### Beautiful Soup: Webpages in HTML

For most URLs, sending an HTTP request will simply get you the content of the webpage itself. This is almost always in a format called HTML (HyperText Markup Language). The formatting of HTML can often be quite difficult to read, and thus we recommend using the [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) library to process HTML data in Python. (Unfortunately, the documentation can be a bit difficult to understand without a decent knowledge of HTML.) If you want to learn more about HTML, we recommend [HTML Dog’s Tutorial](https://htmldog.com/guides/html/beginner/), but again, doing this is optional.

### Pandas: Data in Tables

Finally, a common format for tables of data (similar to those found in spreadsheets) is CSV (comma-separated values). For this, we recommend using the Pandas library, which makes it quite easy to work with tabular data. Pandas defines two new types: `Series`, which represents a single column of data, and `DataFrame`, which represents a spreadsheet-like table of data. As you might expect from a spreadsheet, it is possible to name or otherwise index the rows and columns. You can then work with the data using these names.

While we could try to reinvent the wheel and explain the different features of Pandas, their tutorials are excellent, and so we will link the relevant ones here:

*   [What kind of data does Pandas handle?](https://pandas.pydata.org/docs/getting_started/intro_tutorials/01_table_oriented.html)
*   [How do I read and write tabular data?](https://pandas.pydata.org/docs/getting_started/intro_tutorials/02_read_write.html)
*   [How do I select a subset of a DataFrame?](https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html)
*   [How to create new columns derived from existing columns?](https://pandas.pydata.org/docs/getting_started/intro_tutorials/05_add_columns.html)
*   [How to calculate summary statistics?](https://pandas.pydata.org/docs/getting_started/intro_tutorials/06_calculate_statistics.html)

### NumPy: Numerical Arrays

If you are working with purely numerical data, we recommend using NumPy, which is a library optimized for scientific computing with arrays. If you have worked with MATLAB in the past, you can think of NumPy as a reasonably close equivalent in Python. Particularly when working with large arrays of data, you will find that NumPy is often far faster than even Python’s built-in libraries.

NumPy has several documentation pages aimed at different audiences. If you are newer to Python programming, we recommend their [beginner’s guide](https://numpy.org/doc/stable/user/absolute_beginners.html). If you have some scientific computing experience and want a guide with more code and less explanation, we recommend the [quickstart tutorial](https://numpy.org/doc/stable/user/quickstart.html).