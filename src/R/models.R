train_gbm_model <- function(th1, holdout=FALSE) {
	mdl_def_tree <- paste(
		"C1+banner_pos+site_id_int+C14+C15+C16+C17+C18+C19+C20+C21",
		"+site_domain_int+site_category_int+app_id_int+app_domain_int+app_category_int+device_id_int+device_ip_int+device_model_int",
		"+device_type+device_conn_type"
		#"+C1_cnt+banner_pos_cnt",
		#"+C14_cnt+C15_cnt+C16_cnt+C17_cnt+C18_cnt+C19_cnt+C20_cnt+C21_cnt",
		#"+site_id_device_ip_cnt+app_id_device_ip_cnt+site_id_device_model_cnt+app_id_device_model_cnt"
	)

	#GBM
	if (holdout) {
		t_frac <- with(th1, sum(split==0)/length(split))
	} else {
		t_frac <- 1
	}

	print(t_frac)
	model <- gbm(as.formula(paste("y~", mdl_def_tree)), weight=th1$ws[th1$split<=1],
		data=th1[th1$split<=1,], train.fraction=t_frac, n.trees=50, interaction.depth=8, n.minobsinnode=20, distribution="bernoulli",
		shrinkage=0.03, bag.fraction=0.5, keep.data=FALSE, verbose=TRUE)

	# save(gbm_model, file="../../model/gbm_model.RData")

	return(model)
}

valid_gbm_model <- function(model, th1) {
	valid_set <- th1[th1$split==1,]
	valid_actual <- valid_set$y
	valid_pred <- predict(model, newdata=valid_set, type="response", n.trees=50)
	valid_loss <- LogLoss(actual=valid_actual, predicted=valid_pred)
	print(valid_loss)
}

gbm_model_predict <- function(model, th1, all_test, output) {
	test_set <- all_test
	test_set$pred <- -1
	test_set$pred[test_set$split==2] <- predict(model, newdata=th1[th1$split==2,], type="response", n.trees=50)

	# output
	final_output <- test_set[,c("id", "pred")]
	names(final_output)[2]<-"ACTION"
	write.csv(final_output, quote=F, file=paste(output), row.names=F)
}