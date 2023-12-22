import sklearn
from skops.card import Card
from pathlib import Path

def generate_model_card(model, slots):
	# init model card
	model_card = Card(model)

	# adding parts from slots dictionary
	for part in ["Model description", "Intended uses & limitations", "How to Get Started with the Model",\
	"Model Card Authors", "Model Card Contact", "Citation", "Evaluation Results", "Hyperparameters"]:
		if(part in slots.keys()):
			model_card.add(**{part : slots[part]})

	
	# saving model card into README.md
	p = Path('.\\models')
	model_card.save(p / "README.md")