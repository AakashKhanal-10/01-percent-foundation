
#1 Our raw training data(experience vs salary)
X=[1.0,2.0,3.0]
y= [2.0, 3.0, 7.0] # These are target values

# Calulating the average(mean)
mean_x=sum(X)/len(X)
mean_y=sum(y)/len(y)

# Initializing our counters for the numerator and denominator of the slope (m)
numerator=0.0
denominator=0.0


# Distance Loop(part1)
for i in range(len(X)):
     x_dist=X[i]-mean_x
     y_dist=y[i]-mean_y
     # Filling the Both the numerator and denominator
     numerator+=x_dist*y_dist
     denominator+=x_dist**2

# Calculating the slope (m) and intercept (c)
beta_1=numerator/denominator
beta_0=mean_y-(beta_1*mean_x)


print(f"Learned Slope (Beta_1): {beta_1:.2f}")
print(f"Learned Intercept (Beta_0): {beta_0:.2f}")

# Make a prediction for 4 hours of study time
test_hours = 4.0
prediction = beta_0 + (beta_1 * test_hours)

print(f"Predicted score for {test_hours} hours of study: {prediction:.2f}")