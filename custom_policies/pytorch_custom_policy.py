import os
import torch
from typing import Any, Dict, Text
from rasa.core.policies.policy import Policy
from rasa.engine.recipes.default_recipe import DefaultV1Recipe

@DefaultV1Recipe.register(
    [DefaultV1Recipe.ComponentType.POLICY_WITHOUT_END_TO_END_SUPPORT],
    is_trainable=True
)
class PyTorchCustomPolicy(Policy):
    def __init__(self, config: Dict[Text, Any], model=None, **kwargs) -> None:
        super().__init__(config, **kwargs)
        self.model = model if model else self.build_model()

    @staticmethod
    def build_model():
        return torch.nn.Sequential(
            torch.nn.Linear(128, 64),
            torch.nn.ReLU(),
            torch.nn.Linear(64, 2)
        )

    def train(self, training_data, config, **kwargs):
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model.to(device)

        optimizer = torch.optim.Adam(self.model.parameters(), lr=0.001)
        criterion = torch.nn.CrossEntropyLoss()

        for epoch in range(10):
            inputs = torch.tensor(training_data.X).float().to(device)
            labels = torch.tensor(training_data.y).long().to(device)

            optimizer.zero_grad()
            outputs = self.model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

        print("Model trained on GPU" if torch.cuda.is_available() else "Model trained on CPU")

    def predict_action_probabilities(self, tracker, domain):
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model.to(device)

        inputs = torch.tensor([tracker.current_state()]).float().to(device)
        outputs = self.model(inputs)
        probs = torch.softmax(outputs, dim=-1).cpu().detach().numpy()[0]

        return self._prediction(probs)

    def persist(self, file_name: Text, model_dir: Text) -> Dict[Text, Any]:
        """Persist the policy to a file."""
        model_path = os.path.join(model_dir, f"{file_name}.pt")
        torch.save(self.model.state_dict(), model_path)
        return {"model_file": file_name}

    @classmethod
    def load(cls, meta: Dict[Text, Any], model_dir: Text, **kwargs: Any) -> "PyTorchCustomPolicy":
        """Load the policy from a persisted model."""
        file_name = meta.get("model_file")
        model_path = os.path.join(model_dir, f"{file_name}.pt")
        model = cls.build_model()
        model.load_state_dict(torch.load(model_path))
        return cls(meta, model)
