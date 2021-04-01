### ASSIGNMENT QUESTION 2
## SETUP
executives.df <- read.table("/home/jack-o-connor/College/secondyear/ST2053/datasets/Executives.txt",
                            header=T)
attach(executives.df)
executives.lm = lm(Salary ~ Experience + Education + Profits + Sales)


## a) Matrix of Correlation Coefficients
cor(executives.df[1:5])
# Experience is the prediction variable which correlates the most with
# Salary having a strong correlation coefficient of 0.71 and is not strongly 
# correlated with any other prediction variables other than maybe Education. This
# would be a good variable to include in our linear model.
# Sales is highly correlated with Profits having a correlation coefficient of 0.9.
# It is possible including both of these variables may lead to collinearity issues
# in our model and one or more of them will have to be removed.
# On top of this Profits and Sales have weak to non-existent correlation with
# Salary having correlation coefficients of -0.03 and -0.1 respectively so 
# including them may not provide any additional prediction accuracy and just
# cause noise.


## b) Interpret Beta-1
summary(executives.lm)
# Beta-1 equals 2805.5. This means that if it were possible to increase an executive's
# experience by one year and keep all his/her other attributes constant we would expect
# their salary to increase by approximately by €2805.50.


## c) R-squared
# The R-squared from the simple linear regression using just Experience as a prediction
# achieved an R-squared value of 0.5 compared to the 0.55 R-squared of our current 
# linear model.
# The inclusion of other variables in the linear model besides Experience
# has been able to explain an extra 5% of the variability in salary. This is
# only a small improvement though. It may be worth checking that this isn't
# caused by over-fitting of the model to the sample data and that the extra data are worth
# including in the final model.


## d) Experience should be the only variable?
# Partial F-test to determine if only experience worth including.
# F ~ (0.05; 1, 161) using 5% level of significance
# H0: Beta-2 = Beta-3 = Beta-4 = 0
# H1: Beta-2, Beta-3, Beta-4 not all 0

executives.cons2.lm <- lm(Salary ~ Experience, data=executives.df)
anova(executives.lm, executives.cons2.lm)
qf(0.95, 3, 161)

executives.cons3.lm <- lm(Salary ~ Education + Profits + Sales, data=executives.df)
ssreg.experience.adjusted <- sum(resid(executives.cons2.lm)^2) - sum(resid(executives.lm)^2)
anova(executives.lm, executives.cons2.lm)
f <- (ssreg.experience.adjusted / 3) / (sum(resid(executives.lm)^2) / 161)
p.val <- pf(f, 3, 161, lower.tail = F) # 3 = variables being tested, 161 = n - p + 1 (full model)

# Since our F-statistic of 5.6821 is > qf(0.95, 3, 161) = 2.661 (insert p < 0.05) we reject the null
# hypothesis and instead accept the alternative hypothesis H1 that .at least one of
# beta-2, beta-3, beta-4 should be included in the model.


## e) Explain Collinearity + problems associated with it.
#Collinearity occurs when at least one predictor variable in a linear model can be expressed as a linear 
#combination of the other variables in the model.Problems associated with collinearity include the variance 
#of the slopes of collinear variables being greatly inflated and in the case of perfect collinearity, regression coefficients not being defined at all.

## f) VIF for each predictor
experience.lm <- lm(Experience ~ Education + Profits + Sales, data=executives.df)
education.lm <- lm(Education ~ Experience + Profits + Sales, data=executives.df)
profits.lm <- lm(Profits ~ Experience + Education + Sales, data=executives.df)
sales.lm <- lm(Sales ~ Experience + Education + Profits, data=executives.df)

sum.experience <- summary(experience.lm)
sum.education <- summary(education.lm)
sum.profits <- summary(profits.lm)
sum.sales <- summary(sales.lm)

vif.experience <- 1 / (1 - sum.experience$r.squared)
vif.education <- 1 / (1 - sum.education$r.squared)
vif.profits <- 1 / (1 - sum.profits$r.squared)
vif.sales <- 1 / (1 - sum.sales$r.squared)

# Max vif < 10 so collinearity is not a serious problem.