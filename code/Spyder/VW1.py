vw avazu.train.vw -c -k --passes 300 -b 24 -f avazu.model.vw --loss_function logistic --l2 0.000001
vw avazu.test.vw -t -i avazu.model.vw -p avazu.preds.txt --link logistic

vw avazu.train.vw -c -k --passes 9 -b 24 -f avazu.model.vw --holdout_off --loss_function logistic --l2 1e-9

vw avazu.train.vw -c -k --passes 300 -b 24 -f avazu.model.vw --loss_function hinge
vw avazu.test.vw -t -i avazu.model.vw -p avazu.preds.txt --link logistic




None       0.3838 8

1e-7       0.3911 4
1e-8       0.385  8
1e-9       0.3837 9
1e-10      0.3838 8




~/code/vowpal_wabbit/utl/vw-varinfo --passes 1 -b 24 --readable_model avazu.model.vw --loss_function logistic avazu.trunc_train.vw