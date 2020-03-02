from __future__ import print_function
import pandas as pd
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import RMSprop
from keras.optimizers import Adam, SGD
from keras.callbacks import ModelCheckpoint
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
import final_dataframe_prep


pd.set_option('display.max_columns', None)

#df = pd.read_csv('data/prepped_for_model.csv' )
#df = pd.read_csv('data/prepped_for_model_under_3mill.csv' )
df = pd.read_csv('data/prepped_for_model_logged_price.csv' )
X  = df.drop('log_price', axis=1)
Y  = df['log_price']
X_train, X_test,y_train,y_test = final_dataframe_prep.get_train_test_split(df, 'log_price')

print(X_train.shape)

def baseline_model():
    model = Sequential()
    model.add(Dense(120, kernel_initializer='normal', input_dim=35, activation='relu'))
    model.add(Dense(120, kernel_initializer='normal', activation='relu'))
    model.add(Dense(120, kernel_initializer='normal', activation='relu'))
    model.add(Dense(1, kernel_initializer='normal', activation='linear'))
    model.compile(loss='mean_squared_error', optimizer='adam', metrics=['mean_absolute_error'])
    print(model.summary())
    return model


def compile_model():
    estimator = KerasRegressor(build_fn=baseline_model, epochs=100, batch_size=5, verbose=0)
    kfold = KFold(n_splits=5)
    results = cross_val_score(estimator, X_train, y_train, cv=kfold)
    print("Baseline: %.2f (%.2f) MSE" % (results.mean(), results.std()))

model_1 = baseline_model()

checkpoint_name = 'Weights-{epoch:03d}--{val_loss:.5f}.hdf5'
checkpoint = ModelCheckpoint(checkpoint_name, monitor='val_loss', verbose = 1, save_best_only = True, mode ='auto')
callbacks_list = [checkpoint]

#model_1.fit(X, Y, epochs=40, batch_size=32, validation_split = 0.2, callbacks=callbacks_list)
model_1.fit(X, Y, epochs=40, batch_size=32, validation_split = 0.2)


df['predicted_log'] = model_1.predict(X)

df.to_csv('data/data_with_predictions_1.csv', index=False)

#compile_model()
