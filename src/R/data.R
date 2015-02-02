#######################################################################################################################

gen_features <- function(th1) {

	#######################################################################################################################
	#convert variables into sequential IDs
	#th1$C1_f<-factor(th1$C1)
	#th1$C1_f_id<-as.integer(th1$C1_f)
	#th1$banner_pos_f<-factor(th1$banner_pos)
	#th1$banner_pos_f_id<-as.integer(th1$banner_pos_f)
	#th1$device_type_f<-factor(th1$device_type)
	#th1$device_type_f_id<-as.integer(th1$device_type_f)
	#th1$device_conn_type_f<-factor(th1$device_conn_type)
	#th1$device_conn_type_f_id<-as.integer(th1$device_conn_type_f)
	#th1$C14_f<-factor(th1$C14)
	#th1$C14_f_id<-as.integer(th1$C14_f)
	#th1$C15_f<-factor(th1$C15)
	#th1$C15_f_id<-as.integer(th1$C15_f)
	#th1$C16_f<-factor(th1$C16)
	#th1$C16_f_id<-as.integer(th1$C16_f)
	#th1$C17_f<-factor(th1$C17)
	#th1$C17_f_id<-as.integer(th1$C17_f)
	#th1$C18_f<-factor(th1$C18)
	#th1$C18_f_id<-as.integer(th1$C18_f)
	#th1$C19_f<-factor(th1$C19)
	#th1$C19_f_id<-as.integer(th1$C19_f)
	#th1$C20_f<-factor(th1$C20)
	#th1$C20_f_id<-as.integer(th1$C20_f)
	#th1$C21_f<-factor(th1$C21)
	#th1$C21_f_id<-as.integer(th1$C21_f)

	th1$site_id_int <- as.integer(th1$site_id)
	th1$site_domain_int <- as.integer(th1$site_domain)
	th1$site_category_int <- as.integer(th1$site_category)
	th1$app_id_int <- as.integer(th1$app_id)
	th1$app_domain_int <- as.integer(th1$app_domain)
	th1$app_category_int <- as.integer(th1$app_category)
	th1$device_id_int <- as.integer(th1$device_id)
	th1$device_ip_int <- as.integer(th1$device_ip)
	th1$device_model_int <- as.integer(th1$device_model)

	#######################################################################################################################
	#one way count
	mean_t<-with(th1[th1$split1==0,], sum(click)*1.0/length(click))
	for(ii in 4:24) {
	  print(names(th1)[ii])
	  th1$x<-th1[, ii]
	  sum1<-sqldf("select x, sum(1) as cnt
	              from th1  group by 1 ")
	  tmp<-sqldf("select cnt from th1 a left join sum1 b on a.x=b.x")
	  th1[, paste(names(th1)[ii], "_cnt", sep="")]<-tmp$cnt
	}

	#######################################################################################################################
	#selected 2-way count

	# print("C1_banner_pos_cnt")
	# th1[,"C1_banner_pos_cnt"] <- my.f2cnt(th1, "C1", "banner_pos")

	for (ii in 4:24) {
		for(jj in ii+1:24) {
			print(paste(names(th1)[ii],"_",names(th1)[jj],"_cnt", sep=""))
			th1[,paste(names(th1)[ii], "_", names(th1)[jj], "_cnt", sep="")]<-my.f2cnt(th1, names(th1)[ii], names(th1)[jj])
		}
	}

	return(th1)
}

#import and merge
train <- read.csv(file="../../data/train", colClasses=c("id"="character"))
train <- train[train$site_id=='12fb4121',]
train$split <- 0
train$split[train$hour>=14103000] <- 1
train$ws<-1
train$ws[train$hour>=14103000] <- 0

test <- read.csv(file="../../data/test", colClasses=c("id"="character"))
test$split <- 0
test$split[test$site_id=='12fb4121'] <- 2
test1 <- test[test$site_id=='12fb4121',]
test1$click <- -1
test1$split <- 2
test1$ws <- 0

data<-rbind(train, test1)
#th1 <- th1[th1$hour<=14102300,]
data$y <- data$click

fea <- gen_features(data)