# Geospatial_Project
[portada](https://github.com/Andrestart/geospatial_project/blob/master/images/geo.jpg)

# Objective
The objective of this project is to determine the perfect location for a new company in the gaming industry. In order to do that, we need to take into account  the following information:
- **Designers** need to be near to companies that do design.
- **30% of the company**  have at least 1 child.
- **Executives** like Starbucks a lot.
- **Account managers**  travel a lot.
- **CEO** is vegan.
- **Maintenance guy** would like to be close to a basketball court.


Based on all the information given by the employees, the first filters I applied in the companies database to look for possible locations were:
 1. Companies that do design.
 2. Density of Starbucks stores: the country with the most Starbucks per capita is Monaco, but there are no design companies, so I chose the second  one (United States).

Only 3 companies have been found after apllying this database filter, which are located in Ellensburg, Brooklyn and San Francisco. These 3 will be compared.

# Working plan 
![workingflow](https://github.com/AnaAGG/P3_Geospatial_Data/blob/main/Images/Work_Flow.jpg)
I used MongoDB to get the 3 companies that meet the criteria whose coordinates are located in **Ellensburg, Brooklyn and San Francisco**. 

The coordinates were used to make the API Foursquare calls filtering by "vegan restaurants", "starbucks", "school","train station subway", "basketball court" .

Once all the information was downloaded and converted to a dataframe, I made a calculation of the distances between the coordinates of origin and the information obtained from Foursquare. I used MongoDB to get the geodataframes and be able to compare the coordinates of the 3 cities and the distance to the different locations (vegan restaurants, starbucks, etc.).

In order to make the final decision of the location I have made a normalisation and assigned weights to the distances obtained. In the end, a ranking has been obtained on which the final decision has been based. 

The following resources have been used to achieve the objective of this project: 
-  [Foursquare API](https://foursquare.com/): get access to global data and  content from thousands trusted sources. To access all the necessary information about the resources surrounding the possible locations of the enterprise. 
- [MongoDB](https://www.mongodb.com/): is a document database with the scalability and flexibility that we want using querying and indexing.

### Structure of the project files

The structure of this project is composed of:
 1. A folder of notebooks: 
    a) **1_query_database.ipynb** -->with the preliminary analysis where I search for companies that meet the requirements established a priori to be able to pre-select locations. 

    b) **2_info_from_API.ipynb** --> the call is made to the API "Foursquare Developers", where we will get some preferred conditions where we want our company to be located. 

    c) **3_geoqueries.ipynb** --> we make the spatial queries to calculate the distance between each point obtained in the Foursquare API and the locations selected at the beginning.

    d) **4_geoweights.ipynb** --> the relationship between each selected parameter (vegan restaurants, starbucks, school, train station subway and basketball court) and the possible locations (Ellensburg, Brooklyn and San Francisco) is evaluated. For this purpose, a normalisation and categorisation has been used. 

 2. src folder: folder where all the .py files are stored with all the explained functions used during the whole project.

 3. newdata: you will get this folder with the cleaned and finished dataframes with the information needed when you run the program.


# Libraries used in the project

[sys](https://docs.python.org/3/library/sys.html)

[requests](https://pypi.org/project/requests/2.7.0/)

[pandas](https://pandas.pydata.org/)

[dotenv](https://pypi.org/project/python-dotenv/)

[pymongo](https://www.mongodb.com/2)

[json](https://docs.python.org/3/library/json.html)

[os](https://docs.python.org/3/library/os.html)

[geopandas](https://geopandas.org/)

[shapely](https://pypi.org/project/Shapely/)

[reduce](https://docs.python.org/3/library/functools.html)

[operator](https://docs.python.org/3/library/operator.html)

[time](https://docs.python.org/3/library/time.html)