## PRACTICE QUESTION#
# Attach dataset
forbes.df <- read.table("forbes.txt", header=T)
attach(forbes.df)

# Scatter plot
plot(Boilingpt, 100*log10(Pressure),
     main="Plot of 100*log10(Pressure) vs. Boiling Point", pch=16)

# Fit Regression Line
forbes.lm <- lm(100*log10(Pressure) ~ Boilingpt,
                data=forbes.df)
coef(forbes.lm)

# Scatter plot with fitted line
plot(Boilingpt, 100*log10(Pressure),
     main="Plot of 100*log10(Pressure) vs. Boiling point", pch=16)
abline(forbes.lm) # currently active plot

# Residual standard error
# Multiple R^2 (proportion of variability explained by model)
# Standard errors of regression coefficients
summary(forbes.lm)

# Critical value of t(0.95, n-1)
qt(0.95, 15)

# 90% confidence interval for for beta-0
-42.16418 + qt(0.95, 15)*3.34136 # intercept and standard error from summary output
-42.16418 - qt(0.95, 15)*3.34136

# 90% confidence interval for beta-1
0.89562 + qt(0.95, 15)*0.01646
0.85962 - qt(0.95, 15)*0.01646


# Anova table, F-test
anova(forbes.lm)

# 99% CI for mean of y.
predict(forbes.lm, data.frame(Boilingpt=200), se.fit=T,
        interval="confidence", level=0.99)

# Critical value of t-distribution (0.995 not 0.99 because two-sided)
qt(0.995, 15)

# Manual confidence interval using t-statistic
136.6529 + qt(0.995, 15)*0.104 # se.fit from predict output
136.6529 - qt(0.995, 15)*0.104

# 99% prediction interval for individual value of y
predict(forbes.lm, data.frame(Boilingpt=200), se.fit=T,
        interval="prediction", level=0.99)


# Plot of residuals vs. fitted values
plot(fitted(forbes.lm), resid(forbes.lm),
     main="Plot of residuals vs. fitted values",
     xlab="Fitted: Boilingpt", ylab="Residuals",
     ylim=c(-2, 2), pch=16)
abline(h=0, lty=2)


# Omitting a case
# Identify an outlier
'
outlier <-
  identify(fitted(forbes.lm),resid(forbes.lm),n=1) # manually select outlier with mouse

subset.forbes.lm <- lm(100*log10(Pressure) ~ Boilingpt,
                       data=forbes.df, subset=-outlier)
summary(subset.forbes.lm)

# Plot of residuals vs.fitted values with outlier removed
plot(fitted(subset.forbes.lm),resid(subset.forbes.lm),
     main="Plot of residuals vs. fitted values; omit case 12",
     xlab="Fitted : Boilingpt",ylab="Residuals",ylim=c(-2,2),
     pch=16)
abline(h=0,lty=2)
'

### Assignment question
## Setup
executives.df <- read.table("Executives.txt", header=T)
attach(executives.df)
executives.lm <- lm(Salary ~ Experience, data=executives.df)

## a) Scatter-plot
plot(Experience, Salary, main="Plot of Salary vs. Experience", pch=16)
abline(executives.lm, col='red')
cor(Salary, Experience)

# plot of residuals
plot(fitted(executives.lm), resid(executives.lm),
     main="Distribution of residuals around fitted regression line",
     xlab="Salary prediction", ylab="Residuals", ylim=c(-61000, 61000), pch=16)
abline(h=0, lty=2, col="red") # normally distributed with common variance

hist(resid(executives.lm), breaks=6, xlab="Residual", ylab="Frequency",
     main="Histogram of residuals", col="lightblue") # normally distributed

# Yes, this scatter plot does suggest that it is appropriate to fit a linear
# regression model to these data. 
# Salary very clearly trends upwards at a steady rate as experience grows.
# In fact these data have a strong correlation coefficient of 0.71.
# The absence of data points in the upper-left and lower-right areas of
# the plot also support that salary amount depends on experience.
#
# A plot of the residuals around the fitted regression line also shows that
# it is safe to assume that the common variance principle is upheld by the data
# since the residuals 


## b) Intercept and slope
summary(executives.lm)


# The y-intercept beta-0 of the fitted regression line is equal to 58699 and the
# slope beta-1 is equal to 2892.
# This means that we can expect the starting salary of an executive to be
# approximately €58,699 and that this salary will grow roughly at a rate of
# €2,892 per year of experience.

## c) 98% confidence interval for slope
# alpha = 2%, two-tailed test -> t(alpha/2, df)
qt(0.99, 164)

# Lower bound
58699 - qt(0.99, 164)*224.7
# Upper bound
58699 + qt(0.99, 164)*224.7

# After performing some statistical analysis on our sample data, we expect that
# there is a 98% chance that the true value of the slope lies in the interval
# 58171 <= beta-1 <= 59226.

## d) Test hypothesis H0: beta-1 = 0
# The null hypothesis that the value of beta-1 = 0 should be rejected due to the
# fact that it lies well outside our previously computed 98% confidence interval of
# 58171 <= beta-1 <= 59226.
# In practice this means that the likelihood that salary does not depend on 
# experience (beta-1 = 0) is very small and it is appropriate to model the
# relationship of these two variable using simple linear regression.
# Using a 2% level of significance means that our confidence interval for the range
# of values we expect the true value of beta-1 lie in is actually quite broad,
# so it is extremely unlikely for beta-1 to actually equal 0 when it is so far
# outside our generous estimate of likely values.

## e) Interpret value of R^2
# The value of R^2 is 0.502 which means that about 50% of the variability in
# Salary can be explained by Experience, which is good byt leaves room for improvement.
# My recommendation for the current model would be to see if any of the other 
# features in the executives data frame such as Education, Sales, etc correlate
# with Salary and see if a multiple linear regression model using these features
# as well as Experience would create better predictions.
