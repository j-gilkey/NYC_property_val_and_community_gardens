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

def baseline_model():
    #this function instantiates the nueral network with 3 layers
    model = Sequential()
    model.add(Dense(55, kernel_initializer='normal', input_dim=35, activation='relu'))
    model.add(Dense(55, kernel_initializer='normal', activation='relu'))
    model.add(Dense(1, kernel_initializer='normal', activation='linear'))
    model.compile(loss='mean_squared_error', optimizer='adam', metrics=['mean_absolute_error'])
    print(model.summary())
    return model



def neural_apartment_pricing():
    df = pd.read_csv('data/prepped_for_model_logged_price.csv' )
    #read in CSV
    X  = df.drop('log_price', axis=1)
    #break out independents
    Y  = df['log_price']
    #dependent
    X_train, X_test,y_train,y_test = final_dataframe_prep.get_train_test_split(df, 'log_price')
    #then train, test, split

    model_1 = baseline_model()
    #instantiate the model

    checkpoint_name = 'Weights-{epoch:03d}--{val_loss:.5f}.hdf5'
    checkpoint = ModelCheckpoint(checkpoint_name, monitor='val_loss', verbose = 1, save_best_only = True, mode ='auto')
    callbacks_list = [checkpoint]
    #set checkpoints and callbacks

    model_1.fit(X, Y, epochs=20, batch_size=32, validation_split = 0.2)
    #fit the model

    df['predicted_log'] = model_1.predict(X)
    #create a new column comprised of predictions for each row

    #df.to_csv('data/data_with_predictions_1.csv', index=False)

#neural_apartment_pricing()
