import tensorflow as tf
import pandas as pd
import kagglehub

path = kagglehub.dataset_download("robikscube/hourly-energy-consumption")

print("Path to dataset files:", path)

'''
Import Hourly Energy Consumption Dataset
The hourly energy consumption datasets consist of energy (megawatt units) of different power companies in the US.
'''
path_holiday = kagglehub.dataset_download("donnetew/us-holiday-dates-2004-2021")
print("Path to holiday dataset:", path_holiday)


'''
Data Exploration and Analysis
Merging the energy consumption datasets
'''
aep = pd.read_csv(os.path.join(path, "AEP_hourly.csv"))
comed = pd.read_csv(os.path.join(path, "COMED_hourly.csv"))
dayton = pd.read_csv(os.path.join(path, "DAYTON_hourly.csv"))
deok = pd.read_csv(os.path.join(path, "DEOK_hourly.csv"))
dom = pd.read_csv(os.path.join(path, "DOM_hourly.csv"))
duq = pd.read_csv(os.path.join(path, "DUQ_hourly.csv"))
ekpc = pd.read_csv(os.path.join(path, "EKPC_hourly.csv"))
fe = pd.read_csv(os.path.join(path, "FE_hourly.csv"))
ni = pd.read_csv(os.path.join(path, "NI_hourly.csv"))
pjme = pd.read_csv(os.path.join(path, "PJME_hourly.csv"))
pjm = pd.read_csv(os.path.join(path, "pjm_hourly_est.csv")) # diff format
pjm_load = pd.read_csv(os.path.join(path, "PJM_Load_hourly.csv"))
pjmw = pd.read_csv(os.path.join(path, "PJMW_hourly.csv"))
aep["company"] = "AEP_MW"
comed["company"] = "COMED_MW"
dayton["company"] = "DAYTON_MW"
deok["company"] = "DEOK_MW"
dom["company"] = "DOM_MW"
duq["company"] = "DUQ_MW"
ekpc["company"] = "EKPC_MW"
fe["company"] = "FE_MW"
ni["company"] = "NI_MW"
pjme["company"] = "PJME_MW"
pjmw["company"] = "PJMW_MW"
pjm_load["company"] = "PJM_Load_MW"
aep = aep.rename(columns={"AEP_MW": "MW"})
comed = comed.rename(columns={"COMED_MW": "MW"})
dayton = dayton.rename(columns={"DAYTON_MW": "MW"})
deok = deok.rename(columns={"DEOK_MW": "MW"})
dom = dom.rename(columns={"DOM_MW": "MW"})
duq = duq.rename(columns={"DUQ_MW": "MW"})
ekpc = ekpc.rename(columns={"EKPC_MW": "MW"})
fe = fe.rename(columns={"FE_MW": "MW"})
ni = ni.rename(columns={"NI_MW": "MW"})
pjme = pjme.rename(columns={"PJME_MW": "MW"})
pjmw = pjmw.rename(columns={"PJMW_MW": "MW"})
pjm_load = pjm_load.rename(columns={"PJM_Load_MW": "MW"})
df_combined = pd.concat([aep, comed, dayton, deok, dom, duq, ekpc, fe, ni, pjme, pjmw, pjm_load], ignore_index=True)
df_combined.head()
df_combined.shape
df = df_combined.copy()
df.columns
'''
Check dataset type and statistical breakdown
'''
'''
Data Analysis
Get the central tendency mean and median of the energy consumption dataset to check the typical data point. Check standard deviation, skewness and kurtosis of the dataset
'''
num_att_mean = pd.DataFrame(numerical_attributes.apply(np.mean)).T
num_att_median = pd.DataFrame(numerical_attributes.apply(np.median)).T
d1 = pd.DataFrame(numerical_attributes.apply(np.std)).T # standard deviation
d2 = pd.DataFrame(numerical_attributes.apply(min)).T
d3 = pd.DataFrame(numerical_attributes.apply(max)).T
d4 = pd.DataFrame(numerical_attributes.apply(lambda x: x.max() - x.min())).T # range
d5 = pd.DataFrame(numerical_attributes.apply(lambda x: x.skew())).T # skewness
d6 = pd.DataFrame(numerical_attributes.apply(lambda x: x.kurtosis())).T # kurtosis
stats_df = pd.concat([d1,d2,d3,d4,d5,d6,num_att_mean,num_att_median]).T
# rename columns
stats_df.columns = ["std", "min", "max", "range", "skew", "kurtosis", "mean", "median"]
stats_df
'''
Check the distribution of the data
'''
import seaborn as sns
sns.histplot( df['MW'] )
'''
Data Analysis
From the histogram we can see the distribution of the data, which shows a right-skewed distribution. The high standard deviation (10534.39) also indicates a large spread and variability in the energy consumption values. Most of the data points are concentrated in the lower range, with a long tail extending to the right. The right tail indicates some extreme outliers, where energy consumption is high in some cases on certain dates, pulling the distribution to the right. We shall analysis what are the causes of these outliers and apply normalization technique to help our predictive modeling. Beause our data has a high range and standard deviation, it is better to normalize the data first so our model can converge more efficiently when learning the patterns of the training data. The mean of the dataset is 11209.25, which is higher than the median (8217.00), which is also typical in right-skewed distribution in this case.
'''
plt.figure(figsize=(14, 8))
sns.boxplot( x="company", y="MW", data=df, palette="pastel", hue="company")
plt.xticks(rotation=45, ha="right", fontsize=10)
plt.title("MW Distribution by Company")
plt.xlabel("Electric Company")
plt.ylabel("Energy Consumption in MW")
plt.show()

'''
Check if US holidays have any correlation or pattern on energy consumption
Hypothesis 1: There is more energy consumption on holiday days
Check Holiday Dates and add is_holiday boolean column
'''
#@title Check Holiday Dates and add is_holiday boolean column
df_combined["Datetime"] = pd.to_datetime(df_combined["Datetime"])
us_holidays = holidays.US()
df_combined["is_holiday"] = df_combined["Datetime"].apply(lambda x: True if x in us_holidays else False)

correlation = df_combined["is_holiday"].corr(df_combined["MW"])
print(f"Correlation between holidays and energy consumption: {correlation:.2f}")

'''
Correlation between holidays and energy consumption: -0.01
'''

holiday_consumption = df_combined.groupby("is_holiday")["MW"].mean()
print(holiday_consumption)

import matplotlib.pyplot as plt

holiday_consumption.plot(kind="bar", title="Average Energy Consumption Holidays vs. Non-holidays")
plt.ylabel("Mean Energy Consumption in MW")
plt.xticks([0, 1], ["Non-holiday", "Holiday"], rotation=0)
plt.show()

'''
Findings on correlation between average use of energy on holiday days and non-holiday days
The correation is -0.01, and from the bar chart we find the average consumption of energy is actually less on holiday days. The low negative correlation shows that there's no significant linear correlation between holidays and energy consumption.
Check specific holiday days (Thanksgiving and Christmas) and one week leading up to these holidays
Check if there's a correlationship between energy consumption one week leading up to the major holidays like Christmas and Thanksgiving, and on the day of these holidays
'''

def is_christmas(date):
    return date.month == 12 and date.day == 25

def is_thanksgiving(date):
    return date in us_holidays and us_holidays.get(date) == "Thanksgiving"

df_combined["is_christmas"] = df_combined["Datetime"].dt.date.apply(is_christmas)
df_combined["is_thanksgiving"] = df_combined["Datetime"].dt.date.apply(is_thanksgiving)

df_combined["is_week_before_christmas"] = df_combined["Datetime"].dt.date.apply(
    lambda x: (pd.Timestamp(year=x.year, month=12, day=18) <= pd.Timestamp(x) < pd.Timestamp(year=x.year, month=12, day=25))
)

df_combined["is_week_before_thanksgiving"] = df_combined["Datetime"].dt.date.apply(
    lambda x: (pd.Timestamp(x) - pd.DateOffset(weeks=1)).date() in us_holidays and us_holidays.get((pd.Timestamp(x) - pd.DateOffset(weeks=1)).date()) == "Thanksgiving"
)

'''
calculating correlation
'''

#@title calculating correlation

christmas_corr = df_combined["is_christmas"].corr(df_combined["MW"])
thanksgiving_corr = df_combined["is_thanksgiving"].corr(df_combined["MW"])
week_before_christmas_corr = df_combined["is_week_before_christmas"].corr(df_combined["MW"])
week_before_thanksgiving_corr = df_combined["is_week_before_thanksgiving"].corr(df_combined["MW"])

print(f"Correlation on Christmas: {christmas_corr:.4f}")
print(f"Correlation on Thanksgiving: {thanksgiving_corr:.4f}")
print(f"Correlation 1 week before Christmas: {week_before_christmas_corr:.4f}")
print(f"Correlation 1 week before Thanksgiving: {week_before_thanksgiving_corr:.4f}")

'''
Visualization on average daily consumption of energy one week before Christmas and On Christmas
'''

#@title Visualization on average daily consumption of energy one week before Christmas and On Christmas
# aggregate data by daily mean instead of hourly
df_combined['Date'] = df_combined['Datetime'].dt.date
daily_consumption = df_combined.groupby('Date')['MW'].mean().reset_index()

# check energy consumption pattern a week before christmas and on christmas
daily_consumption['is_christmas'] = daily_consumption['Date'].apply(lambda x: is_christmas(pd.Timestamp(x)))
daily_consumption['is_week_before_christmas'] = daily_consumption['Date'].apply(
    lambda x: pd.Timestamp(x) >= pd.Timestamp(x.year, 12, 18) and pd.Timestamp(x) < pd.Timestamp(x.year, 12, 25)
)

plt.figure(figsize=(14, 6))
plt.scatter(daily_consumption[daily_consumption['is_christmas']]['Date'],
            daily_consumption[daily_consumption['is_christmas']]['MW'],
            color='red', label="Christmas", s=50)
plt.scatter(daily_consumption[daily_consumption['is_week_before_christmas']]['Date'],
            daily_consumption[daily_consumption['is_week_before_christmas']]['MW'],
            color='orange', label="Week Before Christmas", s=50)
plt.plot(daily_consumption['Date'], daily_consumption['MW'], label="Daily Avg Energy Consumption", color='blue',alpha=0.5)


plt.title("Daily Average Energy Consumption Before and On Christmas")
plt.xlabel("Date")
plt.ylabel("Average MW")
plt.legend()
plt.grid()
plt.show()

'''
Visualization on daily average energy consumption one week before Thanksgiving and on Thanksgiving day


'''

#@title Visualization on daily average energy consumption one week before Thanksgiving and on Thanksgiving day
daily_consumption['is_thanksgiving'] = daily_consumption['Date'].apply(lambda x: is_thanksgiving(pd.Timestamp(x)))
daily_consumption['is_week_before_thanksgiving'] = daily_consumption['Date'].apply(
    lambda x: (pd.Timestamp(x) - pd.DateOffset(weeks=1)).date() in us_holidays and
              us_holidays.get((pd.Timestamp(x) - pd.DateOffset(weeks=1)).date()) == "Thanksgiving"
)

plt.figure(figsize=(14, 6))

plt.scatter(daily_consumption[daily_consumption['is_thanksgiving']]['Date'],
            daily_consumption[daily_consumption['is_thanksgiving']]['MW'],
            color='red', label="Thanksgiving", s=50)
plt.scatter(daily_consumption[daily_consumption['is_week_before_thanksgiving']]['Date'],
            daily_consumption[daily_consumption['is_week_before_thanksgiving']]['MW'],
            color='orange', label="Week Before Thanksgiving", s=100)

plt.plot(daily_consumption['Date'], daily_consumption['MW'], label="Daily Avg Energy Consumption", color='blue',alpha=0.5)

plt.title("Daily Average Energy Consumption Before and On Thanksgiving")
plt.xlabel("Date")
plt.ylabel("Average MW")
plt.legend()
plt.grid()
plt.show()



'''
Findings on correlation between major winter holidays
The correlation between holidays and a week leading up to holidays and average energy daily consumption seem very weak, suggesting there is no linear correlation. Hypothesis 1 is False and the relevance is low.

Check correlation between seasons and energy consumption
By Yian
Hypothesis 2: Different seasons could have different energy consumption needs. Seasons with higher or lower temperatures require more energy use.
'''

#@title Categorize the seasons by month
def get_season(date):
    month = date.month
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    elif month in [9, 10, 11]:
        return 'Autumn'
    return None

daily_consumption['season'] = daily_consumption['Date'].apply(lambda x: get_season(pd.Timestamp(x)))



'''
RNN Model
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
import sklearn.preprocessing
from sklearn.metrics import r2_score
from keras.layers import Dense,Dropout,SimpleRNN,LSTM
from keras.models import Sequential


#Plotting hourly energy usage:
AEP = pd.read_csv(os.path.join(path, "AEP_hourly.csv"), index_col=[0], parse_dates=[0])

mau = ["#F8766D", "#D39200", "#93AA00", "#00BA38", "#00C19F", "#00B9E3", "#619CFF", "#DB72FB"]
bieudo = AEP.plot(style='.',figsize=(15,5), color=mau[0], title='AEP')

#Data transformation
def create_features(df, label=None):
    df = df.copy()
    df['date'] = df.index
    df['hour'] = df['date'].dt.hour
    df['dayofweek'] = df['date'].dt.dayofweek
    df['quarter'] = df['date'].dt.quarter
    df['month'] = df['date'].dt.month
    df['year'] = df['date'].dt.year
    df['dayofyear'] = df['date'].dt.dayofyear
    df['dayofmonth'] = df['date'].dt.day

    X = df[['hour', 'dayofweek', 'quarter', 'month', 'year',
            'dayofyear', 'dayofmonth']]
    if label:
        y = df[label]
        return X, y
    return X

X, y = create_features(AEP, label='AEP_MW')
features_and_target = pd.concat([X, y], axis=1)
print(features_and_target)
plt.show()

plt.figure(figsize=(15,6))
data_csv = AEP.dropna()
dataset = data_csv.values
dataset = dataset.astype('float32')
max_value = np.max(dataset)
min_value = np.min(dataset)
scalar = max_value - min_value
dataset = list(map(lambda x: (x-min_value) / scalar, dataset))
plt.plot(dataset)
print(max_value, min_value)


#choosing DOM_hourly.csv data for analysis
fpath='./dataset/DOM_hourly.csv'

#Let's use datetime(2012-10-01 12:00:00,...) as index instead of numbers(0,1,...)
#This will be helpful for further data analysis as we are dealing with time series data
df = pd.read_csv(os.path.join(path, "DOM_hourly.csv"), index_col='Datetime', parse_dates=['Datetime'])
df.head()

#checking missing data
df.isna().sum()

#Data visualization

df.plot(figsize=(16,4),legend=True)

plt.title('DOM hourly power consumption data - BEFORE NORMALIZATION')

plt.show()


#Normalize DOM hourly power consumption data

def normalize_data(df):
    scaler = sklearn.preprocessing.MinMaxScaler()
    df['DOM_MW']=scaler.fit_transform(df['DOM_MW'].values.reshape(-1,1))
    return df

df_norm = normalize_data(df)
df_norm.shape

#Visualize data after normalization

df_norm.plot(figsize=(16,4),legend=True)

plt.title('DOM hourly power consumption data - AFTER NORMALIZATION')

plt.show()


# train data for deep learning models

def load_data(stock, seq_len):
    X_train = []
    y_train = []
    for i in range(seq_len, len(stock)):
        X_train.append(stock.iloc[i - seq_len: i, 0])
        y_train.append(stock.iloc[i, 0])

    # 1 last 6189 days are going to be used in test
    X_test = X_train[110000:]
    y_test = y_train[110000:]

    # 2 first 110000 days are going to be used in training
    X_train = X_train[:110000]
    y_train = y_train[:110000]

    # 3 convert to numpy array
    X_train = np.array(X_train)
    y_train = np.array(y_train)

    X_test = np.array(X_test)
    y_test = np.array(y_test)

    # 4 reshape data to input into RNN models
    X_train = np.reshape(X_train, (110000, seq_len, 1))

    X_test = np.reshape(X_test, (X_test.shape[0], seq_len, 1))

    return [X_train, y_train, X_test, y_test]


#create train, test data
seq_len = 20 #choose sequence length

X_train, y_train, X_test, y_test = load_data(df, seq_len)

print('X_train.shape = ',X_train.shape)
print('y_train.shape = ', y_train.shape)
print('X_test.shape = ', X_test.shape)
print('y_test.shape = ',y_test.shape)


#RNN model
rnn_model = Sequential()
rnn_model.add(SimpleRNN(40,activation="tanh",return_sequences=True, input_shape=(X_train.shape[1],1)))
rnn_model.add(Dropout(0.15))
rnn_model.add(SimpleRNN(40,activation="tanh",return_sequences=True))
rnn_model.add(Dropout(0.15))
rnn_model.add(SimpleRNN(40,activation="tanh",return_sequences=False))
rnn_model.add(Dropout(0.15))
rnn_model.add(Dense(1))
rnn_model.summary()
rnn_model.compile(optimizer="adam",loss="MSE")
rnn_model.fit(X_train, y_train, epochs=10, batch_size=1000)


#r2 score for the values predicted by the above trained SIMPLE RNN model

rnn_predictions = rnn_model.predict(X_test)
rnn_score = r2_score(y_test,rnn_predictions)
print("R2 Score of RNN model = ",rnn_score)


# compare the actual values vs predicted values by plotting a graph

def plot_predictions(test, predicted, title):
    plt.figure(figsize=(16, 4))
    plt.plot(test, color='blue', label='Actual power consumption data')
    plt.plot(predicted, alpha=0.7, color='orange', label='Predicted power consumption data')
    plt.title(title)
    plt.xlabel('Time')
    plt.ylabel('Normalized power consumption scale')
    plt.legend()
    plt.show()
plot_predictions(y_test, rnn_predictions, "Predictions made by simple RNN model")


#train model for LSTM

lstm_model = Sequential()
lstm_model.add(LSTM(40,activation="tanh",return_sequences=True, input_shape=(X_train.shape[1],1)))
lstm_model.add(Dropout(0.15))
lstm_model.add(LSTM(40,activation="tanh",return_sequences=True))
lstm_model.add(Dropout(0.15))
lstm_model.add(LSTM(40,activation="tanh",return_sequences=False))
lstm_model.add(Dropout(0.15))
lstm_model.add(Dense(1))
lstm_model.summary()
lstm_model.compile(optimizer="adam",loss="MSE")
lstm_model.fit(X_train, y_train, epochs=10, batch_size=1000)


#r2 score for the values predicted by the above trained LSTM model
lstm_predictions = lstm_model.predict(X_test)
lstm_score = r2_score(y_test, lstm_predictions)
print("R^2 Score of LSTM model = ",lstm_score)


#actual values vs predicted values by plotting a graph
plot_predictions(y_test, lstm_predictions, "Predictions made by LSTM model")

#RNN, LSTM model by plotting data in a single graph
plt.figure(figsize=(15,8))
plt.plot(y_test, c="orange", linewidth=3, label="Original values")
plt.plot(lstm_predictions, c="red", linewidth=3, label="LSTM predictions")
plt.plot(rnn_predictions, alpha=0.5, c="blue", linewidth=3, label="RNN predictions")
plt.legend()
plt.title("Predictions vs actual data", fontsize=20)
plt.show()