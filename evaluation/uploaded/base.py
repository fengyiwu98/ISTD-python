import numpy as np
from abc import ABCMeta, abstractmethod


class BaseEvaluator(object):
    '''
    Basic class of infrared small targets evaluator.
    '''
    def __init__(self):
        self.reset()

    @abstractmethod
    def update(self, preds=None, labels=None, in_img=None):
        '''
        Update parameters of this evaluator.

            Parameters
            ----------
            preds : ndarray
                The saliency map or detection result of algorithms.
            labels : ndarray
                The labeled image.
            in_img : ndarray
                The original image. Required when Evaluating some metrics such BSF and SCR Gain.
        '''
        pass

    @abstractmethod
    def get(self):
        '''
        Get metric for the sequence.

            Return
            ------
            out : single value
                A single value satisfying the specified requirements.
        '''
        pass

    def get_all(self):
        '''
        Get metric for all images.

            Return
            -------
            out : numpy array
                An array object satisfying the specified requirements.
        '''
        pass

    @abstractmethod
    def reset(self):
        '''
        Reset all of the parameters.
        '''
        pass
