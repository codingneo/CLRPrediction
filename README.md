CLRPrediction (v0.1)
=============

The Repository For Kaggle Avazu Click-Through Rate Prediction


VW Solution
-------------------
1. Prepare the data
pypy ./src/vw-helper/csv_to_vw_format.py

2. Train the model
vw ./data/train.vw --power_t 0.2 -b 24 -l 0.1 -q cc -f ./model/vw_model_train.vw --loss_function logistic

3. Prediction
vw ./data/valid.vw --link logistic -t -i ./model/vw_model_train.vw -p ./submissions/vw-preds-valid.txt

4. Evaluation
pypy ./src/vw-helper/vw_evaluate.py

5. Generate submission
pypy ./src/vw-helper/vw_to_submission.py


full training & submission
-------------------
vw ./data/all_train.vw --power_t 0.2 -b 24 -l 0.1 -q cc -f ./model/vw_model_train_all.vw --loss_function logistic

vw ./data/test.vw --link logistic -t -i ./model/vw_model_train_all.vw -p ./submissions/vw-preds-test.txt

pypy ./src/vw-helper/vw_to_submission.py

pypy ./src/fusion/merger.py