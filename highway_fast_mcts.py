import gymnasium as gym
import highway_env
import sys
import os
from rl_agents.trainer.evaluation import Evaluation
from rl_agents.agents.common.factory import load_agent, load_environment

# Get the environment and agent configurations from the rl-agents repository
os.chdir('rl-agents/scripts/')
print(os.getcwd())
env_config = 'utils/HighwayEnv/env.json'
agent_config = 'utils/HighwayEnv/agents/MCTSAgent/baseline.json'

env = load_environment(env_config)
agent = load_agent(agent_config, env)
evaluation = Evaluation(env, agent, num_episodes=10, display_env=False, display_agent=False)
print(f"Ready to train {agent} on {env}")


evaluation.train()

