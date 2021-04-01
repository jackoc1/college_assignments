executives.df <- read.table('/home/jack-o-connor/College/secondyear/ST2053/datasets/Executives.txt',
                          header=T)
attach(executives.df)
executives.cons1.lm <- lm(Salary ~ Experience + Education + Profits + Sales)

p <- length(coef(executives.cons1.lm))
e <- resid(executives.cons1.lm)
s <- summary(executives.cons1.lm)$sigma
h <- lm.influence(executives.cons1.lm)$hat
r <- e / (s * (1 - h) ^ 0.5)
d <- (1 / p) * (h / (1 - h)) * (r ^ 2)

# a)
# The residuals of a linear model are equal to, for each case in the data set, the difference
# between the actual value of the response value we are trying to predict and the predicted value of our linear
# model for that case.
e[1]

# b)
# If the absolute value of a case's studentized residual is > 2 then it is considered to be an outlier.
# Since studentized residuals are assumed to be normally distributed with mean 0 and variance 1,
# we expect around 5% of cases to be outliers.
length(r) * 0.05 # expect 8.3 (5%) of cases to be outliers
length(r[r > 2 | r < -2]) # 7 identified using student residuals


# Leverage
# A case's leverage h_ii in multiple regression is said to be high leverage if it is greater than 2p'/n where p' is 1 plus the number of predictors
# and n is the number of cases.
h[h == max(h)]
(2 * p) / length(h)
# If asked why high leverage make sure to examine each component of the vector and compare to mean.

# The most extreme case having high leverage follows from the fact that leverage is a measure of how unusual
# an individual case is compared to the average case, with higher leverage being more unusual.

# d)
# A case is said to be a case of high influence if the omission of this case from the dataset causes large changes
# in the least squares estimates of the regression coefficients.
d[d == max(d)]
paste("r=", r[43], "h=", h[43])
# This case has high influence because it's studentized residual of 1.86 is high (almost qualifying
# as an outlier) and its leverage of 0.11 qualifies as high leverage since it is greater than the cutoff 0.06.

# e)
exclude43 <- c(1:42, 44:166)
executives.cons2.lm <- lm(Salary[Salary] ~ Experience[exclude43] + Education[exclude43]
                           + Profits[exclude43] + Sales[exclude43])

summary(executives.lm)
summary(executives.cons2.lm)
executives.cons3.lm <- lm(Salary ~ Experience + Education + Sales)
executives.cons4.lm <- lm(Salary[exclude43] ~ Experience[exclude43] + Education[exclude43]
                          + Sales[exclude43])


f1 <- qf(0.95, 1, 161)
f2 <- qf(0.95, 1, 160)
# H0 is not worth including profits
anova(executives.cons1.lm, executives.cons3.lm) 

# H0 is not worth including profits
anova(executives.cons2.lm, executives.cons4.lm)

# Performing a partial f-test on both linear models (include/exclude case 43) it can be
# seen that almost all of the contribution of profit as a predictor is provided by case 43.
# It would be well worth investigating this case and seeing why it is the only one with this property.