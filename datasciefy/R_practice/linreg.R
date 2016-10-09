
set.seed(101)

# Generate Data

N = 100 # 100 data points

Int = 20

xCoef = 2

X1 = rnorm(N, 20, 10)
hist(X1)

numIt = 1:1000
Yit = rep(0, 1000)
for(var in numIt) {
  Y = Int + X1*xCoef + rnorm(N, 0, 20)
  #plot(X1, Y)
  #abline(20, 2, col="red")
  #fit a linear regression
  fit = lm(Y~X1)
  summary(fit)
  #abline(fit, col="blue")
  Yit[var] = coef(fit)[2]
}

sd(Yit)
Yit
Y = Int + X1*xCoef + rnorm(N, 0, 20)
fit = lm(Y~X1)
summary(fit)
