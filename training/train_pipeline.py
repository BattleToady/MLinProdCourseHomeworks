import wandb
import sklearn
import time

def train_model(clf, model_name, config, X_train, y_train, X_test, y_test):
	# init wabdb
	wandb.init(project="MachineLearningInProduction", name = model_name)
	wandb.config = config

	# training
	training_time = time.time()
	model_name.fit(X_train, y_train)
	print(f'Train running time:  {(time.time() - training_time):.2f}')

	# metrics calculation
	testing_time = time.time()
	y_pred = clf.predict(X_test)
	MAE = sklearn.metrics.mean_absolute_error(y_test, y_pred)
	RMSE = sklearn.metrics.mean_squared_error(y_test, y_pred, squared = False)
	max_error = sklearn.metrics.max_error(y_test, y_pred)
	R2 = sklearn.metrics.r2_score(y_test, y_pred)
	Explained_variance = sklearn.metrics.explained_variance_score(y_test, y_pred)
	print(f'Test running time: {(time.time() - testing_time):.2f}')

	# logging
	wandb.log({"MAE": MAE, "RMSE" : RMSE, "max error" : max_error, 'R2' : R2, 'explained variance score' : Explained_variance})
	print('Result is logged')

	# saving model

	model.to_onnx()
	wandb.save(f'models/{model_name}.onnx')

	wandb.finish()