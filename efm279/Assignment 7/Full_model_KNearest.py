#!/usr/bin/env python

import numpy as np
import cv2
import datetime as dt

def load_base(fn):
    a = np.loadtxt(fn, np.float32, delimiter=',', converters={ 0 : lambda ch : ord(ch)-ord('A') })
    samples, responses = a[:,1:], a[:,0]
    return samples, responses

class LetterStatModel(object):
    class_n = 26
    train_ratio = 0.8    # first 16000 samples for training

    def load(self, fn):
        self.model.load(fn)
    def save(self, fn):
        self.model.save(fn)

    def unroll_samples(self, samples):
        sample_n, var_n = samples.shape
        new_samples = np.zeros((sample_n * self.class_n, var_n+1), np.float32)
        new_samples[:,:-1] = np.repeat(samples, self.class_n, axis=0)
        new_samples[:,-1] = np.tile(np.arange(self.class_n), sample_n)
        return new_samples

    def unroll_responses(self, responses):
        sample_n = len(responses)
        new_responses = np.zeros(sample_n*self.class_n, np.int32)
        resp_idx = np.int32( responses + np.arange(sample_n)*self.class_n )
        new_responses[resp_idx] = 1
        return new_responses

class RTrees(LetterStatModel):
    def __init__(self):
        self.model = cv2.RTrees()

    def train(self, samples, responses):
        sample_n, var_n = samples.shape
        var_types = np.array([cv2.CV_VAR_NUMERICAL] * var_n + [cv2.CV_VAR_CATEGORICAL], np.uint8)
        #CvRTParams(10,10,0,false,15,0,true,4,100,0.01f,CV_TERMCRIT_ITER));
        params = dict(max_depth=10 )
        self.model.train(samples, cv2.CV_ROW_SAMPLE, responses, varType = var_types, params = params)

    def predict(self, samples):
        return np.float32( [self.model.predict(s) for s in samples] )


class KNearest(LetterStatModel):
    def __init__(self):
        self.model = cv2.KNearest()

    def train(self, samples, responses):
        self.model.train(samples, responses)

    def predict(self, samples):
        retval, results, neigh_resp, dists = self.model.find_nearest(samples, k = 10)
        return results.ravel()


class Boost(LetterStatModel):
    def __init__(self):
        self.model = cv2.Boost()

    def train(self, samples, responses):
        sample_n, var_n = samples.shape
        new_samples = self.unroll_samples(samples)
        new_responses = self.unroll_responses(responses)
        var_types = np.array([cv2.CV_VAR_NUMERICAL] * var_n + [cv2.CV_VAR_CATEGORICAL, cv2.CV_VAR_CATEGORICAL], np.uint8)
        #CvBoostParams(CvBoost::REAL, 100, 0.95, 5, false, 0 )
        params = dict(max_depth=5) #, use_surrogates=False)
        self.model.train(new_samples, cv2.CV_ROW_SAMPLE, new_responses, varType = var_types, params=params)

    def predict(self, samples):
        new_samples = self.unroll_samples(samples)
        pred = np.array( [self.model.predict(s, returnSum = True) for s in new_samples] )
        pred = pred.reshape(-1, self.class_n).argmax(1)
        return pred


class SVM(LetterStatModel):
    def __init__(self):
        self.model = cv2.SVM()

    def train(self, samples, responses):
        params = dict( kernel_type = cv2.SVM_LINEAR,
                       svm_type = cv2.SVM_C_SVC,
                       C = 1 )
        self.model.train(samples, responses, params = params)

    def predict(self, samples):
        return self.model.predict_all(samples).ravel()


class MLP(LetterStatModel):
    def __init__(self):
        self.model = cv2.ANN_MLP()

    def train(self, samples, responses):
        sample_n, var_n = samples.shape
        new_responses = self.unroll_responses(responses).reshape(-1, self.class_n)

        layer_sizes = np.int32([var_n, 100, 100, self.class_n])
        self.model.create(layer_sizes)

        # CvANN_MLP_TrainParams::BACKPROP,0.001
        params = dict( term_crit = (cv2.TERM_CRITERIA_COUNT, 300, 0.01),
                       train_method = cv2.ANN_MLP_TRAIN_PARAMS_BACKPROP,
                       bp_dw_scale = 0.001,
                       bp_moment_scale = 0.0 )
        self.model.train(samples, np.float32(new_responses), None, params = params)

    def predict(self, samples):
        ret, resp = self.model.predict(samples)
        return resp.argmax(-1)


if __name__ == '__main__':
    import getopt
    import sys

    print  __doc__

    models = [RTrees, KNearest, Boost, SVM, MLP] # NBayes
    models = dict( [(cls.__name__.lower(), cls) for cls in models] )


    args, dummy = getopt.getopt(sys.argv[1:], '', ['model=', 'data=', 'load=', 'save='])
    args = dict(args)
    args.setdefault('--model', 'knearest')
    args.setdefault('--data', 'letter-recognition.data')


    n1=dt.datetime.now()
    print 'loading data %s ...' % args['--data']
    samples, responses = load_base(args['--data'])
    Model = models[args['--model']]
    model = Model()
    n2=dt.datetime.now()
    print 'data loading time is ' +str(((n2-n1).microseconds)/1e6) +' seconds'


    n3=dt.datetime.now()
    train_n = int(len(samples)*model.train_ratio)
    if '--load' in args:
        fn = args['--load']
        print 'loading model from %s ...' % fn
        model.load(fn)
    else:
        print 'training %s ...' % Model.__name__
        model.train(samples[:train_n], responses[:train_n])
    n4=dt.datetime.now()
    print 'elapsed training time is ' +str(((n4-n3).seconds)) +' seconds'
    
    print 'testing...'
    train_rate = np.mean(model.predict(samples[:train_n]) == responses[:train_n])
    test_rate  = np.mean(model.predict(samples[train_n:]) == responses[train_n:])

    print 'train rate: %f  test rate: %f' % (train_rate*100, test_rate*100)

    if '--save' in args:
        fn = args['--save']
        print 'saving model to %s ...' % fn
        model.save(fn)
    cv2.destroyAllWindows()


def F1_score(tags,predicted):


    tags = set(tags)
    predicted = set(predicted)

    tp = len(tags & predicted)
    fp = len(predicted) - tp 
    fn = len(tags) - tp

    if tp>0:
        precision=float(tp)/(tp+fp)
        recall=float(tp)/(tp+fn)


        return 2*((precision*recall)/(precision+recall))
    else:
        return 0




letter_a=[elem for elem in range(0,len(responses[train_n:])) if responses[train_n:][elem]==0]
la=np.mean(model.predict(samples[letter_a]) == responses[letter_a])
print 'Accuracy percentage for letter A is '+ str(la)
f11= F1_score(model.predict(samples[train_n:][letter_a]),responses[train_n:][letter_a])
print '#Method 1: F 1 Measure for Letter A is '+ str(f11)


def true_positives(s1, s2):
    """
    The "true positives" are the intersection of the two lists
      s1: true labels
      s2: predicted labels
    """
    return len(set(s1).intersection(s2))

def false_positives(s1, s2):
    """
    false positives are predicted items that aren't real
      s1: true labels
      s2: predicted labels
    """
    return len(set(s1).difference(s2))

def false_negatives(s1, s2):
    """
    false negatives are real items that aren't predicted
      s1: true labels
      s2: predicted labels
    """
    return len(set(s2).difference(s1))

def precision(s1, s2):
    """
    Precision is the ratio of true positives (tp) to all predicted positives (tp + fp)
      s1: true labels
      s2: predicted labels
    """
    tp = true_positives(s1, s2)
    fp = false_positives(s1, s2)
    if tp == 0 and fp == 0:
        return 0.0
    return 1.0 * tp / (tp + fp)

def recall(s1, s2):
    """
    Recall is the ratio of true positives to all actual positives (tp + fn)
      s1: true labels
      s2: predicted labels
    """
    tp = true_positives(s1, s2)
    fn = false_negatives(s1, s2)
    if tp == 0 and fn == 0:
        return 0.0
    return 1.0 * tp / (tp + fn)

def f1(s1, s2):
    """
    The F1 score, commonly used in information retrieval, measures accuracy using the statistics precision (p) and recall (r).
      s1: true labels
      s2: predicted labels
    """
    p = precision(s1, s2)
    r = recall(s1, s2)
    if p == 0 and r == 0:
        return 0.0
    return 2.0 * p * r / (p + r)

def mean_f1(y_true, y_pred):
    sets = zip(y_true, y_pred)
    return sum([f1(s1, s2) for s1, s2 in sets]) / len(sets)

if __name__ == '__main__':
    y_true = [
              [1, 2],
              [3, 4, 5],
              [6],
              [7]
    ]
    y_pred = [
              [1, 2, 3, 9],
              [3, 4],
              [6, 12],
              [1]
    ]
    print '#Method 2: F 1 measure for Letter A is '+ str(mean_f1([model.predict(samples[train_n:][letter_a]).tolist()],[responses[train_n:][letter_a].tolist()]))


