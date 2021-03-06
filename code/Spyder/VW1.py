L2 REgularization -
vw avazu.train.vw -c --passes 300 -b 24 -f avazu.model.vw --loss_function logistic --l2 0.000001
vw avazu.test.vw -t -i avazu.model.vw -p avazu.preds.txt --link logistic

None       0.3838 8

1e-7       0.3911 4
1e-8       0.385  8
1e-9       0.3837 9
1e-10      0.3838 8

After L1 of 1e-10 - 
1e-9       0.3837    7

L1 REgularization -
vw avazu.train.vw -c --passes 300 -b 24 -f l1_model.vw --loss_function logistic --l1 1e-9
vw avazu.test.vw -t -i avazu.model.vw -p avazu.preds.txt --link logistic


None        

1e-7     0.3983    4    3048156303
1e-8     0.3852    5    7620378900
1e-9     0.3841    9    6858345753
1e-10    0.3836    7    5334265230

Train on reduced features - 
vw avazu.train.vw -c --passes 300 -b 24 --feature_mask l1_model.vw -f avazu.model --loss_function logistic --l2 1e-9 

No l2 - 
0.3444    4    3048151581

L2 -

1e-9     0.3447  4   3048156303
1e-10    0.3445  4   3048156303


Smaller file -
vw avazu.trunc_train.vw -c --passes 300 -b 24 -f avazu.model.vw --loss_function logistic

Holdout off - 
vw avazu.train.vw -c -k --passes 9 -b 24 -f avazu.model.vw --holdout_off --loss_function logistic --l2 1e-9

HInge - 
vw avazu.train.vw -c -k --passes 300 -b 24 -f avazu.model.vw --loss_function hinge
vw avazu.test.vw -t -i avazu.model.vw -p avazu.preds.txt --link logistic



Feature names - 
~/code/vowpal_wabbit/utl/vw-varinfo -c --passes 3 -b 24 -f avazu.model.vw --loss_function logistic avazu.train.vw > varinfo.txt

vw avazu.trunc_train.vw --passes 1 -b 24 --invert_hash avazu.model.vw --loss_function logistic 


Hypersearch - 

~/code/vowpal_wabbit/utl/vw-hypersearch -L 1e-10 1e-6 vw avazu.train.vw -c --passes 300 -b 24 -f l1_model.vw --loss_function logistic --l1 %

clicks:  6865066
no_clicks:  33563901



train - 
vw avazu.train.vw -c --passes 300 -b 24 -f avazu.model.vw --loss_function logistic
vw avazu.train.vw -c --passes 8 -b 24 -f avazu.model.vw --holdout_off --loss_function logistic
test -
vw avazu.test.vw -t -i avazu.model.vw -p avazu.preds.txt --link logistic
score - 0.4059982


train - 
~/code/vowpal_wabbit/utl/vw-hypersearch -L 1e-10 1e-6 vw avazu.train.vw -c --passes 300 -b 24 -f l1_model.vw --loss_function logistic --l1 %
vw avazu.train.vw -c --passes 300 -b 24 -f avazu.model.vw --loss_function logistic --l1 1e-10
vw avazu.train.vw -c --passes 8 -b 24 -f avazu.model.vw --holdout_off --loss_function logistic --l1 1e-10
score - 0.4056106


train (weighted examples) - 
vw avazu.train.vw -c --passes 300 -b 24 -f avazu.model.vw --loss_function logistic
vw avazu.train.vw -c --passes 13 -b 24 -f avazu.model.vw --holdout_off --loss_function logistic
test -
vw avazu.test.vw -t -i avazu.model.vw -p avazu.preds.txt --link logistic
score - 0.4059982