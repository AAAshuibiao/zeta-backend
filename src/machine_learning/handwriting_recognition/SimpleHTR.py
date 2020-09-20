from __future__ import division
from __future__ import print_function

import json
import cv2
import editdistance
from DataLoader import DataLoader, Batch
from Model import Model, DecoderType
from SamplePreprocessor import preprocess


class FilePaths:
	"filenames and paths to data"
	fnCharList = '.\\model\\charList.txt'
	fnAccuracy = '.\\model\\accuracy.txt'


def infer(model, fnImg, printOut = False):
	"recognize text in image provided by file path"
	img = preprocess(cv2.imread(fnImg, cv2.IMREAD_GRAYSCALE), Model.imgSize)
	batch = Batch(None, [img])
	(recognized, probability) = model.inferBatch(batch, True)
	if not printOut:
		return recognized, probability
	else:
		print('Recognized:', '"' + recognized[0] + '"')
		print('Probability:', probability[0])
		return recognized, probability


def predict(filepath, printOut = False):
	"predict"

	# infer text on test image
	if printOut: print(open(FilePaths.fnAccuracy).read())
	model = Model(open(FilePaths.fnCharList).read(), DecoderType.BestPath, mustRestore=True, dump = False)
	return infer(model, filepath, printOut)


# results = predict(FilePaths.fnPic)

# open(FilePaths.fnResults, 'w').write(
# 	json.dumps({
# 		"recognized": results[0][0],
# 		"probability": float(results[1][0])
# 	})
# )
