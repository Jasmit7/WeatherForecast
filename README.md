## Weather App
This Python script fetches weather information for a city from the OpenWeatherMap API. The script also keeps track of the previous 7 days of temperature data and displays the maximum and minimum temperatures.

## Requirements
    1. Python 3
    2. requests library
    3. tabulate library
### Usage
To run the script, simply provide the name of the city as input. For example, to get the weather information for London, you would run the following command:

python weather.py London

## Output

The script will output a table with the following information:

* Current weather
* Description
* Temperature (ºF)
* Humidity (%)
* Wind Speed (mph)
* Cloudiness (%)
* Visibility (meters)
* Max Temperature (ºF)
* Min Temperature (ºF)

The output table will be formatted in a grid.

## Example

Here is an example of the output for the city of London:

* Current weather: Clouds
* Description: scattered clouds
* Temperature (ºF): 65°F (18°C)
* Humidity (%): 65%
* Wind Speed (mph): 10 mph (16 km/h)
* Cloudiness (%): 40%
* Visibility (meters): 10000 meters (10 km)
* Max Temperature (ºF): 75°F (24°C)
* Min Temperature (ºF): 55°F (13°C)

## License

This code is released under the MIT License.
Use code with caution. Learn more
