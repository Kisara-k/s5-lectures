## 4 Time Series Part 2

[Study Notes](#study-notes)

[Questions](#questions)



### Key Points

#### 1. 🔄 Autocorrelation and Partial Autocorrelation  
- Autocorrelation (ACF) measures the correlation between a time series and its lagged version, including direct and indirect dependencies.  
- ACF at lag \( k \) is calculated as the correlation between \( X_t \) and \( X_{t-k} \).  
- Partial Autocorrelation (PACF) measures the direct correlation between \( X_t \) and \( X_{t-k} \), removing effects of intermediate lags.  
- PACF at lag \( k \) is obtained by fitting a linear regression of \( X_t \) on all lags up to \( k \) and extracting the coefficient for lag \( k \).

#### 2. 🧮 Traditional Time Series Models  
- AR(p) models predict current values using a linear combination of the previous \( p \) values of the series.  
- MA(q) models predict current values using a linear combination of the previous \( q \) forecast errors.  
- ARMA models combine AR and MA components and assume stationarity (no trend or seasonality).  
- ARIMA models extend ARMA by including differencing (order \( d \)) to handle non-stationary data.  
- SARIMA models extend ARIMA by adding seasonal components with parameters \( (P, D, Q)_m \), where \( m \) is the seasonal period.

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
- DTW has a computational complexity of \( O(mn) \) or \( O(nw) \) with a warping window \( w \).

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
  For a lag \( k \), the autocorrelation is the correlation between the original series \( X_t \) and the lagged series \( X_{t-k} \). Mathematically,  
  \[
  ACF(k) = \text{corr}(X_t, X_{t-k})
  \]

- **Partial Autocorrelation (PACF)**: While ACF includes both direct and indirect correlations, PACF isolates the **direct** relationship between the series and its lag, removing the influence of intermediate lags. For example, PACF at lag 2 measures the correlation between \( X_t \) and \( X_{t-2} \) after removing the effect of \( X_{t-1} \).

- **How to calculate PACF?**  
  PACF at lag \( k \) is found by fitting a linear regression of \( X_t \) on all lags up to \( k \) and extracting the coefficient of the \( k^{th} \) lag.

These plots (ACF and PACF) are essential tools for identifying the order of models like AR and MA, which we will discuss next.


### 2. 🧮 Traditional Time Series Models: AR, MA, ARMA, ARIMA, SARIMA

Time series models help us understand and forecast data that changes over time. The traditional models can be divided into:

#### Autoregressive Model (AR)
- The AR model predicts the current value of the series as a linear combination of its past values.
- The term "autoregressive" means the variable is regressed on itself.
- For example, an AR(2) model uses the two previous values to predict the current value:
  \[
  X_t = \phi_1 X_{t-1} + \phi_2 X_{t-2} + \epsilon_t
  \]
  where \( \epsilon_t \) is white noise (random error).
- The order \( p \) indicates how many past values are used.

#### Moving Average Model (MA)
- Instead of past values, the MA model uses past forecast errors to predict the current value.
- An MA(q) model uses the last \( q \) error terms:
  \[
  X_t = \mu + \epsilon_t + \theta_1 \epsilon_{t-1} + \cdots + \theta_q \epsilon_{t-q}
  \]
- This model smooths out fluctuations by accounting for noise.

#### Autoregressive Moving Average Model (ARMA)
- Combines AR and MA models to capture both past values and past errors.
- Useful for stationary time series (no trend or seasonality).

#### Autoregressive Integrated Moving Average (ARIMA)
- Extends ARMA by including differencing (integration) to make non-stationary data stationary.
- The parameters are \( (p, d, q) \) where:
  - \( p \) = AR order
  - \( d \) = degree of differencing
  - \( q \) = MA order

#### Seasonal ARIMA (SARIMA)
- Further extends ARIMA to handle seasonality.
- Parameters: \( (p, d, q)(P, D, Q)_m \), where uppercase letters represent seasonal components and \( m \) is the seasonal period (e.g., 12 for monthly data with yearly seasonality).


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
- **Lp norms**: Generalized distance measures (e.g., Manhattan distance for \( p=1 \)).
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



<br>

## Questions

#### 1. Which of the following statements about autocorrelation (ACF) are true?  
A) ACF measures the correlation between a time series and its lagged values including both direct and indirect effects.  
B) ACF only measures the direct correlation between the current value and a specific lag.  
C) ACF values can be used to identify seasonality in a time series.  
D) ACF is only meaningful for stationary time series.


#### 2. Partial autocorrelation (PACF) differs from autocorrelation (ACF) because:  
A) PACF removes the influence of intermediate lags to show direct relationships only.  
B) PACF is always smaller in magnitude than ACF for the same lag.  
C) PACF is calculated by fitting a linear regression model including all lags up to the current lag.  
D) PACF can be used to determine the order of the moving average (MA) component in ARIMA models.


#### 3. In an AR(p) model, which of the following is true?  
A) The current value depends only on the white noise error terms.  
B) The model regresses the variable on its own past \( p \) values.  
C) The order \( p \) indicates the number of past error terms used.  
D) The model assumes stationarity of the time series.


#### 4. Which of the following statements about Moving Average (MA) models are correct?  
A) MA models use past forecast errors to predict the current value.  
B) An MA(q) model uses the last \( q \) observed values of the series.  
C) MA models can be expressed as infinite AR models under certain conditions.  
D) Parameter estimation in MA models is typically done using maximum likelihood or non-linear least squares.


#### 5. The ARMA model combines which two components?  
A) Autoregressive (AR) and Moving Average (MA)  
B) Autoregressive (AR) and Integrated (I)  
C) Moving Average (MA) and Differencing (I)  
D) Seasonal and Non-seasonal components


#### 6. What is the main purpose of differencing in ARIMA models?  
A) To remove seasonality from the data.  
B) To stabilize the variance of the series.  
C) To make a non-stationary time series stationary by removing trends.  
D) To smooth out noise in the data.


#### 7. Which of the following are true about Seasonal ARIMA (SARIMA) models?  
A) They include seasonal differencing to handle seasonal trends.  
B) The seasonal order parameters are denoted as (P, D, Q).  
C) SARIMA models cannot handle non-seasonal trends.  
D) The seasonal period \( m \) defines the length of the seasonal cycle.


#### 8. Simple Exponential Smoothing (SES) is most appropriate when:  
A) The time series has a strong seasonal pattern.  
B) The time series has no clear trend or seasonality.  
C) The time series exhibits a linear trend.  
D) The weights assigned to past observations decrease exponentially.


#### 9. Which of the following statements about Double and Triple Exponential Smoothing are correct?  
A) Double Exponential Smoothing accounts for level and trend.  
B) Triple Exponential Smoothing accounts for level, trend, and seasonality.  
C) Triple Exponential Smoothing is also known as Holt-Winters method.  
D) Double Exponential Smoothing is suitable for seasonal data.


#### 10. When evaluating time series models, which of the following are valid criteria or methods?  
A) Residual plots to check for randomness of errors.  
B) Akaike Information Criterion (AIC) to balance fit and complexity.  
C) Using only training data error to select the best model.  
D) Bayesian Information Criterion (BIC) penalizes model complexity more than AIC.


#### 11. Which of the following statements about time series mining tasks are true?  
A) Indexing involves finding time series similar to a query series.  
B) Clustering groups time series based on similarity.  
C) Classification assigns labels to time series based on their patterns.  
D) Summarization is unrelated to anomaly detection.


#### 12. In time series indexing, which of the following methods improve efficiency?  
A) Brute force linear matching of raw sequences.  
B) Using compressed representations of time series for initial filtering.  
C) Index structures that cluster similar sequences together.  
D) Ignoring dimensionality reduction to preserve all data details.


#### 13. Which of the following are true about Dynamic Time Warping (DTW)?  
A) DTW aligns sequences that may be out of phase or have different speeds.  
B) DTW always has a computational complexity of \( O(n^2) \) regardless of constraints.  
C) DTW is useful when Euclidean distance fails to capture similarity due to time shifts.  
D) DTW cannot handle sequences of different lengths.


#### 14. Which of the following statements about similarity measures for time series are correct?  
A) Euclidean distance requires sequences to be of the same length.  
B) Lp norms generalize Euclidean and Manhattan distances.  
C) Probabilistic similarity measures rely on statistical models.  
D) Similarity is the same as distance.


#### 15. The matrix profile is useful because:  
A) It stores distances between subsequences and their nearest neighbors.  
B) Large values in the matrix profile indicate repeated patterns.  
C) It can be used to detect anomalies and motifs efficiently.  
D) It requires multiple hyperparameters to tune for different datasets.


#### 16. Which of the following are true about time series compression techniques?  
A) Delta encoding stores the difference between consecutive values.  
B) Run Length Encoding (RLE) compresses repeated values efficiently.  
C) Compression always leads to loss of important information.  
D) Compression helps reduce storage and speeds up similarity searches.


#### 17. When selecting a time series forecasting model, which of the following are important considerations?  
A) The model should have the lowest possible training error regardless of complexity.  
B) Residuals should resemble white noise with no autocorrelation.  
C) Models with fewer parameters are preferred if accuracy is similar.  
D) A model with the lowest AIC or BIC is generally better.


#### 18. Which of the following statements about forecasting methods are true?  
A) The naive method forecasts future values as the last observed value.  
B) The seasonal naive method forecasts based on the last observed value from the same season.  
C) The drift method assumes no trend in the data.  
D) Simple forecasting methods are often used as benchmarks.


#### 19. Which of the following are true about the assumptions underlying ARMA, ARIMA, and SARIMA models?  
A) ARMA assumes constant mean and variance with no trend or seasonality.  
B) ARIMA includes differencing to remove trends.  
C) SARIMA models include seasonal differencing and seasonal AR and MA terms.  
D) All these models assume the time series is non-stationary.


#### 20. Which of the following statements about partial autocorrelation function (PACF) plots are correct?  
A) PACF can help identify the order \( p \) of an AR model.  
B) PACF values at lag \( k \) represent the correlation between \( X_t \) and \( X_{t-k} \) after removing effects of lags 1 to \( k-1 \).  
C) PACF is useful for identifying the order \( q \) of an MA model.  
D) PACF values are always positive.



<br>

## Answers

#### 1. Which of the following statements about autocorrelation (ACF) are true?  
A) ✓ ACF measures the correlation between a time series and its lagged values including both direct and indirect effects.  
B) ✗ ACF includes indirect effects, not only direct correlation.  
C) ✓ ACF values can reveal seasonality by showing repeated patterns at seasonal lags.  
D) ✗ ACF can be computed for non-stationary series but interpretation is valid mainly for stationary series.

**Correct:** A, C


#### 2. Partial autocorrelation (PACF) differs from autocorrelation (ACF) because:  
A) ✓ PACF removes intermediate lag effects to show direct relationships only.  
B) ✗ PACF can be larger or smaller than ACF depending on data; no fixed rule.  
C) ✓ PACF is calculated via regression including all lags up to the current lag.  
D) ✗ PACF helps identify AR order, not MA order.

**Correct:** A, C


#### 3. In an AR(p) model, which of the following is true?  
A) ✗ AR models use past values, not just white noise errors.  
B) ✓ The model regresses the variable on its own past \( p \) values.  
C) ✗ The order \( p \) refers to past values, not error terms.  
D) ✓ Stationarity is assumed for AR models to be valid.

**Correct:** B, D


#### 4. Which of the following statements about Moving Average (MA) models are correct?  
A) ✓ MA models use past forecast errors to predict current values.  
B) ✗ MA(q) uses past error terms, not past observed values.  
C) ✓ Under certain conditions, MA can be represented as infinite AR.  
D) ✓ Parameter estimation often uses maximum likelihood or non-linear least squares.

**Correct:** A, C, D


#### 5. The ARMA model combines which two components?  
A) ✓ AR and MA components are combined in ARMA.  
B) ✗ Integrated (I) is part of ARIMA, not ARMA.  
C) ✗ Differencing (I) is not part of ARMA.  
D) ✗ Seasonal components are handled in SARIMA, not basic ARMA.

**Correct:** A


#### 6. What is the main purpose of differencing in ARIMA models?  
A) ✗ Differencing removes trends, not seasonality (seasonality is handled separately).  
B) ✗ Differencing stabilizes mean, not variance.  
C) ✓ Differencing makes non-stationary series stationary by removing trends.  
D) ✗ Differencing is not primarily for smoothing noise.

**Correct:** C


#### 7. Which of the following are true about Seasonal ARIMA (SARIMA) models?  
A) ✓ Seasonal differencing handles seasonal trends.  
B) ✓ Seasonal order parameters are (P, D, Q).  
C) ✗ SARIMA can handle non-seasonal trends via differencing.  
D) ✓ Seasonal period \( m \) defines the length of the seasonal cycle.

**Correct:** A, B, D


#### 8. Simple Exponential Smoothing (SES) is most appropriate when:  
A) ✗ SES is not suitable for seasonal data.  
B) ✓ SES is for data without trend or seasonality.  
C) ✗ SES does not model trends.  
D) ✓ Weights decrease exponentially for older observations.

**Correct:** B, D


#### 9. Which of the following statements about Double and Triple Exponential Smoothing are correct?  
A) ✓ Double Exponential Smoothing models level and trend.  
B) ✓ Triple Exponential Smoothing models level, trend, and seasonality.  
C) ✓ Triple Exponential Smoothing is also called Holt-Winters method.  
D) ✗ Double Exponential Smoothing does not handle seasonality.

**Correct:** A, B, C


#### 10. When evaluating time series models, which of the following are valid criteria or methods?  
A) ✓ Residual plots check randomness of errors.  
B) ✓ AIC balances model fit and complexity.  
C) ✗ Using only training error risks overfitting; test/validation error is needed.  
D) ✓ BIC penalizes complexity more than AIC.

**Correct:** A, B, D


#### 11. Which of the following statements about time series mining tasks are true?  
A) ✓ Indexing finds series similar to a query.  
B) ✓ Clustering groups similar series.  
C) ✓ Classification assigns labels based on patterns.  
D) ✗ Summarization can include anomaly detection as a special case.

**Correct:** A, B, C


#### 12. In time series indexing, which of the following methods improve efficiency?  
A) ✗ Brute force is slow and inefficient.  
B) ✓ Using compressed versions for initial filtering speeds up search.  
C) ✓ Index structures cluster similar sequences to improve performance.  
D) ✗ Ignoring dimensionality reduction usually worsens performance.

**Correct:** B, C


#### 13. Which of the following are true about Dynamic Time Warping (DTW)?  
A) ✓ DTW aligns sequences with time shifts or speed differences.  
B) ✗ DTW complexity can be reduced with warping windows.  
C) ✓ DTW is useful when Euclidean distance fails due to misalignment.  
D) ✗ DTW can handle sequences of different lengths by repeating elements.

**Correct:** A, C, D


#### 14. Which of the following statements about similarity measures for time series are correct?  
A) ✓ Euclidean distance requires equal-length sequences.  
B) ✓ Lp norms generalize Euclidean (p=2) and Manhattan (p=1) distances.  
C) ✓ Probabilistic measures use statistical models to assess similarity.  
D) ✗ Similarity is inverse of distance, not the same.

**Correct:** A, B, C


#### 15. The matrix profile is useful because:  
A) ✓ It stores distances between subsequences and their nearest neighbors.  
B) ✗ Large values indicate anomalies, not repeated patterns.  
C) ✓ It efficiently detects motifs and anomalies.  
D) ✗ It requires only one hyperparameter, not many.

**Correct:** A, C, D


#### 16. Which of the following are true about time series compression techniques?  
A) ✓ Delta encoding stores differences between consecutive values.  
B) ✓ Run Length Encoding compresses repeated values efficiently.  
C) ✗ Compression can be lossless or lossy; not always losing information.  
D) ✓ Compression reduces storage and speeds up similarity searches.

**Correct:** A, B, D


#### 17. When selecting a time series forecasting model, which of the following are important considerations?  
A) ✗ Lowest training error alone can cause overfitting.  
B) ✓ Residuals should resemble white noise with no autocorrelation.  
C) ✓ Simpler models preferred if accuracy is similar.  
D) ✓ Lower AIC or BIC generally indicates better model.

**Correct:** B, C, D


#### 18. Which of the following statements about forecasting methods are true?  
A) ✓ Naive method uses last observed value as forecast.  
B) ✓ Seasonal naive uses last observed value from same season.  
C) ✗ Drift method assumes a linear trend, not no trend.  
D) ✓ Simple methods serve as benchmarks.

**Correct:** A, B, D


#### 19. Which of the following are true about the assumptions underlying ARMA, ARIMA, and SARIMA models?  
A) ✓ ARMA assumes constant mean and variance, no trend or seasonality.  
B) ✓ ARIMA includes differencing to remove trends.  
C) ✓ SARIMA includes seasonal differencing and seasonal AR/MA terms.  
D) ✗ These models assume stationarity after differencing (ARIMA/SARIMA).

**Correct:** A, B, C


#### 20. Which of the following statements about partial autocorrelation function (PACF) plots are correct?  
A) ✓ PACF helps identify AR order \( p \).  
B) ✓ PACF at lag \( k \) shows correlation after removing effects of lags 1 to \( k-1 \).  
C) ✗ PACF is not used to identify MA order \( q \).  
D) ✗ PACF values can be positive or negative.

**Correct:** A, B