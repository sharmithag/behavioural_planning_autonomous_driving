import gymnasium as gym
from rl_agents.trainer.evaluation import Evaluation
from rl_agents.agents.common.factory import load_agent, load_environment

# Importing environment configuration
env_config = 'utils/IntersectionEnv/env.json'
#Importing agent configuration
agent_config = 'utils/IntersectionEnv/agents/DQNAgent/ego_attention_2h.json'
# Setting the environment as the imported configuration
env = load_environment(env_config)
# Setting the agent as DQNQNQN agent
agent = load_agent(agent_config, env)
# Setting up the parameters for the model
evaluation = Evaluation(env, agent, num_episodes=1)
print(f"Ready to train {agent} on {env}")
# Training the model
evaluation.train()


