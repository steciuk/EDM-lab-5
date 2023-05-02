library("iml")
library("randomForest")

house = read.csv('kc_house_data.csv')
rf_house = randomForest(price ~ bedrooms + bathrooms + sqft_living + sqft_lot + floors + yr_built, data = house)
X = subset(house, select = c('bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'yr_built'))
model = Predictor$new(rf_house, data = X, y = house$price)
effect = FeatureEffects$new(model, features = c('bedrooms', 'bathrooms', 'sqft_living', 'floors'), method = "pdp")
effect$plot()