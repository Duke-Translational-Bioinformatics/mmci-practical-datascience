## nytimesAPI.R

## Erich S. Huang, MD, PhD
## For MMCi Practical Data Science

## REQUIRE
require(RCurl)
require(RJSONIO)
require(jpeg)

## Get Top Travel Stories
rootURL <- 'https://api.nytimes.com/svc/topstories/v2/travel.json?'
apiToken <- apiEnv$nytimesAPIKey
reqURL <- paste0(rootURL, '&api-key=', apiToken)
cat('Querying the NYTimes API')
queryResponse <- getURL(reqURL)
cat('Returning results\n')
parsedResponse <- fromJSON(queryResponse)
dataExtract <- parsedResponse$results
loopLength <- length(dataExtract)

## Loop through the response to render NYTimes Travel images from top travel stories
for(i in 1:loopLength){
  picURL <- dataExtract[[i]]$multimedia[[4]]$url
  picFile <- download.file(url = picURL, destfile = 'pic.jpg', mode = 'wb')
  pic <- readJPEG("pic.jpg",native=TRUE)
  cat(paste('Retrieving and displaying image from article ', i, '\n'))
  plot(0:1, 0:1, type = "n", ann = FALSE, axes = FALSE)
  rasterImage(pic, 0, 0, 1, 1) 
}

