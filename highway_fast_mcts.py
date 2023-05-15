import gymnasium as gym
import highway_env
import sys
import os
from rl_agents.trainer.evaluation import Evaluation
from rl_agents.agents.common.factory import load_agent, load_environment

# Importing environment configuration
env_config = 'utils/HighwayEnv/env.json'
#Importing agent configuration
agent_config = 'utils/HighwayEnv/agents/MCTSAgent/baseline.json'
# Setting the environment as the imported configuration
env = load_environment(env_config)
# Setting the agent as Deterministic planning agent
agent = load_agent(agent_config, env)
# Setting up the parameters for the model
evaluation = Evaluation(env, agent, num_episodes=10)
print(f"Ready to train {agent} on {env}")

# Training the model
evaluation.train()

