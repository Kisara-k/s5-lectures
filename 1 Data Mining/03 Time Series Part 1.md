## 03 Time Series Part 1

[Study Notes](#study-notes)

[Questions](#questions)



### Key Points



#### 1. 📅 Definition of Time Series  
- A time series is an ordered sequence of values of a variable, usually at equally spaced time intervals.  
- The mean and standard deviation of a time series can vary over time.  

#### 2. 🔄 Time Series Components  
- Level is the average value in the series.  
- Trend is the increasing or decreasing value over time, which can be linear or nonlinear.  
- Seasonality is a repeating short-term cycle with a fixed period (e.g., monthly, yearly).  
- Cycle refers to long-term fluctuations without a fixed period (e.g., economic recessions).  
- Noise is the random, unsystematic variation in the series.  

#### 3. 📈 Trend and Seasonality Detection  
- Moving averages and polynomial fitting are methods to detect trends.  
- Autocorrelation plots show seasonality by spikes at specific lags corresponding to the seasonal period.  
- Fast Fourier Transform (FFT) can identify dominant frequencies indicating seasonality.  

#### 4. 🔁 Autocorrelation and Memory  
- Autocorrelation measures correlation between a time series and its lagged values.  
- Short memory means only recent past values influence the current value (e.g., financial data).  
- Long memory means distant past values influence the current value (e.g., climate data).  
- Stationary time series often have short memory; non-stationary series often have long memory.  

#### 5. 🧩 Time Series Decomposition Models  
- Additive model: \( y(t) = \text{Level} + \text{Trend} + \text{Seasonality} + \text{Noise} \)  
- Multiplicative model: \( y(t) = \text{Level} \times \text{Trend} \times \text{Seasonality} \times \text{Noise} \)  
- Real-world time series may have mixed additive and multiplicative components.  

#### 6. 🧮 STL Decomposition  
- STL uses LOESS smoothing to extract trend and seasonal components.  
- Trend extraction applies LOESS to the original series to capture growth trajectory.  
- Seasonal extraction applies LOESS to the detrended series to capture seasonality.  
- Residuals are calculated as Original Series - Trend - Seasonality, representing noise and anomalies.  

#### 7. 🔄 Cycles vs Seasonality  
- Seasonality has fixed, repeating periods; cycles have variable, longer durations without fixed periods.  
- Spectral analysis (Fourier Transform) identifies dominant frequencies for cycles and seasonality.  
- Wavelet transform decomposes time series into frequency bands, useful for non-stationary data.  

#### 8. 📊 Stationarity  
- A stationary time series has constant mean, variance, and no trend or seasonality.  
- Stationarity can be checked by visual inspection, seasonal-trend decomposition, and statistical tests like the Augmented Dickey-Fuller (ADF) test.  

#### 9. 🛠️ Fixing Non-Stationarity  
- Logarithmic, square root, and Box-Cox transforms stabilize variance in time series.  
- Differencing (first-order or second-order) removes trends to achieve stationarity.  
- Combining Box-Cox transform and differencing is a common approach to fix non-stationarity.  

#### 10. 🧪 Practical Tools  
- The Python **statsmodels** package provides functions for seasonal decomposition and stationarity tests.  
- Autocorrelation plots and spectral density plots are essential for detecting seasonality and cycles.  



<br>

## Study Notes



*Based on Dr. Thanuja Ambegoda’s Lecture*


### 1. 📅 What is a Time Series? Introduction and Importance

A **time series** is a sequence of data points collected or recorded at successive, usually equally spaced, points in time. For example, daily temperatures, monthly sales, or yearly sunspot counts. Unlike random data points, time series data have a natural order and often show patterns over time.

#### Key Characteristics:
- **Ordered sequence:** The order of data points matters because time flows forward.
- **Equally spaced intervals:** Most time series data are recorded at regular intervals (e.g., hourly, daily, monthly).
- **Changing statistics:** The mean (average) and standard deviation (spread) of the data can change over time, unlike in simple random data.

#### Why study time series?
Understanding time series helps us **predict future values** based on past patterns. This is crucial in many fields such as finance (stock prices), weather forecasting, healthcare (patient monitoring), and industry (equipment maintenance).


### 2. 🔍 Components of a Time Series

Time series data can be thought of as a combination of several underlying components that explain its behavior over time:

- **Level:** The baseline or average value around which the data fluctuates.
- **Trend:** The long-term increase or decrease in the data. For example, a steady rise in sales over years.
- **Seasonality:** Regular, repeating patterns within fixed periods, such as higher ice cream sales every summer.
- **Cycle:** Longer-term fluctuations that are not fixed in length, like economic recessions or booms.
- **Noise:** Random, unpredictable variations that do not follow any pattern.

#### Why decompose?
Breaking down a time series into these components helps us understand the data better and improves forecasting accuracy.


### 3. 📈 Trend and Seasonality: Detecting Patterns

#### Trend Analysis
A **trend** shows the general direction in which the data is moving over time. It can be:

- **Linear:** A straight-line increase or decrease.
- **Nonlinear:** More complex shapes like curves.

**Methods to detect trends:**
- **Moving averages:** Smooth out short-term fluctuations to highlight the trend.
- **Polynomial fitting:** Fit a curve to the data points to capture nonlinear trends.

#### Seasonality
Seasonality refers to **regular, repeating patterns** within a fixed period, such as daily, weekly, monthly, or yearly cycles.

**Examples:**
- Retail sales peaking every December.
- Temperature changes with seasons.

**How to detect seasonality:**
- **Autocorrelation plots:** Measure how data points relate to their past values at different lags. A spike at lag 12 in monthly data suggests yearly seasonality.
- **Fast Fourier Transform (FFT):** Converts time series data into frequency components to identify dominant cycles.
- **Seasonal decomposition:** Separates the series into trend, seasonal, and residual parts.


### 4. 🔄 Autocorrelation and Memory in Time Series

**Autocorrelation** measures how related a time series is to its past values. It tells us if past values influence future values.

- **Short memory:** Only recent past values affect the current value (common in financial data).
- **Long memory:** Distant past values also influence the current value (seen in climate data).

**Stationary time series** often have short memory, meaning their statistical properties don’t change over time. **Non-stationary series** may have long memory and require more complex models.


### 5. 🧩 Decomposing Time Series: Additive and Multiplicative Models

Decomposition helps us separate the time series into understandable parts:

- **Additive model:**  
  \( y(t) = \text{Level} + \text{Trend} + \text{Seasonality} + \text{Noise} \)  
  Used when components add together linearly.

- **Multiplicative model:**  
  \( y(t) = \text{Level} \times \text{Trend} \times \text{Seasonality} \times \text{Noise} \)  
  Used when components multiply, often when seasonal effects grow with the level.

Real-world data can be messy, with mixed additive and multiplicative effects, changing trends, and irregular cycles.


### 6. 🧮 Seasonal-Trend Decomposition using LOESS (STL)

**STL** is a powerful method to decompose time series using **LOESS** (Locally Weighted Scatterplot Smoothing), a non-parametric smoothing technique.

#### How STL works:
- **Trend extraction:** Applies LOESS smoothing to capture the overall growth or decline, ignoring seasonality.
- **Seasonal extraction:** Removes the trend and applies LOESS again to isolate seasonal patterns.
- **Residual extraction:** The leftover part after removing trend and seasonality, representing noise and anomalies.

STL is flexible and can handle complex seasonal patterns, making it useful for real-world noisy data.


### 7. 🔄 Cyclic Patterns vs Seasonality

While **seasonality** is a fixed, repeating pattern (e.g., yearly), **cycles** are longer-term oscillations without a fixed period, often driven by economic or environmental factors.

#### Why detect cycles?
- To improve forecasting by separating long-term fluctuations from noise.
- To understand underlying economic or business conditions.

#### Detecting cycles:
- **Spectral analysis:** Uses Fourier Transform to find dominant frequencies.
- **Wavelet transform:** Breaks down the series into different frequency bands, useful for non-stationary data.


### 8. 📊 Stationarity in Time Series

A **stationary time series** has statistical properties (mean, variance) that do not change over time. Stationarity is important because many forecasting models assume it.

#### Characteristics of stationary series:
- Constant mean and variance.
- No trend or seasonality.

#### Checking stationarity:
- **Visual inspection:** Look for constant mean and variance over time.
- **Seasonal-trend decomposition:** Separate components to see if residuals are stationary.
- **Statistical tests:** Augmented Dickey-Fuller (ADF) test checks for unit roots indicating non-stationarity.


### 9. 🛠️ Fixing Non-Stationarity: Transformations and Differencing

Many real-world time series are non-stationary. To apply forecasting models, we often need to **transform** or **difference** the data.

#### Common transformations:
- **Logarithmic transform:** Reduces exponential growth trends.
- **Square root transform:** Handles quadratic growth.
- **Box-Cox transform:** A flexible method that includes log and square root as special cases.

#### Differencing:
- **First-order differencing:** Replace each value with the difference from the previous value to remove trends.
- **Second-order differencing:** Difference the differenced series to remove more complex trends.

#### Combining methods:
Often, a Box-Cox transform is applied first to stabilize variance, followed by differencing to remove trends, resulting in a stationary series ready for modeling.


### 10. 🧪 Summary and Practical Tools

- Time series analysis helps us understand and predict data that changes over time.
- Decomposition into trend, seasonality, cycle, and noise clarifies complex patterns.
- Stationarity is a key concept; non-stationary data must be transformed for many models.
- Tools like **statsmodels** in Python provide functions for decomposition and stationarity tests.
- Visualizations like autocorrelation plots and spectral density plots are essential for detecting patterns.


### Final Thoughts

Time series data is everywhere, from weather to finance to healthcare. Understanding its components and properties is the first step toward effective forecasting and decision-making. This lecture lays the foundation by introducing key concepts, methods for detecting patterns, and techniques to prepare data for analysis.



<br>

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

