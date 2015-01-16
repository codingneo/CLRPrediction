options(java.parameters="-Xmx8g")

require(irlba)
require(sqldf)
require(gbm)
#require(randomForest)
#require(extraTrees)
#equire(glmnet)


setwd("./")
source("utils.R")
source("data.R")
source("models.R")