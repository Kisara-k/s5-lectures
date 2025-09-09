## 3. Time Series Part 1

## Questions

#### 1. What distinguishes a time series from a simple random variable with a known mean and standard deviation?  
A) Time series data points are independent of each other.  
B) Time series data points are ordered and often dependent on past values.  
C) The mean and standard deviation of a time series are always constant.  
D) Time series data can exhibit memory or autocorrelation.


#### 2. Which of the following are components of a time series?  
A) Level  
B) Trend  
C) Seasonality  
D) Autocorrelation


#### 3. Which statements about seasonality in time series are true?  
A) Seasonality always has a fixed and known period.  
B) Seasonality can be detected using autocorrelation plots.  
C) Seasonality refers to long-term economic cycles.  
D) Seasonal decomposition can separate seasonality from trend and noise.


#### 4. What does a significant spike at lag 12 in an autocorrelation plot of monthly data most likely indicate?  
A) Presence of yearly seasonality  
B) Presence of a 12-month cycle with no seasonality  
C) Random noise in the data  
D) A non-stationary trend


#### 5. Which of the following best describe the difference between cycles and seasonality?  
A) Cycles have fixed, known periods; seasonality does not.  
B) Seasonality is a repeating short-term pattern; cycles are longer-term and irregular.  
C) Cycles can be detected using spectral analysis; seasonality cannot.  
D) Cycles often relate to economic or large-scale phenomena.


#### 6. What is the primary purpose of decomposing a time series into components?  
A) To remove noise completely from the data  
B) To better understand underlying patterns and improve forecasting accuracy  
C) To convert a non-stationary series into a stationary one  
D) To separate additive and multiplicative effects for modeling


#### 7. Which of the following are true about the STL (Seasonal-Trend decomposition using LOESS) method?  
A) It uses locally weighted polynomial regression to smooth data.  
B) It requires the time series to be stationary before decomposition.  
C) It can handle complex and changing seasonal patterns.  
D) It assumes the seasonal component is multiplicative.


#### 8. In the context of time series, what does “memory” refer to?  
A) The length of the time series data  
B) The influence of past values on future values  
C) The number of seasonal cycles in the data  
D) The amount of noise present in the series


#### 9. Which of the following statements about stationarity are correct?  
A) A stationary time series has constant mean and variance over time.  
B) Stationarity implies no seasonality or trend in the data.  
C) Non-stationary series can be directly modeled using ARIMA without transformation.  
D) Stationarity can be checked using the Augmented Dickey-Fuller test.


#### 10. Which transformations can help stabilize variance in a time series with exponential growth?  
A) Logarithmic transform  
B) Square root transform  
C) Differencing  
D) Box-Cox transform


#### 11. Differencing a time series is primarily used to:  
A) Remove seasonality  
B) Remove trend and make the series stationary  
C) Stabilize variance  
D) Extract the noise component


#### 12. Which of the following are true about autocorrelation in time series?  
A) It measures the correlation between a time series and its lagged values.  
B) A high autocorrelation at lag 1 always indicates seasonality.  
C) Autocorrelation can help detect both seasonality and trend.  
D) Stationary time series often have short memory reflected in autocorrelation.


#### 13. When is a multiplicative time series model preferred over an additive model?  
A) When seasonal fluctuations increase proportionally with the level of the series  
B) When the trend is linear and constant  
C) When noise is independent of the level  
D) When seasonal effects are constant in magnitude


#### 14. Which of the following statements about cycles in time series are true?  
A) Cycles always have a fixed and known period.  
B) Spectral analysis can identify cyclical components by detecting broad peaks at low frequencies.  
C) Wavelet transform is suitable for detecting cycles in non-stationary time series.  
D) Cycles are typically shorter than seasonal patterns.


#### 15. What is the role of noise in a time series?  
A) It represents the systematic, predictable part of the data.  
B) It is the random, unsystematic variation that cannot be explained by trend or seasonality.  
C) Noise can be completely removed by decomposition.  
D) Noise can sometimes indicate anomalies or outliers.


#### 16. Which of the following are valid methods to check for stationarity in a time series?  
A) Visual inspection of mean and variance over time  
B) Seasonal-trend decomposition and analysis of residuals  
C) Augmented Dickey-Fuller test  
D) Calculating the mean absolute error


#### 17. Why might a time series with long memory require more complex models?  
A) Because distant past values influence future values, increasing model complexity  
B) Because short-term dependencies are easier to model  
C) Because long memory implies the series is stationary  
D) Because long memory time series have no trend or seasonality


#### 18. Which of the following statements about the Box-Cox transformation are true?  
A) It can only be applied to stationary time series.  
B) It includes logarithmic and square root transformations as special cases.  
C) It helps stabilize variance and make the series more normally distributed.  
D) The transformation parameter lambda is always equal to 1.


#### 19. What is the main difference between time series analysis and time series mining?  
A) Analysis focuses on identifying temporal dependencies; mining focuses on forecasting future values.  
B) Mining is about understanding what has happened; forecasting is about predicting what will happen.  
C) Time series mining involves discovering patterns and anomalies in data.  
D) Time series analysis only uses regression models.


#### 20. Which of the following statements about autocorrelation plots are correct?  
A) A significant spike at lag k indicates a potential seasonal pattern with period k.  
B) Autocorrelation plots can distinguish between noise and signal in the data.  
C) If autocorrelation is zero at all lags, the series is likely non-stationary.  
D) Autocorrelation plots are not useful for detecting cycles.



<br>

## Answers

#### 1. What distinguishes a time series from a simple random variable with a known mean and standard deviation?  
A) ✗ Time series data points are usually dependent, not independent.  
B) ✓ Time series data points are ordered and often depend on past values.  
C) ✗ Mean and standard deviation can vary over time in a time series.  
D) ✓ Time series often exhibit memory or autocorrelation.

**Correct:** B, D


#### 2. Which of the following are components of a time series?  
A) ✓ Level is the baseline average value.  
B) ✓ Trend is the long-term increase or decrease.  
C) ✓ Seasonality is the repeating short-term pattern.  
D) ✗ Autocorrelation is a property, not a component.

**Correct:** A, B, C


#### 3. Which statements about seasonality in time series are true?  
A) ✗ Seasonality usually has a fixed period but not always perfectly known.  
B) ✓ Autocorrelation plots can reveal seasonality through spikes at seasonal lags.  
C) ✗ Seasonality is short-term; economic cycles are cyclical, not seasonal.  
D) ✓ Seasonal decomposition separates seasonality from trend and noise.

**Correct:** B, D


#### 4. What does a significant spike at lag 12 in an autocorrelation plot of monthly data most likely indicate?  
A) ✓ Indicates yearly seasonality (12 months).  
B) ✗ Cycle is irregular and not fixed at lag 12.  
C) ✗ Random noise does not produce significant spikes.  
D) ✗ Spike at lag 12 is more related to seasonality than trend.

**Correct:** A


#### 5. Which statements best describe the difference between cycles and seasonality?  
A) ✗ Cycles do not have fixed periods; seasonality does.  
B) ✓ Seasonality is fixed and repeating; cycles are longer-term and irregular.  
C) ✗ Both can be detected by spectral analysis, but seasonality shows sharp peaks.  
D) ✓ Cycles often relate to economic or large-scale phenomena.

**Correct:** B, D


#### 6. What is the primary purpose of decomposing a time series into components?  
A) ✗ Noise cannot be completely removed.  
B) ✓ Helps understand patterns and improve forecasting.  
C) ✗ Decomposition itself does not guarantee stationarity.  
D) ✓ Separates additive and multiplicative effects for modeling.

**Correct:** B, D


#### 7. Which of the following are true about the STL method?  
A) ✓ Uses locally weighted polynomial regression (LOESS).  
B) ✗ Does not require stationarity before decomposition.  
C) ✓ Can handle complex and changing seasonal patterns.  
D) ✗ STL can be used with additive or multiplicative models, not only multiplicative.

**Correct:** A, C


#### 8. In the context of time series, what does “memory” refer to?  
A) ✗ Length of data is unrelated to memory.  
B) ✓ Influence of past values on future values.  
C) ✗ Number of seasonal cycles is unrelated to memory.  
D) ✗ Noise is random variation, not memory.

**Correct:** B


#### 9. Which of the following statements about stationarity are correct?  
A) ✓ Stationary series have constant mean and variance.  
B) ✓ Stationarity implies no trend or seasonality.  
C) ✗ Non-stationary series usually require transformation before ARIMA.  
D) ✓ ADF test is a standard stationarity test.

**Correct:** A, B, D


#### 10. Which transformations can help stabilize variance in a time series with exponential growth?  
A) ✓ Log transform reduces exponential trends.  
B) ✓ Square root transform can reduce quadratic growth.  
C) ✗ Differencing removes trend, not variance instability.  
D) ✓ Box-Cox transform generalizes log and sqrt transforms.

**Correct:** A, B, D


#### 11. Differencing a time series is primarily used to:  
A) ✗ Differencing does not remove seasonality directly.  
B) ✓ Removes trend and helps achieve stationarity.  
C) ✗ Variance stabilization is done by transformations, not differencing.  
D) ✗ Differencing does not isolate noise.

**Correct:** B


#### 12. Which of the following are true about autocorrelation in time series?  
A) ✓ Measures correlation between series and lagged values.  
B) ✗ High autocorrelation at lag 1 may indicate trend, not necessarily seasonality.  
C) ✓ Autocorrelation helps detect both seasonality and trend.  
D) ✓ Stationary series often have short memory reflected in autocorrelation.

**Correct:** A, C, D


#### 13. When is a multiplicative time series model preferred over an additive model?  
A) ✓ When seasonal fluctuations grow proportionally with the level.  
B) ✗ Linear and constant trend fits additive better.  
C) ✗ Noise independence is not a deciding factor here.  
D) ✗ Constant seasonal effects favor additive models.

**Correct:** A


#### 14. Which of the following statements about cycles in time series are true?  
A) ✗ Cycles do not have fixed periods.  
B) ✓ Spectral analysis shows broad peaks at low frequencies for cycles.  
C) ✓ Wavelet transform is suitable for non-stationary series and cycles.  
D) ✗ Cycles are typically longer than seasonal patterns.

**Correct:** B, C


#### 15. What is the role of noise in a time series?  
A) ✗ Noise is random, not systematic.  
B) ✓ Noise is random variation unexplained by trend or seasonality.  
C) ✗ Noise cannot be completely removed by decomposition.  
D) ✓ Noise can indicate anomalies or outliers.

**Correct:** B, D


#### 16. Which of the following are valid methods to check for stationarity in a time series?  
A) ✓ Visual inspection of mean and variance over time.  
B) ✓ Seasonal-trend decomposition to analyze residuals.  
C) ✓ Augmented Dickey-Fuller test.  
D) ✗ Mean absolute error measures forecast accuracy, not stationarity.

**Correct:** A, B, C


#### 17. Why might a time series with long memory require more complex models?  
A) ✓ Because distant past values influence future values, increasing complexity.  
B) ✗ Short-term dependencies are simpler but not the reason for complexity here.  
C) ✗ Long memory series are often non-stationary.  
D) ✗ Long memory does not imply absence of trend or seasonality.

**Correct:** A


#### 18. Which of the following statements about the Box-Cox transformation are true?  
A) ✗ It can be applied to non-stationary series to stabilize variance.  
B) ✓ Includes log and square root as special cases.  
C) ✓ Helps stabilize variance and normalize data.  
D) ✗ Lambda varies and is estimated from data, not always 1.

**Correct:** B, C


#### 19. What is the main difference between time series analysis and time series mining?  
A) ✗ Analysis includes forecasting; mining includes pattern discovery.  
B) ✓ Mining focuses on what has happened; forecasting predicts what will happen.  
C) ✓ Mining involves discovering patterns and anomalies.  
D) ✗ Analysis is not limited to regression models.

**Correct:** B, C


#### 20. Which of the following statements about autocorrelation plots are correct?  
A) ✓ Significant spike at lag k suggests seasonality with period k.  
B) ✓ Autocorrelation plots help distinguish signal from noise.  
C) ✗ Zero autocorrelation at all lags suggests white noise, often stationary.  
D) ✗ Autocorrelation plots are useful for detecting cycles as well.

**Correct:** A, B, D