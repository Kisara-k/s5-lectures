## 3. Time Series I

## Key Points

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
- Additive model: $y(t) = \text{Level} + \text{Trend} + \text{Seasonality} + \text{Noise}$  
- Multiplicative model: $y(t) = \text{Level} \times \text{Trend} \times \text{Seasonality} \times \text{Noise}$  
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
  $y(t) = \text{Level} + \text{Trend} + \text{Seasonality} + \text{Noise}$  
  Used when components add together linearly.

- **Multiplicative model:**  
  $y(t) = \text{Level} \times \text{Trend} \times \text{Seasonality} \times \text{Noise}$  
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