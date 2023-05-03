library("iml")
library("randomForest")

rf_house = readRDS(file = "models/house_model.rds")
house = read.csv('data/kc_house_data.csv')
house_sample = house[1:10,]
X = subset(house_sample, select = c('bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'yr_built'))
model = Predictor$new(rf_house, data = X, y = house_sample$price)
effect = FeatureEffects$new(model, features = c('bedrooms', 'bathrooms', 'sqft_living', 'floors'), method = "pdp")
png("plots/exercise_3/plot.png")
effect$plot()
dev.off()