library(randomForest)
library(pdp)


day <- read.csv("data/day_prepared.csv")
# Set a seed for reproducibility
set.seed(123)

# Sample 500 rows randomly
sample_indices <- sample(nrow(day), 200, replace = FALSE)
day_sample <- day[sample_indices, ]

# Train a random forest model to predict the number of bikes rented
rf_model2 <- randomForest(cnt ~ temp + hum, data = day_sample)

saveRDS(rf_model2, file = 'models/RandomForest_temp_hum.rds')