noise_means.df <- read.table("/home/jack-o-connor/College/secondyear/ST2053/assignment_5/q5_noise_means.txt",
                         header=TRUE)
noise_individuals.df <- read.table("/home/jack-o-connor/College/secondyear/ST2053/assignment_5/q5_noise_individual.txt",
                                  header=TRUE)
Means.Noise <- noise_means.df$MeanNoise
Means.Distance <- noise_means.df$Distance
Means.N <- noise_means.df$N
Individuals.Noise <- noise_individuals.df$Noise
Individuals.Distance <- noise_individuals.df$Distance

# A) Why weighted regression?
noise_means.lm <- lm(Means.Noise ~ Means.Distance, weights=Means.N)

# Weighted regression is required to satisfy the constant variance assumption
# of our linear regression model. Since each instance of Mean.Noise is a mean of
# noise values that occur at Distance d, the variance of the error term for each Mean.Noise
# instance should be equal to the population variance of all the noise instances, divided
# by the number of noise instances at distance d.
# Multiplying the variance of mean noise at distance d by the number
# of instances in the sub-population mean noise at distance d gives the population noise variance.
# Doing this for each mean noise  at distance d should ensure our model's error terms all
# have equal variance.

# B) Lack of Fit test (Weighted model method)

noise_individuals.lm <- lm(Individuals.Noise ~ Individuals.Distance)

ss.lof <- deviance(noise_means.lm) # lack of fit in unweighted == deviation of weighted model
df.lof <- noise_means.lm$df.residual # == residual df freedom in weighted

ss.pe <- deviance(noise_individuals.lm) - ss.lof # pure error == rss - lack of fit
df.pe <- noise_individuals.lm$df.residual - df.lof # pure error df == rss(df) - lof(df)

f.statistic <- (ss.lof/df.lof) / (ss.pe/df.pe)
p.val <- pf(f.statistic, df.lof, df.pe, lower.tail=FALSE)
f.statistic
p.val

# C) Lack of Fit using ANOVA (model free)
noise_individuals.aov <- aov(Individuals.Noise ~ factor(Individuals.Distance))
anova(noise_individuals.lm, noise_individuals.aov)

# aov method manually
# SD <- by(Individuals.Noise, factor(Individuals.Distance), sd)
#ss.pe <- sum((Means.N-1)*SD^2)
#df.pe <- sum(Means.N-1)
#ss.lof <- deviance(noise_individuals.lm) - ss.pe
#ss.df <- noise_individuals.lm$df.residual - df.pe

# D) Why different?
