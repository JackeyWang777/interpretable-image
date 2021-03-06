import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--gpuid', type=str, default='0')
parser.add_argument('--start', type=int, default=1)
parser.add_argument('--trials', type=int, default=4)

args = parser.parse_args()


for trial in range(args.start,args.start+args.trials):	
	print("trial: %d" % trial)
	save_path = "saved_models_noCEDA%s/" % str(trial)
	
	os.system("python main.py --gpuid %s --save_path %s" % (args.gpuid,save_path))
	print("python main.py --gpuid %s --save_path %s" % (args.gpuid,save_path))
		
	os.system("python test.py --gpuid %s --resume_path %s" % (args.gpuid,save_path))
	print("python test.py --gpuid %s --resume_path %s" % (args.gpuid,save_path))
