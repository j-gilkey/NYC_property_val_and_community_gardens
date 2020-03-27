# NYC_property_val_and_community_gardens

The goal of this project is to use a combination of [NYC PLUTO](https://www1.nyc.gov/site/planning/data-maps/open-data/dwn-pluto-mappluto.page) (Primary Land Use Tax Output) data and public [Rolling Sales](https://www1.nyc.gov/site/finance/taxes/property-rolling-sales-data.page)
data to model sale price of Manhattan real estate and explore the effects of the dependent variables. Specific interest was taken into measuring the effect that proximity to a community garden has to on price.

Initial notes:
* properties included in the model are limited to exclusively residential buildings in Manhattan.
* Sales entries are limited to single-unit sales only and not entire buildings
* This model is primarily intended for exploratory purposes and is under no illusions of being a perfect model of propertly value since it contains no unit-specific data


# Feature Engineering and EDA

In order to study the affect of community garden proximity a distance_to_garden metric needs to be engineered.
* Garden lots were isolated using two PLUTO criteria, lots classified as vacant that are also owned by parks. In PLUTO field terms this is LandUse = 11 and OwnerName = "NYC DEPARTMENT OF PARKS AND RECREATION"
* A KNN model was then instantiated using the lat, long of all Manhattan community gardens
* Each relevant Manhattan lots was then fed into the model and return in the distance to the closed garden

To see a thourough EDA of both datasets please refer to the presentation found [here](https://docs.google.com/presentation/d/1L8Ux4gOaie1ffT31EYIwLck_G0lXFQNpwux9fBS5fQY/edit?usp=sharing). 
