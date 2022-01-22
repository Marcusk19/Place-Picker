# Python-picker #
A personal project using the Google places api and IpInfo to find restaurants nearby. <br />

## Structure ##
Some things were mixed around when I started trying to package this app using Beeware,
as a result there are several folders I'm not sure what they are for yet. <br />
What I can say is that the main code I wrote is in `picker/src/picker` <br />

## Getting Started ##
Clone this repo and then install the necessary requirements by running `pip install -r requirements.txt` <br />
Run the code by changing into the `picker` directory and then run `briefcase dev` <br />
You will need to enter your api key for Google and access token for IpInfo in a config.py file similar to the `picker/src/picer/exampleConfig.py` <br />

## TODO ##
Need to finish packaging up this application and then polishing the frontend. <br />
Improvements to be made in fetching restaurants as well (more learning required for Google Places API) <br />