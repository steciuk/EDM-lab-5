library("iml")
library("randomForest")

house = read.csv('data/kc_house_data.csv')
rf_house = randomForest(price ~ bedrooms + bathrooms + sqft_living + sqft_lot + floors + yr_built, data = house)
saveRDS(rf_house, file = "models/house_model.rds")