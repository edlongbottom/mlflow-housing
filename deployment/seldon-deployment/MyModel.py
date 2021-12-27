# import libs
import os, glob
import joblib
import pandas as pd

# define the model class with predict function
class MyModel(object):
    """
    Model template. You can load your model parameters in __init__ from a location accessible at runtime
    """

    def __init__(self):
        """
        Add any initialization parameters. These will be passed at runtime from the graph definition parameters defined in your seldondeployment kubernetes resource manifest.
        """
        self.model = joblib.load(glob.glob(os.path.join(os.getcwd(),'*.pkl'))[0])
    
        print("Initializing")

    def predict(self, X, feature_names):
        """
        Return a prediction.

        Parameters
        ----------
        X : array of data (np.array)
        feature_names : array of feature names (list)
        """  
        print("Predict called - will run identity function")

        X_inf = pd.DataFrame(data=X,columns=feature_names)
        scores = self.model.predict(X_inf)
        return scores