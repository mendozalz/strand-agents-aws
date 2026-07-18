from strands import Agent
from strands.models import BedrockModel


model = BedrockModel(model_id="us.mistral.pixtral-large-2502-v1:0", region_name="us-east-2", temperature=0.3)
agent = Agent(model=model)

agent("Explica en una frase que es Strand agents y para que sirve")

print("/*********************************/")
print(agent.model.config)