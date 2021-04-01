# ASSIGNMENT 4 - JACK O'CONNOR
executives.df <- read.table('/home/jack-o-connor/College/secondyear/ST2053/datasets/Executives.txt',
                            header=T)
attach(executives.df)
executives.lm.1 <- lm(Salary ~ Experience)
executives.lm.2 <- lm(log(Salary) ~ Experience)
executives.lm.3 <- lm(sqrt(Salary) ~ Experience)

# A) DIAGNOSTIC PLOTS
# cons1
par(mfrow=c(2, 2))  # Split graphics window into a 2 x 2 grid.
scatter.smooth(Experience, Salary, main="Scatter.smooth plot")
plot(fitted(executives.lm.1), resid(executives.lm.1), main="Plot of Residual vs Fitted Values")
abline(h=0, lty=2)
hist(resid(executives.lm.1), main="Histogram of Residuals")
qqnorm(resid(executives.lm.1), main="Normal Probability Plot of Residuals")
qqline(resid(executives.lm.1))
par(mfrow=c(1, 1))

# cons2
par(mfrow=c(2, 2))
scatter.smooth(Experience, log(Salary), main="Scatter.smooth plot")
plot(fitted(executives.lm.2), resid(executives.lm.2), main="Plot of Residual vs Fitted Values")
abline(h=0, lty=2)
hist(resid(executives.lm.2), main="Histogram of Residuals")
qqnorm(resid(executives.lm.2), main="Normal Probability Plot of Residuals")
qqline(resid(executives.lm.2))
par(mfrow=c(1, 1))

# cons3
par(mfrow=c(2, 2))
scatter.smooth(Experience, sqrt(Salary), main="Scatter.smooth plot")
plot(fitted(executives.lm.3), resid(executives.lm.3), main="Plot of Residual vs Fitted Values")
abline(h=0, lty=2)
hist(resid(executives.lm.3), main="Histogram of Residuals")
qqnorm(resid(executives.lm.3), main="Normal Probability Plot of Residuals")
qqline(resid(executives.lm.3))
par(mfrow=c(1, 1))
