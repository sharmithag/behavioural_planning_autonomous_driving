import gymnasium as gym
import highway_env
import sys
import os
from rl_agents.trainer.evaluation import Evaluation
from rl_agents.agents.common.factory import load_agent, load_environment

# Get the environment and agent configurations from the rl-agents repository
os.chdir('rl-agents/scripts/')
print(os.getcwd())
env_config = 'configs/IntersectionEnv/env.json'
agent_config = 'configs/IntersectionEnv/agents/ValueIterationAgent/baseline.json'

env = load_environment(env_config)
agent = load_agent(agent_config, env)
evaluation = Evaluation(env, agent, num_episodes=1, display_env=False, display_agent=False)
print(f"Ready to train {agent} on {env}")


evaluation.train()

env = load_environment(env_config)
env.configure({"offscreen_rendering": True})
agent = load_agent(agent_config, env)
evaluation = Evaluation(env, agent, num_episodes=1)
evaluation.train()

sys.path.insert(0, './highway-env/scripts/')

from utils import record_videos, show_videos
show_videos(evaluation.run_directory)