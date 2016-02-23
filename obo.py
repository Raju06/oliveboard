#create URLs for search results pages and save the files
def getSearchResults(query, kwparse, fromYear, fromMonth, toYear, toMonth, entries):

    import urllib2, os, re, time

    cleanQuery = re.sub(r'\W+', '', query)
    if not os.path.exists(cleanQuery):
        os.makedirs(cleanQuery)

    startValue = 0

    #Determine how many files need to be downloaded.
    pageCount = entries / 10
    remainder = entries % 10
    if remainder > 0:
        pageCount += 1

    for pages in range(1, pageCount +1):

        #each part of the URL. Split up to be easier to read.
        url = 'http://www.oldbaileyonline.org/search.jsp?foo=bar&form=searchHomePage&_divs_fulltext='
        url += query
        url += '&kwparse=' + kwparse
        url += '&_divs_div0Type_div1Type=sessionsPaper%7CtrialAccount'
        url += '&fromYear=' + fromYear
        url += '&fromMonth=' + fromMonth
        url += '&toYear=' + toYear
        url += '&toMonth=' + toMonth
        url += '&start=' + str(startValue)
        url += '&count=0'

        #download the page and save the result.
        response = urllib2.urlopen(url)
        webContent = response.read()

        #save the result to the new directory
        filename = cleanQuery + '/' + 'search-result' + str(startValue)

        f = open(filename + ".html", 'w')
        f.write(webContent)
        f.close

        startValue = startValue + 10

        #pause for 3 seconds
        time.sleep(3)

def getIndivTrials(query):
    import os, re, urllib2, time

    #import built-in python functions for building file paths
    from os.path import join as pjoin

    cleanQuery = re.sub(r'\W+', '', query)
    searchResults = os.listdir(cleanQuery)

    urls = []

    #find search-results pages
    for files in searchResults:
        if files.find("search-result") != -1:
            f = open(cleanQuery + "/" + files, 'r')
            text = f.read().split(" ")
            f.close()

            #look for trial IDs
            for words in text:
                if words.find("browse.jsp?id=") != -1:
                    #isolate the id
                    urls.append(words[words.find("id=") +3: words.find("&")])

    #new from here down!
    for items in urls:
        #generate the URL
        url = "http://www.oldbaileyonline.org/print.jsp?div=" + items

        #download the page
        socket.setdefaulttimeout(10)
        try:
            response = urllib2.urlopen(url)
            webContent = response.read()

            #create the filename and place it in the new directory
            filename = items + '.html'
            filePath = pjoin(cleanQuery, filename)

            #save the file
            f = open(filePath, 'w')
            f.write(webContent)
            f.close
        except:
            failedAttempts.append(url)
        #pause for 3 seconds
        time.sleep(3)
    print "failed to download: " + str(failedAttempts)