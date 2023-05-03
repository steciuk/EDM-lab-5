library("iml")
library("randomForest")

house = read.csv('data/kc_house_data.csv')
house_sample = house[1:10,]
rf_house = randomForest(price ~ bedrooms + bathrooms + sqft_living + sqft_lot + floors + yr_built, data = house_sample)

# Save an object to a file
saveRDS(rf_house, file = "models/house_model.rds")