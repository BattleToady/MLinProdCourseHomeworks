import wandb
import sklearn
import time

def train_model(clf, model_name, description, X_train, y_train, X_test, y_test):
	# init wabdb
	wandb.init(project="MachineLearningInProduction", name = model_name)

	# training
	training_time = time.time()
	clf.fit(X_train, y_train)
	print(f'Train running time:  {(time.time() - training_time):.2f}')
	train_predict_time = time.time()
	y_train_pred = clf.predict(X_train)
	print(f'Train set predicting running time:  {(time.time() - train_predict_time):.2f}')
	train_metrics = {"accuracy": sklearn.metrics.accuracy_score(y_train, y_train_pred), 
		"f1": sklearn.metrics.f1_score(y_train, y_train_pred), 
		"recall": sklearn.metrics.recall_score(y_train, y_train_pred),
		"precision": sklearn.metrics.precision_score(y_train, y_train_pred)}
	print('Train metrics:\n', train_metrics)

	# metrics calculation
	testing_time = time.time()
	y_test_pred = clf.predict(X_test)
	print(f'Test running time: {(time.time() - testing_time):.2f}')
	test_metrics = {"accuracy": sklearn.metrics.accuracy_score(y_test, y_test_pred), 
		"f1": sklearn.metrics.f1_score(y_test, y_test_pred), 
		"recall": sklearn.metrics.recall_score(y_test, y_test_pred),
		"precision": sklearn.metrics.precision_score(y_test, y_test_pred)}
	print('Test metrics:\n', test_metrics)

	# logging
	params = clf.get_params()

	artifact = wandb.Artifact(model_name, type='model', description=description,
                          metadata={"parameters": params, "train_metrics": train_metrics, "test_metrics": test_metrics})

	# saving model
	import joblib

	joblib.dump(clf, filename = f"{model_name}.joblib")
	artifact.add_file(f"{model_name}.joblib")
	wandb.log_artifact(artifact)

	wandb.finish()