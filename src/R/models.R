mdl_def_tree <- paste(
	"C1+banner_pos+site_id_int+C14+C15+C16+C17+C18+C19+C20+C21",
	"+site_domain_int+site_category_int+app_id_int+app_domain_int+app_category_int+device_id_int+device_ip_int+device_model_int",
	"+device_type+device_conn_type"
)

#GBM
t_frac <- with(th1, sum(split1==0)/length(split1))
gbm_model <- gbm(as.formula(paste("y~", mdl_def_tree)), weight=th1$ws,
	data=th1, train.fraction=t_frac, n.trees=50, interaction.depth=8, n.minobsinnode=20, distribution="bernoulli",
	shrinkage=0.03, bag.fraction=0.5, keep.data=FALSE, verbose=TRUE)


save(gbm_model, file="../../model/gbm_model.RData")

valid_set <- th1[th1$split1==2,]
valid_actual <- valid_set$y
valid_pred <- predict(gbm_model, newdata=valid_set, type="response", n.trees=50)
valid_loss <- LogLoss(actual=valid_actual, predicted=valid_pred)
print(valid_loss)
