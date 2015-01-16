#2 way count
my.f2cnt<-function(th2, vn1, vn2, filter=TRUE) {
  df<-data.frame(f1=th2[,vn1], f2=th2[,vn2], filter=filter)
  sum1<-sqldf("select f1, f2, count(*) as cnt from df where filter=1 group by 1,2")
  tmp<-sqldf("select b.cnt from df a left join sum1 b on a.f1=b.f1 and a.f2=b.f2")
  tmp$cnt[is.na(tmp$cnt)]<-0
  return(tmp$cnt)
}

#3 way count
my.f3cnt<-function(th2, vn1, vn2, vn3, filter=TRUE) {
  df<-data.frame(f1=th2[,vn1], f2=th2[,vn2], f3=th2[, vn3], filter=filter)
  sum1<-sqldf("select f1, f2, f3, count(*) as cnt from df where filter=1 group by 1,2, 3")
  tmp<-sqldf("select b.cnt from df a left join sum1 b on a.f1=b.f1 and a.f2=b.f2 and a.f3=b.f3")
  tmp$cnt[is.na(tmp$cnt)]<-0
  return(tmp$cnt)
}

#shrank and randomized leave-one-out average actual for categorical variables 
my_exp1<-function(d1, vn1, vn2, y, vnp, filter, cred_k, r_k=.3){
  d2<-d1[, c(vn1, vn2, y, vnp)]
  names(d2)<-c("f1", "f2", "a", "p")
  d2$filter<-filter
  sum1<-sqldf("select f1, f2, sum(1) as cnt, sum(p) as sump, sum(a) as suma from d2 where filter=1 group by 1,2")
  tmp1<-sqldf("select a.p, b.cnt, b.sump, b.suma from d2 a left join sum1 b on a.f1=b.f1 and a.f2=b.f2")
  tmp1$cnt[is.na(tmp1$cnt)]<-0
  tmp1$avgp<-with(tmp1, sump/cnt)
  tmp1$avgp[is.na(tmp1$avgp)]<-0
  tmp1$suma[is.na(tmp1$suma)]<-0
  tmp1$cnt[filter]<-tmp1$cnt[filter]-1
  tmp1$suma[filter]<-tmp1$suma[filter]-d1$y[filter]
  tmp1$exp_a<-with(tmp1, suma/cnt)
  tmp1$adj_a<-with(tmp1, (suma+p*cred_k)/(cnt+cred_k))
  tmp1$exp_a[is.na(tmp1$exp_a)]<-tmp1$p[is.na(tmp1$exp_a)]
  tmp1$adj_a[is.na(tmp1$adj_a)]<-tmp1$p[is.na(tmp1$adj_a)]
  tmp1$adj_a[filter]<-tmp1$adj_a[filter]*(1+(runif(sum(filter))-0.5)*r_k)
  return(tmp1)
}

#calc exps for selected one way and 2 ways
tv_spec_trans<-function(th1, calc_pred=T) {
  
  
  if(calc_pred) {
    th1$pred0<-with(th1[th1$split1==0,], mean(ACTION*1.0))
    th1$pred0_offset<-0
  } else {
    th1$pred0_offset<-th1$pred0
    
  }
  th1$dummy<-1
}

#logarithmic loss
LogLoss<-function(actual, predicted) {
  predicted<-(pmax(predicted, 0.00001))
  predicted<-(pmin(predicted, 0.99999))
  result<- -1/length(actual)*(sum((actual*log(predicted)+(1-actual)*log(1-predicted))))
  return(result)
}