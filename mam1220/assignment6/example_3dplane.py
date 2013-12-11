import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


#----- Create some synthetic data (X,t) that is of the form t ~ N(wX,sigma^2) (i.e. it comes from a linear relationship with added white/Gaussian noise)

sigma=30 #The variance of the noise - try changing it to see how the data (and SNR) changes
x1 = np.random.uniform(low=0.0, high=100, size=(100, 1)) #The original data (1st dimension)
X = np.concatenate((np.ones((100,1)), x1),axis=1) #Add ones for the intercept and combine everything into X matrix (dim=100x2)

w_orig = np.random.randn(1,2) # Sample some parameters to create a line

t = X.dot(w_orig.T) + sigma*np.random.randn(100,1)# the response, t ~ N(wX,sigma^2) by adding noise to the line

#----- Add another dimension that is non-linear in the data x_2 = \Phi(x)=x^degree. You can play with other functions as well

x2 = x1**10 #degree of polynomial term (e.g. square, qube or higher) of the data - this is your 2nd dimension or "basis expansion" \Phi(X). Try some big values to see what happens
X_nonlin = np.concatenate(( x1, x2, np.ones((100,1))),axis=1) #Add ones for the intercept and combine everything into X_nonlin=[ones X \Phi(X)] (dim=100x3)
X_nonlin1 = np.concatenate(( x1**2, x2**2, x1, x2, np.ones((100,1))),axis=1) #Add ones for the intercept and combine everything into X_nonlin=[ones X \Phi(X)] (dim=100x3)
# print x1
# print x2
# print t
print X_nonlin

#----- Solve to get OLS estimate, if we could handle noise perfectly (see ML bias on estimating noise variance) we would get back the w we used to create the data in the first place)

w_ols = np.linalg.lstsq(X_nonlin,t)[0] # obtaining the parameters by fitting a hyper-plane in this expanded space
w_ols2 = np.linalg.lstsq(X_nonlin1,t)[0] # obtaining the parameters by fitting a hyper-plane in this expanded space
print w_ols
print w_ols2
t_hat = X_nonlin.dot(w_ols) # Our OLS estimator/predictions (on the training data). You can try creating "unseen"/test data, coding cross-validation to choose model complexity, and predict on it as well
t_hat1 = w_ols2[4] + x2.T*w_ols2[3] + x1.T*w_ols2[2] + x2.T**2*w_ols2[1] + x1.T**2*w_ols2[0]

print t_hat1.shape
print x1.shape
# # print t_hat

# #--- Ploting

fig = plt.figure()
ax = fig.gca(projection='3d')

 # You should see a curve of your estimates living on a plane (linear structure). Rotate the 3D figure till all the red points fall on a plane. Thats the plane you fitted
plt.figure(1)
ax.scatter(x1, x2, t_hat, c='r', marker='o') #The linear view of the plane (your estimate t_hat) in the expanded space
ax.scatter(x1, x2, t_hat1, c='g', marker='.') #The linear view of the plane (your estimate t_hat) in the expanded space
ax.scatter(x1, x2, t, c='b', marker='+') # The original data
	
plt.figure(2)
plt.plot(x1,t_hat,'ro') # The nonlinear view of the linear plane (your estimate t_hat) in the original data
plt.plot(x1,t_hat1.T,'go') # The nonlinear view of the linear plane (your estimate t_hat) in the original data
plt.plot(x1,t,'b+') # The original data
plt.show()

#--Notes
# Our expanded data in this script is 2-D. e.g. for degree 2 we have [x x^2]. In the lecture we saw very complicated functions from high order polynomials
# of degree d where \Phi(x) was e.g. [x x^2 x^3 x^4 x^5 .... x^d]. The hyperplane in this case lives in a d-dimensional space and hence I cannot (I can but I need to do other research) 
# really plot it for you (if you do code up or find code to visualize it (projection?PCA down?google visualizing hyperplanes) I'll buy you a beer). In this script no matter how you increase the power/degree for x2 you 
# always have only 2 terms [x x^d] so the plane is a 2-D plane in a 3-D world. That's why we can see it.

