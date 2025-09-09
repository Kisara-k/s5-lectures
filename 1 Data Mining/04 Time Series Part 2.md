## 4. Time Series Part 2

## Key Points

#### 1. 🔄 Autocorrelation and Partial Autocorrelation  
- Autocorrelation (ACF) measures the correlation between a time series and its lagged version, including direct and indirect dependencies.  
- ACF at lag $k$ is calculated as the correlation between $X_t$ and $X_{t-k}$.  
- Partial Autocorrelation (PACF) measures the direct correlation between $X_t$ and $X_{t-k}$, removing effects of intermediate lags.  
- PACF at lag $k$ is obtained by fitting a linear regression of $X_t$ on all lags up to $k$ and extracting the coefficient for lag $k$.

#### 2. 🧮 Traditional Time Series Models  
- AR(p) models predict current values using a linear combination of the previous $p$ values of the series.  
- MA(q) models predict current values using a linear combination of the previous $q$ forecast errors.  
- ARMA models combine AR and MA components and assume stationarity (no trend or seasonality).  
- ARIMA models extend ARMA by including differencing (order $d$) to handle non-stationary data.  
- SARIMA models extend ARIMA by adding seasonal components with parameters $(P, D, Q)_m$, where $m$ is the seasonal period.

#### 3. 🔮 Simple Forecasting Methods and Exponential Smoothing  
- Simple forecasting methods include average, naive, seasonal naive, and drift methods, used as baseline benchmarks.  
- Simple Exponential Smoothing (SES) applies weighted averages with exponentially decreasing weights, suitable for data without trend or seasonality.  
- Double Exponential Smoothing (Holt’s method) accounts for level and trend.  
- Triple Exponential Smoothing (Holt-Winters method) accounts for level, trend, and seasonality.

#### 4. 📊 Model Evaluation and Selection  
- Residuals should behave like white noise for a good model fit.  
- ACF and PACF plots of residuals help detect remaining autocorrelation.  
- AIC and BIC are information criteria used to compare models; lower values indicate better models.  
- Grid search is used to exhaustively test model parameters for best performance.  
- The preferred model balances accuracy (low error) and simplicity (fewer parameters).

#### 5. 🕵️‍♂️ Time Series Mining Tasks  
- Indexing involves matching query time series to a database, either whole matching or subsequence matching.  
- Clustering groups similar time series; classification assigns labels based on patterns.  
- Prediction forecasts future values; summarization creates concise descriptions.  
- Anomaly detection identifies unusual patterns; segmentation divides series into meaningful parts.

#### 6. 💾 Time Series Compression and Similarity Measures  
- Delta encoding and run-length encoding (RLE) are common compression techniques for time series.  
- Euclidean distance measures similarity between sequences of equal length in n-dimensional space.  
- Dynamic Time Warping (DTW) aligns sequences that are similar in shape but out of phase by warping the time axis.  
- DTW has a computational complexity of $O(mn)$ or $O(nw)$ with a warping window $w$.

#### 7. 🔍 Motifs, Matrix Profile, Discords, and Anomalies  
- The matrix profile stores distances between each subsequence and its nearest neighbor in a time series.  
- Large matrix profile values indicate anomalies (discords); small values indicate repeated patterns (motifs).  
- Matrix profile supports fast, exact or approximate motif and anomaly detection, streaming data, and missing data handling.

#### 8. 🧩 Time Series Representations  
- Time series can be represented in raw form or transformed into symbolic or frequency domains to reduce noise and dimensionality.  
- Good representations preserve important patterns while enabling efficient mining and forecasting.



<br>

## Study Notes

### 1. 🔄 Understanding Autocorrelation and Partial Autocorrelation

When working with time series data, one of the fundamental concepts is **autocorrelation**. Autocorrelation measures how related a time series is with a lagged version of itself. In simpler terms, it tells us how much the value of the series at one time point is related to its value at a previous time point.

- **Autocorrelation (ACF)**: This is the correlation between the time series and a lagged version of itself. For example, the temperature today might be correlated with the temperature yesterday or two days ago. The autocorrelation function (ACF) plot shows these correlations for different lags (time steps back). It includes both direct and indirect relationships.

- **How to calculate ACF?**  
  For a lag $k$, the autocorrelation is the correlation between the original series $X_t$ and the lagged series $X_{t-k}$. Mathematically,  

$$
  ACF(k) = \text{corr}(X_t, X_{t-k})
$$


- **Partial Autocorrelation (PACF)**: While ACF includes both direct and indirect correlations, PACF isolates the **direct** relationship between the series and its lag, removing the influence of intermediate lags. For example, PACF at lag 2 measures the correlation between $X_t$ and $X_{t-2}$ after removing the effect of $X_{t-1}$.

- **How to calculate PACF?**  
  PACF at lag $k$ is found by fitting a linear regression of $X_t$ on all lags up to $k$ and extracting the coefficient of the $k^{th}$ lag.

These plots (ACF and PACF) are essential tools for identifying the order of models like AR and MA, which we will discuss next.


### 2. 🧮 Traditional Time Series Models: AR, MA, ARMA, ARIMA, SARIMA

Time series models help us understand and forecast data that changes over time. The traditional models can be divided into:

#### Autoregressive Model (AR)
- The AR model predicts the current value of the series as a linear combination of its past values.
- The term "autoregressive" means the variable is regressed on itself.
- For example, an AR(2) model uses the two previous values to predict the current value:

$$
  X_t = \phi_1 X_{t-1} + \phi_2 X_{t-2} + \epsilon_t
$$

  where $\epsilon_t$ is white noise (random error).
- The order $p$ indicates how many past values are used.

#### Moving Average Model (MA)
- Instead of past values, the MA model uses past forecast errors to predict the current value.
- An MA(q) model uses the last $q$ error terms:

$$
  X_t = \mu + \epsilon_t + \theta_1 \epsilon_{t-1} + \cdots + \theta_q \epsilon_{t-q}
$$

- This model smooths out fluctuations by accounting for noise.

#### Autoregressive Moving Average Model (ARMA)
- Combines AR and MA models to capture both past values and past errors.
- Useful for stationary time series (no trend or seasonality).

#### Autoregressive Integrated Moving Average (ARIMA)
- Extends ARMA by including differencing (integration) to make non-stationary data stationary.
- The parameters are $(p, d, q)$ where:
  - $p$ = AR order
  - $d$ = degree of differencing
  - $q$ = MA order

#### Seasonal ARIMA (SARIMA)
- Further extends ARIMA to handle seasonality.
- Parameters: $(p, d, q)(P, D, Q)_m$, where uppercase letters represent seasonal components and $m$ is the seasonal period (e.g., 12 for monthly data with yearly seasonality).


### 3. 🔮 Simple Forecasting Methods and Exponential Smoothing

Before diving into complex models, simple forecasting methods provide baseline predictions:

- **Average method**: Forecast future values as the average of past observations.
- **Naive method**: Forecast future values as the last observed value.
- **Seasonal naive method**: Forecast future values as the last observed value from the same season.
- **Drift method**: Forecasts based on a linear trend estimated from the first and last observations.

#### Exponential Smoothing
Exponential smoothing methods forecast future values by weighting past observations, with weights decreasing exponentially for older data.

- **Simple Exponential Smoothing (SES)**: Suitable for data without trend or seasonality. Recent observations have more influence.
- **Double Exponential Smoothing (Holt’s method)**: Accounts for both level and trend.
- **Triple Exponential Smoothing (Holt-Winters method)**: Accounts for level, trend, and seasonality.

These methods are computationally efficient and often used for short-term forecasting.


### 4. 📊 Model Evaluation and Selection

Choosing the right model requires evaluating how well it fits the data and how well it predicts unseen data.

- **Residual analysis**: After fitting a model, analyze residuals (errors) to check if they behave like white noise (random, no pattern).
- **Autocorrelation of residuals**: Use ACF and PACF plots on residuals to detect remaining patterns.
- **Information criteria**:
  - **AIC (Akaike Information Criterion)** and **BIC (Bayesian Information Criterion)** balance model fit and complexity.
  - Lower AIC/BIC values indicate better models.
- **Cross-validation and test error**: Use a hold-out test set to measure prediction accuracy.
- **Grid search**: Systematically test different model parameters to find the best combination.


### 5. 🕵️‍♂️ Time Series Mining: Tasks and Techniques

Time series mining involves extracting useful patterns and knowledge from time series data. Key tasks include:

- **Indexing (Query by content)**: Finding time series similar to a query series.
  - Whole matching: Compare entire series.
  - Subsequence matching: Find similar patterns within longer series.
- **Clustering**: Group similar time series.
- **Classification**: Assign labels to time series based on patterns.
- **Prediction**: Forecast future values.
- **Summarization**: Create concise descriptions of large datasets.
- **Anomaly detection**: Identify unusual or unexpected patterns.
- **Segmentation**: Divide series into meaningful segments.

Efficient indexing often uses compressed representations or specialized data structures to speed up similarity searches.


### 6. 💾 Time Series Compression and Similarity Measures

#### Compression
- Reduces storage and speeds up processing.
- Techniques include **delta encoding** (storing differences between consecutive values) and **run-length encoding** (compressing repeated values).

#### Similarity Measures
Similarity is crucial for mining tasks like clustering and anomaly detection.

- **Euclidean distance**: Measures straight-line distance between two sequences of equal length.
- **Lp norms**: Generalized distance measures (e.g., Manhattan distance for $p=1$).
- **Dynamic Time Warping (DTW)**: Aligns sequences that may be out of phase or have different speeds by warping the time axis. Useful when sequences have similar shapes but are shifted or stretched in time.
- **Longest Common Subsequence**: Measures similarity based on the longest matching subsequence.
- **Probabilistic measures**: Use statistical models to assess similarity.


### 7. 🔍 Motifs, Matrix Profile, Discords, and Anomalies

- **Motifs**: Repeated patterns or subsequences in time series data.
- **Discords**: Unusual or anomalous subsequences that differ significantly from the rest.
- **Matrix Profile**: A powerful data structure that stores the distance between each subsequence and its nearest neighbor. It helps quickly identify motifs and discords.
  - Large values in the matrix profile indicate anomalies.
  - Small values indicate repeated patterns.
- The matrix profile is efficient, scalable, and supports streaming data, making it a popular tool for time series mining.


### 8. 🧩 Time Series Representations

Representing time series data in a compact and meaningful way is important for mining and forecasting.

- Common representations include raw data, symbolic approximations, and transformed spaces (e.g., Fourier or wavelet transforms).
- Good representations reduce noise and dimensionality while preserving important patterns.


### Summary

This lecture covered advanced concepts in time series analysis, focusing on:

- Understanding autocorrelation and partial autocorrelation to identify model orders.
- Traditional time series models (AR, MA, ARMA, ARIMA, SARIMA) and their use cases.
- Simple forecasting methods and exponential smoothing techniques.
- Model evaluation using residual analysis and information criteria.
- Time series mining tasks such as indexing, clustering, classification, and anomaly detection.
- Compression and similarity measures, including Euclidean distance and DTW.
- The matrix profile for motif and anomaly detection.
- The importance of effective time series representations.

These concepts form the foundation for analyzing, forecasting, and mining time series data effectively.