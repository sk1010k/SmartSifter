"""Implementation of 'On-line Unsupervised Outlier Detection Using Finite Mixtures with Discounting Learning Algorithm' (Yamanishi et al, 2004)."""


from sklearn.mixture import GaussianMixture
import numpy as np


class SDEM(GaussianMixture):
    
    def __init__(self, r, alpha, **kwargs):
        """
        Args:
            r: discounting parameter
            alpha = parameter to improve the stability of the estimates of mixture component weights
        """
        
        super(SDEM, self).__init__(**kwargs)
        
        self.r = r
        self.alpha = alpha
        
    def fit(self, X, y=None):
        """Initialize weights, means and covariances."""
        
        super(SDEM, self).fit(X, y)
        self.means_bar = np.copy(self.means_) # \overline{\mu}_i^{(t)} in the paper
        self.covariances_bar = np.copy(self.covariances_) # \overline{\Lambda}_i^{(t)} in the paper
        
    
    def update(self, x):
        """Employ SDEM algorithm."""
        
        # E-step for weights
        gamma = (1-self.alpha*self.r) * self.predict_proba(x) + self.alpha*self.r/self.weights_.shape[0] # \overline{\gamma}_i^{(t)} in the paper
        gamma = gamma.flatten()
        self.weights_ = (1-self.r)*self.weights_ + self.r*gamma # \overline{\c}_i^{(t)} in the paper
        
        x = x.flatten()
        means, means_bar, covariances, covariances_bar = [], [], [], []
        for i, (w, m, cov) in enumerate(zip(self.weights_, self.means_bar, self.covariances_bar)):
            
            # E-step for mean and covariance
            m = (1-self.r)*m + self.r*gamma[i]*x
            cov = (1-self.r)*cov + self.r*gamma[i]*np.outer(x,x)
            means_bar.append(m)
            covariances_bar.append(cov)

            # M-step for mean and covariance
            m = m/w
            cov = cov/w - np.outer(m, m)
            means.append(m)
            covariances.append(cov)

        self.means_ = np.asarray(means) # \mu_i^{(t)} in the paper
        self.covariances_ = np.asarray(covariances) # \Lambda_i^{(t)} in the paper
        self.means_bar = np.asarray(means_bar)
        self.covariances_bar = np.asarray(covariances_bar)
    