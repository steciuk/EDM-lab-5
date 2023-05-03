library(randomForest)
library(ggplot2)
library(pdp)

rf_model2 = readRDS(file = 'models/RandomForest_temp_hum.rds')
day <- read.csv("data/day_prepared.csv")
pdp_data <- pdp::partial(rf_model2, pred.var = c("temp", "hum"), train=day)
png('plots/exercise_2/pdp.png')
ggplot(pdp_data, aes(x = temp, y = hum, fill = yhat)) + geom_tile() + ggtitle('Bidimensional Partial Dependency Plot.
')+ scale_fill_gradient(low = "white", high = "red", name='Bike Rentals') + theme(panel.grid.major = element_blank(),  panel.grid.minor = element_blank())+ xlab('Temperature') + ylab('Humidity')
dev.off()