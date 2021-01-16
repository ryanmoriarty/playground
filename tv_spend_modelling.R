
# read in raw data from CSV
tv_spend <- read.csv('/Users/ryan/Desktop/tv_spend.csv') 

# create a daily (freq=7) timeseries object of our the orders data...
ts <- ts(tv_spend$orders,frequency=7,start=c(2015,08,29))
ts <- stl(ts,s.window = "periodic")
# create a chart of the daily order data
plot(ts)

# plot a scatter of total orders and facebook spend to see if they are correlated...
plot(tv_spend$orders,tv_spend$fb_spend)

# do some shit to convert the date struct ure into a date format (so you can make a selection on it)
# note: should review how you import this stuff to start with
tv_spend$Date <- as.character(tv_spend$Date)
dates <- c('26/11/2015','27/11/2015','28/11/2015','05/12/2015','06/12/2015','07/12/2015','08/12/2015','09/12/2015')

# create a data frame for the date period you're interested in 
tv_spend_ex_out <- tv_spend[!tv_spend$Date %in% dates,]

# lag it using the code you found googling "media mix modelling lag curve"
tv_spend$tv_ads_lag50 <- as.numeric(filter(x=tv_ads, filter=0.50, method="recursive"))
tv_spend$tv_ads_lag30 <- as.numeric(filter(x=tv_ads, filter=0.30, method="recursive"))

attach(tv_spend)

# plot how it looks
plot(tv_ads,type="line")
lines(tv_ads_lag50,type="l",col="grey")
lines(tv_ads_lag30,type="l",col="pink")

# create a lot of TV Ads... maybe the first n1000 are more important?
tv_spend$tv_ads_lg <- log(tv_ads)

plot(orders - fb_orders,type="l")
mod1 <- lm(formula = orders ~ tv_reach, data = tv_spend_ex_out)
summary(mod1)
plot(mod1)

mod2 <- lm(formula = orders ~ tv_ads_lag50 + fb_spend, data = tv_spend)
summary(mod2)

mod3 <- lm(formula = orders - fb_orders ~ tv_ads, data = tv_spend)
summary(mod3)

mod4 <- lm(formula = orders - fb_orders ~ tv_ads, data = tv_spend)
summary(mod4)

pred <- predict(mod)
plot(orders,type="l")
plot(fb_spend, type ="l")


install.packages("gvlma")
library(gvlma)
gvl_mod <- gvlma(mod1)
summary(gvl_mod)



hat.plot <- function(x) {
  p <- length(coefficients(x))
  n <- length(fitted(x))
  plot(hatvalues(x), main="Index Plot of Hat Values")
  abline(h=c(2,3)*p/n,col="red",lty=2)
  identify(1:n, hatvalues(x), names(hatvalues(x)))
}
hat.plot(mod1)

