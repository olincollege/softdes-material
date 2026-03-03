---
title: The Requests Library
nav_order: 9
layout: default
---

# The `requests` Library

If you are not generating your own data, it is likely that you will get much of your data from the Web. Downloading a single file through your Web browser is one way to get this data, but if you need to download a large number of files, you will find it easier to automate this task using Python.

In this reading, we will describe how to use the `requests` library to programmatically download data from the Web. We recommend `requests` because it has a relatively straightforward syntax and a large number of convenience features, but keep in mind that there are other libraries that can provide similar functionality.

## HTTP

The `requests` library assumes that you know a little about HTTP, the protocol by which you access Web pages. In short, when you visit a webpage like [https://www.youtube.com/watch?v=dQw4w9WgXcQ](https://www.youtube.com/watch?v=dQw4w9WgXcQ), your computer is making an HTTP request to YouTube, whose response is the webpage content. Your browser then processes this content to show you the webpage, putting the video player, links, etc. in the correct places.

An HTTP request is a specially formatted message that provides details on what is being requested from the server. When visiting the page above, your browser contacts [https://www.youtube.com](https://www.youtube.com) with an HTTP request that includes the following information:

*   The desired page on the YouTube server, which in this case is `/watch` (we describe what `?v=dQw4w9WgXcQ` means below)
*   Cookies for any accounts logged into YouTube on the browser
*   The languages, file formats, etc., that the browser will accept as a response
*   Information about the browser’s version number and operating system (called the _user agent_)
*   Parameters for the request - in this case, there is only one parameter `v` with the value `dQw4w9WgXcQ`

This is called a GET request, and is one of the most common types of HTTP requests. Notice that the URL ends with `/watch?v=dQw4w9WgXcQ` - this is called a _query string_. In a query string, what comes before the question mark (`?`) is the page to request from the server, and what follows is a series of parameters and values written in the form `x=1&y=foo&z=true`, where each parameter (`x`, `y`, and `z`) is set to some value, and each parameter-value pair is separated by the ampersand (`&`) symbol. When using parameters in `requests`, note that parameter values should _all_ be written as strings, even if they represent other types like integers.

### Tutorial and Exercise

With this in mind, you likely have enough context to learn how to use the `requests` library. You can do this by visiting their [Quickstart page](https://requests.readthedocs.io/en/master/user/quickstart/) and reading through the end of the “Response Content” section. Do this before moving on.

If you want to test this feature for yourself, you can try accessing [this text file](/files/jabberwocky.txt), which contains the text of the Lewis Carroll poem “Jabberwocky”. Specifically, you can try a GET request for this file, and simply print the contents of the response text to see if it matches the text found in the file itself. If you want to challenge yourself, you can write the text to a new file using the techniques from above.